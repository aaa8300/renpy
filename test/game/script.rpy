# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define queen = Character("Queen", color="#c8ffc8")
define police = Character("Ft. Lauderdale Police Station", color="#c8c8ff")
define detective = Character("Detective", color="#ffc8c8")
image detective room = im.Scale("detective room.jpeg", 1920, 1080)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # PREMISE
    scene newsroom
    "A family was reported missing while going out for a swim. Witnesses say that were suddenly pulled underneath and never came back."
    with fade

    # PART 1: BEGINNING
    scene detective room
    police "Detective, we need you for a new case." 
    detective "Detective here, what's the issue?" 
    police "There's been a missing persons case for a while now, but there has been no sign of success. The files are in your mailbox."
    detective "I'll get on it now."
    with fade

    label choices: 
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
        "Shocked Bystander" "I WAS THERE! One second they're swimming happily as a family and the next second they're GONE!"
        "Senile Old Man" "It was a monster, I tell you… It swept 'em in those depths… They ain't coming back alive, if at all."
        jump choices

    label choices3: 
        # scene photos
        jump choices
    

label next:
    scene detective room
    detective "I finished reviewing the case. I'll grab my briefcase and head over now."
    with fade

# PART 2: UNDERWATER
    scene shore
    "After obtaining scuba gear from a nearby shop, the Detective finally arrives at the shore."
    detective "Let's see what is going on here..."
    "The Detective gathers potential traces of evidence from the shore. Then, after suiting up, the Detective heads into the ocean."
    
    # splash sound effect
    scene shore
    with fade
    
    scene underwater
    detective "Where could these people have gone... Wait, what's that?"
    # insert photo of tattered summer clothing
    detective "This is… a piece of clothing! How can it be all the way here?"
    "(The Detective looks around the area of the clothing)."
    detective "A cave!"
    with fade

    scene entrance
    "(The Detective goes deeper and deeper into the cave, but it only gets darker and darker, with the only source of light coming from the dim flashlight from the Detective's helmet.)"
    with fade

    scene deep
    detective "It's a dead end..."
    "The Detective continues searching for any more leads, until noticing a strange message carved on the wall with an empty altar right below it."
    with fade
    "'In the deep, there is no light. In the dark, will be your blight. There's no escape from their deadly sting. All you can do is hope that you'd bring a pinch of sodium and chlorine.'"










    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy


    # These display lines of dialogue.
    # e "You've created a new Ren'Py game."


    # This ends the game.

    return
