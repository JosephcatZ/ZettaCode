j = ' '
code = []
pointer = 0

with open("Main.ZC") as main:
    for i in main:
        code.append(i.split("\n")[0])
Numbers = "0123456789"
CODE = {}
for i in code:
    j = 0
    line = 0
    length = 0
    while i[j] in Numbers:
        line = line*10 + int(i[j])
        length += 1
        j+=1
    
    CODE[line] = i[length+1:]
line = 1
OUT = False
out = []
global memory
memory = {}
pointer = 0
while not OUT:
    #print(line,CODE[line])
    if "print" in CODE[line]:
        print(CODE[line][6:])
        out.append(CODE[line][6:])
    elif "goto " in CODE[line]:
        line = int(CODE[line][5:])-1
    elif "store" in CODE[line]:
        memory[pointer] = CODE[line][6:]
    elif "gotoIf0" in CODE[line]:
        if int(memory[pointer]) == 0:
            line = int(CODE[line][7:])-1
    elif "+$" in CODE[line]:
        memory[pointer] = int(memory[pointer]) + int(memory[int(CODE[line][2:])])
    elif "-$" in CODE[line]:
        memory[pointer] = int(memory[pointer]) - int(memory[int(CODE[line][2:])])
    elif "*$" in CODE[line]:
        memory[pointer] = int(memory[pointer]) * int(memory[int(CODE[line][2:])])
    elif "/$" in CODE[line]:
        memory[pointer] = int(memory[pointer]) / int(memory[int(CODE[line][2:])])
    elif "%$" in CODE[line]:
        memory[pointer] = int(memory[pointer]) % int(memory[int(CODE[line][2:])])
    elif "$+" in CODE[line]:
        memory[int(CODE[line][2:])] = int(memory[pointer]) + int(memory[int(CODE[line][2:])])
    elif "$-" in CODE[line]:
        memory[int(CODE[line][2:])] = int(memory[int(CODE[line][2:])]) - int(memory[pointer])
    elif "$*" in CODE[line]:
        memory[int(CODE[line][2:])] = int(memory[pointer]) * int(memory[int(CODE[line][2:])])
    elif "$/" in CODE[line]:
        memory[int(CODE[line][2:])] = int(memory[int(CODE[line][2:])])/int(memory[pointer])
    elif "$%" in CODE[line]:
        memory[int(CODE[line][2:])] = int(memory[pointer]) % int(memory[int(CODE[line][2:])])
    elif "+" in CODE[line]:
        memory[pointer] = int(memory[pointer]) + int(CODE[line][1:])
    elif "-" in CODE[line]:
        memory[pointer] = int(memory[pointer]) - int(CODE[line][1:])
    elif "*" in CODE[line]:
        memory[pointer] = int(memory[pointer]) * int(CODE[line][1:])
    elif "/" in CODE[line]:
        memory[pointer] = int(memory[pointer]) / int(CODE[line][1:])
    elif "%" in CODE[line]:
        memory[pointer] = int(memory[pointer]) % int(CODE[line][1:])
    elif "strIn" in CODE[line]:
        IN = '                                                     '
        while IN == "                                                     ":
            IN = input("> ")
            memory[int(CODE[line][6:])] = IN
    elif "memPrint" in CODE[line]:
        print(memory[pointer])
        out.append(memory[pointer])
    elif "point" in CODE[line]:
        pointer = int(CODE[line][6:])
    elif "memPoint" in CODE[line]:
        pointer = memory[pointer]
    elif "concat~" in CODE[line]:
        memory[pointer] = str(memory[pointer]) + CODE[line][8:]
    elif "~concat" in CODE[line]:
        memory[pointer] = CODE[line][8:] + str(memory[pointer])
    elif "$concat~" in CODE[line]:
        memory[int(CODE[line][9:])] = str(memory[pointer]) + memory[int(CODE[line][9:])]
    elif "$~concat" in CODE[line]:
        memory[int(CODE[line][9:])] = memory[int(CODE[line][9:])] + str(memory[pointer])
    elif "concat~$" in CODE[line]:
        memory[pointer] = str(memory[pointer]) + memory[int(CODE[line][9:])]
    elif "~concat$" in CODE[line]:
        memory[pointer] = memory[int(CODE[line][9:])] + str(memory[pointer])
    elif CODE[line] == "EXIT":
        OUT = True
    #print(memory,pointer)
    #print(memory,pointer)
    #while input() != "":
    #    print("")
    line += 1