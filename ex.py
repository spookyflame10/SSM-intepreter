class AssemblyInterpreter:

    def __init__(self):
        self.registers = {} #dictionary. key = name of variable. value = value of variable
        self.program_counter = 0 #current instruciton we are executing
        self.instructions = { #create dictionary: maps instruction name to functions
            'mov': self._move,
            'inc': self._increment,
            'dec': self._decrement,
            'jnz': self._jump_not_zero
        }

    def resolve(self, operand):
        return self.registers[operand] if operand in self.registers else int(operand)

    def execute(self, program):

        while self.program_counter < len(program):
            parsed = program[self.program_counter].split()
            current_instruction = parsed[0]
            args = parsed[1:]
            self.program_counter += 1
            self.instructions[current_instruction](*args) #invoke instruction

        return self.registers # returns registers

    def _move(self, x, y):
        self.registers[x] = self.resolve(y)

    def _increment(self, x):
        self.registers[x] += 1

    def _decrement(self, x):
        self.registers[x] -= 1

    def _jump_not_zero(self, x, y):
        if(self.resolve(x) != 0):
            self.program_counter += self.resolve(y) - 1

def simple_assembler(program): #string of operations we will execute
	return AssemblyInterpreter().execute(program)

# import ply.lex as lex
# import ply.yacc as yacc
# import re

# # List of tokens[i] names. This is always required.
# tokens = (
#     'ILDC',
#     'IADD',
#     'ISUB',
#     'IMUL',
#     'IDIV',
#     'IMOD',
#     'POP',
#     'DUP',
#     'SWAP',
#     'JZ',
#     'JNZ',
#     'JMP',
#     'LOAD',
#     'STORE',
#     'LABEL',
#     'NUMBER',
# )


                    
            
# # Regular expression rules for simple tokens
# def t_LABEL(t):
#     #*\b\s*-\s*\b(ildc|iadd|isub|imul|idiv|imod|pop|dup|swap|jz|jnz|jmp|load|store)\b
#     r'[a-zA-Z][a-zA-Z_0-9]*:?'
#     if t.value[-1] == ':':
#         t.value = t.value[:-1]  # Remove the trailing colon
#     return t
# t_ILDC = r'ildc'
# t_IADD = r'iadd'
# t_ISUB = r'isub'
# t_IMUL = r'imul'
# t_IDIV = r'idiv'
# t_IMOD = r'imod'
# t_POP = r'pop'
# t_DUP = r'dup'
# t_SWAP = r'swap'
# t_JZ = r'jz'
# t_JNZ = r'jnz'
# t_JMP = r'jmp'
# t_LOAD = r'load'
# t_STORE = r'store'
# #t_LABEL = r'her:'
# precedence = (
#     ('left', '  '),
#     ('left', 'IADD', 'ISUB'),
#     ('left', 'IMUL', 'IDIV', 'IMOD'),
#     ('left', 'ILDC', 'IDIV', 'IMOD'),
# )


# # A regular expression rule for NUMBER tokens[i] (same as before)
# def t_NUMBER(t):
#     r'-?\d+'
#     t.value = int(t.value)
#     return t

# # Define a rule so we can track line numbers (same as before)
# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += len(t.value)

# # Define a rule to ignore whitespace and comments (same as before)
# def t_ignore_WHITESPACE(t):
#     r'[ \n\t]+'

# def t_ignore_COMMENT(t):
#     r'\#.*'

# # Error handling for illegal characters (same as before)
# def t_error(t):
#     print("Illegal character '%s'" % t.value[0])
#     t.lexer.skip(1)

# # Build the lexer
# lexer = lex.lex()

# # Function to parse tokens and group them into instructions
# def parse_tokens(tokens):
#     instructions = []
#     i = 0
#     while i < len(tokens):
#         #print(tokens[i])
#         if tokens[i].type == 'ILDC':
#             i += 1
#             if i < len(tokens) and tokens[i].type == 'NUMBER':
#                 instructions.append(('ILDC', tokens[i].value))
#             else:
#                 print("Parsing error")
#         elif tokens[i].type in ['JZ', 'JNZ', 'JMP']:
#             i += 1
#             if i < len(tokens) and tokens[i].type == 'LABEL':
#                 instructions.append((tokens[i - 1].type, tokens[i].value))
#             else:
#                 print("Parsing error")
#         else:
#             instructions.append((tokens[i].type, tokens[i].value))
#         i += 1
#     return instructions