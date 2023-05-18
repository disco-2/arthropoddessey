init python:
    def callback(event, **kwargs):
        if event == "show":
            renpy.music.play("/audio/beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

define n1 = Character(
ctc="page_ctc",
ctc_pause="arrow_ctc",
kind=nvl, 
ctc_position="nestled",
#what_prefix="\"", 
#what_suffix="\"", 
what_style="nvl",
callback=callback,
)

define n2 = Character(
ctc="arrow_ctc",
ctc_pause="arrow_ctc",
kind=nvl, 
ctc_position="nestled",
what_style="nvl",
#what_prefix="\"", 
#what_suffix="\"", 
callback=callback,
)