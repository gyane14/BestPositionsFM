import json
import sys
from collections import Counter


def readMe(filename):
    with open(filename) as f:
        lines = f.readlines()
    try:
        string1 = ''
        for i in range(len(lines)):
            if(lines[i] == '| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| \n'):
                lines[i] = ''

            if(lines[i] == '| ------------------------------------------------------------------------------| \n'):
                lines[i] = ''

            if(lines[i] == '| -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| \n'):
                lines[i] = ''

            if(lines[i] == '| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| \n'):
                lines[i] = ''

            if(lines[i] == '\n'):
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
        for i in range(4, 144, 4):
            dict[string_list[i]] = string_list[i+2]

    except:
        for i in range(len(lines)):
            if(lines[i] == '\n'):
                lines[i] = ''

            if(len(lines) > 115 and len(lines) - i <= 12):
                lines[i] = ''

            if(lines[i] == '| ------------------------------------------------------------------------------| \n'):
                lines[i] = ''

        try:
            lines.pop(0)
            lines.pop(14)
            lines.pop(28)
        except:
            pass

        try:
            string1 = ''
            for ele in lines:
                string1 += ele

            stringtoList = string1.split('|')
            string_list = [x.strip() for x in stringtoList]

            dict = {}
            for i in range(0, 106, 3):
                dict[string_list[i+1]] = string_list[i+2]

        except:
            pass

    compareMe(dict)


def compareMe(dict):
    pfjson = dict
    pfroles = json.load(open('roles/atom.json'))

    positions = [position for position in pfroles]
    # modes = ['Attack', 'Support', 'Defend']
    if(len(selected_mode) > 1):
        modes = selected_mode
    else:
        mode = [selected_mode]

    selections = {}
    for position in positions:
        for mode in modes:
            tsum = 0
            for i in pfroles[position][mode]['vital']:
                selections[position, mode] = 0
                for j in pfjson:
                    if (i == j):
                        tsum += float(pfjson[i])

            for k in pfroles[position][mode]['prefer']:
                for l in pfjson:
                    if (k == l):
                        tsum += float(float(pfjson[k])*0.8)

            try:
                selections[position, mode] = float(format(
                    (tsum) / (len(pfroles[position][mode]['vital']) + len(pfroles[position][mode]['prefer'])), ".3f"))
            except:
                selections[position, mode] = 0

    selection = Counter(selections)
    best_selection = selection.most_common(10)

    for i in best_selection:
        print(i[0],"==>",i[1])
    
    exit()


print("=========================================")
print("||  Please enter the name of the file  ||")
print("=========================================")

filename = "players/" + input() + ".rtf"

print("Select the mode (A/S/D/*):")
mode_i = input()
global selected_mode
if (mode_i == "A" or mode_i == "a"):
    selected_mode='Attack'
elif (mode_i == "S" or mode_i == "s"):
    selected_mode='Support'
elif (mode_i == "D" or mode_i == "d"):
    selected_mode='Defend'
else:
    selected_mode=['Attack', 'Support', 'Defend']    

readMe(filename)

    # print("|              Menu Options:            |")
    # print("|        1. Select a Squad Player       |")
    # print("|    2. Select a Fully Scouted Player   |")
    # print("|      3. Alter Attribute Multipier     |")
    # print("|        4. Clear Players Folder        |")
    # print("=========================================")
    # print(" Format: name_of_file <space> menu_option")
    # print("=========================================")