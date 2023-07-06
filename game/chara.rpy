#defualt character, use kind=defaultcharacter on future characters to use these settings as default
define defaultcharacter = Character(
what_prefix="\"",
what_suffix="\"",
ctc="page_ctc",
ctc_pause="arrow_ctc",
ctc_position="nestled",
what_color="#000",
nvl_mode=True,
)

define n2 = Character(
#what_prefix="\"", 
#what_suffix="\"", 
what_color="#00f",
)

define narrator = Character(
"",
what_color = "#000",
kind=defaultcharacter,
)

define n = Character(
"naja",
what_color = "#11c",
)

define r = Character(
"rhue",
what_color = "#c11",
)

define c = Character(
"calyx",
what_color = "#1a1",
)