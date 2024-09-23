# Initialize the stack with 256 cells, each initialized to 0
stack = [0] * 256
pointer = 0  # stack pointer
output = []  # to store the characters that will be printed

# Input the Emoji Stack program (Replace with your actual program)
program = """
👉👉👉👉👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉🔁08👍🔁34👈👈👈👈👈👈👈👈👈👈👍🔁48👉🔁15👍🔁5e👈🔁07👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉🔁02👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👍🔁42👉🔁02👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉🔁17👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👈🔁14👍🔁20👉🔁06👍🔁51👉🔁0c👍🔁34👉👉👍🔁46👈🔁14👍🔁4d👈🔁01👍🔁51👉🔁04👍🔁20👉🔁03👍🔁2f👉👉👉👉👉👉👉👉👍🔁4d👈🔁17👍🔁42👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👍🔁7c👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉🔁0c👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👈👈👈👈👈👈👈👈👈👈👈👈👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉🔁0c👍🔁32👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉🔁04👍🔁5e👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👍🔁47👈🔁0f👍🔁46👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👈🔁03👍🔁20👈🔁08👍🔁5e👉🔁10👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👈🔁1d👍🔁40👉🔁10👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉👉👉👉👍🔁5e👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬
"""

# Function to execute the instructions
def execute_instruction(instr):
    global pointer, stack, output

    if instr == '👉':
        pointer = (pointer + 1) % 256
    elif instr == '👈':
        pointer = (pointer - 1) % 256
    elif instr == '👍':
        stack[pointer] = (stack[pointer] + 1) % 256
    elif instr == '👎':
        stack[pointer] = (stack[pointer] - 1) % 256
    elif instr == '💬':
        output.append(chr(stack[pointer]))

# Parsing and executing the program
i = 0
while i < len(program):
    instr = program[i]
    if instr == '🔁':
        # Repeat the previous instruction
        repeat_count = int(program[i+1:i+3], 16)  # Parse the hex number
        for _ in range(repeat_count):
            execute_instruction(program[i-1])
        i += 2  # Skip over the repeat count
    else:
        execute_instruction(instr)
    i += 1

# Join the output to form the flag
flag = ''.join(output)
print("Flag:", flag)
