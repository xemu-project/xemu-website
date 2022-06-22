;(function(){
"use strict"
window.addEventListener("load", setupWebGL, false);

var gl, program;
var time_loc;
var buffer;
var ebuffer;
var pending_disable_fallback = true;
var restart_anim = true;
var last_started = 0;
var loaded = false;

var vert_src = `

#version 100
attribute vec2 in_Position;
attribute vec2 in_Texcoord;
varying vec2 Texcoord;
void main() {
    Texcoord = in_Texcoord;
    gl_Position = vec4(in_Position, 0.0, 1.0);
}

`;

var frag_src = `

#version 100
precision highp float;
uniform sampler2D tex;
uniform float iTime;
const float pi = 3.14159265359;
const float scale = 1.4;
const float pxRange = 6.0;
const float lineWidth = 0.175;
const float duration = 1.25;
const float pause = 6.;
const int numParticles = 35;
const int numSpotlights = 5;
const vec2 texSize = vec2(128.0,128.0);
const vec4 bgColor = vec4(0.);
const vec4 fgColor = vec4(0.384, 0.792, 0.075, 1.);
const vec4 particleColor = fgColor;
const vec4 textPos = vec4(0.01, 0, 0.98, 0.125);

// Thanks to: https://www.shadertoy.com/view/Xl2SRR
float random(float co)
{
    return fract(abs(sin(co*12.989)) * 43758.545);
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
    float lhs = sign(clamp(x - uv.x,         0., 1.));
    float rhs = sign(clamp(x - uv.x + width, 0., 1.));
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
    float l_s = abs(cos(t*pi*2.));
    float pos = t - uv.x + textPos.x;
    float left = l_s*smoothstep(0., 1., 0.5-abs(pos - lineWidth)*(20.+80.*(1.-l_s)));
    float r_s = abs(sin(t*pi*2.));
    float right = r_s*smoothstep(0., 1., 0.5-abs(pos)*(20.+80.*(1.-r_s)));
    float gradient_y = smoothstep(0.7, 1., 1.-abs(0.5-uv.y));
    return (left + right) * gradient_y;
}

vec2 getSpotlightPos(int i)
{
    float t = getCurrentTime();
    vec2 initialPos = textPos.zw*vec2(
        float(i)/float(numSpotlights-1), // Even
        sign(random(float(i+62)) - 0.6)*2.); // Top biased

    vec2 velocity;
    velocity.x = sign(random(float(i+63)) - 0.5)*0.7*(0.3+0.6*random(float(i+100)));
    velocity.y = -sign(initialPos.y)*0.8*(0.1+0.9*random(float(i+62)));
    return initialPos + velocity * t + vec2(textPos.x, 0.5); // Offset to center
}

float getSpotlights(vec2 uv)
{
    float t = getCurrentTime();
    float right = smoothstep(0.3, 0.7, 0.8-8.*abs(t - uv.x + textPos.x + 0.05));

    // Compute contribution from all spotlights to this frag
    float c = 0.;
    for (int j = 0; j < numSpotlights; j++) {
        vec2 pos = getSpotlightPos(j);
        float d = distance(uv, pos);
        c += (1.-smoothstep(0.04, 0.07835, d));
    }

    return 0.6*right + 0.4*c;
}

// Note: Does not include offset, added in getParticlePosition
vec2 getParticleInitialPosition(int i)
{
    return textPos.zw*vec2(
        float(i)/float(numParticles-1), // Even
        sign(random(float(i)) - 0.2)); // Top biased
}

float prob(float p, int i)
{
    return sign(clamp(random(float(i*30))-(1.-p), 0., 1.));
}

float getParticleLifespan(int i)
{
    return 1. + 1.25*exp(-10.*random(float(i*30))) + 0.5*prob(0.3, i);
}

float getParticleTime(int i)
{
    return getCurrentTime()-getParticleInitialPosition(i).x;
}

float getParticleAlive(int i)
{
  return clamp(sign(getParticleTime(i)), 0., 1.);
}

float getParticleIntensity(int i)
{
    return getParticleAlive(i)*clamp(getParticleLifespan(i)-getParticleTime(i), 0., 1.);
}

vec2 getParticlePosition(int i)
{
    float pt = getParticleTime(i);
    float impulse = quaImpulse(20., pt*0.25+0.05+0.4*random(float(i+30)));
    vec2 initialPos = getParticleInitialPosition(i);
    vec2 velocity;
    // Move mostly right, sometimes left
    velocity.x = 0.4*impulse*sign(random(float(i+66)) - 0.1)*(0.3 + 0.6*random(float(i + 100)));
    // Move vertically in whatever direction particle spawned in
    velocity.y = 0.8*impulse*sign(initialPos.y)*(0.1 + 0.9*random(float(i + 62)));
    return initialPos + getParticleAlive(i) * velocity * pt + vec2(textPos.x, 0.5); // Offset to center
}

float getParticles(vec2 uv)
{
    // Compute contribution from all particles to this frag
    float c = 0.;
    for (int j = 0; j < numParticles; j++) {
        vec2 pos = getParticlePosition(j);
        float d = distance(uv, pos);
        c += (1.-smoothstep(0.004, 0.00835,d))*getParticleIntensity(j);
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
    float mask_rhs = clamp(sign(uv.x-lineWidth-getSweepingLinePos()),0.,1.);
    gl_FragColor += fill_color*mask_rhs*getSpotlights(uv);
    gl_FragColor += mix(vec4(0), particleColor, getParticles(uv));
    gl_FragColor += 2.*particleColor*getBox(uv, textPos.x, textPos.z)*getGradients(uv);
}

`;

function reset_time() {
  restart_anim = true;
}

// https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial/Using_textures_in_WebGL
function loadTexture(gl, url) {
  const texture = gl.createTexture();
  gl.bindTexture(gl.TEXTURE_2D, texture);
  const level = 0;
  const internalFormat = gl.RGBA;
  const width = 1;
  const height = 1;
  const border = 0;
  const srcFormat = gl.RGBA;
  const srcType = gl.UNSIGNED_BYTE;
  const pixel = new Uint8Array([0, 0, 255, 255]);  // opaque blue
  gl.texImage2D(gl.TEXTURE_2D, level, internalFormat,
                width, height, border, srcFormat, srcType,
                pixel);

  const image = new Image();
  image.onload = function() {
    gl.bindTexture(gl.TEXTURE_2D, texture);
    gl.texImage2D(gl.TEXTURE_2D, level, internalFormat,
                  srcFormat, srcType, image);

    // WebGL1 has different requirements for power of 2 images
    // vs non power of 2 images so check if the image is a
    // power of 2 in both dimensions.
    if (isPowerOf2(image.width) && isPowerOf2(image.height)) {
       // Yes, it's a power of 2. Generate mips.
       gl.generateMipmap(gl.TEXTURE_2D);
    } else {
       // No, it's not a power of 2. Turn off mips and set
       // wrapping to clamp to edge
       gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
    }

    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
    loaded = true;
  };
  image.src = url;
  return texture;
}

function isPowerOf2(value) {
  return (value & (value - 1)) == 0;
}

function setupWebGL (evt) {
  window.removeEventListener(evt.type, setupWebGL, false);
  if (!(gl = getRenderingContext()))
    return;

  var vertexShader = gl.createShader(gl.VERTEX_SHADER);
  gl.shaderSource(vertexShader, vert_src);
  gl.compileShader(vertexShader);
  if (!gl.getShaderParameter(vertexShader, gl.COMPILE_STATUS)) {
    var err_str = gl.getShaderInfoLog(vertexShader);
    console.log("Vertex shader compilation failed: " + err_str);
    return;
  }

  var fragmentShader = gl.createShader(gl.FRAGMENT_SHADER);
  gl.shaderSource(fragmentShader, frag_src);
  gl.compileShader(fragmentShader);
  if (!gl.getShaderParameter(fragmentShader, gl.COMPILE_STATUS)) {
    var err_str = gl.getShaderInfoLog(fragmentShader);
    console.log("Fragment shader compilation failed: " + err_str);
    return;
  }

  program = gl.createProgram();
  gl.attachShader(program, vertexShader);
  gl.attachShader(program, fragmentShader);
  gl.linkProgram(program);
  gl.detachShader(program, vertexShader);
  gl.detachShader(program, fragmentShader);
  gl.deleteShader(vertexShader);
  gl.deleteShader(fragmentShader);
  if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
    var err_str = gl.getProgramInfoLog(program);
    console.log("Shader linking failed: " + err_str);
    return;
  }

  buffer = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([
    -1.0, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0, -1.0]), gl.STATIC_DRAW);
  ebuffer = gl.createBuffer();
  gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, ebuffer);
  gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Int8Array([ 0, 1, 2, 3 ]), gl.STATIC_DRAW);

  var pos_attr_loc = gl.getAttribLocation(program, "in_Position");
  gl.vertexAttribPointer(pos_attr_loc, 2, gl.FLOAT, false, 2*4, 0);
  gl.enableVertexAttribArray(pos_attr_loc);
  var tex = loadTexture(gl, "logo_sdf.png")
  var tex_loc = gl.getUniformLocation(program, "tex");
  time_loc = gl.getUniformLocation(program, "iTime");
  gl.useProgram(program);
  gl.viewport(0, 0, gl.canvas.width, gl.canvas.height);
  requestAnimationFrame(render);
}

function render(ts) {
  if (!loaded) {
    requestAnimationFrame(render);
    return;
  }
  if (!(gl = getRenderingContext()))
    return;
  if (pending_disable_fallback) {
    document.getElementById("logo-canvas").style.visibility = "visible";
    document.getElementById("logo-fallback").style.visibility = "hidden";
    document.getElementById("logo-canvas").onclick = reset_time;
    pending_disable_fallback = false;
  }
  gl.clearColor(0, 0, 0, 0);
  gl.clear(gl.COLOR_BUFFER_BIT);
  if (restart_anim) {
    last_started = ts;
    restart_anim = false;
  }
  gl.uniform1f(time_loc, (ts-last_started)/1000.0);
  gl.drawElements(gl.TRIANGLE_FAN, 4, gl.UNSIGNED_BYTE, 0);
  requestAnimationFrame(render);
}

function getRenderingContext() {
  var canvas = document.querySelector("#logo-canvas");
  canvas.width = 512;
  canvas.height = 512;
  var gl = canvas.getContext("webgl");
  if (!gl) {
    return null;
  }
  return gl;
}
})();
