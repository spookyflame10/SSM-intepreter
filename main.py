import ply.lex as lex
import ply.yacc as yacc
import re

# List of token names. This is always required.
tokens = (
    'ILDC',
    'IADD',
    'ISUB',
    'IMUL',
    'IDIV',
    'IMOD',
    'POP',
    'DUP',
    'SWAP',
    'JZ',
    'JNZ',
    'JMP',
    'LOAD',
    'STORE',
    'LABEL',
    'NUMBER',
)


                    
            
# Regular expression rules for simple tokens
def t_LABEL(t):
    #*\b\s*-\s*\b(ildc|iadd|isub|imul|idiv|imod|pop|dup|swap|jz|jnz|jmp|load|store)\b
    r'[a-zA-Z][a-zA-Z_0-9]*:?'
    if t.value[-1] == ':':
        t.value = t.value[:-1]  # Remove the trailing colon
    return t
t_ILDC = r'ildc'
t_IADD = r'iadd'
t_ISUB = r'isub'
t_IMUL = r'imul'
t_IDIV = r'idiv'
t_IMOD = r'imod'
t_POP = r'pop'
t_DUP = r'dup'
t_SWAP = r'swap'
t_JZ = r'jz'
t_JNZ = r'jnz'
t_JMP = r'jmp'
t_LOAD = r'load'
t_STORE = r'store'
#t_LABEL = r'her:'
precedence = (
    ('left', '  '),
    ('left', 'IADD', 'ISUB'),
    ('left', 'IMUL', 'IDIV', 'IMOD'),
    ('left', 'ILDC', 'IDIV', 'IMOD'),
)


# A regular expression rule for NUMBER token (same as before)
def t_NUMBER(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers (same as before)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define a rule to ignore whitespace and comments (same as before)
def t_ignore_WHITESPACE(t):
    r'[ \n\t]+'

def t_ignore_COMMENT(t):
    r'\#.*'

# Error handling for illegal characters (same as before)
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Function to parse tokens and group them into instructions
def parse_tokens(tokens):
    instructions = []
    i = 0
    while i < len(tokens):
        #print(tokens[i])
        if tokens[i].type == 'ILDC':
            i += 1
            if i < len(tokens) and tokens[i].type == 'NUMBER':
                instructions.append(('ILDC', tokens[i].value))
            else:
                print("Parsing error")
        elif tokens[i].type in ['JZ', 'JNZ', 'JMP']:
            i += 1
            if i < len(tokens) and tokens[i].type == 'LABEL':
                instructions.append((tokens[i - 1].type, tokens[i].value))
            else:
                print("Parsing error")
        else:
            instructions.append((tokens[i].type, tokens[i].value))
        i += 1
    return instructions

class SSMInterpreter:
    def __init__(self):
        self.stack = []  # stack
        self.store = [0] * 1000  # Store memory with 1000 cells
        self.labels = {}  # Dictionary to store labels and their positions
        self.program_counter = 0  # Initialize program counter
    def tokenize(instructions):
        ret = []
        for line in instructions:
            tokens = line.split()
            for i, token in enumerate(tokens):
                if token in {'iadd','isub','imul','idiv','imod','pop','dup','swap','load','store'}:
                    ret.append([token])
                
                elif token in {'jz','jnz','jmp'}:
                    if i + 1 < len(tokens) and re.match(r'^[a-zA-Z][a-zA-Z_0-9]*', tokens[i + 1]):
                        ret.append(['token', tokens[i + 1]])
                    else:
                        print("syntax error: no label after jump")
                elif token == 'ildc':
                    if i + 1 < len(tokens) and re.match(r'^-?\d+$', tokens[i + 1]):
                        ret.append(['ildc', int(tokens[i + 1])])
                        i+=1
                    else:
                        print("syntax error: no number after ildc")
                elif re.match(r'[a-zA-Z][a-zA-Z_0-9]*:?', tokens[i]):
                    self.labels[tokens[i]] = i+1
                else:
                    print("Error. no matches")
        return ret
    def execute_instructions(self, instructions):
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
        #print(opcode, instr[1], self.program_counter)
        if opcode == 'LABEL':
            
            self.labels[instr[1]] = self.program_counter
        if opcode == 'ILDC':
            num = instr[1]
            self.stack.append(num)
        elif opcode == 'IADD':
            if len(self.stack) < 2:
                raise Exception("Stack underflow")
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a + b)
        elif opcode == 'ISUB':
            if len(self.stack) < 2:
                raise Exception("Stack underflow")
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(b - a)
        elif opcode == 'IMUL':
            if len(self.stack) < 2:
                raise Exception("Stack underflow")
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a * b)
        elif opcode == 'IDIV':
            if len(self.stack) < 2:
                raise Exception("Stack underflow")
            a = self.stack.pop()
            b = self.stack.pop()
            if a == 0:
                raise Exception("Division by zero")
            self.stack.append(b // a)
        elif opcode == 'IMOD':
            if len(self.stack) < 2:
                raise Exception("Stack underflow")
            a = self.stack.pop()
            b = self.stack.pop()
            if a == 0:
                raise Exception("Division by zero")
            self.stack.append(b % a)
# Implement other instructions
        elif opcode == 'POP':
            if len(self.stack) > 0:
                self.stack.pop()
            else:
                raise Exception("Stack underflow")
        elif opcode == 'DUP':
            if len(self.stack) > 0:
                self.stack.append(self.stack[-1])
            else:
                raise Exception("Stack underflow")
        elif opcode == 'SWAP':
            if len(self.stack) < 2:
                raise Exception("Stack underflow")
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a)
            self.stack.append(b)
        elif opcode == 'JZ':
            label = instr[1]
            if len(self.stack) > 0 and self.stack.pop() == 0:
                if label in self.labels:
                    self.program_counter = self.labels[label]
                else:
                    raise Exception(f"Undefined label '{label}'")
        elif opcode == 'JNZ':
            label = instr[1]
            if len(self.stack) > 0 and self.stack.pop() != 0:
                if label in self.labels:
                    self.program_counter = self.labels[label]
                else:
                    raise Exception(f"Undefined label '{label}'")
        elif opcode == 'JMP':
            label = instr[1]
            if label in self.labels:
                self.program_counter = self.labels[label]
            else:
                raise Exception(f"Undefined label '{label}'")
        #else:
            #raise Exception(f"Undefined opcode '{opcode}'")

if __name__ == "__main__":
    filename = input("Enter the name of the SSM file: ")

    try:
        with open(filename, "r") as file:
            instructions = file.read()

        # Tokenize the input instructions
        tokens = tokenize(instructions)
        lexer.input(instructions)
        tokens = list(lexer)
        for tok in tokens:
            print(tok)

        # Parse tokens into instructions
        instructions = parse_tokens(tokens)

        interpreter = SSMInterpreter()
        interpreter.execute_instructions(instructions)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")