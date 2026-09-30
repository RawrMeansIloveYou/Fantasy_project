init offset = -1

transform crystal_ball_float:
    subpixel True
    xalign 0.5
    ypos 230
    on appear, show:
        linear 1.0 ypos 210
        block:
            linear 2.0 ypos 260
            linear 2.0 ypos 230
            repeat
    on hide:
        easein_expo 0.5 ypos 225

transform crystal_ball_stop:
    subpixel True
    xalign 0.5
    ypos 225
    alpha 0.0
    on show:
        time 0.5
        alpha 1.0
    on hide:
        alpha 0.0