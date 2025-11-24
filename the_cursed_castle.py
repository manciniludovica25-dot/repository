CASTLE_ART = r"""
                                                  ,.=,,==. ,,_ 
                                    _ ,====, _    |I|`` ||  `|I `| 
                _|\_,              |`I|    || `==,|``   ^^   ``  |
        ,.--,   \_ `a\_            | ``    ^^    ||_,===TT`==,,_ | 
   6^`--:_ ||  ,/  ,-,,\           |,==Y``Y==,,__| \L=_-`'   +J/`
  / \```\ \|\_/ /-/\\  `            \|=_  ' -=#J/..-|=_-     =|
 /  \.., | \/  /-/  `                |=_   -;-='`. .|=_-     =|----T--,
 /   \..,'|    /-|                   |=/\  -|=_-. . |=_-/^\  =||-|-|::|____
    \__     \_L-==,                  |=||  -|=_-. . |=_-| |  =|-|-||::\____
    |  /   \_.-..=                   |=LJ  -|=_-. . |=_-|_|  =||-|-|:::::::
    \ /    /--_/\                    |=_   -|=_-_.  |=_-     =|-|-||::::::
   _J`   .'-_,/\_``=                 |=_   -|=//^\. |=_-     =||-|-|:::::::
`X`    \/--_/    `-`             ,   |/&_,_-|=||  | |=_-     =|-|-||:::::::
/   \   |_/                   ,--``8%,/    ',%||  | |=_-     =||-|-|%::::::
   _/  / /                ,---`_,888`  ,.'''''`-.,|,|/!,--,.&\|&\-,|&#:::::
./`; /`/`                |;:;K`__,...;=\_____,=``           %%%&     %#,--- 
    \\\\                 |;::::::::::::|       `'.________+-------\   `` 
     w w           |    /8M%;:::;;:::::|                  |        `-------
                   |   |`   88`V  /&8%\|_______,__,,      |
                   |   /,  %8,  ,/&888% &,       ,  `-----`,--..../|--,,,,_
                  / \/88%  88%  8888%88% &,       \,     `\      /     &,,
                  |,M8,  , `8%   ,,8% `8, `         , \,        &\     ,&##
                 /8888%  888`    ```    `            `  `               ```
"""

GAME_OVER_ASCII = r'''
 _____                                                               _____ 
( ___ )-------------------------------------------------------------( ___ )
 |   |                                                               |   | 
 |   |   ___|                                _ \                     |   | 
 |   |  |       _` |  __ `__ \    _ \       |   | \ \   /  _ \   __| |   | 
 |   |  |   |  (   |  |   |   |   __/       |   |  \ \ /   __/  |    |   | 
 |   | \____| \__,_| _|  _|  _| \___|      \___/    \_/  \___| _|    |   | 
 |___|                                                               |___| 
(_____)-------------------------------------------------------------(_____)
'''

TITLE_ASCII = r'''   _____                                                                        _____ 
( ___ )----------------------------------------------------------------------( ___ )
 |   |                                                                        |   | 
 |   |   ____          _   _        _____       _                             |   | 
 |   |  / ___|__ _ ___| |_| | ___  | ____|_ __ | |_ _ __ __ _ _ __   ___ ___  |   | 
 |   | | |   / _` / __| __| |/ _ \ |  _| | '_ \| __| '__/ _` | '_ \ / __/ _ \ |   | 
 |   | | |__| (_| \__ \ |_| |  __/ | |___| | | | |_| | | (_| | | | | (_|  __/ |   | 
 |   |  \____\__,_|___/\__|_|\___| |_____|_| |_|\__|_|  \__,_|_| |_|\___\___| |   | 
 |___|                                                                        |___| 
(_____)----------------------------------------------------------------------(_____) '''

END = r'''
 _____                                        _____ 
( ___ )--------------------------------------( ___ )
 |   |                                        |   | 
 |   |  _____ _            _____           _  |   | 
 |   | |_   _| |__   ___  | ____|_ __   __| | |   | 
 |   |   | | | '_ \ / _ \ |  _| | '_ \ / _` | |   | 
 |   |   | | | | | |  __/ | |___| | | | (_| | |   | 
 |   |   |_| |_| |_|\___| |_____|_| |_|\__,_| |   | 
 |___|                                        |___| 
(_____)--------------------------------------(_____)
'''

AMULET_ART = r'''

  ____
 /\__/\
/_/  \_\
\ \__/ /
 \/__\/
 
 '''

KING_ASCII_ART = r'''


                             .
                            / \
                           _\ /_
                 .     .  (,'v`.)  .     .
                 \)   ( )  ,' `.  ( )   (/
                  \`. / `-'     `-' \ ,'/ 
                   : '    _______    ' :
                   |  _,-'  ,-.  `-._  |
                   |,' ( )__`-'__( ) `.| 
                   (|,-,'-._   _.-`.-.|)
                   /  /<( o)> <( o)>\  \ 
                   :  :     | |     :  :
                   |  |     ; :     |  |
                   |  |    (.-.)    |  |
                   |  |  ,' ___ `.  |  |
                   ;  |)/ ,'---'. \(|  :
               _,-/   |/\(       )/\|   \-._ 
         _..--'.-(    |   `-----'   |    )-.`--.._
                  `.  ;`._________,':  ,'
                 ,' `/               \'`. 
                      `------.------'          
                             '



'''

def king():
    print(KING_ASCII_ART)

def game_over():
    print(GAME_OVER_ASCII)

def amulet():
    print(AMULET_ART)

has_amulet = False


def node_entry():
    print(CASTLE_ART)

    print("Welcome to the Cursed Castle.")
    print("Your mission is to break the king’s ancient curse.")
    print("A cold mist wraps around the walls. Once you enter, leaving won’t be easy.")
    print('Distant voice: "Go back while you can..."')

    print(TITLE_ASCII)

    print("You stand before the castle. The main gate is sealed shut.")
    print("On one side there is a misty courtyard, on the other a staircase leading down to the crypt.")
    print('You: "I don’t have many choices… I must pick a way in."')
    print('Whispering voice: "Light deceives, shadow reveals..."')

    entry = input('Do you enter through the "courtyard" or the "crypt"?\n')

    if entry == "courtyard":
        node_courtyard()
    elif entry == "crypt":
        node_crypt()
    else:
        game_over()


def node_courtyard():
    print("You slip through a side door and step into the courtyard, wrapped in unnatural fog.")
    print("To your left you see a tall tower, to your right the ruins of the old stables.")

    print('You: "Something is watching me from inside this fog…"')
    print('Whisper in the mist: "Climb high to see the truth… or walk where the horses never sleep."')

    courtyard = input('Where do you go: the "tower" or the "stables"?\n')

    if courtyard == "tower":
        node_tower()
    elif courtyard == "stables":
        node_stables()
    else:
        game_over()


def node_tower():
    print("You climb the spiral staircase of the tower.")
    print("At the top you find a circular chamber.")
    print("A ghostly knight in broken armor stands in the shadows, watching you.")

    print('Ghost Knight: "Few dare to come this far."')
    print('You: "Who are you?"')
    print('Ghost Knight: "I am the guardian of the true throne. I can help you… if you listen."')

    knight = input('Do you "listen" to the knight or do you "ignore" him and move on alone?\n')

    if knight == "listen":
        print("You gain a hint.")
        print("You step closer. The knight lowers his voice.")
        print('Ghost Knight: "Remember these words: \'The true throne never shines.\'"')
        print('Ghost Knight: "When you reach the throne room, choose what is cold, dull, and forgotten."')
        node_prison()
    else:
        print("You turn your back on the knight and grab a wooden door on the opposite side.")
        print("Spectral chains coil around your arms.")
        print('Ghost Knight: "Those who refuse to listen do not deserve freedom."')
        game_over()


def node_stables():
    global has_amulet

    print("You enter the stables. The smell of rotten straw and rust fills the air.")
    print("In one corner, a faintly glowing amulet lies on a pile of bones.")
    print("Further inside, a ghost horse watches you with empty eyes.")

    print('You: "This place is even worse than the courtyard."')
    print('Low whisper: "Every gift has a price… every escape has a cost."')

    stables = input('What do you do: take the "amulet" or mount the "horse"?\n')

    if stables == "amulet":

        has_amulet = True
        print("You gain the amulet.")
        amulet()

        node_crypt()
    elif stables == "horse":
        print("You mount the ghost horse and escape the castle… but the curse remains.")
        print(END)
    else:
        game_over()


def node_crypt():
    print("You walk into the crypt corridor.")
    print("Ahead, a rope bridge hangs over a bottomless pit and a narrow ledge runs along the wall.")

    print('You: "I don’t trust that bridge, but the ledge looks dangerous too."')
    print('Voice in the dark: "The easiest way is usually the shortest…"')

    choice = input('Do you cross the "bridge" or follow the "ledge"?\n')

    if choice == "ledge":
        node_hall_of_candles()
    elif choice == "bridge":
        node_shaky_bridge()
    else:
        game_over()


def node_shaky_bridge():
    print("You step onto the rope bridge. Each step makes the wooden planks creak.")
    print("The ropes creak and stretch dangerously.")

    print('You: "This was a bad idea…"')
    print('Uneasy voice: "Go on… or turn back while you still can."')

    bridge = input('Do you "continue" crossing or do you "turn" back?\n')

    if bridge == "continue":
        print("You take a few more steps. A rope snaps. The bridge falls and you plunge into the abyss.")
        game_over()
    elif bridge == "turn":
        node_hall_of_candles()
    else:
        print("You hesitate in the middle of the bridge. The ropes give way and you fall.")
        game_over()


def node_hall_of_candles():
    print("You reach a hall lit by black candles that burn without smoke.")
    print("Two doors stand before you: one marked with the symbol of a book (the library), "
          "the other sealed with iron bars (the prison).")

    print('Whispering voice: "Knowledge or mercy… what do you choose?"')
    print('You: "I need to get closer to the truth… but how?"')

    hall = input('Do you enter the "library" or the "prison"?\n')

    if hall == "library":
        node_cursed_library()
    elif hall == "prison":
        node_prison()
    else:
        game_over()


def node_cursed_library():
    print("The library is filled with towering shelves. Only one book lies open on a stone lectern.")
    print("Its pages turn by themselves, as if moved by an invisible hand.")

    print('Voice from the book: "Finally, someone brave enough to read."')
    print('You: "What is this curse?"')
    print('Voice from the book: "The throne that shines brightest is the one that destroys."')

    book = input('What do you do: "read" the book, "talk" to the voice, or "tear" out a page?\n')

    if book == "read":
        print("You carefully read the moving lines.")
        print('Voice: "Remember: Gold deceives, wood betrays, only stone survives time."')
        print("You feel you understand which throne might be the right one.")
        node_cursed_throne_room()

    elif book == "talk":
        print('You: "Who created the curse?"')
        print('Voice: "A king who wanted to shine brighter than the sun."')
        print('Voice: "Do you want power in his place?"')

        power = input('Do you answer "yes" or "no"?\n')

        if power == "yes":
            print("The book slams shut. A burning mark appears on your skin.")
            print("You become the new keeper of the curse. The castle is yours, but you are never free.")
            king()
        elif power == "no":
            print("The voice falls silent. A hidden door opens behind you.")
            node_cursed_throne_room()
        else:
            print("You hesitate, giving no clear answer. The pages close and the hall fades away.")
            game_over()

    elif book == "tear":
        print("You rip out a page. The letters turn into fiery moths and circle around you.")
        print('Voice: "Knowledge does not break so easily."')
        print("Flames rise and consume you.")
        game_over()

    else:
        game_over()


def node_prison():
    global has_amulet

    print("You descend a few stone steps and reach a small prison cell.")
    print("Behind the bars, the ghostly figure of a chained king sits in silence.")

    print('Ghost King: "Stranger… have you come to free me or replace me?"')
    print('You: "Are you the source of the curse?"')
    print('Ghost King: "I tried to stop it, but now I am only a prisoner."')

    choice = input('Do you "free" the king or do you "ignore" him and move on?\n')

    if choice == "free":
        if has_amulet:
            print("You reach for the chains. The amulet grows warm and the ghostly shackles break.")
        else:
            print("You reach for the chains. A pale light surrounds your hands and the shackles break anyway.")
        print('Ghost King: "Your mercy will not be forgotten."')
        print('Ghost King: "Take this stone key. It opens the way to the throne room."')
        king()
        node_cursed_throne_room()
    elif choice == "ignore":
        print("You walk past the cell, leaving the king in chains, and follow the corridor to a large hall.")
        node_cursed_throne_room()
    else:
        print("You hesitate, and the chains turn into serpents of shadow that coil around you.")
        game_over()


def node_cursed_throne_room():
    print("You enter the cursed throne room.")
    print("Three thrones await you: one of stone, one of wood, and one of gold.")

    print('Echoing voice: "Gold deceives, wood betrays, only stone survives."')
    print('Whisper: "Choose wisely… or take the king\'s place."')

    throne = input('On which throne do you sit: "stone", "wood", or "gold"?\n')

    if throne == "stone":
        print("You sit on the stone throne. It is cold, but solid.")
        print("The green flames around the hall die out one by one.")
        print("The curse is broken. You are free… and so is the castle.")
        print(END)
    elif throne == "wood":
        print("You sit on the wooden throne. At first it feels harmless.")
        print("Dark roots grow from the armrests and wrap around your body.")
        print('Voice: "Those who seek comfort find only prison."')
        game_over()
    elif throne == "gold":
        print("You sit on the golden throne, dazzled by its shine.")
        print("The metal heats up, turns red-hot, and flames engulf you.")
        print('Voice: "You chose the shine of the curse."')
        game_over()
    else:
        print("You try not to choose at all, but the hall will not allow it.")
        print("Shadows drag you away from the thrones.")
        game_over()


if __name__ == "__main__":
    node_entry()
