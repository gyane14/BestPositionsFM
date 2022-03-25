import json
from collections import Counter

def readMe(filename):
    with open(filename) as f:
        lines = f.readlines()
    string1 = ''
    for i in range(len(lines)):
        if( lines[i] == '| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| \n' ):
            lines[i] = ''

        if( lines[i] == '| ------------------------------------------------------------------------------| \n' ):
            lines[i] = ''

        if( lines[i] == '| -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| \n' ):
            lines[i] = ''

        if( lines[i] == '| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| \n' ):
            lines[i] = ''

        if( lines[i] == '\n' ):
            lines[i] = ''

    for i in lines:
        string1 += i

    stringtoList = string1.split('|')
    string_list = [x.strip() for x in stringtoList]

    # Technical
    for i in range(5):
        string_list.pop(0)
    
    # Mental
    for i in range(4):
        string_list.pop(55)
    
    # Physical
    for i in range(4):
        string_list.pop(111)

    # Extras
    for i in range(9):
        string_list.pop(144)

    dict = {}
    for i in range(4,144,4):
        dict[string_list[i]] = string_list[i+2]

    compareMe(dict)

def compareMe(dict):
    pfjson = dict
    pfroles = json.load(open('roles/roles.json'))

    positions = [position for position in pfroles]
    modes = ['Attack', 'Support', 'Defend']

    selections = {}
    for position in positions:
        for mode in modes:
            tsum = 0
            for i in pfroles[position][mode]['vital']:
                selections[position,mode] = 0
                for j in pfjson:
                    if ( i == j ):
                        tsum += float(pfjson[i])

            for k in pfroles[position][mode]['prefer']:
                for l in pfjson:
                    if ( k == l ):
                        tsum += float(float(pfjson[k])*0.75)

            try: 
                selections[position,mode] = float(format((tsum) / (len(pfroles[position][mode]['vital']) + len(pfroles[position][mode]['prefer'])),".3f"))
            except:
                selections[position,mode] = 0

    selection = Counter(selections)
    best_selection = selection.most_common(3)

    for i in best_selection:
        print(i[0]," :",i[1]," ")

print("=========================================")
print("||  Please enter the name of the file  ||")
print("=========================================")
# print("|              Menu Options:            |")
# print("|        1. Select a Squad Player       |")
# print("|    2. Select a Fully Scouted Player   |")
# print("|      3. Alter Attribute Multipier     |")
# print("|        4. Clear Players Folder        |")
# print("=========================================")
# print(" Format: name_of_file <space> menu_option")
# print("=========================================")

filename = "players/" + input() + ".rtf"
readMe(filename)