init python:
    def callback(event, **kwargs):
        if event == "show":
            renpy.music.play("/audio/beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

define n1 = Character(
#what_prefix="\"", 
#what_suffix="\"", 
callback=callback,
)

define n2 = Character(
#what_prefix="\"", 
#what_suffix="\"", 
callback=callback,
)