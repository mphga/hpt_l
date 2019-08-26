"""
this program tracks an rpg characters info during combat

    show player current data
        

    file name format = <handle>.pcdata
    ex. althea.pcdata
    
    data file format by line:
    
    line 1 is character name
    line 2 is max_hp
    line 3 is last current_hp
    
      ex.   
      Althea
      54
      45
"""
# does player have existing file?

# Yes
# id file
import yaml

def create_file_name(handle):
    
    return handle + '.yaml'


def player_stats():
    handle = input('what is your character\'s name: ')
    pc_data_file_name = create_file_name(handle)
    # Open file

    try:
        with open(pc_data_file_name, 'r') as pc:
        # read file
        # change to use YAML
            pstats = yaml.load(pc, Loader=yaml.FullLoader)

            handle = pstats['handle']
            max_hp = pstats['max_hp']
            current_hp = pstats['current_hp']

            print(handle)
           
            print('max_hp: {}'.format(max_hp))
            
            print('starting hp: {}'.format(current_hp))

    #No
    except:

        print('no file found, additional data needed')

        #Collect data 
        max_hp = input('enter maximum hit points: ')
        max_hp = int(max_hp)
        current_hp = input('enter current hit points: ')
        current_hp = int(current_hp)
        #print all data

        print(handle)
        print('max_hp: {}'.format(max_hp))
        print('starting hp: {}'.format(current_hp))  #change current to starting HP


    return {
            'handle': handle,
            'max_hp': max_hp,
            'current_hp': current_hp,
            'pc_file': pc_data_file_name,
            }

#run loop

#save this data when program ends
def combat(pstats):

    handle = pstats['handle']
    max_hp = pstats['max_hp']
    current_hp = pstats['current_hp']

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

            current_hp = max_hp
            print('\ncurrent HP: {}'.format(current_hp))

        # number indicates change go to calc    
        else:
        #calc & test HP change
            current_hp = current_hp + int(hp_change)

            if current_hp <= (max_hp) and current_hp >15:
                print('\ncurrent HP: {}'.format(current_hp) + '\n')

            elif current_hp > max_hp:
                print('\ncurrent HP: {}'.format(max_hp) + '\n')

            elif current_hp <=15:
                print('\ncurrentHP!: {}'.format(current_hp) + '\nDANGER LOW HP!' + '\n')

    pstats['current_hp'] = current_hp

def save_data(pstats):

    handle = pstats['handle']
    max_hp = pstats['max_hp']
    current_hp = pstats['current_hp']
    pc_file = pstats['pc_file']

    with open(pc_file, 'w') as pc:
        yaml.dump(pstats, pc)

       
        # pc.write(handle + '\n')
        # pc.write(str(max_hp) + '\n')
        # pc.write(str(current_hp))