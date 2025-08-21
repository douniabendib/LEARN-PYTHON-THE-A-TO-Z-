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

## Adapter Pattern


The Adapter Pattern allows objects with incompatible interfaces to work together. It acts as a bridge by wrapping an existing class with a new interface that clients expect.

Here are two systems with incompatible interfaces:
```python
class OldPrinter:
    def old_print(self, text):
        return f"OLD: {text}"

class NewPrinter:
    def print(self, text):
        return f"NEW: {text}"
```
The old printer uses old_print() while the new one uses print().

Create an adapter to make the old printer work with the new interface:
```python
class PrinterAdapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer
    
    def print(self, text):
        # Adapt old interface to new interface
        return self.old_printer.old_print(text)
```
The adapter wraps the old printer and provides the expected interface.

Use both printers with the same client code:
```python
def print_document(printer, text):
    return printer.print(text)  # Expects print() method

# Use new printer directly
new_printer = NewPrinter()
print(print_document(new_printer, "Hello"))

# Use old printer through adapter
old_printer = OldPrinter()
adapter = PrinterAdapter(old_printer)
print(print_document(adapter, "Hello"))
```
Create another example with media players:
```python
class Mp3Player:
    def play_mp3(self, filename):
        return f"Playing MP3: {filename}"

class Mp4Player:
    def play_mp4(self, filename):
        return f"Playing MP4: {filename}"

class MediaAdapter:
    def __init__(self, player, audio_type):
        self.player = player
        self.audio_type = audio_type
    
    def play(self, filename):
        if self.audio_type == "mp3":
            return self.player.play_mp3(filename)
        elif self.audio_type == "mp4":
            return self.player.play_mp4(filename)

class AudioPlayer:
    def play(self, audio_type, filename):
        if audio_type == "mp3":
            return Mp3Player().play_mp3(filename)
        else:
            adapter = MediaAdapter(Mp4Player(), audio_type)
            return adapter.play(filename)

player = AudioPlayer()
print(player.play("mp3", "song.mp3"))
print(player.play("mp4", "video.mp4"))
```
Output:
```python
NEW: Hello
OLD: Hello
Playing MP3: song.mp3
Playing MP4: video.mp4
```
Key Point: The Adapter Pattern makes incompatible interfaces work together by wrapping an existing class with a new interface. The adapter translates calls from the expected interface to the actual interface of the wrapped object. This is useful for integrating legacy code or third-party libraries without modifying existing code.
