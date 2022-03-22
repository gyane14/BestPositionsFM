import json
from collections import Counter


def readMe(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        # removing unwanted line breaks
        if( lines[i] == '\n' ):
            lines[i] = ''

        # removing last 11 lines of the file
        if( len(lines) > 115 and len(lines) - i <= 12 ):
            lines[i] = ''

        # removing
        if( lines[i] == '| ------------------------------------------------------------------------------| \n' ):
            lines[i] = ''

    f.close()

    with open(filename, 'w') as fw1:
        fw1.writelines(lines)

    fw1.close()

    with open(filename, 'r') as f2:
        lines2 = f2.readlines()

    try:
        lines2.pop(0)
        lines2.pop(14)
        lines2.pop(28)
    except:
        pass

    try:
        string1 = ''
        for ele in lines2:
            string1 += ele

        stringtoList = string1.split('|')
        string_list = [x.strip() for x in stringtoList]
    
        dict={}
        for i in range(0,106,3):
            dict[string_list[i+1]]=string_list[i+2]

        f2.close()

        # important - writing file
        with open(filename, 'w') as fw2:
            fw2.writelines(json.dumps(dict))

        fw2.close()

    except:
        pass

    compareMe(filename)


def compareMe(filename):
    pfjson = json.load(open(filename))
    # print(pfjson['Crossing'])
    pfroles = json.load(open('roles/roles.json'))

    positions = ["Attacking Midfielder", "Advanced Playmaker", "Shadow Striker", "Trequartista", "Enganche"]
    modes = ['Attack', 'Support', 'Defend']

    selections = {}
    # Attacking Midfielder - Attack : <average_points>
    # Attacking Midfielder - Support : <average_points>

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
 
    # Finding 3 highest values
    best_selection = selection.most_common(3)

    for i in best_selection:
        print(i[0]," :",i[1]," ")


print("Please enter the name of the file: ")
filename = "players/"+ input() + ".rtf"
readMe(filename)