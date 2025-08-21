# Design Patterns Part 2

## Command Pattern


The Command Pattern encapsulates a request as an object, allowing you to queue operations, log requests, and support undo functionality. It separates the object that calls the operation from the one that performs it.

Here are simple command classes:
```python
class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_off()
```
Each command encapsulates a specific operation on a receiver object.

Create the receiver that performs the actual work:
```python
class Light:
    def turn_on(self):
        print("Light is on")
    
    def turn_off(self):
        print("Light is off")
```
Create an invoker that executes commands:
```python
class RemoteControl:
    def __init__(self):
        self.command = None
    
    def set_command(self, command):
        self.command = command
    
    def press_button(self):
        self.command.execute()
```
Use the command pattern:
```python
# Create receiver
light = Light()

# Create commands
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

# Create invoker
remote = RemoteControl()

# Execute different commands
remote.set_command(light_on)
remote.press_button()

remote.set_command(light_off)
remote.press_button()
```
Add support for undo operations:
```python
class UndoableCommand(Command):
    def undo(self):
        pass

class LightOnCommand(UndoableCommand):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_on()
    
    def undo(self):
        self.light.turn_off()

class SmartRemote:
    def __init__(self):
        self.last_command = None
    
    def execute_command(self, command):
        command.execute()
        self.last_command = command
    
    def undo(self):
        if self.last_command:
            self.last_command.undo()

smart_remote = SmartRemote()
smart_remote.execute_command(LightOnCommand(light))
smart_remote.undo()  # Turns light off
```
Output:
```python
Light is on
Light is off
Light is on
Light is off
```
Key Point: The Command Pattern turns requests into objects that can be stored, passed around, and executed later. The invoker doesn't need to know how to perform the operation - it just calls execute() on the command object. This enables features like undo/redo, queuing operations, and logging commands.
