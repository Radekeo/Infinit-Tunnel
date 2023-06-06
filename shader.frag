#version 330 core

layout (location = 0) out vec4 fragColor;

uniform sampler2D u_texture_0;
uniform float PI;
uniform float u_time;
uniform vec2 iRes;

void main() {
    vec2 uv = (gl_FragCoord.xy - 0.5 * iRes.xy)/iRes.y;
    // uv += vec2(0.2 * sin(u_time/2), 0.3 * cos(u_time/3));
    
    
    float phi = atan(uv.y, uv.x);
    float rho = length(uv);

    vec2 fragPos = vec2(phi/PI, 0.2/rho);
    fragPos.x +=  0.1 * u_time;
    fragPos.y += u_time/4;

    vec3 color = texture(u_texture_0, fragPos).rgb;
    color *= rho + 0.2;
    //add light
    color += 0.1/rho * vec3(0.2, 0.2, 0.2);

    fragColor = vec4(color, 1.0);
   
}