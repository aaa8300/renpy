# The script of the game goes in this file.


# settings
define config.name = _('Case File: The Stinging Swindler')

define gui.show_name = True

define config.version = "1.0"

define gui.about = _("Created for Campfire Miami 2026.\n\nCode in Ren'py written by Ana Albornoz.\n\nArt drawn by Hannah Chang. Storyline written by Cing Cin")

define gui.text_font = "OldNewspaperTypes.ttf"
define gui.name_text_font = "OldNewspaperTypes.ttf"




# characters
define queen = Character("Queen", color="#dbe1ff")
define police = Character("Ft. Lauderdale Police Station", color="#6c8cf4")
define detective = Character("You (Detective)", color="#eb446e")
define shocked = Character("Shocked Bystander", color="#e06802")
define old = Character("Senile Old Man", color="#feb546")
define child = Character("Bystander's Child", color="#ffeba9")
define servant = Character("Human Servant", color="#5fdfff")


# scenes
image detective room = im.Scale("office - 2, 5.PNG", 1920, 1080)
image shore = im.Scale("shoreline - 9.PNG", 1920, 1080)
image deep = im.Scale("deep.jpeg", 1920, 1080)
image entrance = im.Scale("entrance.jpeg", 1920, 1080)
image deep = im.Scale("deep.jpeg", 1920, 1080)
image underwater = im.Scale("ocean (before cave) - 10.PNG", 1920, 1080)
image newspaper = im.Scale("newspaper on office - 6.PNG", 1920, 1080)
image anonymous = im.Scale("sillhouettes on office - 7.PNG", 1920, 1080)
image photos = im.Scale("photos in office - 8.PNG", 1920, 1080)
image stacy smile = im.Scale("stacy smile - 3.PNG", 1920, 1080)
image stacy scribble = im.Scale("stacy scribble 1.PNG", 1920, 1080)
image clothing = im.Scale("torn shirt in ocean - 11.PNG", 1920, 1080)
image entrance = im.Scale("ocean cave entrance - 12.PNG", 1920, 1080)
image deep = im.Scale("inside cave - 13.PNG", 1920, 1080)
image kingdom = im.Scale("castle 14.PNG", 1920, 1080)
image throne room = im.Scale("throne room queen 15.PNG", 1920, 1080)
image throne room two = im.Scale("throne room no queen (after sprite shows up) 16.PNG", 1920, 1080)
image hallway = im.Scale("hallway 17.PNG", 1920, 1080)
image black = im.Scale("1920x1080-black-solid-color-background.jpg", 1920, 1080)

# sprites
image queen dark smile = im.Scale("queen dark smile.png", 960, 1080)
image queen mad = im.Scale("queen angry hand up.png", 960, 1080)
image queen happy = im.Scale("queen smile heart.png", 960, 1080)
image queen shocked = im.Scale("queen gasp hand up.png", 960, 1080)
image jellyfish = im.Scale("jellyfish.PNG", 960, 1080)
image servant = im.Scale("servant neutral.PNG", 960, 1080)





# The game starts here.

label start:
    # music
    play music "music idea 1.wav" fadein 0.5

    # PREMISE
    scene newsroom
    "A family was reported missing while going out for a swim. Witnesses say that were suddenly pulled underneath and never came back."
    with fade

    # PART 1: BEGINNING
    scene detective room
    police "Detective, we need you for a new case." 
    detective "I'm not going." 
    police "It's been two years. You can't mope around forever."
    detective "I said I'm not going."
    police "People have been disappearing for months but there has been no sign of success."
    police "Everyone else we've dispatched have not returned."
    detective "So be it."
    police "Detective, you are our last hope. We can't lose anymore people."
    detective "..."
    police "Please, for the sake of the families, we need you to investigate. You understand, don't you? She wouldn't want to see you like this anymore. Solve this. For her."
    with fade
    scene stacy smile
    with fade
    "..."
    scene stacy scribble
    "..."
    with fade
    scene detective room
    detective "...What is it now?"
    police "Fort Lauderdale shore. Around the evening, entire families disappear in the ocean in the blink on an eye. We've sent several experts beneath the surface, but none of them came back. This is urgent. The files are in your mailbox."
    detective "I'll get on it now."
    police "Glad to have you back, pal."
    detective "Yeah…  back at you, donuts. Surprised to see you do anything but eat."
    police "You punk---"
    play sound "audio/phone disconnect.mp3"
    "(Phone disconnects)"
    detective "(Two years, huh?)"
    with fade


    label choices: 
        scene detective room
        menu: 
            "Document 1 - Police Newspaper Statement":
                jump choices1

            "Document 2 - Anonymous Witness Statements":
                jump choices2

            "Document 3 - Photographic Evidence":
                jump choices3

            "Exit":
                jump next


    label choices1:
        scene newspaper
        "The news states that an ancient sea creature may be at fault, and while it is only speculation, there has been evidence of unnatural deep sea sediments found on the shore that raised cause for concern."
        jump choices

    label choices2:
        scene anonymous
        shocked "I WAS THERE! One second they're swimming happily as a family and the next second they're GONE! In the blink of an eye!"
        shocked "I'm not crazy, I swear!"
        shocked "I'm not crazy!"
        child "Mommy, you're scaring me..."
        shocked "I'M NOT---"
        detective "The audio cuts off? Let's see the second statement."

        old "It was a monster, I tell you… It swept 'em in those depths… They ain't coming back alive, if at all."
        detective "They say the elderly either have seen things or are seeing things."
        detective "Usually, I can't tell which it is, but this case seems to be the former."
        jump choices

    label choices3: 
        scene photos
        detective "So it was at 6:11PM... They're gone after two seconds passed?"
        detective "Impossible... Something's up."
        jump choices
    

label next:

    scene detective room
    detective "I finished reviewing the case. I'll grab my briefcase and head over now."
    with fade

# PART 2: UNDERWATER
    scene shore
    "After obtaining scuba gear from a nearby shop, you finally arrive at the shore."
    detective "Let's see what is going on here..."
    "You gather potential traces of evidence from the shore. Then, after suiting up, you head into the ocean."

    play sound "audio/watersplash.mp3"
    with fade
    
    scene underwater
    detective "I've always hated the water… especially after that incident…"
    detective "(No, not now. I can't be thinking about that right now. I need to focus. Focus, darn it!)"
    detective "(Where could have all these people have gone… Hold on. Wait, what's that?)"
    "You swim closer to the ocean floor. Something stood out on the blue."
    scene clothing
    detective "This is… clothing! Looks like it has been torn off... How can it be all the way here?"
    "(You search the area and find a nearby cave)."
    detective "This must be it."
    with fade

    scene entrance
    "(You go deeper and deeper into the cave, but it only gets darker the further along you go, with the only source of light coming from the dim flashlight from your scuba helmet.)"
    with fade

    scene deep
    detective "It's a dead end..."
    "You continue searching for any more leads, until noticing a strange message carved on the wall with an empty altar right below it."
    detective "'In the deep, there is no light. In the dark, will be your blight. There's no escape from their deadly sting. All you can do is hope that you'd bring a pinch of sodium and chlorine.'"
    detective "(This altar... looks like I need to put something there.)"
    "(You search your briefcase for something you can put there that aligns with the message. You come across two options.)"
    
    label altar:
        menu:
            "Option 1 - Place Salt on Altar":
                play music "music idea 2.wav" fadein 2.0
                play sound "audio/crumble.mp3"
                "(The entire cave shakes. The wall breaks open and reveals more ocean beyond.)"
                with fade
                jump kingdom

            "Option 2 - Place Pepper on Altar":
                stop music fadeout 2.0
                play sound "audio/Thud Sound Effect.mp3"
                "(Heavy currents rush through the cave and sweeps you away uncontrollably. You crash your head into another wall, pass out, and drown.)"
                scene black
                with fade
                detective "(Stacy...)"
                "GAME OVER"
                return
    

# PART 3: HIDDEN KINGDOM
label kingdom:
    
    scene kingdom
    "(You enter a new world — what looks like an underwater kingdom. However, you can't shake off this uncanny feeling that something's off… that something more sinister lies beneath the surface.)"
    detective "An underwater kingdom?  It's suspiciously quiet… Is it abandoned?)"
    detective "(You'd think there would be a singing little mermaid and a harmonizing chorus of crustaceans under the sea.)"
    "(You head into the biggest structure of the kingdom — the castle. Despite the danger, your intuition tells you that the truth of the matter can finally be found in there…)"
    with fade

    scene hallway
    "(You pass through the kingdom's interior hallways, luxurious yet run-down… beautiful yet eerie… Until you notice horrendous.)"
    detective "Are those… human-shaped skulls? Displayed so arrogantly in plain view? If these are real, what kind of ludricrous beast could be hiding down here…"
    scene black 
    with fade
    "(You continue exploring the vast kingdom decorated with death… until stepping into the heart of the castle, the Queen's throne room.)"
    scene throne room
    "(Just around the corner, you can feel the a dreadful prescence and a pressing instinct to flee.)"
    detective "(But you need to get to the bottom of this case. For her.)"
    detective "(For the lives who were lost. For the families that are suffering.)"
    detective "(That's why you decided to be a detective in the first place. You can't make the same mistake again.)"
    "(In that instant, the Queen felt a disturbance in the force, noticing your presence.)"
    scene throne room two

    show queen shocked
    queen "A human? Here?"
    "(Her voice alone made you tremble. You couldn't move, let alone speak.)"
    show queen happy
    queen "I LOVE humans! You cute, scrumptious little sea rodents! How did you get here?"
    detective "Do you know of the disappearance of humans recently? Traces of human activity leads me to—"
    show queen mad
    queen "It's your MAJESTY to you, peanut-brained peasent. Humans… Always so nosy…"
    show queen dark smile
    queen "But I just love humans… I want to befriend all of them and have them join me in my castle eternally! Wouldn't that just be a dream come true?"
    queen "I've already done it a couple of times… I would just LOVE to have more over, of course…."
    detective "Just what have you been---"
    
    play sound "audio/Crash.mp3"
    scene black
    with fade


    # PART 4: DEEP DIVE

    # with fade
    scene throne room two 
    show queen shocked
    queen "Just a moment, dear..."
    "(The Queen momentarily leaves the room to check on the strange sound.)"
    hide queen
    detective "I need to hurry and get out of here."
    "(You quickly investigate the room before the Queen can get back. After checking several rooms, there comes an unexpected character…)"
    scene black
    play sound "audio/thud-ouch.mp3"
    with fade
    scene hallway
    show servant
    detective "What the... wait-- a human?!"
    "Human Servant" "..."
    detective "Are you... okay?"
    detective "(This person doesn't look... normal... but it's a person, isn't it?)"



    label human: 
        menu: 
            "Save the Suspicious 'Human'":
                detective "Come with me."
                scene black 
                with fade
                play sound "audio/paper-tear-sound-effect.mp3"
                "(You grab hold of the servant's hand, but it tears away the disguise, revealing what's underneath…)"
                scene hallway
                show jellyfish
                play sound "audio/electrocute_NOdcFrc.mp3"
                "(The jellyfish underling kills you with its poisonous sting.)"
                scene black
                with fade
                "GAME OVER"
                return
            "Fight the Suspicious 'Human'":
                detective "Die, you quack!"
                
                play sound "audio/Thud Sound Effect.mp3"
                scene black
                with fade

                scene hallway
                show jellyfish
                detective "What..?!"
                show queen mad
                queen "YOU!!! DIE!!!"

                jump finale


            
# PART 5: FINALE
label finale:

    play music "chase idea 2.mp3" fadein 0.5
    hide queen
    "(You try to flee and escape with evidence, but the Queen gains speed from the currents and stretches out its venomous tentacles.)"
    detective "(I need to make a move to survive.)"
    scene kingdom
    "(As you approach the exit, you spot the salt you placed on the altar.)"


    label end:
        menu:
            "Do Not Throw Salt":
                stop music fadeout 2.0
                play sound "audio/electrocute_NOdcFrc.mp3"
                scene black
                with fade
                "(You get caught up by all the jellyfishes, get stinged to death, and brutally eaten by the Queen.)"
                detective "(Stacy...)"
                "GAME OVER"
                return
            "Do Throw Salt":
                stop music fadeout 2.0
                "(The salt temporarily stops the Queen and you escape the cave…)"
                scene black
                with fade
                "Humans..."
                "..."
                "(Success!! You escaped in one piece... for now.)"
                with fade
                return
