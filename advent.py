f = open("adventday2.txt","r")
correct = 0
incorrect = 0
lines = f.readlines()
for x in range(0, len(lines)):
    count = 0
    newline1 = lines[x].split(' ')
    newline2 = newline1[0].split('-')
    firstnum = int(newline2[0])
    secnum = int(newline2[1])
    newline3 = newline1[1].split(':')
    alphabet = newline3[0]
    alplen = int(len(newline1[2]))
    for i in range(0, alplen-1):
        if alphabet == newline1[2][i]:
            count = count + 1
        else:
            continue
    if (count >= firstnum) and (count <= secnum):
        correct = correct + 1
    elif (count < firstnum) or (count > secnum):
        incorrect = incorrect + 1
print(len(lines))
print(correct)
print(incorrect)