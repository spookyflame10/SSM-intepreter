import re
#sasdkjfhsad
class SSMInterpreter:
    def __init__(self):
        self.stack = []         # Stack
        self.store = [0] * 1000 # Store memory with 1000 cells
        self.labels = {}        # Dictionary to store labels and their positions
        self.program_counter = 0 # Initialize program counter

    def tokenize(self, instructions):
        ret = []
        tokens = instructions.split()
        j = 0
        
        for i in range(len(tokens)):
            if tokens[i] in {'iadd', 'isub', 'imul', 'idiv', 'imod', 'pop', 'dup', 'swap', 'load', 'store'}:
                j += 1
                ret.append([tokens[i]])
            elif tokens[i] in {'jz', 'jnz', 'jmp'}:
                j += 1
                if i + 1 < len(tokens) and re.match(r'^[a-zA-Z][a-zA-Z_0-9]*', tokens[i + 1]):
                    ret.append([tokens[i], tokens[i + 1]])
                else:
                    print("syntax error: no label after jump")
            elif tokens[i] == 'ildc':
                j += 1
                if i + 1 < len(tokens) and re.match(r'^-?\d+$', tokens[i + 1]):
                    ret.append(['ildc', int(tokens[i + 1])])
                else:
                    print("syntax error: no number after ildc")
            elif re.match(r'[a-zA-Z][a-zA-Z_0-9]*:?', tokens[i]):
                tokens[i] = tokens[i][:-1]
                self.labels[tokens[i]] = j
            elif re.match(r'^-?\d+$', tokens[i]):
                continue
            else:
                print("Error. no matches")
        
        return ret

    def execute_instructions(self, instructions):
        # print(instructions)
        while self.program_counter < len(instructions):
            instr = instructions[self.program_counter]
            self.program_counter += 1
            self.execute(instr)
        
        if len(self.stack) > 0:
            print(f"Result: {self.stack[-1]}")
        else:
            print("Stack is empty")

    def execute(self, instr):
        opcode = instr[0]
        if opcode == 'ildc':
            num = instr[1]
            self.stack.append(num)
        elif opcode == 'iadd':
            if len(self.stack) < 2:
                raise Exception("Stack underflow")
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a + b)
        elif opcode == 'isub':
            if len(self.stack) < 2:
                raise Exception("Stack underflow")
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(b - a)
        elif opcode == 'imul':
            if len(self.stack) < 2:
                raise Exception("Stack underflow")
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a * b)
        elif opcode == 'idiv':
            if len(self.stack) < 2:
                raise Exception("Stack underflow")
            a = self.stack.pop()
            b = self.stack.pop()
            if a == 0:
                raise Exception("Division by zero")
            self.stack.append(b // a)
        elif opcode == 'imod':
            if len(self.stack) < 2:
                raise Exception("Stack underflow")
            a = self.stack.pop()
            b = self.stack.pop()
            if a == 0:
                raise Exception("Division by zero")
            self.stack.append(b % a)
        # Implement other instructions
        elif opcode == 'pop':
            if len(self.stack) > 0:
                self.stack.pop()
            else:
                raise Exception("Stack underflow")
        elif opcode == 'dup':
            if len(self.stack) > 0:
                self.stack.append(self.stack[-1])
            else:
                raise Exception("Stack underflow")
        elif opcode == 'swap':
            if len(self.stack) < 2:
                raise Exception("Stack underflow")
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a)
            self.stack.append(b)
        elif opcode == 'jz':
            label = instr[1]
            if len(self.stack) > 0 and self.stack.pop() == 0:
                if label in self.labels:
                    self.program_counter = self.labels[label]
                else:
                    raise Exception(f"Undefined label '{label}'")
        elif opcode == 'jnz':
            label = instr[1]
            if len(self.stack) > 0 and self.stack.pop() != 0:
                if label in self.labels:
                    self.program_counter = self.labels[label]
                else:
                    raise Exception(f"Undefined label '{label}'")
        elif opcode == 'jmp':
            label = instr[1]
            if label in self.labels:
                self.program_counter = self.labels[label]
            else:
                raise Exception(f"Undefined label '{label}'")

if __name__ == "__main__":
    filename = input("Enter the name of the SSM file: ")
    try:
        with open(filename, "r") as file:
            instructions = file.read()
            interpreter = SSMInterpreter()
            tokens = interpreter.tokenize(instructions)
            interpreter.execute_instructions(tokens)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
