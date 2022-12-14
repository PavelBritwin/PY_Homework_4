# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
file1 = open("file_1.txt", "r")
pol1 = file1.readline()
file1.close()
file2 = open("file_2.txt", "r")
pol2 = file2.readline()
file2.close()
def returnPolInDict(pol):
    poldict = {0: 0, 1: 0}
    l = list(reversed(pol[:-3].replace(" ", "").split('+')))
    print(l)
    for i in range(len(l)):
        if l[i].isdigit():
            poldict[0] = int(l[i])
        elif '*x^' in l[i]:
            poldict[int(l[i].split('*x^', 1)[1])] = int(l[i].split('*x^', 1)[0])
        else:
            poldict[1] = int(l[i].split('*x', 1)[0])
    return poldict
d1, d2 = returnPolInDict(pol1), returnPolInDict(pol2)
print(f'First dict: {d1}')
print(f'Second dict: {d2}')
d = {}
for item in range(max(max(d1.keys()), max(d2.keys())) + 1):
    if item in d1 and item in d2:
        d[item] = d1[item] + d2[item]
    elif item in d1:
        d[item] = d1[item]
    elif item in d2:
        d[item] = d2[item]
    else:
        d[item] = 0
print(f'Result dict: {d}')
def writePolInFile(pol):
    resultpol = ' = 0'
    for item in (list(pol.keys())):
        if item == 0 and pol[item] != 0:
            resultpol = str(pol[item]) + resultpol
        elif item == 0 and pol[item] == 0:
            continue
        elif item == 1 and pol[item] != 0:
            resultpol = str(pol[item]) + '*x' + ' + ' + resultpol
        elif item == 0:
            continue
        elif item > 1 and pol[item] != 0:
            resultpol = str(pol[item]) + '*x^' + str(item) + ' + ' + resultpol
        else:
            continue
    return resultpol
file3 = open("file_3.txt", "w")
file3.writelines(writePolInFile(d))
file3.close()
print(writePolInFile(d))