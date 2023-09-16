from stack import stack
class SSM_INTEPRETER:
    def __init__(self):
        self.registers = {} #dictionary. key = name of variable. value = value of variable
        self.stack = stack();
        self.label_map = {} # key is label, value is program counter
        self.program_counter = 0 #current instruction we are executing
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