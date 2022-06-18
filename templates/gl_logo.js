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

  var source = document.querySelector("#vertex-shader").innerHTML;
  var vertexShader = gl.createShader(gl.VERTEX_SHADER);
  gl.shaderSource(vertexShader,source);
  gl.compileShader(vertexShader);
  if (!gl.getShaderParameter(vertexShader, gl.COMPILE_STATUS)) {
    var err_str = gl.getShaderInfoLog(vertexShader);
    console.log("Vertex shader compilation failed: " + err_str);
    return;
  }

  source = document.querySelector("#fragment-shader").innerHTML
  var fragmentShader = gl.createShader(gl.FRAGMENT_SHADER);
  gl.shaderSource(fragmentShader,source);
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
  var canvas = document.querySelector("canvas");
  canvas.width = 512;
  canvas.height = 512;
  var gl = canvas.getContext("webgl");
  if (!gl) {
    return null;
  }
  return gl;
}
})();
