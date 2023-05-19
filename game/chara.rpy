init python:
    def callback(event, **kwargs):
        if event == "show":
            renpy.music.play("/audio/beep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

#defualt character, use kind=defaultcharacter on future characters to use these settings as default
define defaultcharacter = Character(
ctc="page_ctc",
ctc_pause="arrow_ctc",
ctc_position="nestled",
callback=callback,
what_color="#ff0000",
)

<<<<<<< HEAD
define n2 = Character(
#what_prefix="\"", 
#what_suffix="\"", 
callback=callback,
what_color="#00f",
=======
define testchara = Character(
"TEST",
what_color = "#fff",
kind=defaultcharacter,
>>>>>>> c8b12b98e2a3636f36e30a31e3767543c9957922
)