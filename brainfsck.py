from sys import argv

def interpret(srcCode: str):
    memory = [0] * 30000
    mem_index = 0

    instruction = [char for char in srcCode]
    instruction_pointer = 0

    loopPosition = []

    while instruction_pointer < len(instruction):
        match (instruction[instruction_pointer]):
            #value change token
            case '+':
                memory[mem_index] += 1
                if memory[mem_index] > 255:
                    memory[mem_index] = 0
            case '-':
                memory[mem_index] -= 1
                if memory[mem_index] < 0:
                    memory[mem_index] = 255

            #pointer position token
            case '>':
                mem_index += 1
            case '<':
                mem_index -= 1

            #loop token
            case '[':
                loopPosition.append(instruction_pointer)
            case ']':
                if memory[mem_index] != 0:
                    instruction_pointer = loopPosition[len(loopPosition) - 1]                 
                else:
                    instruction_pointer += 1
                    loopPosition.pop(len(loopPosition) - 1)

            #in/out token
            case '.':
                print(chr(memory[mem_index]), end='')
            case ',':
                memory[mem_index] = ord(input())
        
        instruction_pointer += 1

def main(file: str):
    with open(file, 'r') as srcFile:
        src = srcFile.read()
        interpret(src)

if __name__ == "__main__":
    if len(argv) < 2:
        print("py brainfsck.py <path to .bf file>")
    else:
        main(argv[1])