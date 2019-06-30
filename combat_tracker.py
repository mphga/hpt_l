"""
this program tracks an rpg characters info during combat
"""

handle = input('what\'s character name: ') #example of using escape
print(handle) 
max_hp = input('enter maximum hit points: ')
print(max_hp)
current_hp = input('enter current hit points: ')
print(current_hp)
#ask for HP change
hp_change = input('enter hit point change: ')
#calc & test HP change
current_hp = int(current_hp) - int(hp_change)

if current_hp <= int(max_hp) and current_hp >15:
    print('current HP:' + str(current_hp))

elif current_hp > int(max_hp):
    print(max_hp)

elif current_hp <=15:
    print('Danger LOW HP!' + str(current_hp))


#print new current HP total


#ask for HP change
hp_change = input('enter hit points lost(-) or gained (+): ')
