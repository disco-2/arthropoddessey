#here you can define character sprites and backgrounds...
image badlands = "/bg/badlands.png"
image topPark = "/bg/topPark.png"
image parkStairs = "/bg/parkStairs.png"
image greenRoom = "/bg/greenRoom.png"
image televisionRemote = "/itm/televisionRemote.png"
label start:
    # year 2578 - text onscreen
    # naja sprite is in /chara, it is called naja_3_1.png
    # show naja_3_1 i this like
    show naja neutral at left
    n "I wanted to tell you,{w=1} we had a nice time in \"NORTH DAKOTA\""
    # show badlands
    # show n(?)
    # fade to topPark
    # flip naja sprite
    show rhue happy at right:
        xzoom -1
    r "We've moved on since then, though."
    show naja happy at left
    n "Coming here was a good decision,{w} I'm really glad we made it."
    show calyx confused arms crossed at center
    c "A north takotah?"
    # show parkStairs
    show naja confused  at left
    n "I've seen alot of fearful subjects, perhaps..."
    show calyx angry at center:
        xzoom -1
    c "Ah, you really have!? {w} I haven't faced anything too terrible, thankfully..." #sprite similar to (;-_-')
    show naja happy at left
    n "They're out there, somehow. {w} I'ts still daunting to even consider approaching the sights!"
    show rhue confused at right:
        xzoom -1
    r "They really give me the creeps sometimes,{w} though it's not hard to imaging what they're up to."
    show calyx confused at center
    c "I see..."
    show calyx happy arms out at center
    c "Or wait, {w} I guess I haven't yet..! {w} Are these things cool!?"
    show naja happy at left
    n "Ahh... {w} there's a lot to wonder!"
    # laughing r -  need to make sfx
    show rhue happy at right:
        xzoom -1
    r "Hey, naja... {w} A little outpost around here, {w} there were a few things you wanted to retrieve, right?"
    show naja happy arms out at left
    n "!!! {w} You're right, {w} thats right-! {w} I almost forgot!"
    c "Oh yeah? {w} It's the light-beam contraption, right??"
    n "^^ Right, right~! {w}"
    # scene green room
    narrator "They enter a warped building, {w} a twisted small eminates unusually from the walls"
    c "{w} All that walking {w}, wow-wow~"
    r "It's rare to see you tired, {w} I'm surprised!"
    n "We've just about got everything to go back home!"
    # clutter sfx
    r "Hmm~ {w} Hm.. ? {w} What's this thing..."
    # show television remote 
    # show c confused sprite
    r "No-way, {w} It's a ramone!"
    n "I haven't seen one of these in forever!"
    c "I-I Really gotta see this!! {w} Can I hold it?"
    n "Here, here!"
    # beep beep sfx
    # every1 is smiling
    # show r puzzled
    n "I wonder if mog-mog would like it..."
return