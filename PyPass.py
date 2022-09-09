import keyboard

while True:
    
    recorded = keyboard.record(until='`')

    keyboard.play(recorded, 3)

    break
