#here you can define character sprites and backgrounds...
image badlands = "/bg/badlands.png"
image topPark = "/bg/topPark.png"
image parkStairs = "/bg/parkStairs.png"
image greenRoom = "/bg/greenRoom.png"
image televisionRemote = "/itm/televisionRemote.png"
label start:
    # year 2578 - text onscreen
    naja "I wanted to tell you,{w=1} we had a nice time in \"NORTH DAKOTA\""
    # show badlands
    # show naja(?)
    # fade to topPark
    rhue "We've moved on since then, though."
    naja "Coming here was a good decision,{w} I'm really glad we made it."
    calyx "A north takotah?"
    # show parkStairs
    naja "I've seen alot of fearful subjects, perhaps..."
    calyx "Ah, you really have!? {w} I haven't faced anything too terrible, thankfully..." #sprite similar to (;-_-')
    naja "They're out there, somehow. {w} I'ts still daunting to even consider approaching the sights!"
    rhue "They really give me the creeps sometimes,{w} though it's not hard to imaging what they're up to."
    calyx "I see..."
    calyx "Or wait, {w} I guess I haven't yet..! {w} Are these things cool!?"
    naja "Ahh... {w} there's a lot to wonder!"
    # laughing rhue -  need to make sfx
    rhue "Hey, Naja... {w} A little outpost around here, {w} there were a few things you wanted to retrieve, right?"
    naja "!!! {w} You're right, {w} thats right-! {w} I almost forgot!"
    calyx "Oh yeah? {w} It's the light-beam contraption, right??"
    naja "^^ Right, right~! {w}"
    # scene green room
    narrator "They enter a warped building, {w} a twisted small eminates unusually from the walls"
    calyx "{w} All that walking {w}, wow-wow~"
    rhue "It's rare to see you tired, {w} I'm surprised!"
    naja "We've just about got everything to go back home!"
    # clutter sfx
    rhue "Hmm~ {w} Hm.. ? {w} What's this thing..."
    # show television remote 
    # show calyx confused sprite
    rhue "No-way, {w} It's a ramone!"
    naja "I haven't seen one of these in forever!"
    calyx "I-I Really gotta see this!! {w} Can I hold it?"
    naja "Here, here!"
    # beep beep sfx
    # every1 is smiling
    # show rhue puzzled
    naja "I wonder if mog-mog would like it..."
return