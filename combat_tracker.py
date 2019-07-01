"""
this program tracks an rpg characters info during combat
"""

handle = input('what\'s character name: ') #example of using escape
print(handle) 
max_hp = input('enter maximum hit points: ')
print(max_hp)
current_hp = input('enter current hit points: ')
print(current_hp)

go = True
while go: 
    #end loop or ask for HP change --number of hp lost or gained 
    # option to indicate long rest to set current hp to max

    hp_change = input('enter hit points lost(-) or gained (+), l for long rest, e to end: ')
    #test for change, reset to max or end loop

    #e ends loop
    if hp_change == 'e': 
        go = False
    # l resets current_hp to max
    elif hp_change == 'l':
        print('current HP: ' + str(max_hp))

    # number indicates change go to calc    
    else:
    #calc & test HP change
        current_hp = int(current_hp) + int(hp_change)

        if current_hp <= int(max_hp) and current_hp >15:
            print('current HP:' + str(current_hp))

        elif current_hp > int(max_hp):
            print('current HP: ' + str(max_hp))

        elif current_hp <=15:
            print('Danger LOW HP!' + str(current_hp))





