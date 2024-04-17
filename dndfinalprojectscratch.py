#this version of the project is far smaller than it was meant to be. I cant afford an incomplete on this class so I am taking my chances.
#please keep in mind that I lost close to 1600 lines of code in my crash, which included multiple core mechanics of the game that took a very long time
#to figure out, including a class system including 4 different chracter classes with unique abilities and skills, a magic system, full
#combats against various monsters, and several non-player characters to interact with. I've done the best I can in the last few weeks to recreate it.

'''TO BUGFIX: FIXED
-add part to khirn square for coming back to talk to Dis
-add dialogue to Dis indicating that Gimli always wore a red cape and that she would like to see him again
-add part to khirn square for if Dis remembers the attack, bringing her Gimli's cape
-add part to khirn square for bringing Dis gimli's red cape
-make sure manhole and other similar variables stay constant

ONGOING
-General:
    -Add better spacing between text segments for easier reading FIXED
    -Health display has an extra space before current hp FIXED
-Great Gates:
    -hidden door text great gates: says partally instead of partially FIXED
-Sewer:
    -sewer text: sitting is cut off at sitti FIXED
    -investigate backpack and backpack dont work FIXED
-Otyugh:
    -otyugh text displays janky
    -throwing rubble not obvious, should implement an investigate option NO NEED, PLAYER MUST THINK
    -add investigate treasure and investigate mudpit to prompts FIXED
    -pit is misspelled 'bit' in look around FIXED
    -words cut off in look around display FIXED
    -go to treasures only works in plural FIXED
    -go to treasure text is cut off FIXED
-Cistern:
    -thieves' cant is misspelled FIXED
    -no hidden passages were added after hint from writing, add or remove? REMOVED>> FIXED
    -buy is misspelled by in balins intro FIXED
    -make balin tell the player about the manhole exit FIXED
    -courtyard or square doesnt have a space after for input FIXED
    -wierdness with look around between cistern and sewer, test if im an idiot or if an actual bug FIXED
-Khirn Square:
    -make it more clear the the collapsed house and rubble are seperate FIXED
    -statue arcana: fairly spell wrong FIXED
    -run on sentences with Dis NO ISSUE
    -climbing or lifting rubble successfully causes crash FIXED
    -investigating collapsed house more than once repeates the sequence FIXED
-Market:
    -Going backwards while climbing rubble continuously loops FIXED
    -E is cut off in return text for Khirn Square FIXED
    -text when entering through rubble is janky
    -update scrawl to show skeleton FIXED
    -approaching goblin nest loop forces you to choose sneak or approach twice before displaying outcome FIXED
    -goblin wreckage text is cut off NO ISSUE
-Church:
    -text is janky, multiple typos FIXED
    -add flick coin option FIXED
    -add space after entre y/n FIXED
    -add a pray option in church? NO
    -make it clear that after choices conclude, you leave the church FIXED
    -leaving offering breaks the loop FIXED
-Grand Hall:
    -text janky on walk up FIXED
-Audience Chamber:
    -no lok around function FIXED
    -no go back function FIXED
    -staircase spelled wrong FIXED
-Dungeon:
    -if picking the cell doesn't work, the game can't be won, add a key rack somewhere with the dungeon key FIXED
    - conflicting text about cell being locked or not FIXED'''

import random
import sys


def d(sides):
    roll=int(random.randint(1, sides))
    return roll

inventory = ['Healing Potion']
merchantinventory= ['Healing Potion', 'Healing Potion', 'Ornate Key']
global merchantgold
merchantgold=20

global hp, hpmax
global talktodis
talktodis=0  #0=cant talk to her, 1=can come back, 2=questline complete, dis is happy but not moved on yet
global disremembers
disremembers=0
global dismovedon
dismovedon=0
global invhouse
invhouse=0
global houselocked
houselocked=0
global prayer
prayer=0
global secretdoor
secretdoor=0
global manhole
manhole=0
global merchnotice
merchnotice=0
global merchdead
merchdead=0
global pocketempty
pocketempty=0
global shopsopen
shopsopen=0
global sewerdooropen
sewerdooropen=0
global goblins
goblins=1
global bookshelfdooropen
bookshelfdooropen=0
global valeanmovedon
valeanmovedon=0
global celllocked
celllocked=1
global foundarch
foundarch=0
global streetclear
streetclear=0
global codelockfound
codelockfound=0


class actions():
    def strcheck():
        s=d(20)+strmod
        return s
    def dexcheck():
        dexteritycheckeroo=d(20)+dexmod
        return dexteritycheckeroo
    def concheck():
        c=d(20)+conmod
        return c
    def intcheck():
        i=d(20)+intmod
        return i
    def wischeck():
        w=d(20)+wismodifier
        return w
    def chacheck():
        c=d(20)+chamod
        return c
    def inventory():
        print(inventory)
        print('You have', gold, 'gold remaining.')
        return inventory, gold
    def health():
        print('You have',hp, 'out of', hpmax, 'hp left.')
    def healingpotion():
        global hp, hpmax
        hp+=d(4)+4
        if hp > hpmax:
            hp=hpmax
        print('''Health restored''')
        print('You now have ',hp, 'out of', hpmax, 'hp left.')


class dnd():
    def intro():
        print('''Oh you poor soul. You truly wish to embark on this journey? Knowing the chance you're taking?
Well, I never did vouch for the sanity of adventurers, and I won't start now. I will be your narrator for this evening,
you can simply call me D. I'm here to walk you through everything from creating your character, to the rules of the game, to 
decribing your surroundings to you as you progress. But we'll start simple.''')
        print()
        print('''Your character will be defined, mechanically speaking, by 6 statistics. Strength, Dexterity, Constitution,
Intelligence, Wisdom, and Charisma. Each of these govern different skills and tasks you may have to perform, providing a small bonus
or penalty to rolls you make depending on the score. For example, if you attempt to move a large piece of rubble blocking your path, 
you roll a strength check. If your strength is higher, you have a better chance of being able to get past.''')
        print()
        while True:
            c=input('''Type continue when ready. ''')

            if c == 'continue':
                break
            else:
                print('Just type continue when you are ready to move on.')
        print()
        print('''The most important and common of the skills are:
- Perception: Uses wisdom, allows you to look around and reveal information. Prompted by 'look around' or 'perception'.
- Investigation: Uses intelligence, allows you to take a detailed look at specific places in the room. Prompted with 'investigate...'.
- Arcana: Uses intelligence, alloww you to recall specific information relating to magic, monsters, or other esoteric fields about objects or things around you. Prompted with 'arcana on ...'
- History: Uses intelligence, allows you to recall historical information about an object, place, or thing to recieve context or clues. Prompted with 'history on...' or 'history of..'
- Athletics: Uses strength, will be used to perform feats of raw strength like breaking down a door. Prompted with specific text based on the action.
- Stealth: Uses dexterity, will be used to sneak past enemies. Prompted with 'sneak', but will sometimes be unavailable due to not being relevant.
- Lockpick: Uses dexterty, wll be used to attmept to pick locks on doors or chests. Prompted by 'pick lock on...'
There are other actions you can take, but they are not nearly as common. Don't be afraid to try something that isn't obvious, you might find a secret.
Your constitution will also determine your health. You can loose health by failing certain checks, encountering enemies, 
or falling for a trap.
If your hp reaches 0, you die and lose the game. There are health potions scattered around the map which restore small amounts of hp.''')
        print('''You will be able to allocate scores to these stats, choosing which stat gets which score from a list.''')
        while True:
            m=input('''When you are ready to allocate scores, type continue. ''')

            if m=='continue':
                break
            else:
                print('''Just type continue when you are ready to move on. ''')

        stan=[15, 14, 13, 12, 10, 8]
        stre=0
        dex=0
        con=0
        inte=0
        wis=0
        cha=0
        stats=[stre, dex, con, inte, wis, cha]
        statnames=['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']

        while True:
            for i in range (0, len(stats)):
                print('Available Scores: ', stan)
                x=int(input('Which score for {}? '.format(statnames[i])))
                if x in stan:
                    stats[i]=x
                    stan.remove(x)
                else:
                    print('Number unavailable. Try again.')
                    sys.exit()
            break
        stre=stats[0]
        dex=stats[1]
        con=stats[2]
        inte=stats[3]
        wis=stats[4]
        cha=stats[5]

        mods=[0]*6
        for i in range(0, len(stats)):
            if stats[i] == 15:
                mods[i] = 3
            if stats[i] == 14:
                mods[i] = 2
            if stats[i] == 13:
                mods[i] = 1
            if stats[i] == 12:
                mods[i] = 1
            if stats[i] == 10:
                mods[i] = 0
            if stats[i] == 8:
                mods[i] = -1

        global strmod, dexmod, conmod, intmod, wismodifier, chamod

        strmod=mods[0]
        dexmod=mods[1]
        conmod=mods[2]
        intmod=mods[3]
        wismodifier=mods[4]
        chamod=mods[5]

        global hpmax, hp
        hpmax=0
        if conmod < 1:
            hpmax=4
        if conmod >=1:
            hpmax=conmod*3+10
        
        hp=hpmax


        print('Strength: ',stre, 'Mod: ',strmod)
        print('Dexterity: ',dex, 'Mod: ',dexmod)
        print('Constitution: ',con, 'Mod: ',conmod)
        print('Intelligence: ',inte, 'Mod: ',intmod)
        print('Wisdom: ',wis, 'Mod: ',wismodifier)
        print('Charisma: ',cha, 'Mod: ',chamod)

        global gold
        gold = 5

        print('''You've now created the numerical basis for the character, the rest is up to your imagination.
We now embark on our journey. If you ever need help, simply ask by saying 'help' or 'D, i need help please'. 
I prefer the second one. I'll help you whenever you need, but I will slightly judge you for it.''')
        print()
        print('''In the human majority fortress city of Tierengard, the market square is buzzing with intrigue. An archaeological team has recently
discovered the ruins of a once great, ancient dwarvish kingdom beneath the mountains to the West. The most recent news, however,
is the disappearance of the archaeological team that went about 2 weeks ago. They were funded by the city government, 
so them not returning means that something terrible probably happened. You eagerly snatch the first contract poster you can find and embark 
to be the first to find them, and claim the hefty bounty.''')

        while True:
            w=input('When you are ready to continue, type continue. If you wish to back out now, type exit. ')
            if w=='continue':
                print()
                print('''You arrive, after several days of travel through the mountains. The great gates of the ruins are left slightly ajar,
likely a remnant of the archaeological team that went in some weeks prior. As you enter, you are struck by the scale. 
Ahead of you, a MAIN ROAD with stairs on either side spirals down into the rest of the city, giving way to darkness after a 
few meters. On the sides of the road, carved into the walls, is a massive and gorgeous MOSAIC mural depicting some historical 
battle between dwarves which you don't immediately recognize. The only sound here is your own breathing, the wind rushing from 
below, and the soft dripping of melting snow outside falling onto the floor.''')
                print()
                print('''If you ever wish me to repeat my description, say 'repeat'.''')
                print()
                dnd.greatgates()
            if w == 'exit':
                print('A shame.')
                sys.exit()
            else:
                print('''I don't understand''')
                continue
    pass
#great gates possible rolls/variables
    '''global w,s,lock,h,i,secretdoor
    w=actions.wischeck()
    s=actions.strcheck()
    lock=actions.dexcheck()
    h=actions.intcheck()
    i=actions.intcheck()
    secretdoor=0'''

    def greatgates():
        global gold
        global secretdoor
        global sewerdooropen
        print()
        scrawl1='''You arrive, after several days of travel through the mountains. The great gates of the ruins are left slightly ajar,
likely a remnant of the archaeological team that went in some weeks prior. As you enter, you are struck by the scale. 
Ahead of you, a MAIN ROAD with stairs on either side spirals down into the rest of the city, giving way to darkness after a 
few meters. On the sides of the road, carved into the walls, is a massive and gorgeous MOSAIC mural depicting some historical 
battle between dwarves which you don't immediately recognize. The only sound here is your own breathing, the wind rushing from 
below, and the soft dripping of melting snow outside falling onto the floor.'''

        w=actions.wischeck()
        s=actions.strcheck()
        lock=actions.dexcheck()
        h=actions.intcheck()
        i=actions.intcheck()

        #secretdoor=0
        if secretdoor==1:
            secretdoor=1
        else:
            secretdoor=0
        
        if sewerdooropen==1:
            sewerdooropen=1
        else:
            sewerdooropen=0

        while True:
            act=input('''What would you like to do? ''')
            
            if act == 'help' or act == 'D, I need help please':
                print('''This is the first room, and it is very dark. I recommend you LOOK AROUND a bit to find what you can
find. You may uncover a secret or find information that will inform your decision about where to go next.''')
            elif act == 'status':
                actions.health()
            elif act == 'look around' or act == 'perception':
                print('Perception: ', w)

                if w >= 15:
                    print('''You see a small, decrepit HIDDEN DOOR in the corner, seemingly purposefully placed out of view. The bottom of the door
is caked in some very old looking blood and the lock is severely rusted. You also notice that there is a loose tile 
within reach on the wall MURAL.''')
                    secretdoor=1
                if w < 15 and w >= 13:
                    print('''On the wall mural, there is a loose tile within reach.''')
                if w < 13:
                    print('''The scale of the hall has left you short of breath and incapable of thinking straight. You don't notice anything interesting.''')
            elif act == 'repeat':
                print()
                print(scrawl1)
            elif act == 'investigate mural' or act == 'investigate mosaic':
                print('Investigaion: ', i)
                if i >=13:
                    print('''This mural has seen much wear over the years, but it's artisanship is obvious. The battle depicted seems important,
with a figure holding a sword above his head, light shining from behind him. There is a LOOSE TILE at his feet.''')
                if i < 13:
                    print('''This mural has seen much wear over the years, but it's artisanship is obvious. The battle depicted seems important,
with a figure holding a sword above his head, light shining from behind him. He seems important, but you can't
recognize him without thinking much harder about it.''')
            elif act == 'loose tile' or act == 'investigate loose tile':
                print('''There is a loose tile at his feet, which you can open.
Inside is a small cubby that holds a small bag and a letter. The bag contains 4 ancient looking gold coins, and the notes reads: ''')
                print()
                print('''The path to freedom will be harsh, but if followed thoroughly you will reap its rewards. I cannot say more in a letter such as this,
in case the wrong person finds it. If you are the right person, you are on the right path. Bow at Khirns feet, and watch him raise his blade.
Place this letter back for next brother or sister and leave some gold if you can, or take it if you need.''')
                print()
                print('''Curious, no?''')
                while True:
                    smug=input(' Take gold, leave gold, or do nothing? (t/l/n) ')
                    if smug == 't':
                        print('He did say to take it if you need it.')
                        gold+=4
                        break
                    elif smug == 'l':
                        print('You leave a gold piece and close the cubby, in honor of travellers long forgotten.')
                        gold-=1
                        break
                    elif smug == 'n':
                        print("You're too broke to leave anything, but too superstitious to take anything either.")
                        break
                    else:
                        print('I dont understand')

            elif act == 'history of mural' or act == 'history of mosaic':
                print('History: ', h)
                if h >= 15:
                    print('''This mural depicts Khirn the Conqueror, an almost deified hustorical figure to the dwarves who once lived here,
standing in victory over the other dwarvish peoples he subjugated. If Khirn was real, he lived close to 1200 years ago, 
and was responsible for creating the first unified dwarvish state, gathering rival clans and destroying those that 
opposed him. He would eventually found his capital here, naming it Khirngolir, or 'Khirn City' in dwarvish. Eventually his holdings split into the 9
dwarvish kingdoms that are around today. He became a symbol of the royal family,
who would have been decended from him, and also a symbol of dwarvish culture and pride. He was used as the symbol
of multiple rebellions throughout the years, including the Kruezung rebellion against Khirni vassalization which happened
about 600 years ago. This mural seems to date to around that time, likely pieces together by imprisoned Kruezung soldiers.''')
                if h < 15 and h >=10:
                    print('''This mural depicts Khirn the Conqueror, an almost deified hustorical figure to the dwarves who once lived here,
standing in victory over the other dwarvish peoples he subjugated. If Khirn was real, he lived close to 1200 years ago, and
was responsible for creating the first unified dwarvish state, gathering rival clans and destroying those that opposed him. He
would eventually found his capital here, naming it Khirngolir, or 'Khirn City' in dwarvish. Eventually his holdings split into the 9
dwarvish kingdoms that are around today. He became a symbol of the royal family, who would have been decended from him, and also a symbol of dwarvish culture and pride.''')
                if h < 10:
                    print('''This mural depicts some large historical battle between dwarves and some figure standing in the foreground, 
but the specifics of what or who it is depicting is lost on you.''')
            elif act == 'sneak':
                print('''Why? Do you see something I don't? Oh wait, you can't see anything I don't tell you about. No need for stealth here.''')
            elif act == 'inventory':
                actions.inventory()
            elif act == 'investigate door' or act == 'hidden door' or act =='investigate hidden door' or act == 'secret door' or act == 'take hidden door' or act == 'take secret door':
                if secretdoor==0:
                    print('What door?')
                if secretdoor==1 and sewerdooropen==0:
                    print('''The door has a thin crust of blood at the bottom, and it's wood is partially rotted. The lock and hinges
are rusty and creak as you try to open it, however the door does not budge. You can hear the faint sound of running water.''')
                if secretdoor==1 and sewerdooropen==1:
                    print('''You head through the door to the sewer maintenance shaft.''')
                    print('''The sewer air is damp with the smell of rotting meat and mold. The sound of slowly running water is echoing through
the maintenance shaft you find yourself in. The age old dried BLOODSTAINS on the floor lead directly to a skeleton just behind the door, seeming 
as though this person died while crawling towards it in an attempt to flee...something. At the end of the hallway, you find the source of the sound.
A T in the road contains a channel, carrying flowing water from right to left. Another SKELETON with a BACKPACK is 
sitting propped on the wall.''')
                    dnd.sewer()
            elif act == 'main street' or act == 'take main road' or act == 'main road' or act == 'take stairs' or act == 'take main stairs':
                print('''Walking down the cavernous main road of the city, you eventually spiral down into a large townsquare.
In the center of this square is a large STATUE of a dwarvish figure, his sword planted in the ground in front of him. There are numerous
buildings packed tightly together around the edge of the square, many of them collapsed into themselves, including a particular COLLAPSED 
HOUSE, where part of it has fallen and blocked the MAIN ROAD with RUBBLE.''')
                print('''If you ever wish me to repeat my description, say 'repeat'.''')
                dnd.khirnsquare()
            elif act == 'break down door' or act == 'break down hidden door':
                if secretdoor == 0:
                    print('''What door?''')
                if secretdoor == 1 and sewerdooropen==0:
                    print('Athletics: ', s)
                    if s >=11:
                        sewerdooropen=1
                        print('''You break the door down and enter.''')
                        print('''The sewer air is damp with the smell of rotting meat and mold. The sound of slowly running water is echoing through
the maintenance shaft you find yourself in. The age old dried BLOODSTAINS on the floor lead directly to a skeleton just behind the door, 
seeming as though this person died while crawling towards it in an attempt to flee...something. At the end of the hallway, you find the 
source of the sound. A T in the road contains a channel, carrying flowing water from right to left. Another SKELETON with a BACKPACK is 
sitting propped on the wall.''')
                        dnd.sewer()
                    else:
                        print('''Unfortunately, dwarves are famous for the craftsmanship, and even this
rusted, partially rotted door is well enough constructed that it doesn't budge, 
no matter how hard you hit it.''')
                elif secretdoor==1 and sewerdooropen==1:
                    print('The door is already open, you can just walk through.')
            elif act == 'lockpick hidden door' or act == 'lockpick' or act == 'pick lock' or act == 'pick hidden door':
                if secretdoor==0:
                    print('''What lock?''')
                if secretdoor==1 and sewerdooropen==0:
                    print('Lockpick: ',lock)
                    if lock >= 11:
                        sewerdooropen=1
                        print('''You deftly pick the old rusted lock, and enter the door.''')
                        print('''The sewer air is damp with the smell of rotting meat and mold. The sound of slowly running water is echoing through
the maintenance shaft you find yourself in. The age old dried BLOODSTAINS on the floor lead directly to a skeleton just behind the door, seeming 
as though this person died while crawling towards it in an attempt to flee...something. At the end of the hallway, you find the source of the sound.
A T in the road contains a channel, carrying flowing water from right to left. Another SKELETON with a BACKPACK is sitting propped on the wall.''')
                        dnd.sewer()
                    else:
                        print('''Dwarvish craftsmanship proves it's mettle yet again, as your lockpicks
find no purchase within the doors complex interior mechanisms.''')
                elif secretdoor==1 and sewerdooropen==1:
                    print('The door is already open, you can just walk through.')
            else:
                print('''I don't understand.''')
        pass

    #khirn square possible rolls/variables
    '''global gimlisring,talktodis,disremembers,dismovedon,houselocked,w2,istat,ihouse,h2,a2,s2,dexchecker2,c2,khirnstairs
    gimlisring=0
    talktodis=0
    disremembers=0
    dismovedon=0
    houselocked=0

    w2=actions.wischeck()
    istat=actions.intcheck()
    ihouse=actions.intcheck()
    h2=actions.intcheck()
    a2=actions.intcheck()
    s2=actions.strcheck()
    dexchecker2=actions.dexcheck()
    c2=actions.chacheck()
    khirnstairs=0'''

    def khirnsquare():
        global gold
        global hp
        global hpmax
        global chamod
        print()
        scrawl2='''Walking down the cavernous main road of the city, you eventually spiral down into a large townsquare.
In the center of this square is a large STATUE of a dwarvish figure, his sword planted in the ground in front of him. There are numerous
buildings packed tightly together around the edge of the square, many of them collapsed into themselves. There is a COLLAPSED HOUSE, where
part of it has fallen as RUBBLE and blocked the MAIN ROAD going forward.'''

        scrawl2clear='''In the center of this square is a large STATUE of a dwarvish figure, his sword planted in the ground in front of him. There are numerous
buildings packed tightly together around the edge of the square, many of them collapsed into themselves, except for the now cleared road leading to the MARKET.'''

        w2=actions.wischeck()
        istat=actions.intcheck()
        ihouse=actions.intcheck()
        h2=actions.intcheck()
        a2=actions.intcheck()
        s2=actions.strcheck()
        dexchecker2=actions.dexcheck()
        c2=actions.chacheck()
        c22=actions.chacheck()
        khirnstairs=0

        global talktodis #0=cant talk to her, 1=can come back, 2=questline complete
        global disremembers
        global dismovedon
        global invhouse
        global houselocked
        global manhole
        global streetclear

        if manhole==1:   #this kind of thing is located all throughout the code, if I remove them the game doesnt work so I had to leave them in
            manhole=1
        else:
            manhole=0

        while True:
            act=input('What would you like to do? ')

            if act == 'repeat':
                if streetclear==0:
                    print(scrawl2)
                if streetclear==1:
                    print(scrawl2clear)
            elif act == 'help':
                print('''There is a lot to see here, so don't be afraid to poke around. Some things may not be exactly as they seem.
Some hints are baked right into the puzzle themselves.''')
            elif act == 'use lockbox key' or act == 'use key':
                if 'gimlis ring' in inventory:
                    print('''You already have the ring.''')
                elif 'lockbox' in inventory and 'lockbox key' in inventory:
                    print('''You take the key you got from Khirn Square and place it in the lock. With a gentle click, the box opens, revealing a beautifully
crafted golden ring. You take it, dropping the key and lockbox on the ground since they are now useless.''')
                    print('''You've recieved GIMLIS RING''')
                    inventory.remove('lockbox')
                    inventory.remove('lockbox key')
                    inventory.append('gimlis ring')
                elif 'lockbox' not in inventory and 'lockbox key' in inventory:
                    print('''You haven't found the lockbox yet, but it should be around here somewhere.''')
                elif 'lockbox' not in inventory and 'lockbox key' not in inventory:
                    print('''I don't know what you mean by that. ''')
                elif 'lockbox' in inventory and 'lockbox key' not in inventory:
                    print('''You do not have the key to this lockbox.''')

            elif act == 'look around':
                print('Perception: ', w2)
                
                if w2 >= 13:
                    if streetclear==0:
                        print('''The STATUE in the center of the square looks remarkably old, the armor, arms, and sword
are covered in runes and ARCANE symbols. The street circles around the statue, continuing past the square down farther towards
a castle in the distance, however the MAIN ROAD is blocked by RUBBLE from a COLLAPSED HOUSE. Past the COLLAPSED HOUSE, 
a market can be seen down the street. To the side, an ALLEY winds off into the shadows between the tightly packed dwellings.''')
                    if streetclear==1:
                        print('''The STATUE in the center of the square looks remarkably old, the armor, arms, and sword
are covered in runes and ARCANE symbols. The street circles around the statue, continuing past the square down farther towards
a castle in the distance, where the MAIN ROAD has now been cleared. Past the RUBBLE from the COLLAPSED HOUSE, a market can be seen
down the street. To the side, an ALLEY winds off into the shadows between the tightly packed dwellings.''')
                if w2 < 13:
                    if streetclear==0:
                        print('''The STATUE in the center of the square looks remarkably old. The path the road continues down
is blocked by a COLLAPSED BUILDING, where a market can be seen through the rubble. To the side, an ALLEY snakes off
between the tighly packed buildings.''')
                    if streetclear==1:
                        print('''The STATUE in the center of the square looks remarkably old. The path the road continues down
used to be blocked by the COLLAPSED HOUSE but is now wide open, where a market can be seen through the rubble. To the side, an ALLEY snakes off
between the tighly packed buildings.''')

            elif act == 'investigate statue':
                print('Investigation: ', istat)

                if istat >= 15:
                    print('''This statue is very old, the craftsmanship likely placing it at being built around 500-600 years ago.
The statue is of a dwarvish warrior, wearing traditional armor and holding a sword in both hands, the tip at the ground by his feet.
There is significant scratching on the shoulders and hands, indicating increased wear over the years, as well as the arms being
slightly disjointed from the rest of the body at the shoulder. The plaque at the bottom reads 'King Khirn 'The Conqueror' Kundari,
Shepherd of his People. Let his raised sword guide the way'. The armor he is wearing is covered in strange runes.''')
                if istat < 15 and istat >=10:
                    print('''This statue is very old, the craftsmanship likely placing it at being built around 400-700 years ago.
The statue is of a dwarvish warrior, wearing traditional armor and holding a sword in both hands, the tip at the ground by his feet.
The plaque at the bottom reads 'King Khirn 'The Conqueror' Kundari, Shepherd of his People. Let his raised sword guide the way.'. 
The armor he is wearing is covered in strange runes.''')
                if istat < 10:
                    print('''This statue is very old, the craftsmanship likely placing it at being built around 400-700 years ago.
The statue is of a dwarvish warrior, wearing traditional armor and holding a sword in both hands, the tip at the ground by his feet.
There is a plaque, but the years have rendered it illegible with caked on dirt and rust.''')

            elif act == 'arcana on statue':
                print('Arcana: ', a2)
                
                if a2 >=19:
                    print('''The runes on the armor are ancient and weak, but not inert. They correspond to a fairily
simple echantment that spins the statue upon a certain condition being met, revealing a hidden staircase below.
Mages are often known to work in riddles and puzzles, so I'm sure there must be some sort of clue around here
as to what it is that activates the enchantment...''')
                if a2 < 19 and a2 >= 15:
                    print('''The runes on the armor are ancient and weak, but not inert. They correspond to a fairly
simple enchantment that makes the statue function as some sort of lock, opening whatever it is hiding upon a certain
condition being met. What that condition is, however, remains a mystery.''')
                if a2 < 15 and a2 >=10:
                    print('''The runes on the armor looks almost as if they have been rendered inert with age. Runes
become weaker or inactive all together if the shape of them is damaged or altered, so it is unclear if whatever magic
once effected this statue still functions or not. If it were still active, it appears they would have used the statue
as some kind of lock mechanism, but the rest is too damaged to decipher.''')
                if a2 < 10:
                    print('''The runes on the armor have been damaged beyond use, as far as you can tell.
You cannot decipher any meaning from them, and from the look of how ancient they are, it would be shocking if they
still did anything besides look pretty.''')

            elif act == 'lift sword' or act == 'lift khirns sword' or act == 'lift statues sword' or act == 'raise sword':
                khirnstairs=1
                print('''As you lift the statues sword off the pedestal and above it's head, the arms rotate,
raising the blade swyward in defiance, in the same manner as the mural in the GREAT GATES. When the blade reaches its zenith,
the runes on the armor flare into life, emitting a brilliant blue glow. The statue begins to rotate and spiral downwards, revealing
a staircase that has likely not been walked down for a great number of years.''')
                print()
                print('''You have revealed the SECRET STAIRS''')

            elif act == 'history of khirn' or act == 'history of statue':
                print('''History: ''', h2)

                if h2 >= 13:
                    print('''Khirn the Conqueror was a historical figure, likely real although no one can say for sure,
who is credited with conquering and thus unifying all of the dwarvish tribes of his time into a powerful kingdom for the first time.
Although his holdings would split into the current 9 dwarvish kingdoms that exist today shortly after his death, it is his
conquest that brought about much of what we consider 'dwarvish' culture today, including religious practices and language to some
extent. He is also a symbol of dwarvish pride, and has been used as the symbol of rebellions and political groups for
centuries, to varying degrees of success, the most notable of which being the Kruezung Rebellion from Khirni control about 600 years ago.
You are standing in the ruins of the primary battleground of a large portion of that war. When used as this symbolic figure,
he is often depicted raising his sword above his head in defiance.''')
                if h2 < 13:
                    print('''Khirn the Conqueror was a historical figure of great significance, although it is debated heavily
whether or not he was real or simply a propaganda piece created by the royal family to give their rule leigitmacy. It is said that
Khirn united the dwarvish tribes into a single people through conquest and establish a massive, although short lived, empire, which then
split into the 9 modern dwarvish kingdoms we have today.''')

            elif act == 'investigate collapsed house' and houselocked == 0:
                if invhouse==1:
                    print('''You've already done that.''')
                elif invhouse==0:
                    invhouse=1 #might crash loop
                        
                    if 'gimlis ring' not in inventory:
                        print('Investigation: ', ihouse)

                        if ihouse >= 13:
                            print('''The front of this building collapsed to the side, blocking the street but also revealing a way into the house.
Inside, you see the remnants of what used to be a dwarven home a long time ago. It is modest but cosy, and certainly dwarf sizes.
Looking around, you find 3 gold coins and a small key with a note that reads: 'I left your ring in the lockbox at the market. I am going out
and didn't want to bring the key with me. The goldsmiths did a great job restoring it, I know how much it meant to you. Love you 
Gimli, from Mom.' How touching. That ring might be valuable, I wonder if it might still be there...''')
                            gh=input('Take key? y/n ')
                            if gh == 'y':
                                print('Could be useful.')
                                inventory.append('lockbox key')
                            if gh == 'n':
                                print('Best not steal from the dead.')
                        gold+=3
                        if ihouse < 13:
                            print('''The place seems as if it has been mostly cleared out by whoever or whatever was here before you.''')
                        
                        print('You sense a sad presence coming from one of the rooms. It emanates an immense feeling of loss and grief.')
                        u=input('Investigate?: (y/n) ')

                        if u == 'y':
                            print('''This room was once a bedroom, but now the modest bed is listing to one side, the leg broken. Sitting
on this bed is the figure of a dwarvish woman, although she is partially transparent. She is crying into her hands, and looks up at you,
somewhat embarrassed. She stands up and immediately begins attempting to clean the room, although her hands pass through everything
she touches she doesn't seem to notice. She speaks:''')
                            print(''' 'I am so sorry for the mess, if I would have know Gimli was having company I would have tidied
up more!' She wipes some tears away from her face sheepishly.''')
                            tyr=0 #variable for conversation loop to end
                            while tyr==0:
                                print('''Dialogue Options:
        - A: Give Name
        - B: Why were you crying?
        - C: Who is Gimli?''')
                                
                                convo=input('''I'm Gimli's mother, Dis. What is your name? ''')

                                if convo == 'Give Name' or convo == 'give name' or convo == 'A':
                                    print('''Well, that is a lovely name!. I assume your one of Gimli's friends, he's off fetching groceries
    right now, you know how sweet he is. Well, you're more than welcome to stick around and wait if you like, he should be home any minute.
    However, if you would like to do me a favor, Gimli's ring just got finished being repaired by the goldsmith and I left it at the
    family POTTERY STAND in the market for safe keeping. Would you mind bringing it back to me? I'll go fetch the key for you.''')
                
                                    if 'lockbox key' in inventory:
                                        print('She notices that you already have the key in your hand.')
                                        while True:
                                            print('''Dialogue options:
            - A: I'm sorry, it was a mistake (Charisma Check)
            - B: You werent using it anyway (Antagonize)''')
                                            resp=input('''Oh...well it would seem you've got some sticky fingers to you, don't you? What do you have to say
for yourself? ''')
                                            if resp == '''I'm Sorry''' or resp == 'Im sorry' or resp == 'A':
                                                print('Persuasion: ', c2)
                                                if c2 < 13:
                                                    print('''I think you should leave.''')
                                                    print('''She grabs the key from you and pushes you out the door, slamming it in your face.''')
                                                    inventory.remove('lockbox key')
                                                    talktodis=0
                                                    tyr=1
                                                    break
                                                if c2 >= 13:
                                                    print('''Well, I guess it's alright. Just bring the ring to me and we'll call it even hun. If you see Gimli, tell him to come home will you?
He was wearing his RED SASH, you can't miss it.''')
                                                    print('''Unlocked option in Khirn Square: 'talk to dis' ''')
                                                    talktodis=1
                                                    tyr=1
                                                    break
                                            elif resp == 'You werent using it anyway' or resp == 'B':
                                                print('Her eyes flare wide and her pupils disappear. Some small objects in the room fly off their shelves.')
                                                print('''The nerve of you! I bet you don't even kow my Gimli, you just came here to steal from us!
A liar and a thief! I WILL NOT STAND FOR SUCH DISRESPECT''')
                                                hp-=10
                                                if hp <= 0:
                                                    print('''Dis lunges at you with ghostly fury, so fast you cannot react. You are blasted backwards into the wall
with such force that a loose bit of the unstable building falls and crushes you. You are dead.''')
                                                    print('Even dead dwarves have legendary tempers, I suppose. Better luck next time.')
                                                    sys.exit()
                                                elif hp > 0:
                                                    if 'lockbox key' in inventory:
                                                        print('''You are blasted out of the door, the door slamming behind you. You took a heavy hit,
but are still standing. The key, however, has been taken back by it's owner.''')
                                                        inventory.remove('lockbox key')
                                                        print('You take 10 damage.')
                                                        houselocked=1
                                                        tyr=1
                                                        break
                                                    else:
                                                        print('''You are blasted out of the door, the door slamming behind you. You took a heavy hit,
but are still standing. The key, however, has been taken back by it's owner.''')
                                                        houselocked=1
                                                        tyr=1
                                                        break
                                            else:
                                                print('I dont understand')
                                    elif 'lockbox key' not in inventory:
                                        print('''She hovers away and returns holding a small key, interestingly not falling through her hand.
She gives it to you, the metal cold as ice in your hand. A part of her finger passes through yours as her 
ghostly hand drifts to her side.''')
                                        print('''You recieved LOCKBOX KEY''')
                                        inventory.append('lockbox key')
                                        print('''You're a real doll for doing this for me. When you get there, look for his RED SASH, you can't miss it.''')
                                        print()
                                        print('''Unlocked option in Khirn Square: 'talk to Dis' ''')
                                        talktodis=1
                                        tyr=1
                                        break
                                elif convo == 'Why were you crying?' or convo == 'B':
                                    print(''' 'I honestly don't remember...' ''')
                                    print('''A look of confusion and then realization comes over her face.''')
                                    print('''MORADIN ABOVE! Gimli is still out there! The attack was so sudden I didn't even realize! Please, Please
you have to go find him! Look for his RED SASH, he wears it all the time! He's in danger with all the fighting, I'm not even sure what is happening! Go, Please!''')
                                    print('''She shoves you out the door.''')
                                    print('''Option unlocked in Khirn Square: 'talk to dis' ''')
                                    disremembers=1
                                    talktodis=1
                                    tyr=1
                                    break
                                elif convo == 'Who is Gimli?' or convo == 'C':
                                    print('A look of confusion comes across her face.')
                                    print('''...He's my son. But if you don't know him then...who are you?''')
                                    print('She looks you up and down and a look of panic appears suddenly')
                                    print('''You're here to rob us! You don't know my son! GET OUT NOW!''')
                                    hp-=10
                                    if hp <= 0:
                                        print('''Dis lunges at you with ghostly fury, so fast you cannot react. You are blasted backwards into the wall
with such force that a loose bit of the unstable building falls and crushes you. You are dead.''')
                                        print('Even dead dwarves have legendary tempers, I suppose. Better luck next time.')
                                        sys.exit()
                                    if hp > 0:
                                        print('''You are blasted out of the door, the door slamming behind you. You took a heavy hit,
but are still standing. The key, however, has been taken back by it's owner.''')
                                        print('''You take 10 damage.''')
                                        houselocked=1
                                        tyr=1
                                        break
                                else: 
                                    print('I dont understand')
                        elif u== 'n':
                            print('Seems unsafe.')
                        else:
                            print('''I'll take that as a no.''')
                    elif 'gimlis ring' in inventory:
                        print('Investigation: ', ihouse)

                        if ihouse >= 13:
                            print('''The front of this building collapsed to the side, blocking the street but also revealing a way into the house.
Inside, you see the remnants of what used to be a dwarven home a long time ago. It is modest but cosy, and certainly dwarf sizes.
Looking around, you find 3 gold coins and a small key with a note that reads: 'I left your ring in the lockbox at the market. I am going out
and didn't want to bring the key with me. The goldsmiths did a great job restoring it, I know how much it meant to you. Love you 
Gimli, from Mom.' How touching. That ring might be valuable, I wonder if it might still be there...''')
                            gh=input('Take key? y/n ')
                            if gh == 'y':
                                print('Could be useful.')
                                inventory.append('lockbox key')
                            if gh == 'n':
                                print('Best not steal from the dead.')
                        gold+=3
                        if ihouse < 13:
                            print('''The place seems as if it has been mostly cleared out by whoever or whatever was here before you.''')
                        
                        print('You sense a sad presence coming from one of the rooms. It emanates an immense feeling of loss and grief.')
                        u=input('Investigate?: (y/n) ')

                        if u == 'y':
                            print('''This room was once a bedroom, but now the modest bed is listing to one side, the leg broken. Sitting
on this bed is the figure of a dwarvish woman, although she is partially transparent. She is crying into her hands, and looks up at you,
somewhat embarrassed. She stands up and immediately begins attempting to clean the room, although her hands pass through everything
she touches she doesn't seem to notice. She speaks:''')
                            print(''' 'I am so sorry for the mess, if I would have know Gimli was having company I would have tidied
up more!' She wipes some tears away from her face sheepishly.''')
                            print('''Her eyes widen as she looks at you, slightly confused.''')
                            print('''Dialogue Options:
    -A: What ring? (Lie)
    -B: Yes, I have it right here! (Give Ring)''')
                            re=input(''' 'You have the ring don't you? I can feel it...did you bring it back to me for Gimli?
That is so kind of you!' ''')
                            if re == 'A':
                                print('''...no I feel it in your pocket...my son's ring...why would you lie to me?
You want to keep it for youself! HOW DARE YOU!''')
                                print('''You are suddenly hurled into the wall with a force of such rage that it must have been building
for centuries. The unstable building collapses on you, killing you instantly. Better luck next time.''')
                                sys.exit()

                            if re == 'B':
                                #same as the other things, she is greatful, give necklace, talktodis=2
                                print(''' 'Well, thank you so much, that ring means so much to Gimli!' ''')
                                print('''She takes the ring from you.''')
                                inventory.remove('gimlis ring')
                                print(''' 'There is a reward for you in the closet, please take it.' ''')
                                print('''You leave the room and look in the closet, where you find a small box. Inside, there is a small golden 
necklace. You put it on and feel an immense sense of gratitude wash over you. You gain a +2 bonus to Charisma Rolls while you have the
necklace.''')
                                inventory.append('''Dis' Necklace''')
                                global chamod
                                chamod+=2
                                talktodis=2
                        elif u == 'n':
                            print('''You think of all of the ghost stories you heard as a kid and remember how they started.
You think it is probably wise to stay away.''')
                        else:
                            print('''I'll take that as a no.''')
        

            elif act == 'talk to dis' or act == 'talk to Dis':
                if talktodis==1 and disremembers==0:
                    if 'gimlis ring' in inventory and 'gimlis sash' not in inventory:
                        print('''You enter the house and see Dis sitting on her bed as usual. She looks up and smiles at you.
You pull the ring from your pocket.''')
                        print('''Dialogue Options:
-A: No (Truth)
-B: Yes, he's on his way home (Charisma Check)''')
                        res=input('''Moradins beard, you found it! Gimli will be so happy! His grandfather made this ring and
passed it down to his father, and then when Gimli finally got it he accidentally bent it out of shape! He almost threw a fit 
it means so much to us... Thank you so much for helping! By the way, did you happen to see Gimli? He should be coming 
back any minute now. ''')
                        if res == 'A':
                            print('''She takes the ring from you''')
                            inventory.remove('gimlis ring')
                            print(''' 'Ah well, he's probably off on his own doing whatever it is young dwarves do nowadays.
As a thank you, There's a reward for you in the closet. If you do see Gimli, let him know I'm waiting for him!' ''')
                            print('''The pained look on her face tells you she has been waiting for a very long time.''')
                            print()
                        if res == 'B':
                            print('Deception: ', c22)
                            if c22 > 10:
                                print('''Her face lights up with joy. She takes the ring from you.''')
                                print(''' 'Oh, that makes me so happy! He's been out for...a long time now. I will wait
here patiently for him to return then! Thank you for telling me! ' ''')
                                print('''Oh, there's a little reward for you in the closet, for your troubles. Please, take it.''')
                                inventory.remove('gimlis ring')
                            if c22 < 10:
                                print('''Her face falls as she sees through your lie.''')
                                print('''You're lying aren't you... I appreciate the attempt to spare my feelings but
you can't get my hopes up like that...it's been so long...anyway, there's a reward in the closet for you for finding he ring.''')
                                print('''She sullenly takes the ring from you''')
                                inventory.remove('gimlis ring')

                        print('''You leave the room and look in the closet, where you find a small box. Inside, there is a small golden 
necklace. You put it on and feel an immense sense of gratitude wash over you. You gain a +2 bonus to Charisma Rolls while you have the
necklace.''')
                        inventory.append('''Dis's Necklace''')
                        chamod+=2
                        talktodis=2
                    elif 'gimlis ring' not in inventory and 'gimlis sash' not in inventory:
                        if dismovedon==0:
                            print('''Dis looks up at you from her frantic cleaning, not actually moving any dust around.''')
                            print(''' 'Oh, back already? And no ring I see. I'm sorry I really must continue cleaning. Come back when you have
    the ring darling, although I do appreciate the company.' ''')
                            print('She continues to clean, completely ignoring your every attempt at communication until you leave.')
                        elif dismovedon==1:
                            print('''Dis has moved on to a better place.''')
                    elif 'gimlis ring' not in inventory and 'gimlis sash' in inventory:
                        print('''Dis looks up from her frantic cleaning, not moving any dust around.''')
                        if dismovedon==0:
                            loki=0
                            while loki==0:
                                print('''Dialogue options:
        -A: No, but I'll keep looking! (don't show bloody sash)
        -B: No, but... (show bloody sash)''')
                                tak=input('''You're back! Did you find the ring? ''')

                                if tak == 'A':
                                    print(''' 'Oh, well then why did you come back at all? Go on, go find it!' ''')
                                    print('''She shoos you out of the house playfully and closes the door.''')
                                    loki=1
                                if tak == 'B':
                                    print(''' 'What is thi-...Is this Gimli's? But there's so much blood, what happened!?' ''')
                                    print('''A look of realization washes over her face as the powerful memory makes her remember.''')
                                    print('''Oh, that's right...the soldiers came while Gimli was stil outside...he must have gotten caught out
    in the middle of the fighting. Oh, he's had to spend so many years alone without me...''')
                                    print('She presses the sash tightly to her cheek and cries a soft tear, this time not of grief but of joy.')
                                    print('''She slowly disappears, but not before a great sense of peace washes over you. Dis moves on to the 
    next world, to see her son again. You are filled with her gratitude.''')
                                    inventory.remove('gimlis sash')
                                    print('''You recieve Dis's blessing. You gain +2 to you current hp and hp maximum.''')
                                    hpmax+=2
                                    hp+=2
                                    dismovedon=1
                                    loki=1
                        elif dismovedon==1:
                            print('''Dis has moved on to a better place''')

                    elif 'gimlis ring' in inventory and 'gimlis sash' in inventory:
                        print('''Dis looks up at you from her frantic cleaning, not moving any dust around.''')
                        odin=0
                        while odin==0: #dialogue loop
                            print('''Dialogue options:
    -A: Yes, it's right here! (Don't let her see bloody sash)
    -B: Yes, and... (Show bloody sash)''')
                            conv=input('''You're back! Did you find the ring? ''')

                            if conv == 'A':
                                thor=0
                                while thor==0:
                                    print('''Dialogue Options:
    -A: No (Truth)
    -B: Yes, he's on his way home (Charisma Check)''')
                                    res=input(''' 'Moradins beard, you DID find it! Gimli will be so happy! His grandfather made this ring and
passed it down to his father, and then when Gimli finally got it he accidentally bent it out of shape! He almost threw a fit 
it means so much to us... Thank you so much for helping! By the way, did you happen to see Gimli? He should be coming 
back any minute now.' ''')
                                    if res == 'A':
                                        print(''' 'Ah well, he's probably off on his own doing whatever it is young dwarves do nowadays.
As a thank you, There's a reward for you in the closet. If you do see Gimli, let him know I'm waiting for him!' ''')
                                        print('''The pained look on her face tells you she has been waiting for a very long time.''')
                                        print()
                                        print('''You head back outside.''')
                                        thor=1
                                    elif res == 'B':
                                        print('Deception: ', c22)
                                        if c22 > 10:
                                            print('''Her face lights up with joy.''')
                                            print(''' 'Oh, that makes me so happy! He's been out for...a long time now. I will wait
here patiently for him to return then! Thank you for telling me! ' ''')
                                            print('''Oh, there's a little reward for you in the closet, for your troubles. Please, take it.''')
                                            print('''You leave the room and look in the closet, where you find a small box. Inside, there is a small golden 
necklace. You put it on and feel an immense sense of gratitude wash over you. You gain a +2 bonus to Charisma Rolls while you have the
necklace.''')
                                            inventory.append('''Dis's Necklace''')
                                            chamod+=2
                                            talktodis=2
                                            thor=1
                                        if c22 < 10:
                                            print('''Her face falls as she sees through your lie.''')
                                            print('''You're lying aren't you... I appreciate the attempt to spare my feelings but
you can't get my hopes up like that...it's been so long...''')
                                            thor=1
                                    else:
                                        print('I dont understand')
                                odin=1

                            elif conv == 'B':
                                print('''Oh, Gimli will be so happ- What is this?...Is this Gimli's sash? But there's so much blood
what happened?!...Oh yes...the soldiers came the same day Gimli went out for groceries didn't they...they must have gotten him just like
they got me...thank you for helping me remember.''')
                                print('She presses the sash tightly to her cheek and cries a soft tear, this time not of grief but of joy.')
                                print('''She slowly disappears, but not before a great sense of peace washes over you. Dis moves on to the 
next world, to see her son again. You are filled with her gratitude.''')
                                print('''You recieve Dis's blessing. You gain +2 to you current hp and hp maximum.''')
                                hpmax+=2
                                hp+=2
                                dismovedon=1
                                odin=1
                                inventory.remove('gimlis ring')
                                inventory.remove('gimlis sash')
                            
                            else:
                                print('I dont understand')

                    
                elif talktodis==1 and disremembers==1:
                    if 'gimlis sash' not in inventory:
                        print('''She seems absolutely distraught over the sudden rememberance of her missing son. If only there
was a way to snap her out of it...''')
                    elif 'gimlis sash' in inventory:
                        print('''You calmly approach Dis, sash in hand. She stops her muttering and looks at you.''')
                        print('''This...This is Gimli's...the blood...does this mean he...?''')
                        print('''She doesn't even finish her sentence before she begins crying again. She takes the sash from your hands.''')
                        print('''All this time waiting....and I could have joined him the whole time...thank you for showing me this, traveler.''')
                        print('She presses the sash tightly to her cheek and cries a soft tear, this time not of grief but of joy.')
                        print('''She slowly disappears, but not before a great sense of peace washes over you. Dis moves on to the next world, to
see her son again. You are filled with her gratitude.''')
                        print('''You recieve Dis's blessing. You gain +2 to you current hp and hp maximum.''')
                        hpmax+=2
                        hp+=2
                        dismovedon=1
                elif talktodis==0:
                    print('''The last time you talked to Dis didn't go so well. You shutter to think what she might do if you
see her again now, and think it best to avoid her.''')
                elif talktodis==2:
                    if 'gimlis sash' in inventory:
                        print('''You enter the room, Gimli's sash in your hand. She looks at it and her gentle smile fades.''')
                        print('''That's Gimli's, isn't it? I recognize it... but why is there blood on it?''')
                        print('''A look of remembrance crosses Dis' face.''')
                        print('''Oh...that's right...the soldiers came the day Gimli went to buy groceries didn't they...
and he never made it home...it's been so many years I had forgotten...I must go join him.''')
                        print(''' 'Thank you for freeing my mind traveler. I must pass on now, but you have my gratitude for the rest of
your life. Moradin bless you child.' ''')
                        print('''her spirit fades and is gone, but not before imparting a great sense of peace and gratitude upon you.''')
                        print('''You recieve Dis's blessing. You gain +2 to you current hp and hp maximum.''')
                        hpmax+=2
                        hp+=2
                        dismovedon=1
                        inventory.remove('gimlis sash')
                    elif 'gimlis sash' not in inventory and '''Dis's Necklace''' in inventory and dismovedon==0:
                        print('''Dis sits contently in her room, staring blankly at the wall. She is muttering to herself, seemlingly
unaware of your presence. She is muttering 'Well, I've waited this long, what's a lttle longer?' ''')
                        print('''She is in a good mood, but likely can't move on until she knows about her son. If only there was a way
to show her...''')
                if dismovedon==1 and '''Dis's Necklace''' in inventory or dismovedon==1 and 'gimlis sash' not in inventory: 
                    print('''Remembering what you did for her brings you a great sense of comfort.
You feel a slight warmth as you think of it, and know Dis is with you, even if she is in the next world.''')


            elif act == 'take alley' or act == 'investigate alley':
                #make it so if you come out of the manhole you can go back through
                if manhole==0:
                    print('''This alley seems to have one way in and one way out. A small manhole cover is also present,
but it seems like you cannot open it from this side. On the other side appears to be a small courtyard with a fountain.''')

                    while True:
                        t=input('Go back or continue? ')
                        if t == 'go back':
                            print('Best not')
                            break
                        elif t == 'continue':
                            print('''The courtyard ahead of you is small and secluded. In the middle is a gurgling FOUNTAIN with a statue in the middle.
Behind the fountain is a small but ornate CHURCH, the doors crushed by the partially collapsed stonework and open. Another small ROAD 
leads out opposite of where you came in. To go to Khirn Square, type 'khirn square' ''')
                            dnd.churchcourtyard()
                        else:
                            print('''I don't understand''')
                elif manhole==1:
                    print('''This alley is where you emerged from the cistern, the manhole still lying open. On the other side appears to 
be a small courtyard with a fountain, and behind you is a town square.''')

                    while True:
                        r=input('Where would you like to go? (manhole/courtyard/town square) ')
                        if r == 'manhole':
                            print('You descend back into the cistern.')
                            dnd.cistern()
                        elif r == 'courtyard':
                            print('''The courtyard ahead of you is small and secluded. In the middle is a gurgling FOUNTAIN with a statue in the middle.
Behind the fountain is a small but ornate CHURCH, the doors crushed by the partially collapsed stonework and open. Another small ROAD leads
out opposite of where you came in. To go to Khirn Square, type 'khirn square' ''')
                            dnd.churchcourtyard()
                        elif r == 'town square':
                            print('''You enter into a small square between buildings. In the center of this square is a large STATUE of a dwarvish 
figure. There are numerous buildings packed tightly together around the edge of the square, many of them collapsed into themselves.''')
                            dnd.khirnsquare()
                        else:
                            print('I dont understand.')

            elif act == 'investigate collapsed house' and houselocked == 1:
                print('''You still hear Dis shouting and crying inside. You best not intrude for fear of your life.''')

            elif act == 'take secret stairs':
                if khirnstairs==1:
                    print('''The stairs lead down into a small chamber, which appears to have once been a safehouse of some kind. Lining the shelves
are various trinkets are objects that have all gone inert, except for a healing potion. You take it, then head back up.''')
                    inventory.append('Healing Potion')
                if khirnstairs==0:
                    print('''What stairs?''')
                
            elif act == 'climb collapsed building' or act == 'climb rubble':
                if streetclear==0:
                    print('Acrobatics: ', dexchecker2)
                    
                    if dexchecker2 > 12:
                        print('''You manage to scale the pile of rubble and debris and walk towards the marketplace. The many various stands and stalls have
the remnants of colored cloth banners and signage that would have denoted which stands were which, including one still intact with a clay POT on it. In the center, you can
see a pile of WRECKAGE, and the hint of movement within. To one side, a particular store with a cartoonish bomb denotes an abandoned POWDER SHOP. The MAIN ROAD continues
onward towards a CASTLE in the distance or backwards to KHIRN SQUARE, where it is blocked off by rubble. ''')
                        #market description
                        dnd.market()
                    else:
                        print('''Unfortunately, the rubble is too rough and too high to climb.''')
                elif streetclear==1:
                    print('''You already cleared the street. You walk forward to the market.''')
                    print('''The many various stands and stalls have the remnants of colored cloth banners and signage that would have denoted which stands were 
which, including one still intact with a clay POT on it. In the center, you can see a pile of WRECKAGE, and the hint of movement within. To one side, a particular 
store with a cartoonish bomb denotes an abandoned POWDER SHOP. The MAIN ROAD continues onward towards a CASTLE in the distance or backwards to KHIRN SQUARE. ''')
                    dnd.market()
            elif act == 'lift rubble':
                if streetclear==0:
                    print('Athletics: ', s2)

                    if s2 >= 15:
                        print('''You manage to push enough rubble out of the way that you can walk quickly through to the street
and continue on to the market place as the rubble collapses back down behind you. The many various stands and stalls have the remnants of colored cloth 
banners and signage that would have denoted which stands were which, including one still intact with a clay POT on it. In the center, you can see a pile 
of WRECKAGE, and the hint of movement within. To one side, a particular store with a cartoonish bomb denotes an abandoned POWDER SHOP. The MAIN ROAD continues 
onward towards a CASTLE in the distance or backwards to KHIRN SQUARE, where it is blocked off by rubble. ''')
                    #market description
                        dnd.market()
                    else:
                        print('''Unfortunately, the rubble is too heavy for you to move.''')
                elif streetclear==1:
                    print('''You already cleared the street. You walk forward to the market.''')
                    print('''The many various stands and stalls have the remnants of colored cloth banners and signage that would have denoted which stands were 
which, including one still intact with a clay POT on it. In the center, you can see a pile of WRECKAGE, and the hint of movement within. To one side, a particular 
store with a cartoonish bomb denotes an abandoned POWDER SHOP. The MAIN ROAD continues onward towards a CASTLE in the distance or backwards to KHIRN SQUARE. ''')
                    dnd.market()
            elif act == 'take main road' or act == 'go to market':
                if streetclear==0:
                    print('''It is blocked by rubble from the COLLAPSED HOUSE. You would either have to LIFT the rubble, CLIMB the rubble, or move it
some other way.''')
                elif streetclear==1:
                    print('''You walk on into the market.''')
                    dnd.market()
            elif act == 'blow up rubble':
                if 'bomb' in inventory and streetclear==0:
                    inventory.remove('bomb')
                    print('''You place a bomb next to the rubble and light the fuse with your torch, running for cover behind a building.
You hear a loud BOOM, and when the dust clears, the main road is clear of debris.''')
                    streetclear=1
                if 'bomb' in inventory and streetclear==1:
                    print('''The street is already cleared.''')
                if 'bomb' not in inventory:
                    print('''You need a BOMB for that.''')
            elif act == 'go back':
                print('You turn and walk back up the main road, seemingly having forgotten something. You are back at the Great Gates.')
                dnd.greatgates()
            elif act == 'use healing potion':
                if 'Healing Potion' in inventory:
                    actions.healingpotion()
                if 'Healing Potion' not in inventory:
                    print('You do not have any Healing Potions')
            elif act == 'inventory':
                actions.inventory()
            elif act == 'status':
                actions.health()
            else:
                print('''I don't understand.''')
                pass
    def churchcourtyard():
        print()
        global streetclear
        global gold
        global strmod
        global hp
        global hpmax
        global prayer
        churchscrawl='''The courtyard ahead of you is small and secluded. In the middle is a gurgling FOUNTAIN with a statue in the middle.
Behind the fountain is a small but ornate CHURCH, the doors crushed by the partially collapse stonework and open. Another small ROAD leads
out opposite of where you came in. To go to Khirn Square, type 'khirn square' '''

        w3=actions.wischeck()
        ichurch=actions.intcheck()
        hchurch=actions.intcheck()
        ifountain=actions.intcheck()
        hfountain=actions.intcheck()

        while True:
            act=input('What would you like to do? ')

            if act == 'repeat':
                print(churchscrawl)
            elif act == 'inventory':
                actions.inventory()
            elif act == 'status':
                actions.health()
            elif act == 'help':
                print('''Investigating inside the church could be interesting, or just move on through the road
to advance.''')
            elif act == 'khirn square' or act == 'go to khirn square':
                print('''You head into Khirn Square through the alley.''')
                dnd.khirnsquare()
            elif act == 'look around':
                print('Perception: ', w3)

                if w3 >= 12:
                    print('''This small courtyard seems to have once served as a public egress area for the CHURCH on the other side.
The CHURCH seems to be dedicated to Moradin, a dwarvish god of the Forge. There is a beautifully crafted FOUNTAIN in front of the doors that
has fallen partially to ruin, depicting a female dwarvish figure. A SMALL ROAD leads out to what looks like a MARKET place.''')
                if w3<12:
                    print('''There is a CHURCH on the other side of the courtyard, a FOUNTAIN in front of it, and a SMALL ROAD leading out.''')
            elif act == 'investigate church':
                print('Investigation: ', ichurch)

                if ichurch >= 13:
                    print('''The front of this church is intricately carved to a degree you have never seen, depicting scenes from dwarvish myth,
smiths and other skilled craftsmen working in their field, and images of important theological figures. The doors are stone and wood, the wood partially
rotted away with time and the stone worn down. The doors have been breached inward as a large chunk of the wall has fallen onto them and crushed them,
opening the entrance. Inside you can see a small, simple altar and some pews.''')
                if ichurch < 13:
                    print('''The church appears very old, and the doors have been crushed by a chunk of debris that has opened the way in.''')
                
                ent=input('Enter? y/n ')
                if ent == 'n':
                    print('''Churches get looted first. Most likely nothing good inside.''')
                if ent == 'y':
                    print('''The inside of the church is derilict, but strangely warm. A simple altar lies at the head of the stone pews and
empty torch sconces line the walls and the support pillars. On the altar, a small wooden bowl lies on a simple cloth holding a few scattered gold coins.
A bust of Moradin striking an anvil looks down at the altar.''')
                    print('''Action Choices:
-A: Take the Gold
-B: Leave an offering
-C: Leave the church''')
                    mor=0

                    while mor==0:
                        ch=input('''What do you do? ''')

                        if ch =='A':
                            print('''You take the 3 gold pieces that were left in the offering bowl, and feel the warmth leave the room.
You don't know what it is, but you feel as if you have done wrong.''')
                            gold+=3
                            mor=1
                        elif ch == 'B':
                            mor2=0
                            while mor2==0:
                                print('You have ',gold, 'gold')
                                num = input('How much? ')
                                
                                if int(num) >= gold:
                                    gold=0
                                    print('''You give all you have to the altar and kneel in prayer, hoping for some guidance through
this challenge. You feel the warmth in the room embrace you, and you feel safe. All missing HP is restored.''')
                                    hp=hpmax

                                    if prayer==0:
                                        print('''You gain a +2 bonus to Strength Rolls. You leave the church and head back into the courtyard.''')
                                        strmod+=2
                                        prayer=1
                                        mor2=1
                                    elif prayer==1:
                                        print('You have already gained the blessing of the forge. You leave the church and head back into the courtyard.')
                                        mor2=1
                                    mor=1
                                elif int(num) < gold:
                                    gold-=int(num)
                                    print('''You leave what you feel you can spare, unsure if it will do anything, but feeling like
a little extra luck wouldn't hurt. The warmth of the room feels more inviting than it did before.''')
                                    
                                    if prayer==0:
                                        print('''You gain a +2 bonus to Strength rolls. You leave the church and head back into the courtyard.''')
                                        strmod+=2
                                        prayer=1
                                        mor2=1
                                    elif prayer==1:
                                        print('You have already gained the blessing of the forge. You leave the church and head back into the courtyard.')
                                        mor2=1
                                    mor=1
                                elif int(num) is not int:
                                    print('That is not an amount')

                        elif ch == 'C':
                            print('''You think it wise to not steal from the gods, but you are also a bit light on coin at the moment.
You exit the church.''')
                            mor=1
                        else:
                            print('I dont understand')
            elif act == 'history of church':
                print('History: ', hchurch)

                if hchurch >=13:
                    print('''This church is dedicated to Moradin, the most commonly depicted god in the Svartalfir pantheon, Svartalfir denoting
them as being of dwarvish origin. Moradin is a god of the forge pricipally. He is the patron deity of skilled artisans and craftsmen,
which explains his great populatry with most dwarvish peoples, as one of the through lines through almost all dwarvish cultures is
placing a very high value on craftsmanship. This church is small even by dwarvish standards, but the skill of it's stone masons 
is obvious in what is left of the reliefs carved in the walls and pillars depicting extremely detailed accounts of religious scenes you
are not familiar with.''')
                elif hchurch < 13:
                    print('''This church is dedicated to Moradin, a dwarvish god of the forge.''')
            elif act == 'take road' or act == 'market' or act =='go to market':
                if streetclear==1:
                    print('''You take the small side road leading out of the courtyard, breaking into a large marketplace. The many various stands and stalls have
the remnants of colored cloth banners and signage that would have denoted which stands were which, including one still intact with a clay 
POT on it. In the center, you can see a pile of WRECKAGE, and the hint of movement within. To one side, a particular store with a cartoonish 
bomb denotes an abandoned POWDER SHOP. The MAIN ROAD continues onward towards a CASTLE in the distance or backwards to KHIRN SQUARE, 
where it is blocked off by rubble. To the side of the road lies a SKELETON.''')
                if streetclear==0:
                    print('''You take the small side road leading out of the courtyard, breaking into a large marketplace. The many various stands and stalls have
the remnants of colored cloth banners and signage that would have denoted which stands were which, including one still intact with a clay 
POT on it. In the center, you can see a pile of WRECKAGE, and the hint of movement within. To one side, a particular store with a cartoonish 
bomb denotes an abandoned POWDER SHOP. The MAIN ROAD continues onward towards a CASTLE in the distance or backwards to KHIRN SQUARE. 
To the side of the road lies a SKELETON.''')
                dnd.market()
            elif act == 'history of fountain':
                print('History: ', hfountain)

                if hfountain >= 12:
                    print('''The statue in this fountain depicts an angelic dwrvish goddess known as Mya. A lesser known Svartalfir deity,
Mya is the goddess of clan, family and wisdom. She is often used as a symbol of unity during times of war or struggle by dwarvish societies.
Here, she is being positioned as a protector, providing fresh water to the people of the city.''')
                elif hfountain <12:
                    print('''The fountain's statue depicts a female dwarvish angelic entity, although the specifics of who she is eludes you.''')
            elif act == 'investigate fountain':
                print('Investigation: ', ifountain)

                if ifountain >=12:
                    print('''The statue is remarkably undamaged for how old it is, and is also somehow still functioning, fresh water gurgling
up through the pipework. This probably indicates that whatever force detroyed this city held some sort of reverence for this goddess. You notice
a collection of scatered coins on the bottom of the fountain.''')
                if ifountain<12:
                    print('''The statue is remarkably undamaged for how old it is and somehow still functioning.''')
            elif act == 'throw coin into fountain' or act == 'toss coin into fountain' or act == 'toss coin' or act == 'throw coin' or act == 'flick coin' or act == 'flick coin into fountain':
                if gold > 0:
                    print('''You flick a coin into the fountain, saying a small prayer to Mya for protection. You don't know if she heard you,
but the thought that perhaps she did is conforting.''')
                    gold-=1
                elif gold ==0:
                    print('You want to offer a coin, but realize you have none.')

            else:
                print('I dont understand')
        pass
    def sewer():
        print()
        global gold
        sewerscrawl='''The sewer air is damp with the smell of rotting meat and mold. The sound of slowly running water is echoing through
the maintenance shaft you find yourself in. The age old dried BLOODSTAINS on the floor lead directly to a skeleton just behind the door, seeming 
as though this person died while crawling towards it in an attempt to flee...something. At the end of the hallway, you find the source of the sound.
A T in the road contains a channel, carrying flowing water from right to left. Another SKELETON with a BACKPACK is sitting propped on the wall.'''

        sewerperc=actions.wischeck()
        bodysearch=actions.intcheck()
        bloodcheck=actions.wischeck()
        backpack=actions.intcheck()
        gougecheck=actions.intcheck()
        fangcheck=actions.intcheck()


        while True:
            #look around, cause of death, search skeleton, bloodstains
            act=input('What would you like to do? ')

            if act == 'look around':
                print('Perception: ', sewerperc)

                if sewerperc >= 15:
                    print('''The maintenance shaft intersects a parallel sewer channel, with water flowing from right to left.
A very old corpse on the corner of the wall to the left, where you can see on the wall a few feet farther to the left some very deep GOUGES 
in the wall, which look as though they were carved out by a great impact and are also stained with blood. Looking to the left, you can see 
that the tunnel opens up about 30 feet down, but it is too dark to make out details. To the right, the tunnel appears to continue on for longer.''')
                elif sewerperc < 15 and sewerperc >= 12:
                    print('''The maintenance shaft intersects a parallel sewer channel, with water flowing from right to left.
A very old corpse on the corner of the wall to the left, where you can see on the wall a few feet farther to the left some very deep gouges in the wall,
whch look as though they were carved out by a great impact and are also stained with blood.''')
                elif sewerperc < 12:
                    print('''You look long and hard but don't notice any new details.''')
            elif act == 'repeat':
                print(sewerscrawl)
            elif act == 'investigate skeleton' or act == 'investigate body' or act == 'investigate corpse':
                print('Investigation: ', bodysearch)

                if bodysearch >= 13:
                    print('''Embedded in the skeleton's spinal column are several 2 or 3 inch long SPINES that resemble talons or fangs of some kind. 
In the areas where these spikes are located, the bones are severely cracked, indicating a strong impact. You take one of the SPINES out of curiosity.''')
                    inventory.append('strange spine')
                elif bodysearch < 13:
                    print('''The body has several broken bones indicating some sort of impact, but the source eludes you.''')
            elif act == 'investigate bloodstains':
                print('Investigation: ', bloodcheck)

                if bloodcheck >=13:
                    print('''The blood was smeared across the floor, indicating the person was crawling away from something. Also, the sheer amount
tells you that either the person was grievously wounded or they were infected with some sort of poison preventing clotting.''')
                if bloodcheck < 13:
                    print('''You are unable to learn anything useful from the blood.''')
            elif act == 'investigate backpack':
                print('Investigation: ', backpack)

                if backpack >= 15:
                    print('''In the backpack you find a pouch of 6 gold and a crudely drawn map of the sewer system. Heading to the right
leads to a cistern where you can probably find a way out of the sewer. To the left is a refuse collection pit, that allows water to filter
down and leave behind debris. It is a deadend, but could have some valuable resources.''')
                    gold+=6
                elif backpack < 15:
                    print('''In the backpack you find a pouch of 6 gold.''')
                    gold +=6
            elif act == 'investigate gouges':
                print('Investigation: ', gougecheck)

                if gougecheck >= 13:
                    print('''The gouges form a fixed pattern on the wall suggesting they were made by one single swipe of some monster's
massive claws or tail spikes. The grooves cut about 2-3 inches deep into solid stone, so this beast is clearly extremely dangerous.''')
                if gougecheck < 13:
                    print('''You fail to learn anything new from the gouges in the wall.''')
            elif act == 'look at spine' or act == 'look at spines':
                print('Arcana: ', fangcheck)

                if fangcheck >= 15:
                    print('''The spine reeks of refuse and disease with an almost sulfuric tinge in the back, creating a horrific odor.
Only one creature comes to mind that could have grown this, a type of sludge demon called an Otyugh that lives in garbage and excrement,
which it eats to survive as well as ambushing anything that walks by. This creature is far stronger than you can manage to defeat in combat,
and even if you could kill it, it is likely you would die from infection mere hours after the fight. You should do your best to avoid this creature
unless you are sure it is worth it.''')
                if fangcheck < 15:
                    print('''The spine could belong to any manner of beast, but based on the damage you can see around you, it would likely be
best to avoid it.''')
            elif act == 'go right':
                print('''To the right, the tunnel continues for a fair distance before opening up. The room is a large, cylindrical cistern
with a shallow pool of standing, algae covered water taking up the center. You noticed some WRITING on the walls in a language you do not 
understand, before you notice the large network of wooden bridges built over the water, leading to the other side, where you see a 
PERSON rooting around in a pile of rubble. He is wearing a large backpack and doesn't seem to notice you.''')
                dnd.cistern()
            elif act == 'go left':
                print('''Down this direction you see what would once have likely been a collection point for refuse that would have had to be 
cleaned often, but has since been left to fill up and overflow. The downsides of this are that anything that has died in the city for the last 
600 years has ended up here to decompose, leaving a truly horrendous stench. The benefit, however, is that there seems to be a lot of 
interesting TREASURE piled up in the MUD PIT. Armor, weapons, and unopened bags that could contain any number of trinkets are scattered about 
the pit. The wall next to you is crumbling, leaving some small bits of RUBBLE on the ground.''')
                dnd.otyugh()
            elif act == 'go back':
                print('''You decide to head back out the maintenance shaft into the Great Gates again.''')
                dnd.greatgates()
            elif act == 'inventory':
                actions.inventory()
            elif act == 'status':
                actions.health()
            elif act == 'help':
                print('''Investigate the signs of violence to find what could have caused it and make your decisions from there.''')
            elif act == 'repeat':
                print(sewerscrawl)
            elif act == 'use healing potion':
                if 'Healing Potion' in inventory:
                    actions.healingpotion()
                if 'Healing Potion' not in inventory:
                    print('You do not have any Healing Potions')
            else:
                print('I dont understand.')
        pass
    def otyugh(): #mudpit, some bait illusion loot in it. If they go for it, they make a dex check. On a failure they die, on a success they run.
        otyughscrawl='''The MUD PIT in the middle of this circular room is littered with assorted TREASURES, accumulated over the course of centuries of trapped flow.
The water from the sewer flows slowly into the trap, filtering out the mud and debris before it presumably continues flowing somewhere below. It appears solid enough
to walk on, though you can't be sure. The wall next to you is crumbling, leaving some RUBBLE on the ground.'''
        print()

        #variables
        otlook=actions.wischeck()
        otevade=actions.dexcheck()
        global hp, hpmax, strmod, dexmod
        #action loop
        while True:

            act=input('What would you like to do? ')

            if act == 'repeat':
                print(otyughscrawl)
            elif act == 'inventory':
                actions.inventory()
            elif act == 'status':
                actions.health()
            elif act == 'help': 
                if 'strange spine' in inventory:
                    print('''The spine you found earlier suggests that perhaps there is something lurking in this pit that could be very dangerous. There are a few 
very similar looking spines scattered about the mud pit that you can see.''')
                else:
                    print('''The pit is loaded with scattered debris and items that you could potentially find use of.''')
            elif act == 'use healing potion':
                if 'Healing Potion' in inventory:
                    actions.healingpotion()
                elif 'Healing Potion' not in inventory:
                    print('You do not have any Healing Potions')
            elif act == 'go back':
                print('''You head back to the sewer junction.''')
                dnd.sewer()
            elif act == 'investigate rubble':
                print('''It's just a pile of rocks, each of them roughly the size of a fist.''')
            
            elif act == 'look around' or act == 'look at treasure' or act == 'look at treasures' or act == 'look at mud pit':
                print('Perception: ', otlook)

                if otlook >= 15:
                    print('''As you look about the room you notice a few things that catch your eye, the first being that the shadows
in the mud pit are a bit...off. The light from your torch touches the unpened bags and metallic weapons in the pit, but the bags do 
not cast shadows nor does the shine glint off the metal as it should. Secondly, some of the items appear to pass through the rim of 
the pit as if it were air, the hint of a sword seemingly cut off as it phases through the stone. Thirdly, you notice a very slight, 
almost imperceptible movement beneath the mud. Rhythmic and easily missed, the mud rises and falls accompanied by a slight sound. 
Breathing. Something is hiding under the mud, and you put together that it is likely creating illusions of treasure to lure 
passersby into the pit so it can attack.''')
                if otlook < 15 and otlook >= 10:
                    print('''As you look about the room you notice a few things that catch your eye, the first being that the shadows 
in the mud pit are a bit...off. The light from your torch touches the unpened bags and metallic weapons in the pit, but the bags do 
not cast shadows nor does the shine glint off the metal as it should. Secondly, some of the items appear to pass through the rim of 
the pit as if it were air, the hint of a sword seemingly cut off as it phases through the stone.''')
                if otlook < 10:
                    print('''You look into the pit and see an ecclectic assortment of ancient looking weapons, armor, and other equipment. It's a wonder that no one
has found and taken this yet.''')
            elif act == 'go to treasures' or act == 'walk on mud pit' or act == 'take treasure' or act == 'investigate treasure' or act == 'investigate mudpit' or act == 'go to treasure':
                print('''As you step on the mud pit, your feet sink in to the calf, stuck in the age old build up of mud, mold, slime and other less desirable substances.
The mud in the center of the pit shifts, as you see three large, spine covered tentacles rise out of the refuse. A collection of amber, vertically slited eyes open from beneath the
surface, and a massive toothy maw rises out of the pit, stinking of rot, bacteria, and venom. It lashes out at you with furious hunger.''')
                print('Dexterity Saving Throw: ', otevade)

                if otevade >= 16:
                    print('''You just manage to wrench your feet free of the mud just in time to dive out of the pit, away from the lashing tentacles and sprint down the tunnel back to safety.
You see the massive beast sink back beneath the mud just as you break back to the sewer junction, lucky to be alive. You are back in the sewer junction.''')
                    dnd.sewer()
                if otevade < 16 and otevade >= 12:
                    print('''Your feet are stuck enough in the mud that you cannot get them free, however you manage to duck under the swinging tentacle just as it passes by.
You feel a spine rake across your back, but the majority of the impact is missed, as you then get your feet free and sprint back to the sewer junction. You feel the wound on
your back festering, and surmise the spine was probably either poisonous or coated in enough filth to infect even the smallest wound. You take a -2 penalty to strength rolls,
dexterity rolls, and your hp maximum. You are back in the sewer junction, just as you turn to see the beast sink back into it's filth.''')
                    hpmax-=2
                    if hp> hpmax:
                        hp=hpmax
                    strmod-=2
                    dexmod-=2
                    dnd.sewer()
                if otevade < 12:
                    print('''You are either too stuck or too surprised to react to the tree trunk sized, spine covered appendage that swings towards you. It catches you
directly in the stomach with all of it's might and wraps around you, holding you aloft. Without much posible resistance from you, it drops you into it's mouth and chews. You are dead.''')
                    print('''When something is too good to be true, it most likely isn't. Remember that next time.''')
                    sys.exit()
            elif act == 'throw rock' or act == 'throw rubble':
                print('''You take a piece of debris from the pile next to you and throw it into the pit. Immediately, a tentacle rises from the mud and slams down at the spot 
the rock hits. You don't have time to think about how clever you are before your legs are already carrying you out of the room at break neck speed. you make it back to the
sewer junction just as you turn to see the beast sink back into the filth that is it's home. You are back in the sewer junction, a little bit wiser than when you left.''')
                dnd.sewer()
            elif act == 'look at rubble':
                print('''There is a pile of small ROCKS next to you from a broken portion of the wall.''')
            else:
                print('I dont understand.')
        pass
    def cistern(): #signs of recent action, merchant, exit into Khirn Square Alley (do inside cistern function). Once they leave, they can come back through the manhole.
        cisternscrawl='''The room is a large, cylindrical cistern with a shallow pool of standing, algae covered water taking up the center. You noticed some 
WRITING on the walls in a language you do not understand, before you notice the large network of wooden bridges built over the water, leading to the other side, 
where you see a PERSON rooting aroundin a pile of rubble. He is wearing a large backpack and doesn't seem to notice you. On the other side
of the cistern is a small side room with a LADDER.'''
        print()
        
        lookcistern=actions.wischeck()
        iwriting=actions.intcheck()
        lookperson=actions.wischeck()
        sneakcistern=actions.dexcheck()
        pickpock=actions.dexcheck()
        hagpot=actions.chacheck()
        hagkey=actions.chacheck()
        hagsellspine=actions.chacheck()
        hagsellring=actions.chacheck()
        global manhole
        global merchdead
        global gold
        global pocketempty
        global shopsopen
        global merchnotice
        global inventory
        global merchantinventory

        merchpercept=d(20)+3
        
        if merchnotice == 0:
            merchnotice = 0
        else:
            merchnotice = 1
        
        if merchdead == 0:
            merchdead= 0
        else:
            merchdead= 1
        
        if pocketempty==0:
            pocketempty=0
        else:
            pocketempty=1
        
        if shopsopen==0:
            shopsopen=0
        else:
            shopsopen=1
        


        while True:
            act = input('What would you like to do? ')

            if act == 'repeat':
                print(cisternscrawl)
            elif act == 'inventory':
                actions.inventory()
            elif act == 'status':
                actions.health()
            elif act == 'use healing potion':
                if 'Healing Potion' in inventory:
                    actions.healingpotion()
                if 'Healing Potion' not in inventory:
                    print('You do not have any Healing Potions')
            elif act == 'help':
                print('''The person doesn't seem to notice you yet...try to decide if they are friend or foe, then act accordingly.
You could approach with SNEAK, or simply approach if you think they are safe.''')
            elif act == 'take sewer' or act == 'back to sewer' or act == 'sewer':
                print('''You head back to the sewer junction.''')
                dnd.sewer()
            elif act == 'go back':
                if manhole == 0:
                    print('''You head back to the sewer junction.''')
                    dnd.sewer()
                if manhole == 1:
                    cho=input('Sewer junction or through the Manhole? s/m ') #maybe need loop for unexpected answers

                    if cho == 's':
                        print('''You head back to the sewer junction.''')
                        dnd.sewer()
                    elif cho == 'm':
                        frt=input('''You ascend through the manhole again. Do you want to head to Khirn Square or the Church Courtyard? (k/c) ''')#maybe need loop for unexpected answers
                        
                        if frt == 'k':
                            print('You head back to Khirn Square, emerging from the ALLEY')
                            dnd.khirnsquare()
                        if frt == 'c':
                            print('You turn into the Church Courtyard, emerging from the ALLEY')
                            dnd.churchcourtyard()



##################################################



            elif act == 'look around':
                print('Perception: ', lookcistern)

                if lookcistern >= 12:
                    print('''The wooden bridge network seems to be sturdy enough, although pretty old. The writing on the wall is carved into the stone,
and it is not a language that you recognize, despite your experience. The person across the water does not seem to have noticed you, and to your left
on the other side of the room is another door, where you can see a crude ladder leading up.''')
                if lookcistern < 12:
                    print('''You look again, but don't notice anything new. The ladder on the other side of the room leads up to a closed manhole.''')
            elif act == 'investigate writing':
                print('Investigation: ', iwriting)

                if iwriting >= 14:
                    print('''The writing is very old, but you are able to determine with closer inspection that it is a form of dwarvish Thieves'
Cant, a constructed code language used as a common form of communication with many criminal networks. Each location and organization has it's own
version, so it would be very difficult to decipher this, but it does mark this location as having had heavy criminal traffic in the past.''') 

                if iwriting <14 and iwriting >=8:
                    print('''The writing seems to be a form of Thieve's Cant, a constructed code language used by criminals, but since every region
and organization will have it's own version of the code, it is indecipherable. Additionally, it is so old, the details have been worn away.''')
                if iwriting < 8:
                    print('''The details of the writing have been so worn away with time that you have no clue what this could have once been.''')

            elif act == 'look at person':
                print('Insight: ', lookperson)

                if merchnotice==0:

                    if lookperson >= 13:
                        print('''The person is rummaging through a pile of debris, and has seemlingly not noticed you. You see him looking at pieces of stone
    very closely, brushing them off with a small brush, and then either putting it back or putting it in his backpack. You deduce this is one of your lost archaeologists.''')
                    if lookperson < 13:
                        print('''The person is too far away to make out any details of what he looks like or what he is doing.''')
                elif merchnotice==1:
                    print('''The merchant is sitting contently, looking through his wares.''')
            elif act == 'pick pocket' or act == 'pick merchants pocket' or act == 'pick balins pocket' or act == '''pick merchant's pocket''' or act == '''pick balin's pocket''':
                print('You have to SNEAK UP to him first. Right now he either already knows youre here or youre too far away.')
            elif act == 'sneak up on person' or act == 'sneak up to person' or act == 'sneak up' or act == 'sneak past' or act == 'sneak up to merchant' or act == 'sneak up on merchant':
                if merchdead == 0 and merchnotice==0:
                    print('Stealth: ', sneakcistern)
                    print('Persons Perception: ', merchpercept)

                    if sneakcistern > merchpercept:
                        print('''You manage to sneak up to the person undetected, getting very close to him. You could walk past him to the exit, 
    surprise attack him, or try to pick his pocket.''')

                        print('''Choices:
    -A: Sneak past to exit
    -B: Surprise Attack
    -C: Pick his Pocket
    -D: Talk''')

                        while True:

                            choice=input('What would you like to do? ')

                            if choice == 'A':
                                manhole=1
                                print('''You sneak past, leaving the man to his business. The ladder leads to a manhole.''')
                                print('''Exiting the manhole, you leave it open just in case you wish to return. You 
see a small courtyard to one side of the alley you emerge into, and a larger square on the other.''')
                                move=input('Courtyard or Square?')

                                if move == 'courtyard':
                                    print('''The courtyard ahead of you is small and secluded. In the middle is a gurgling FOUNTAIN with a statue in the middle.
Behind the fountain is a small but ornate CHURCH, the doors crushed by the partially collapse stonework and open. Another small ROAD leads
out opposite of where you came in. To go to Khirn Square, type 'khirn square' ''')
                                    dnd.churchcourtyard()
                                elif move == 'square':
                                    print('''In the center of this square is a large STATUE of a dwarvish figure, his sword planted in the ground in front of him. 
There are numerous buildings packed tightly together around the edge of the square, many of them collapsed into themselves.''')
                                    dnd.khirnsquare()
                                else:
                                    print('I dont understand')
                            elif choice == 'B':
                                merchdead=1
                                print('''You attack the man, and he never saw it coming. He dies quickly, dropping whatever rock he was holding and collapsing.''')
                                print('''In his pockets you find 10 gold and a healing potion and a map with a path from Tierengard to this city marked. 
You realize this was likely one of the archaeologists. You'll never know what happened now, but you could still find the others.''')
                                gold+=10
                                inventory.append('Healing Potion')
                                break
                            elif choice == 'C':
                                print('Sleight of Hand: ', pickpock)
                                print('''Target's Perception: ''', merchpercept)

                                if pickpock > merchpercept and pocketempty==0:
                                    pocketempty=1
                                    print('''You find 5 gold and a Healing Potion.''')
                                    gold +=5
                                    inventory.append('Healing Potion')
                                    break
                                if pickpock > merchpercept and pocketempty==1:
                                    print('You already got everything you could out of his pockets.')
                                    break
                                elif pickpock <= merchpercept:
                                    merchnotice=1
                                    shopsopen=1
                                    print('''The person jumps back as he feels your hand enter his pocket. He screams, startled by your presence.''')
                                    print(''' 'AH! Oh boy, you really gave me a start there...were you trying to pick my pocket? A good collector never keeps his goods where
they can be easily found, you fool! Well, either way, I'm always game for people to test my perceptive skills so I won't hold it against you. The names Balin, pleasure to meet you.
I came here to do some archaeological collecting but my partner got lost somewhere back by the castle...the dungeons collapsed and by the time I got out he was nowhere to be found!
...Oh, you came here on contract to rescue us? Well that IS good fortune isn't it? I'd love to help you out, but you see I'm entrepreneurially minded so here's what I'll do. If you ever
find something you want to sell, or if you want to peruse my collection to by something, you just let me know and I'll consider it. Good luck on your search!
Oh, by the way, that ladder over there leads up and out into the city if you wanted a quick way out.' ''')
                                    break
                            elif choice == 'D':
                                merchnotice=1
                                shopsopen=1
                                print('''You sneak up closer to the merchant without him noticing, then begin to talk. He is extremely startled.''')
                                print('''GAH! Oh boy, you really gave me quite the start there. What are you doing sneaking up on people like that in a place like this? You could
kill someone with that kind of scare. What are you doing all the way down here?...I see...Well, you're in luck then because I am one of those archaeologists! My partner, on the other hand,
I don't know. We were exploring under the castle and then something triggered a collapse, seperating us. I got out but I haven't been able to find him. Oh, by the way, the names Balin, 
pleasure to meet you. I'd love to help you out, but you see I'm entrepreneurially minded so here's what I'll do. If you ever
find something you want to sell, or if you want to peruse my collection to by something, you just let me know and I'll consider it. Good luck on your search!' ''')
                                break
                    elif sneakcistern <= merchpercept:
                        print('''You attempt to sneak up on the person, but your foot hits a creaky board right as you get close and alerts him to your presence.
He turns around and looks at you, terrified.''')
                        merchnotice=1
                        shopsopen=1
                        print('''GAH! Oh boy, you really gave me quite the start there. What are you doing sneaking up on people like that in a place like this? You could
kill someone with that kind of scare. What are you doing all the way down here?...I see...Well, you're in luck then because I am one of those archaeologists! My partner, on the other hand,
I don't know. We were exploring under the castle and then something triggered a collapse, seperating us. I got out but I haven't been able to find him. Oh, by the way, the names Balin, 
pleasure to meet you. I'd love to help you out, but you see I'm entrepreneurially minded so here's what I'll do. If you ever
find something you want to sell, or if you want to peruse my collection to by something, you just let me know and I'll consider it. Good luck on your search!' ''')
                elif merchdead==0 and merchnotice == 1:
                    print('''He already knows you are here...it isn't going to work, so you decide this may not be the best idea.''')
                elif merchdead == 1:
                    print('''What are you sneaking up on? You killed him already.''')

            elif act == 'talk to merchant' or act == 'talk to person' or act == 'talk to balin' or act == 'talk to Balin':
                if merchnotice==0:
                    merchnotice=1
                    shopsopen=1
                    print('''You walk towards the man and announce yourself. The sound of your voice seems to startle him greatly.''')
                    print('''GAH! Oh boy, you really gave me quite the start there. What are you doing sneaking up on people like that in a place like this? You could
kill someone with that kind of scare. What are you doing all the way down here?...I see...Well, you're in luck then because I am one of those archaeologists! My partner, on the other hand,
I don't know. We were exploring under the castle and then something triggered a collapse, seperating us. I got out but I haven't been able to find him. Oh, by the way, the names Balin, 
pleasure to meet you. I'd love to help you out, but you see I'm entrepreneurially minded so here's what I'll do. If you ever
find something you want to sell, or if you want to peruse my collection to buy something, you just let me know and I'll consider it. Good luck on your search!' ''')
                    break
                elif merchdead==1:
                    print('''You attempt to have an intellectual conversation with the merchant's corpse. It goes about as well as you would expect.''')
                    break

                elif merchnotice==1 and shopsopen==1:
                    print('''The merchant turns to you and speaks.''')
                    print(''' 'Oh, you're back! Did you come to buy or sell?' ''')
                    bs=input(' Buy, Sell, or leave? (b/s/exit) ')

                    if bs == 'b':
                        while True: 
                            print('Available Merchandise: ',merchantinventory)
                            print('Your Gold: ',gold)
                            if 'Ornate Key' in merchantinventory:
                                print('The merchant has a very ornate but old looking key dangling in his large collection of useless antiques.')

                            buy=input('''What would you like to buy? type 'never mind' to exit. ''')

                            if buy in merchantinventory:
                                if buy == 'healing potion':
                                    prce= input('That will cost 6 gold. Is that ok? (yes/no/haggle) ')

                                    if prce == 'yes':
                                        if gold >= 6:
                                            gold-=6
                                            inventory.append('Healing Potion')
                                            merchantinventory.remove('Healing Potion')
                                            print('Pleasure doing business.')
                                        elif gold < 6:
                                            print('Youre a little light on coin there. Sorry, cant make the sale.')
                                    elif prce == 'no':
                                        print('Well, if you change your mind I am always here.')
                                    elif prce == 'haggle':
                                        print('Persuasion: ', hagpot)
                                        
                                        if hagpot >= 14:
                                            print('''Well, I suppose since you're looking for my partner I can give you a discount.''')
                                            rex=0
                                            while rex==0:
                                                t=input('How about 4 gold? (y/n) ')

                                                if t == 'y':
                                                    if gold >= 4:
                                                        gold-=4
                                                        inventory.append('Healing Potion')
                                                        merchantinventory.remove('Healing Potion')
                                                        print('Pleasure doing business')
                                                        rex=1
                                                    if gold < 4:
                                                        print('Why would you agree if you didnt have the money anyway?')
                                                        rex=1
                                                elif t == 'n':
                                                    print('Sorry, thats the best the deal is going to get.')
                                                    rex=1
                                                else:
                                                    print('I dont understand')
                                        if hagpot < 14:
                                            print('Sorry, thats the best the deal is going to get. Take it or leave it.')
                                            wdf=0
                                            while wdf==0:
                                                r=input('Take the deal for 6 gold? (y/n)')

                                                if r == 'y':
                                                    if gold >= 6:
                                                        gold-=6
                                                        inventory.append('Healing Potion')
                                                        merchantinventory.remove('Healing Potion')
                                                        print('Pleasure doing business.')
                                                        wdf=1
                                                    elif gold < 6:
                                                        print('You dont even have the coin...')
                                                        wdf=1
                                                elif r == 'n':
                                                    print('Well if you change your mind I am always here')
                                                    wdf=1
                                                else:
                                                    print('I dont understand')
                                if buy == 'Ornate Key':

                                    ####
                                    prce= input('That will cost 45 gold. Is that ok? (yes/no/haggle) ')

                                    if prce == 'yes':
                                        if gold >= 45:
                                            gold-=45
                                            inventory.append('Ornate Key')
                                            merchantinventory.remove('Ornate Key')
                                            print('Pleasure doing business.')
                                        elif gold < 45:
                                            print('Youre a little light on coin there. Sorry, cant make the sale.')
                                    elif prce == 'no':
                                        print('Well, if you change your mind I am always here.')
                                    elif prce == 'haggle':
                                        print('Persuasion: ', hagkey)
                                        
                                        if hagkey >= 18:
                                            print('''Well, I suppose since you're looking for my partner I can give you a discount.''')
                                            rex=0
                                            while rex==0:
                                                t=input('How about 30 gold? (y/n) ')

                                                if t == 'y':
                                                    if gold >= 30:
                                                        gold-=30
                                                        inventory.append('Ornate Key')
                                                        merchantinventory.remove('Ornate Key')
                                                        print('Pleasure doing business')
                                                        rex=1
                                                    if gold < 30:
                                                        print('Why would you agree if you didnt have the money anyway?')
                                                        rex=1
                                                elif t == 'n':
                                                    print('Sorry, thats the best the deal is going to get.')
                                                    rex=1
                                                else:
                                                    print('I dont understand')
                                        if hagkey < 14:
                                            print('Sorry, thats the best the deal is going to get. Take it or leave it.')
                                            wdf=0
                                            while wdf==0:
                                                r=input('Take the deal for 30 gold? (y/n)')

                                                if r == 'y':
                                                    if gold >= 30:
                                                        gold-=30
                                                        inventory.append('Ornate Key')
                                                        merchantinventory.remove('Ornate Key')
                                                        print('Pleasure doing business.')
                                                        wdf=1
                                                    elif gold < 30:
                                                        print('You dont even have the coin...')
                                                        wdf=1
                                                elif r == 'n':
                                                    print('Well if you change your mind I am always here')
                                                    wdf=1
                                                else:
                                                    print('I dont understand')

                                                    ######
                                if buy == 'gimlis ring':
                                    print('''What? You just sold that to me, I'm not giving it back! You know what, I'll cut you a deal but this is
really irregular for me since there's normally a no buybacks rule. I'll sell it back to you for 20 gold how about that? Only a 5 gold loss on you, call it a
time wasters tax.''')
                                    bback=input('Take the deal? y/n ')
                                    if bback=='y' and gold>=20:
                                        gold-=20
                                        merchantinventory.remove('gimlis ring')
                                        inventory.append('gimlis ring')
                                        print('''Thanks, heres your ring back, but I still dont understand why you sold it in the first place if
you wanted it that bad.''')
                                    elif bback=='y' and gold <=20:
                                        print('''What, are you trying to fleece me? You dont even have 20 gold. Get lost.''')
                                    elif bback=='n':
                                        print('''Wel, the ring is staying here then.''')
                                    else:
                                        print('''I'm going to assume that means youre not interested? Oh well, the ring stays with me then.''')

                            elif buy not in merchantinventory:
                                if buy == 'never mind' or buy == 'nevermind':
                                    print('''Oh, well ok then.''')
                                    break
                                else:
                                    print('Sorry, I either ran out of that or I just never had it in the first place. I can be forgetful sometimes.')
                    elif bs == 's':
                        while True: #finish sell function here
                            print('''The merchant approaches you and takes a look at the contants of your bag. He thinks for a moment...''')
                            print(''' 'I dont buy often, but let's see what we have here' ''')

                            if 'strange spine' in inventory:
                                print('''Wow! A real Otyugh spine! These are very difficult to get without dying in the process, I know some demonologists that will spend a pretty penny
on a thing like this. I'll give you ten gold for it!''')
                                de=input('Take the deal? yes/no/haggle ')

                                if de == 'yes' or de == 'y':
                                    gold+=10
                                    inventory.remove('strange spine')
                                    merchantinventory.append('otyugh spine')
                                    print('Thank you for your business')
                                    break
                                elif de == 'no' or de == 'n':
                                    print('''Well, that's a shame.''')
                                    break
                                elif de == 'haggle' or de == 'h':
                                    print('Persuasion: ', hagsellspine)

                                    if hagsellspine >= 14:
                                        print('''Well...I suppose it is valuable. I can give you 12 gold. How about that?''')

                                        trek=0
                                        while trek == 0:
                                            take=input('Take the deal? y/n ')

                                            if take == 'y':
                                                gold+=12
                                                inventory.remove('strange spine')
                                                merchantinventory.append('otyugh spine')
                                                print('Thank you for your business')
                                                take=1
                                            elif take == 'n':
                                                print('''A shame, but I understand.''')
                                                take=1
                                            else:
                                                print('I dont understand')
                                    elif hagsellspine < 14:
                                        print('''Im sorry, I really cant go any higher.''')

                                        wars=0
                                        while wars == 0:
                                            take2=input('Take the 10 gold? y/n ')

                                            if take2 == 'y':
                                                gold+=10
                                                inventory.remove('strange spine')
                                                merchantinventory.append('otyugh spine')
                                                print('Thank you for your business')
                                                wars=1
                                            elif take2 == 'n':
                                                print('A shame.')
                                                wars=1
                                            else:
                                                print('I dont understand')
                                else:
                                    print('What does that mean? If you cant talk sense then we cant do business. Goodbye.')
                            if 'gimlis ring' in inventory:
                                print('He looks in your bag and pulls out the small golden ring you took from the market.')
                                print('''Well well well, what do we have here? You got a special someone at home this means something to? No? Well, in that case
I would be more than happy to take it off your hands. Yes, well crafed...antique aged for sure...inscribed to Gimli? Is that your name? I thought not, but none 
of my business. I can give you...15 gold for it.''')
                                balin=0
                                while balin==0:
                                    deal=input('Take the deal for 15 gold, refuse, or haggle? y/n/h ')

                                    if deal == 'y':
                                        gold+=15
                                        inventory.remove('gimlis ring')
                                        merchantinventory.append('gimlis ring')
                                        print('''Pleasure doing business with you, I'm sure the museum will love this.''')
                                        balin=1
                                    elif deal == 'n':
                                        print('''Oh, that's a shame. Well, if you change your mind I'm here.''')
                                        balin=1
                                    elif deal == 'h':
                                        print('Persuasion: ', hagsellring)

                                        if hagsellring >= 13:
                                            print('''You drive a hard bargain. I'll give you 18 for it, final offer.''')
                                            deal2=input('Take the deal? y/n ')

                                            if deal2=='y':
                                                gold+=18
                                                inventory.remove('gimlis ring')
                                                merchantinventory.append('gimlis ring')
                                                print('''It stings a little bit but as always, a pleasure.''')
                                                balin=1
                                            elif deal2 == 'n':
                                                print('''Well, I can't go any higher without turning a loss so, sorry.''')
                                                balin=1
                                            else:
                                                print('''That wasn't a yes or a no, but I'll assume it meant no. Goodbye then.''')
                                        elif hagsellring < 13:
                                            print('''Sorry, I can't go any higher. 15 gold, final offer.''')
                                            deal3=input('Take the deal? y/n ')

                                            if deal3=='y':
                                                gold+=15
                                                inventory.remove('gimlis ring')
                                                merchantinventory.append('gimlis ring')
                                                print('''Thanks for the business.''')
                                                balin=1
                                            elif deal3=='n':
                                                print('''A shame, I like that ring.''')
                                                balin=1
                                            else:
                                                print('''I'm gonna assume that means no, which is a shame.''')
                                                balin=1
                                    else:
                                        print('What? ')            
                            else:
                                print('''Sorry friend, not interested in much of what you got here.''')
                                break
                    elif bs == 'exit':
                        print('''Stay safe, hope to see you again.''')
                        break

            elif act == 'take exit' or act == 'take manhole' or act == 'manhole' or act == 'take ladder' or act == 'go to ladder' or act == 'go to side room':
                manhole = 1
                print('''You sneak past, leaving the man to his business. The ladder leads to a manhole.''')
                print('''Exiting the manhole, you leave it open just in case you wish to return. You 
see a small courtyard to one side of the alley you emerge into, and a larger square on the other.''')
                move=input('Courtyard or Square? ')

                if move == 'courtyard':
                    print('''The courtyard ahead of you is small and secluded. In the middle is a gurgling FOUNTAIN with a statue in the middle.
Behind the fountain is a small but ornate CHURCH, the doors crushed by the partially collapse stonework and open. Another small ROAD leads
out opposite of where you came in. To go to Khirn Square, type 'khirn square' ''')
                    dnd.churchcourtyard()
                elif move == 'square':
                    print('''In the center of this square is a large STATUE of a dwarvish figure, his sword planted in the ground in front of him. 
There are numerous buildings packed tightly together around the edge of the square, many of them collapsed into themselves.''')
                    dnd.khirnsquare()
                else:
                    print('I dont understand')
        pass
    def market(): #goblin horde?, gimlis corpse, pottery stand with gimlis lockbox/ring, path to castle, bomb shop
        marketscrawl='''The many various stands and stalls have the remnants of colored cloth banners and signage that would have denoted which 
stands were which, including one still intact with a clay POT on it. In the center, you can see a pile of WRECKAGE, and the hint of movement within. 
To one side, a particular store with a cartoonish bomb denotes an abandoned POWDER SHOP. The MAIN ROAD continues onward towards a CASTLE in the distance 
or backwards to KHIRN SQUARE, where it is blocked off by rubble. To the side of the road, a very old skeleton with a RED SCARF is lying.''' 

        marketscrawl2='''The many various stands and stalls have the remnants of colored cloth banners and signage that would have denoted which 
stands were which, including one still intact with a clay POT on it. In the center, you can see a pile of WRECKAGE, and the hint of movement within. 
To one side, a particular store with a cartoonish bomb denotes an abandoned POWDER SHOP. The MAIN ROAD continues onward towards a CASTLE in the distance 
or backwards to KHIRN SQUARE. To the side of the road, a very old skeleton with a RED SCARF is lying.'''
        print()

        #variables
        perc=actions.wischeck()
        istand=actions.intcheck()
        igoblins=actions.intcheck()
        goblinsneak=actions.dexcheck()
        goblinsave=actions.dexcheck()
        boxpick=actions.dexcheck()
        iring=actions.intcheck()
        climbrub=actions.dexcheck()
        liftrub=actions.strcheck()

        global hp, hpmax
        global streetclear
        global goblins
        if goblins == 1:
            goblins =1
        else:
            goblins=0
        #action loop
        while True:

            act=input('What would you like to do? ')

            if act == 'repeat':
                if streetclear==0:
                    print(marketscrawl)
                else:
                    print(marketscrawl2)
            elif act == 'inventory':
                actions.inventory()
            elif act == 'status':
                actions.health()
            elif act == 'help':
                print('''The WRECKAGE in the center of the market had movement happening inside it...could be dangerous or worth checking out. The way forward seems to 
lead to the CASTLE. The POWDER SHOP could be interesting.''')
            elif act == 'use healing potion':
                if 'Healing Potion' in inventory:
                    actions.healingpotion()
                elif 'Healing Potion' not in inventory:
                    print('You do not have any Healing Potions')
            elif act == 'look around':
                print('Perception: ', perc)
                if perc >= 15:
                    if streetclear==0:
                        print('''You notice a pottery stand across the market with a sign saying 'The Khirngolir Kiln'. The wreckage in the center of the market seems to be crawling with goblins,
possibly a nest. You notice a SKELETON in plain clothes who seems to have died a long time ago, wearing a RED SASH. The POWDER SHOP appears to be empty. The MAIN ROAD to the CASTLE is unblocked.
In the other direction, a street sign says KHIRN SQUARE, but the way is blocked by rubble at the end. ''')
                    if streetclear==1:
                        print('''You notice a pottery stand across the market with a sign saying 'The Khirngolir Kiln'. The wreckage in the center of the market seems to be crawling with goblins,
possibly a nest. You notice a SKELETON in plain clothes who seems to have died a long time ago, wearing a RED SASH. The POWDER SHOP appears to be empty. The MAIN ROAD to the CASTLE is unblocked.
In the other direction, a street sign says KHIRN SQUARE where you blew the way clear.''')
                elif perc < 15 and perc >= 10:
                    if streetclear==0:
                        print('''You notice a pottery stand across the market with a sign saying 'The Khirngolir Kiln'. The wreckage in the center of the market is moving slightly. 
You notice a SKELETON in plain clothes who seems to have died a long time ago, wearing a RED SASH. The POWDER SHOP appears to be empty. The MAIN ROAD to the CASTLE is unblocked.
In the other direction, a street sign says KHIRN SQUARE, but the way is blocked by rubble at the end. ''')
                    if streetclear==1:
                        print('''You notice a pottery stand across the market with a sign saying 'The Khirngolir Kiln'. The wreckage in the center of the market is moving slightly. 
You notice a SKELETON in plain clothes who seems to have died a long time ago, wearing a RED SASH. The POWDER SHOP appears to be empty. The MAIN ROAD to the CASTLE is unblocked.
In the other direction, a street sign says KHIRN SQUARE where you blew the way clear. ''')
                elif perc < 10:
                    print('''You don't notice much more than you have already been told.''')
            elif act == 'go to pottery stand' or act == 'pottery stand' or act == 'go to khirngolir kiln' or act == 'khirngolir kiln' or act == 'investigate pottery stand' or act == 'investigate khirngolir kiln':
                print('Investigation: ', istand)

                if istand >= 12:
                    print('''In the pottery stand, you find a few old trinkets and a fairly recent looking dust outline of a box on the shelf, where a box was likely resting for a long time
before being moved recently. You also notice some distinctly goblin shaped footprints tracking all around the premesis. Looking into the nest in the center of the market from the stand, you think you
catch a glimpse of something metallic roughly the same size as the missing box.''')
                if istand < 12:
                    print('''You find a few useless old pots but nothing of note.''')
            elif act == 'go to wreckage' or act == 'investigate wreckage' or act == 'go to goblins' or act == 'investigate goblins':
                if goblins==1:
                    while True:
                        sne=input('''This amount of goblins could be very dangerous. 
    Do you want to try to approach head on (A) or sneak up (B)? A/B (nevermind to exit) ''')

                        if sne == 'A':
                            print('''You approach the goblin nest in the wreckage and spot an old lockbox in the pile of assorted treasure they've amassed. The large group sees 
    your approach and jumps to attack you.''')

                            print('Dexterity Save: ', goblinsave)

                            if goblinsave >= 14:
                                #hp-=6

                                if hp <= 6:
                                    print('''The goblins manage to grab a hold of you and drag you into the nest. They attack you from all angles in a swarm, until you eventually succumb to your wounds. You are dead.''')
                                    print('''Goblins are viscious beasts, weak alone but very dangerous in numbers. You would be wise to remember that next time.''')
                                    sys.exit()
                                if hp > 6:
                                    hp-=6
                                    print('''You barely manage to escape as the goblins claw at your feet trying to drag you into their nest. You kick them off and run far enough away that they don't feel threatened
    by you anymore and stop chasing, but you very nearly paid with your life. You did, however, manage to grab a small lockbox that was sitting in the pile.''')
                                    inventory.append('lockbox')

                                    if 'lockbox key' in inventory:
                                        print('''You take the key out of your pocket and place it in the lock, opening it up. Inside is a small but very well made golden ring. You take it.''')
                                        inventory.remove('lockbox key')
                                        inventory.remove('lockbox')
                                        inventory.append('gimlis ring')
                                        break
                                    if 'lockbox key' not in inventory:
                                        print('''You dont know what this is, but you hear something small rattling around inside.''')
                                        break
                            if goblinsave < 14:
                                #hp-=12

                                if hp <= 12:
                                    print('''The goblins manage to grab a hold of you and drag you into the nest. They attack you from all angles in a swarm, until you eventually succumb to your wounds. You are dead.''')
                                    print('''Goblins are viscious beasts, weak alone but very dangerous in numbers. You would be wise to remember that next time.''')
                                    sys.exit()
                                if hp > 12:
                                    print('''You barely manage to escape as the goblins claw at your feet trying to drag you into their nest. You kick them off and run far enough away that they don't feel threatened
    by you anymore and stop chasing, but you very nearly paid with your life. You saw a small lockbox in the pile, but were unable to grab it in time.''')
                                    break
                        if sne == 'B':
                            print('Stealth: ', goblinsneak)

                            if goblinsneak >= 14:
                                print('''You manage to sneak up to the pile, where you spot a small metallic lock box. You grab it and sneak away safely.''')
                                inventory.append('lockbox')
                                if 'lockbox key' in inventory:
                                        print('''You take the key out of your pocket and place it in the lock, opening it up. Inside is a small but very well made golden ring. You take it.''')
                                        inventory.remove('lockbox key')
                                        inventory.remove('lockbox')
                                        inventory.append('gimlis ring')
                                        break
                                if 'lockbox key' not in inventory:
                                    print('''You dont know what this is, but you hear something small rattling around inside.''')
                                    break
                            if goblinsneak < 14:
                                print('''You approach the goblin nest in the wreckage and spot an old lockbox in the pile of assorted treasure they've amassed. The large group sees 
    your approach and jumps to attack you.''')

                            print('Dexterity Save: ', goblinsave)

                            if goblinsave >= 14:
                                hp-=6

                                if hp <= 0:
                                    print('''The goblins manage to grab a hold of you and drag you into the nest. They attack you from all angles in a swarm, until you eventually succumb to your wounds. You are dead.''')
                                    print('''Goblins are viscious beasts, weak alone but very dangerous in numbers. You would be wise to remember that next time.''')
                                    sys.exit()
                                if hp > 0:
                                    print('''You barely manage to escape as the goblins claw at your feet trying to drag you into their nest. You kick them off and run far enough away that they don't feel threatened
    by you anymore and stop chasing, but you very nearly paid with your life. You did, however, manage to grab a small lockbox that was sitting in the pile.''')
                                    inventory.append('lockbox')

                                    if 'lockbox key' in inventory:
                                        print('''You take the key out of your pocket and place it in the lock, opening it up. Inside is a small but very well made golden ring. You take it.''')
                                        inventory.remove('lockbox key')
                                        inventory.remove('lockbox')
                                        inventory.append('gimlis ring')
                                        break
                                    if 'lockbox key' not in inventory:
                                        print('''You dont know what this is, but you hear something small rattling around inside.''')
                                        break
                            if goblinsave < 14:
                                hp-=12

                                if hp <= 0:
                                    print('''The goblins manage to grab a hold of you and drag you into the nest. They attack you from all angles in a swarm, until you eventually succumb to your wounds. You are dead.''')
                                    print('''Goblins are viscious beasts, weak alone but very dangerous in numbers. You would be wise to remember that next time.''')
                                    sys.exit()
                                if hp > 0:
                                    print('''You barely manage to escape as the goblins claw at your feet trying to drag you into their nest. You kick them off and run far enough away that they don't feel threatened
    by you anymore and stop chasing, but you very nearly paid with your life. You saw a small lockbox in the pile, but were unable to grab it in time.''')
                                    break
                        if sne == 'nevermind':
                            print('You turn back, thinking better of approaching the nest.')
                            break
                elif goblins==0:
                    print('''There's nothing there but fire and dead goblins now. Even if there was more loot, 
you blew it up, so you'll never know.''')

            elif act == 'use lockbox key' or act == 'use key':
                if 'gimlis ring' in inventory:
                    print('''You already have the ring.''')
                elif 'lockbox' in inventory and 'lockbox key' in inventory:
                    print('''You take the key you got from Khirn Square and place it in the lock. With a gentle click, the box opens, revealing a beautifully
crafted golden ring. You take it, dropping the key and lockbox on the ground since they are now useless.''')
                    print('''You've recieved GIMLIS RING''')
                    inventory.remove('lockbox')
                    inventory.remove('lockbox key')
                    inventory.append('gimlis ring')
                elif 'lockbox' not in inventory and 'lockbox key' in inventory:
                    print('''You haven't found the lockbox yet, but it should be around here somewhere.''')
                elif 'lockbox' not in inventory and 'lockbox key' not in inventory:
                    print('''I don't know what you mean by that. ''')
                elif 'lockbox' in inventory and 'lockbox key' not in inventory:
                    print('''You do not have the key to this lockbox.''')
            elif act == 'go to powder store' or act == 'investigate powder store' or act == 'go to powder shop':
                
                print('''The inside of this old powder store is coated in black powder and smells like sulfur een after so many years of disuse. In the back room, you see a stache of countless bombs.
They're large enough that you'll only be able to carry one at a time, but they seem like they could be useful.''')
                print('''Unlocked option: 'take bomb' from Market''')
            elif act == 'take bomb':
                if 'bomb' in inventory:
                    print('''You already have a bomb.''')
                elif 'bomb' not in inventory:
                    inventory.append('bomb')
                    print('''You take one of the cartoonishly large bombs. You never know when a good explosion would come in handy.''')


            elif act == 'blow up goblins' or act == 'bomb goblins' or act == 'blow up nest' or act == 'blow up goblin nest' or act == 'bomb goblin nest':
                if 'bomb' in inventory and 'lockbox' not in inventory and 'gimlis ring' not in inventory:
                    goblins=0
                    inventory.remove('bomb')
                    print('''You chuck the bomb at the goblin nest with the fuse lit. Shortly after, there is an immensely satisfying explosion of splintered wood 
and burning goblins. The goblin nest is no more, and a small lockbox, now lightly charred, falls at your feet. You take it.''')
                    inventory.append('lockbox')

                    if 'lockbox key' in inventory:
                        print('''You take the key out of your pocket and place it in the lock, opening it up. Inside is a small but very well made golden ring. You take it.''')
                        inventory.remove('lockbox key')
                        inventory.remove('lockbox')
                        inventory.append('gimlis ring')
                        
                    elif 'lockbox key' not in inventory:
                        print('''You dont know what this is, but you hear something small rattling around inside.''')
                elif 'bomb' not in inventory and goblins==1:
                    print('''You'll need a bomb for that.''')
                elif goblins==0:
                    print('''You already blew the goblins up.''')
                elif goblins==1 and 'lockbox' in inventory and 'bomb' in inventory:
                    goblins=0
                    inventory.remove('bomb')
                    print('''You chuck the bomb at the goblin nest with the fuse lit. Shortly after, there is an immensely 
satisfying explosion of splintered wood and burning goblins''')
                elif goblins==1 and 'gimlis ring' in inventory and 'bomb' in inventory:
                    goblins=0
                    inventory.remove('bomb')
                    print('''You chuck the bomb at the goblin nest with the fuse lit. Shortly after, there is an immensely 
satisfying explosion of splintered wood and burning goblins''')


            elif act == 'pick lockbox' or act == 'pick lock':
                if 'lockbox' in inventory:
                    print('Lockpick: ', boxpick)

                    if boxpick >= 12:
                        print('''You manage to break the box open, and inside is a small but very well crafted gold ring. You take it.''')
                        inventory.remove('lockbox')
                        inventory.append('gimlis ring')
                    if boxpick < 12:
                        print('''Try as you might, you cannot get the box open with your tools.''')
                if 'lockbox' not in inventory:
                    print('''What lock?''')
            elif act == 'investigate ring':
                if 'gimlis ring' in inventory:
                    print('Investigation: ', iring)

                    if iring > 12:
                        print('''You see an inscription on the inside that says 'for Gimli, Love Mother' ''')
                    else:
                        print('''It is a well made gold ring, but nothing more.''')
                elif 'gimlis ring' not in inventory:
                    print('''What ring?''')
            elif act == 'investigate skeleton' or act == 'skeleton' or act == 'go to skeleton':
                if talktodis>0 and 'gimlis sash' not in inventory:
                    print('''The skeleton is ancient and wearing a dusty RED SASH across it's shoudlers. The skeleton bears numerous scratch marks across the bone 
denoting sword, claw, or arrow strikes.''')
                    print('''You remember Dis' comments about her son and realize this is probably him. You take his sash to bring back to her.''')
                    print('Added to inventory: Gimlis Sash')
                    inventory.append('gimlis sash')
                elif talktodis==0 and 'gimlis sash' not in inventory:
                    print('''Just a dusty old skeleton with an ancient looking RED SASH across it's shoulders.''')
                elif 'gimlis sash' in inventory and talktodis>0:
                    print('''You already took the RED SASH from Gimli's body. I'm sure Dis would appreciate the closure of knowing.''')
                elif dismovedon==1:
                    print('''Dis is in a much better place now thanks to you.''')
            elif act == 'khirn square' or act == 'go to khirn square' or act == 'go back to khirn square':
                if streetclear==0:
                    print('''Down the road, you run into a familiar pile of rubble from the other side. You could climb it or try to move some out of the way.''')

                    while True:

                        do= input('Climb (A), Lift (B) or Leave (C)? ')

                        if do == 'A':
                            print('Acrobatics Check: ', climbrub)

                            if climbrub >= 13:
                                print('''You manage to scale the rubble and land on the other side in 
KHIRN SQUARE.''')
                                dnd.khirnsquare()
                            else:
                                print('''The rubble is too sheer on this side to find and purchase, you cannot climb it.''')
                                break
                        elif do == 'B':
                            print('Athletics Check: ', liftrub)

                            if liftrub >= 13:
                                print('''You manage to push enough rubble out of the way that you can dart through as it collapses back behind you. 
You make it through to KHIRN SQUARE.''')
                                dnd.khirnsquare()
                            else:
                                print('''The rocks are either too heavy or pinned against eachother so that you cannot move them.''')
                                break
                        elif do == 'C':
                            print('''Probably not worth it to try, don't want to get stuck.''')
                            break
                        else:
                            print('''I don't understand''')
                elif streetclear==1:
                    print('''You take the main road back to khirn square.''')
                    dnd.khirnsquare()
            elif act == 'blow up rubble' or act == 'use bomb on rubble':
                if 'bomb' in inventory:
                    inventory.remove('bomb')
                    if streetclear==0:
                        print('''You place the bomb then run behind cover. After a large BOOM, you wait for the shaking to stop. You look out and the way is clear.''')
                        streetclear=1
                    elif streetclear==1:
                        print('''The way is already clear.''')
                elif 'bomb' not in inventory:
                    print('''You'll need a bomb for that.''')
            elif act == 'take main road' or act == 'go to castle' or act == 'main road' or act == 'castle':
                print('''You walk down the main road towards the castle looming in the distance, built into the walls of the subterranean city. 
As it draws closer, you realize just how large and regal it is. You enter into the GRAND HALL of the castle through the main gate. 
The sheer scale of the building is staggering, and you can see three possible ways forward. A set of STAIRS leading to the second floor, 
to the RIGHT a door leading to what appears to be an AUDIENCE HALL.''')
                dnd.grandhall()
            elif act == 'take alley' or act == 'go to church' or act == 'go back to church' or act == 'go back to church courtyard':
                print('''You head to the side alley and take it back to the church courtyard.''')
                dnd.churchcourtyard()
            elif act == 'go back':
                print('''You'll have to be more specific.''')
            else:
                print('''I dont understand''')
            
    
        pass
    def grandhall(): #some history about palace to be found, pathways to kitchen, audience hall, and second floor

        #scrawl
        grandhallscrawl='''The grand hall is a large foyer in this castle, which serves as an entry way and opens out three different ways. The room seems like it was once decorated 
decadently, but the CHANDELIER that once hung has long since fallen to the floor and been robbed of it's jewels, it's metal skeleton sitting on the floor before you. There is 
hundreds of years of HISTORY buried in every detail of this room. There is a large STAIRCASE leading up to the second floor, and
another, more grandly constructed arched doorway leading to an AUDIENCE CHAMBER.'''
        print()
        
        #variables
        portinv=actions.intcheck()

        while True:

            act=input('What would you like to do? ')

            if act == 'repeat':
                print(grandhallscrawl)
            elif act == 'inventory':
                actions.inventory()
            elif act == 'status':
                actions.health()
            elif act == 'help':
                print('''For additional historical information and lore, you could ask about the HISTORY OF THE CASTLE or HISTORY OF THE ROOM, or you could try one of the other rooms. If
you wish to head back to the MARKET, you can always GO BACK.''')
            elif act == 'use healing potion':
                if 'Healing Potion' in inventory:
                    actions.healingpotion()
                elif 'Healing Potion' not in inventory:
                    print('You do not have any Healing Potions')
            elif act == 'go to market' or act == 'market' or act == 'go back':
                print('''You decide to head back down the main road and into the market square again.''')
                dnd.market()
            elif act == 'look around':
                print('''The CHANDELIER on the floor in front of you, although robbed of it's gems and missing any lighting fixtures, is extremely well made and constructed of solid bronze. Decorating the
walls are ancient PORTRAITS and PAINTINGS that the goblins seemingly decided were not of any value to them. The STAIRS leading up are wide and luxuirious.''')
            elif act == 'investigate portaits' or act == 'investigate paintings' or act == 'history of paintings' or act == 'history of portraits':
                print('History/Investigation: ', portinv)

                if portinv >= 13:
                    print('''The portaits on the wall are depictions of dwarvish nobles from ages past, the most recent of which likely being the royal family at the time the city fell. The portait that
catches your attention is the portait of Prince Valean, the youngest son of the King Mror. You recognize the name from an old manuscript you read, speaking of the collapse of the dwarvish states. A key figure
in this portion of history was noted as King Valean the Blind, who you surmise is the same person at a later point. In the manuscript, Valean is decribed as missing his left arm and both of his eyes due to a
failed attempt on his life, which he blamed on his brother Durin and sparked the first conflicts of the war, although it was never confirmed. The war in question is a series of conflicts called the Unification Wars, 
which determined an era of brother wars that shattered the dwarvish states and split the royal family along lines of succession. The issue of the succession drove tensions high and split the states as supporters of Durin
as the new king, Valean as the new king, or the rebels who sought to establish a new dynasty. The happy boy in this portrait had no idea of what would happen in the coming years.
On the botton of the frame is a plaque with the then prince's birthday, May 7th, 589. Almost 600 years ago.''')
                else:
                    print('''Just a dusty old portrait of some old noble named Valean. 
On the botton of the frame is a plaque with the then prince's birthday, May 7th, 589. Almost 600 years ago.''')
            elif act == 'look at chandelier' or act == 'chandelier' or act == 'investigate chandelier':
                print('''The chandelier was knocked or fell down a very long time ago judging by the amount of dust that has settled on it. You can tell it used to be beautful but has since been robbed of its 
precious gems and candles. Oh, what you would give to see this place in it's prime.''')
            elif act == 'go upstairs' or act == 'take stairs':
                print('''You head up the main stairs into a throne room, a grand open room where royal court was once held. Grand pillars stand leading up to the stairs of the raised, simply carved stone throne.
The only remnants of the beautiful stained glass windows that likely once stood behind the imposing throne is a few pieces of colored, dust covered glass on the floor and stuck to the window frame.
Standing at the foot of the staircase, looking up at the throne solemnly, is a man MISSING HIS LEFT ARM. He is turned away from you, and does not notice you yet.''')
                dnd.throneroom()
            elif act == 'go to audience hall' or act == 'audience hall' or act == 'right door' or act == 'take right door' or act == 'go right':
                print('''You head into the audience hall, where you find a large room that was likely used to recieve guests for balls and feasts. There is a 
FIREPLACE on one of the walls, and a large BOOKSHELF in the corner. ''')
                dnd.audiencehall()
            else:
                print('I dont understand')
                    
        pass

        while True:

            act=input('What would you like to do? ')

            if act == 'repeat':
                print('scrawl')
            elif act == 'inventory':
                actions.inventory()
            elif act == 'status':
                actions.health()
            elif act == 'help':
                print('hint')
            elif act == 'use healing potion':
                if 'Healing Potion' in inventory:
                    actions.healingpotion()
                elif 'Healing Potion' not in inventory:
                    print('You do not have any Healing Potions')
        pass
    def audiencehall(): #stairwell to dungeon, fireplace with stached gold, can hear sounds from dungeon

        audiencehallscrawl='''In the center of the derelict room is a very long, rotted out feasting TABLE, which likely would have hosted royal famlies from across the world on diplomatic
missions, served feasts at royal weddings, and fed some of the most important people in history. There is a FIREPLACE on the far wall that was once fantastically ornate. Wooden dragons carved into the
mantle exhibit the power of the once great empire. In the corner, there is a large BOOKSHELF populated with a miriad of colorful tomes from ages long past.'''
        print()
        
        ahalllook=actions.wischeck()
        fplacelook=actions.intcheck()
        bookshelflook=actions.intcheck()
        tablelook=actions.intcheck()
        global bookshelfdooropen

        if bookshelfdooropen==1:
            bookshelfdooropen=1
        else:
            bookshelfdooropen=0

        while True:

            act=input('What would you like to do? ')

            if act == 'repeat':
                print(audiencehallscrawl)
            elif act == 'inventory':
                actions.inventory()
            elif act == 'status':
                actions.health()
            elif act == 'help':
                print('''The FIREPLACE looks interesting. The BOOKSHELF in the corner could contain very interesting manuscripts as well.''')
            elif act == 'use healing potion':
                if 'Healing Potion' in inventory:
                    actions.healingpotion()
                elif 'Healing Potion' not in inventory:
                    print('You do not have any Healing Potions')
            elif act == 'look around':
                print('''The FIREPLACE is ornately carved wood, and the book shelf in the corner holds hundreds of ancient books. The table in the center
has been collapsed in this position for a long time, collecting dust.''')
            elif act == 'investigate fireplace' or act == 'fireplace':
                print('Investigation: ', fplacelook)

                if fplacelook >= 15:
                    print('''You look at the fireplace, the ornately carved dragons on the mantle roaring back at you. Looking into their mouths, you notice one is more hollow than the other.
reaching your hand in, you pull out a sizable sack of gold, containing 60 gold pieces. This was likely an emergency stache by the royal family, but they wont be needing it anymore so you take it.''')
                if fplacelook < 15:
                    print('''The fireplace is beautifully crafted, but otherwise doesn't seem very interesting.''')
            elif act == 'investigate bookshelf' or act == 'bookshelf':
                    print('Investigation: ', bookshelflook)

                    if bookshelflook >= 14:
                        print('''You look at the books on the shelf, all of various sizes, colors, topics and made of different materials. One book in particular sticks out to you,
a manuscript with the title 'Conquest: The life story of Khirn the Conqueror', claiming to be a biography compiled from not only people who knew Khirn personally, but exerpts from 
his personal journal taken during his conquest and after, during his rule as king. It is sticking out of the shelf more than the others. You notice a recent dust pattern on the floor
indicating the shelf swings open.''')
                    if bookshelflook < 14:
                        print('''You look at the books on the shelf, all of various sizes, colors, topics and made of different materials. One book in particular sticks out to you,
a manuscript with the title 'Conquest: The life story of Khirn the Conqueror', claiming to be a biography compiled from not only people who knew Khirn personally, but exerpts from 
his personal journal taken during his conquest and after, during his rule as king.''')
            elif act == 'pull book' or act == 'pull Conquest' or act == 'look at book' or act == 'investigate book' or act == 'look at Conquest' or act == 'pull conquest' or act == 'look at conquest' or act == 'read conquest' or act == 'read Conquest':
                print('''Your fingers find their way to Conquest, the book about Khirn the Conqueror and his exploits during his life, likely the oldest book on 
the shelf. Pulling on it, the bookshelf swings open on creaking hinges, although with less resistance than you might have thought. 
A spiralling staircase into darkness reveals itself, and you take it. The dungeon before you reveals itself as your eyes adjust, 
showing you numerous CELLS, a wooden DOOR to the LEFT, and a COLLAPSED CEILING at the end.''')
                bookshelfdooropen=1
                dnd.dungeon()
            elif act == 'take door' or act == 'take stairs' or act == 'take secret door' or act == 'take secret stairs':
                if bookshelfdooropen==0:
                    print('''I don't understand.''')
                if bookshelfdooropen==1:
                    print('''You take the staircase down into the darkness. The dungeon before you reveals itself as your eyes adjust, 
showing you numerous CELLS, and a COLLAPSED CEILING at the end. To the LEFT there is a nicer looking DOOR that likely leads to the 
GUARD CHAMBER.''')
                    dnd.dungeon()
            elif act == 'go back':
                print('''You head back into the GRAND HALL.''')
                dnd.grandhall()
            else:
                print('''I don't understand.''')

                
            
        pass
    def dungeon(): #many empty cells, collapsed ceiling has pinned archaeologists behind it, save them to win

        dungeonscrawl='''The dungeon is even more decrepit than the rest of the city, with most of what you can see being at least part way through collapse.
There is one undamaged CELL to the side, and massive COLLAPSE at the end of the tunnel that is splattered with blood. To the LEFT is the GUARD CHAMBER.'''
        global celllocked
        global foundarch
        print()

        dunglook=actions.wischeck()
        dungstr=actions.strcheck()
        icell=actions.intcheck()
        lockcell=actions.dexcheck()
        arccell=actions.intcheck()

        while True:

            act=input('What would you like to do? ')

            if act == 'repeat':
                print(dungeonscrawl)
            elif act == 'inventory':
                actions.inventory()
            elif act == 'status':
                actions.health()
            elif act == 'help':
                print('The one undamaged CELL could have something interesting in it, and the blood on the COLLAPSE indicates that this happened recently.')
            elif act == 'use healing potion':
                if 'Healing Potion' in inventory:
                    actions.healingpotion()
                elif 'Healing Potion' not in inventory:
                    print('You do not have any Healing Potions')
            elif act == 'go back':
                print('''You make your way back up into the audience chamber.''')
                dnd.audiencehall()
            elif act == 'look around':
                print('Perception: ', dunglook)

                if dunglook >= 12:
                    print('''The undamaged CELL has remarkably remained locked tight after all these years, but interestingly there is no body inside.
The blood on the COLLAPSE at the end of the dungeon is fairly fresh. Listening closely, you can here labored breathing from the COLLAPSE.''')
                else:
                    print('''You don't see much of note, but you notice the bloodstain on the COLLAPSE is fairly fresh.''')
            elif act == 'investigate cell' or act == 'look at cell':
                if celllocked==1:
                    print('Investigation: ', icell)

                    if icell >= 13:
                        print('''You notice through the bars that there are hundreds of tally marks scratched into the wall, likely with nails. More interestingly though,
    there is no skeleton in this cell, despite the door still being locked. Looking at the marks closer, you notice that they actually form a 
    runic pattern. You would have to get closer to analyze it.''')
                    else:
                        print('''There are tallies carved into the wall that indicate someone was there for a long time, but nothing else interesting.''')
                if celllocked==0:
                    print('Investigation: ', icell)

                    if icell >=11:
                        print('''You feel a strange breeze in the cell, despite it being windowless and underground. It seems to be coming from the
wall with the tallies. As you go to touch it your hand goes right through the wall, clearly an illusion of some kind.''')
                        print('''Option unlocked: walk through wall''')
                    else:
                        print('''You can't place the source, but there is a strange breeze in this room.''')
            elif act == 'pick cell lock' or act == 'pick lock':
                if celllocked==1:
                    print('Lockpick: ', lockcell)

                    if lockcell >= 13:
                        print('''You manage to open the cell door, forcing your way though the rusted old lock with a thud.''')
                        celllocked=0
                    else:
                        print('''Dwarvish craftsmanship once again proves to be the bane of thieves. The door does not budge.''')
                elif celllocked==0:
                    print('''You already unlocked the door.''')
            elif act == 'go into cell' or act == 'investigate tallies' or act == 'investigate in cell' or act == 'investigate inside cell' or act == 'investigate scratch marks' or act == 'open cell' or act == 'arcana on cell' or act == 'arcana on scrathes':
                if celllocked==1:
                    print('''The cell door is locked.''')
                if celllocked==0:
                    print('Arcana: ',arccell)

                    if arccell >= 13:
                        print('''The tallies are cleverly aligned so that they just look like tallies to the average person, but to a learned person like yourself,
you see clearly that these are cleverly constructed runes, creating a spell that allows you to walk through the wall as if it were air. You put your hand up to the wall
to confirm, and sure enough you phase right through as if nothing was there.''')
                        print('''Unlocked option: 'walk through wall' ''')
                    else:
                        print('''You were wrong, looks just like any old wall to you. You do feel a slight breeze in the cell though.''')
            elif act == 'walk through wall' or act == 'touch wall':
                print('''You walk directly through the illusory wall, into a small side room somewhere adjacently underneath the palace, with a small tunnel leading back outside the palace.''')
                dnd.hiddenroom()

            elif act == 'go to collapse' or act == 'look at collapse' or act == 'investigate collapse' or act == 'collapse':
                print('''Looking at the collapsed portion at the end of the hallway, you see the relatively fresh blood splatter on the rocks, and hear labored breathing. You look over
the pile of rubble and see a skinny man, covered in dust and clutching a broken arm, trapped behind the RUBBLE.''')
                print('He looks up at you with weak eyes that suddenly widen in excitement.')
                print(''' 'Oh gods, you found me! Please help, I've been trapped here for days!' ''')
                foundarch=1
            elif act == 'lift rubble' or act == 'lift collapse':
                print('Athletics Check: ', dungstr)

                if dungstr>=15:
                    print('''You manage to lift the rubble out of the way and pull the very weak archaeologist up onto your shoulders.
You escort him back to the entrance of the city, where he informs you that he left his partner in the sewer. You retrieve his partner and begin the long trek 
back to Tierengard to claim your reward.''')
                    print('''You win! Thank you for playing!''')
                    sys.exit()
                else:
                    print('''Try as you might, this is a very large portion of the ceiling that collapsed and you are incapable of moving it.''')
            elif act == 'blow up rubble' or act == 'use bomb on rubble':
                if 'bomb' in inventory:
                    print('''You place the bomb next to the rubble and inform the archaeologist your plan.''')
                    print(''' 'Haha, that's a funny jok- wait did I just hear a fuse light? YOU WERE SERIOUS!? GODS HAVE MERCY!' ''')
                    print('BOOOOM')
                    print('''Turns out, placing a questionably strong explosive device next to an already compromised structure causes it to collapse more.
The ceiling falls and crushes both of you as half of the palace wall slides over and crushes the dungeon.''')
                    print('''So very close to success that you forgot to think critically. Placing the bomb in the main hallway wasn't the right move, but somewhere else perhaps...''')

                    while True:
                        cont=input('''I'll be nice since you were so close to the end. Restart at the dungeon entrance, or just quit? A/B ''')
                        if cont == 'A':
                            print('Smart choice, keep trying.')
                            dnd.dungeon()
                        elif cont == 'B':
                            print('''A shame. Better luck next time''')
                            sys.exit()
                        else:
                            print('I dont understand.')
                if 'bomb' not in inventory:
                    print('''You'll have to visit the POWDER SHOP in the MARKET for a BOMB.''')
            elif act == 'unlock cell' or act == 'use cell key':
                if 'cell key' in inventory and celllocked==1:
                    celllocked=0
                    print('''You use the cell key to open the door.''')
                elif 'cell key' not in inventory and celllocked==1:
                    print('''You have no such key.''')
                elif celllocked==0:
                    print('''Why bother, you already got the door open?''')
            elif act == 'go left' or act == 'go to guard chamber':
                print('''You head in to the guard chamber, where you see a room that once served as the wardens office. There is an old
DESK in the center of the room with some chairs, as well as a rused weapon rack and some torch sconces.''')
                dnd.guardchamber()
    def guardchamber():
        print()

        guardscrawl='''The room has nothing except an old DESK in it.'''
        global codelockfound
        while True:

            act=input('What would you like to do? ')

            if act == 'repeat':
                print(guardscrawl)
            elif act == 'inventory':
                actions.inventory()
            elif act == 'status':
                actions.health()
            elif act == 'help':
                if codelockfound==0:
                    print('Nothing in this room strikes you as worth INVESTIGATING, except perhaps the OLD DESK.')
                if codelockfound==1:
                    print('''The code to that lock can likely be found somewhere else within the CASTLE. 
It could be any 5 digit number, no matter how inconspicuous it might seem, so keep searching.''')
            elif act == 'use healing potion':
                if 'Healing Potion' in inventory:
                    actions.healingpotion()
                elif 'Healing Potion' not in inventory:
                    print('You do not have any Healing Potions')
            elif act == 'look around':
                print('''The room is decrepit and barren. Whatever interesting was in here once was likely removed during whatever catastrophy ruined
the city or looted afterwards. The DESK looks to have some drawers that are still locked, however.''')
            elif act == 'investigate desk':
                codelockfound=1
                print('''The desk has a drawer on it's righthand side with both a code lock on it, which takes a 5 digit numerical passcode.
Whatever is in there was likely very important to the warden.''')
                print('''Option discovered: input code''')
            elif act == 'pick lock':
                print('''There is no key hole to pick the lock through, just the code input.''')
            elif act == 'input code':
                if codelockfound==1:
                    print('''You get close to the lock and start to input digits.''')
                    val=0
                    while val==0:
                        code=input('''What is the 5 digit code? (exit to leave) ''')

                        if code == 'exit':
                            print('''You realize you don't know the code and likely won't guess it, and get up.''')
                            val=1
                        elif code=='57589':
                            if 'cell key' not in inventory:
                                print('''The desk springs open as you correctly input the code, Prince Valean's birthday. Inside is a ring of keys,
each one likely going to a different cell, including the strangely locked one.''')
                                print('''You've recieved CELL KEY''')
                                inventory.append('cell key')
                                print('''The drawer slides closed and locks again as you remove the keys.''')
                                val=1
                            elif 'cell key' in inventory:
                                print('''You input the code again, opening the drawer to find that it is, shockingly, still empty.
I don't know what else you expected.''')
                                val=1
                        else:
                            print('''The desk does not open, must be the wrong code.''')
                elif codelockfound==0:
                    print('''What code? ''')
            elif act == 'leave' or act == 'go back':
                print('''You leave the room and head back into the dungeon.''')
                dnd.dungeon()
            else:
                print('''I dont understand''')
        pass
    def hiddenroom():
        print()
        global foundarch
        hiddenroomscrawl='''This room is unconnected to the dungeon, and was likely some sort of guard quarters or storage room beneath the palace.
You know the LEFT WALL is shared with the COLLAPSED SECTION, and there is a tunnel leading back outside the palace that the mage likely used to escape the prison ages ago.'''
        while True:

            act=input('What would you like to do? ')

            if act == 'repeat':
                print(hiddenroomscrawl)
            elif act == 'inventory':
                actions.inventory()
            elif act == 'status':
                actions.health()
            elif act == 'help':
                print('This room appears much more STRUCTURALLY STABLE, as it is undamaged compared to every other rooms youve seen.')
            elif act == 'use healing potion':
                if 'Healing Potion' in inventory:
                    actions.healingpotion()
                elif 'Healing Potion' not in inventory:
                    print('You do not have any Healing Potions')
            elif act == 'blow up left wall' or act == 'use bomb':
                if 'bomb' in inventory:
                    print('''You place the bomb next to the wall and duck behind the cover of a table in the corner. With a massive BOOM the whole building
seems to shake for a second before settling. On the other side of the newly created hole in the wall is a very scared looking archaeologist, who you've just freed.''')
                    print('''You escort him back to the entrance of the city, where he informs you that he left his partner in the sewer. You retrieve his partner and 
begin the long trek back to Tierengard to claim your reward.''')
                    print('''You win! Thank you for playing!''')
                    sys.exit()
                if 'bomb' not in inventory:
                    print('''You're going to need to go to the POWDER SHOP in the MARKET for one of those.''')
            elif act == 'take tunnel':
                if foundarch==0:
                    print('''The tunnel leads nowhere special, but you have a feeling the DUNGEON still holds something you need.''')
                if foundarch==1:
                    print('''The tunnel doesn't lead anywhere important, and besides your target is in the DUNGEON still trapped.''')
            else:
                print('I dont understand')
    def throneroom(): #ghost of Valean the Blind, demonic presence
        print()

        throneroomscrawl='''The throne room's air is heavy with the weight of long lost grandeur. The dust covered and broken hall boasts 6 massive columns leading upwards to the imposing stone
seat of the dead dwarvish city, a large empty space at the foot of the THRONE where people would gather at court to beseech the crown for favors. Standing in front of the throne is a partially 
transparent SPIRIT of a dwarf, missing his left arm at the elbow, staring solemnly at the throne. The only door that isn't blocked by collapsed rubble is the door you entered from.'''

        while True:

            act=input('What would you like to do? ')

            if act == 'repeat':
                print(throneroomscrawl)
            elif act == 'inventory':
                actions.inventory()
            elif act == 'status':
                actions.health()
            elif act == 'help':
                print('''This room contains only one point of interest, the figure looking solemnly at the throne. You could TALK to him.''')
            elif act == 'use healing potion':
                if 'Healing Potion' in inventory:
                    actions.healingpotion()
                elif 'Healing Potion' not in inventory:
                    print('You do not have any Healing Potions')
            elif act == 'go back':
                print('''You turn back and head down the stairs.''')
                dnd.grandhall()
            elif act == 'look around':
                print('''The room is large and barren, the dust covered walls and pillars hiding the decadence that it once had. The throne itself is a raised, square seat
carved of solid stone. It is simple but sturdy in it's construction, reflective of the strength of dwarvish society. Staring solemnly at the throne
is a spirit of a dwarvish man, missing his left arm and wearing very distinguished clothing.''')
            elif act == 'talk to spirit' or act == 'talk to ghost' or act == 'talk to valean' or act == 'talk':
                if valeanmovedon == 0 and 'ornate key' not in inventory:
                
                    print('''You approach the spirit, and he turns to face you. He bears a massive set of 3 scars across his face, including one slash directly across his eyes,
    which are no more than scarred over sockets. Although he lacks sight, he turns directly towards you. He smiles softly, and tilts his head in wordless acknowledgement of your presence 
    before turning back to the throne.''')
                    print('''Dialogue Options:
    -A: Who are you?
    -B: Why do you look sad?
    -C: Leave (Exit dialogue)''')
                    

                    while True:

                        conv=input('What would you like to say? ')

                        if conv == 'A':
                            print('''I was once a king, although not for long. I tried to lead my people away from the evil we were falling victim to, but I failed them.
    You can see what happened to us because of my failure. My name is Valean.''')
                        elif conv == 'B':
                            print('''This throne was to be my brothers a long time ago. Before he forced my hand into rebellion. My family and my people were torn apart.
    because of his arrogance. If only I could have gotten my CROWN. I believe he locked it away under the throne but I don't know where his key is. If you find it, bring it here.
    You'll know it when you see it, it was quite ORNATE.''')
                        elif conv == 'C':
                            print('You turn and leave the spirit to his thoughts.')
                            break
                        else:
                            print('I dont understand')
                elif valeanmovedon == 0 and 'ornate key' in inventory:
                    print('The spirit turns to you with wide eyes.')
                    print('You have his key, I can feel it on you. Please, give it to me so I can get my crown.')

                    while True: 
                        k=input('Give key? y/n ')

                        if k == 'y':
                            inventory.remove('ornate key')
                            print('''You hand him the key, as he smiles brightly. Valean drifts behind the throne with the key and opens a small compartment. He returns,
wearing the dwarvish crown on his head.''')
                            print('Valean begins to disappear, and fades away, but not before you hear a soft thank you echo through the chamber. The throne room is left empty.')
                            valeanmovedon=1
                            break
                        elif k == 'n':
                            print('''Oh, you pain me so. Please reconsider quickly.''')
                            break
                        else:
                            print('I dont understand')
                elif valeanmovedon == 1:
                    print('''Valean has already departed from this plane.''')
            else:
                print('I dont understand')
        pass

        

ob1=dnd()
dnd.intro()