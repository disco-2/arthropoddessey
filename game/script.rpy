#here you can define character sprites and backgrounds...
image chara test = "test chara.png"
image test bg = "test bg.png"
label start:

scene test bg
show chara test at left

n2 "hi :-)"
n2 "this is a very barebones project file tbh..."
n2 "there is a really good tutorial included with renpy,{w} i recommend checking it out to ge a good idea of how renpy works!!"
n2 "use the n2 character for most dialogue"
n1 "and always use n1 before a screen wipe!"


show chara test at right

n2 "theres also a simple sound effect (/audio/beep.ogg) that plays on loop whenever text appears on screen..."
n2 "we can make it a beep.. typewriter noise.. bug chirp, whatever!"
n1 "thats about it lol{w} ask me if you want me to add anything else.. ^^"

return