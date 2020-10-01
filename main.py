from sys import argv

def parseNumbers(code):
    CODE = {}
    for i in code:
        line = int(i.split(" ")[0])
        CODE[line] = i[len(str(line))+1:]
    return code

# test if filename was given
if len(argv) < 2:
    print("[ERROR] no filename given")
    exit(1)

#retrieve file name and setup code/pointer
filename = argv[1]
code = []
pointer = 0

# parse the file into the code array
with open(filename, "r") as main:
    code = main.readlines() # get lines
    code = [i.strip() for i in code] # strip of the \n's

# parse the line numbers in the code
CODE = {}
for i in code:
    line = int(i.split(" ")[0])
    CODE[line] = i[len(str(line))+1:]

# main program loop
line = 1
memory = {}
pointer = 0
while True:
    if "print" in CODE[line]:
        print(CODE[line][6:])
    elif "goto " in CODE[line]:
        line = int(CODE[line][5:])-1
    elif "$store" in CODE[line]:
        memory[CODE[line][7:]] = pointer
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
        memory[int(CODE[line][6:])] = input("> ")
    elif "memPrint" in CODE[line]:
        print(memory[pointer])
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
        break
    line += 1