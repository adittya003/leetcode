import sys

class CustomStack:
    def __init__(self):
        self.stack = []
        self.command_stack = []

    def insert(self, value):
        self.stack.append(value)
        self.command_stack.append(('insert', value))

    def delete(self, value):
        if len(self.stack) >= value:
            deleted_chars = self.stack[-value:]
            for char in deleted_chars:
                self.stack.remove(char)
            self.command_stack.append(('delete', deleted_chars))
        else:
            print(f"Error: Not enough characters in the stack to delete {value} characters.")

    def get(self, value):
        try:
            char = self.stack[value]
            self.command_stack.append(('get', char))
            return char
        except IndexError:
            print(f"Error: Index {value} out of range.")
            return None

    def undo(self):
        if self.command_stack:
            last_command = self.command_stack.pop()
            if last_command[0] == 'insert':
                inserted_chars = last_command[1]
                self.stack = self.stack[:-len(inserted_chars)]
            elif last_command[0] == 'delete':
                deleted_chars = last_command[1]
                for char in deleted_chars:
                    self.stack.append(char)

def doSomething(inval):
    custom_stack = CustomStack()
    output = []

    commands = inval.split(',')
    for command in commands:
        cmd, *args = command.split()
        if cmd == '1':
            custom_stack.insert(args[0])
        elif cmd == '2':
            custom_stack.delete(int(args[0]))
        elif cmd == '3':
            char = custom_stack.get(int(args[0]))
            if char is not None:
                output.append(char)
        elif cmd == '4':
            custom_stack.undo()

    return output


# Test cases
input_1 = "1 abc,3 3,2 2,3 1"
output_1 = doSomething(input_1)
print(output_1)
                                                                                                                            