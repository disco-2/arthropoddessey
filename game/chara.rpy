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
)

define testchara = Character(
"TEST",
what_color = "#fff",
kind=defaultcharacter,
)