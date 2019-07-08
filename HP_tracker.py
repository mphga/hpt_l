"""
this program tracks an rpg characters info during combat
"""
# does player have existing file?

# Yes
# id file
handle = input('what is your character\'s name: ')
pc_data_file_name = handle + '.pcdata'
# Open file
try:
    with open(pc_data_file_name, 'r') as pc:
    # read file
        character = pc.readline()
        print(character)

        max_hp = pc.readline()
        print('max_hp: ' + max_hp)

        starting_hp = pc.readline()
        print('starting hp: ' + starting_hp)

    # show player current data
        

    # file name format = <handle>.pcdata
    # ex. althea.pcdata
    #
    # data file format by line:
    #
    # line 1 is character name
    # line 2 is max_hp
    # line 3 is last current_hp
    #
    #   ex.   
    #   Althea
    #   54
    #   45


#No
except:

    print('no file found, additional data needed')
#Collect data 

    max_hp = input('enter maximum hit points: ')
    current_hp = input('enter current hit points: ')
    #print all data

    print(handle)
    print(max_hp)
    print('starting HP: ' + (current_hp))  #change current to starting HP


#run loop

#save this data when program ends



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
        print('\ncurrent HP: ' + str(max_hp))

    # number indicates change go to calc    
    else:
    #calc & test HP change
        current_hp = int(current_hp) + int(hp_change)

        if current_hp <= int(max_hp) and current_hp >15:
            print('\ncurrent HP:' + str(current_hp) + '\n')

        elif current_hp > int(max_hp):
            print('\ncurrent HP: ' + str(max_hp) + '\n')

        elif current_hp <=15:
            print('\ncurrentHP!: ' + str(current_hp) + '\nDANGER LOW HP!' + '\n')

with open(pc_data_file_name, 'w') as pc:

    pc.write(character)

    pc.write(max_hp)

    pc.write(current_hp)
    