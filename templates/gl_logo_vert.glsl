#version 100
attribute vec2 in_Position;
attribute vec2 in_Texcoord;
varying vec2 Texcoord;
void main() {
    Texcoord = in_Texcoord;
    gl_Position = vec4(in_Position, 0.0, 1.0);
}
