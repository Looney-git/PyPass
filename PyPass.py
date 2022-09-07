import keyboard

while True:
    
    recorded = keyboard.record(until='esc')

    for key in recorded:

        if key.event_type == 'down':

            print(key.name)

    break