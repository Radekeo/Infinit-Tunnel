#version 330 core

uniform vec2 resolution;
uniform float time;

out vec4 fragColor;
void main() {
    vec2 fragCoord = gl_FragCoord.xy;
    // Normalized pixel coordinates (from 0 to 1)
    vec2 uv = fragCoord / resolution.xy;

    // Time varying pixel color
    vec3 col = 0.5 + 0.5 * cos(time + uv.xyx + vec3(0, 2, 4));

    // Output to screen
    fragColor = vec4(col, 1.0);
}