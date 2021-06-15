#version 100
precision highp float;
uniform sampler2D tex;
uniform float iTime;
varying vec2 Texcoord;
const float scale = 1.4;
const vec2 texSize = vec2(128.0,128.0);
float pxRange = 6.0;
const vec4 bgColor = vec4(0.);
const vec4 fgColor = vec4(0.259, 0.890, 0.208, 1.);
const vec4 particleColor = vec4(0.259, 0.890, 0.208, 1.);
const int numParticles = 40;
const float duration = 1.0;
const float pause = 8.0;
const vec4 textPos = vec4(0.01, 0, 0.98, 0.125);
const float lineWidth = 0.15;

// Thanks to: https://www.shadertoy.com/view/Xl2SRR
float random(float co)
{
    return fract(sin(co*12.989) * 43758.545);
}

float median(float r, float g, float b)
{
    return max(min(r, g), min(max(r, g), b));
}

// Thanks to: https://www.iquilezles.org/www/articles/functions/functions.htm
float quaImpulse( float k, float x )
{
    return 2.0*sqrt(k)*x/(1.0+k*x*x);
}

float getCurrentTime()
{
    return mod(iTime, duration+pause)/duration;
}

float getBox(vec2 uv, float x, float width)
{
    float rhs = sign(clamp(x-uv.x+width, 0., 1.));
    float lhs = sign(clamp(x-uv.x,       0., 1.));
    return rhs-lhs;
}

float getSweepingLinePos()
{
    return getCurrentTime()-lineWidth+textPos.x;
}

float getSweepingLine(vec2 uv)
{
    return getBox(uv, getSweepingLinePos(), lineWidth);
}

float getGradients(vec2 uv)
{
    float t = getCurrentTime();
    float gw = lineWidth/2.;
    float left  = getBox(uv, getSweepingLinePos() - gw,        gw)*smoothstep(0., 1., (gw + lineWidth - (t - uv.x + textPos.x))/lineWidth);
    float right = getBox(uv, getSweepingLinePos() + lineWidth, gw)*smoothstep(0., 1., (gw             + (t - uv.x + textPos.x))/lineWidth);
    float gradient_y = smoothstep(0.8, 1., 1.-abs(0.5-uv.y));
    return (left + right) * gradient_y;
}

// Note: Does not include offset, added in getParticlePosition
vec2 getParticleInitialPosition(int i)
{
    vec2 pos;
    pos.x = float(i)/float(numParticles-1); // Even
    pos.y = sign(random(float(i)) - 0.1); // Top biased
    return pos*textPos.zw;
}

float getParticleTime(int i)
{
    // Compute based on initial x due to sweeping reveal
    return getCurrentTime()-getParticleInitialPosition(i).x;
}

float getParticleIntensity(int i)
{
    float lifespan = 1.0 + 0.4*(random(float(i*44))-0.5);
    float alive = clamp(sign(getParticleTime(i)), 0., 1.);
    return alive*clamp(lifespan-getParticleTime(i), 0., 1.);
}

vec2 getParticlePosition(int i)
{
    float pt = getParticleTime(i);
    float alive = clamp(sign(pt), 0., 1.);
    float falloff = 10.;
    float impulse = quaImpulse(falloff, pt+0.8)+0.2;
    vec2 pos = getParticleInitialPosition(i);

    vec2 velocity;
    // Move mostly right, but sometimes left
    velocity.x  = sign(random(float(i+3000))-0.2);
    velocity.x *= impulse*1.25*(0.00 + random(float(i+62)));
    // Move vertically in whatever direction we spawned in
    velocity.y  = sign(pos.y);
    velocity.y *= impulse*1.40*(0.25 + 1.2*random(float(i+62)));
    return pos + alive * velocity * pt + vec2(textPos.x, 0.5); // Offset to center
}

float getParticles(vec2 uv)
{
    // Compute contribution from all particles to this frag
    float c = 0.;
    for (int j = 0; j < numParticles; j++) {
        vec2 pos = getParticlePosition(j);
        float d = distance(uv, pos);
        c += (1.-smoothstep(0.01, 0.01035,d))*getParticleIntensity(j);
    }

    return c;
}

void main()
{
    vec2 uv = gl_FragCoord.xy/vec2(512,512);
    float scale = 1.4;
    uv -= 0.5 * (1.-1./scale);
    uv *= scale;
    vec2 pos = uv;

    vec3 msd = texture2D(tex, vec2(pos.x, 1.-pos.y)).rgb;
    float sd = median(msd.r, msd.g, msd.b);
    float screenPxDistance = pxRange*(sd - 0.5);
    float opacity = clamp(screenPxDistance + 0.5, 0.0, 1.0);
    vec4 fill_color = mix(bgColor, fgColor, opacity);
    float outline = clamp(screenPxDistance + 1.6, 0., 1.);
    outline -= clamp(screenPxDistance - 1.6, 0., 1.);
    outline = smoothstep(0.5, 1., outline);

    vec4 line_color = mix(bgColor, fgColor, outline);
    gl_FragColor = mix(fill_color, line_color, getSweepingLine(uv));
    gl_FragColor += mix(vec4(0), particleColor, getParticles(uv));
    gl_FragColor += 2.*vec4(1.)*getBox(uv, textPos.x, textPos.z)*getGradients(uv);
}
