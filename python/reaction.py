from microbit import *
import random

def waiting():
    return not(button_a.is_pressed())
    
def clear_button_a():
    button_a.was_pressed() # clear the button_a flag
    

def time():
    # returns the time until waiting is over, in 1/10 secs
    count = 0
    while waiting():
        sleep(100) # 100 ms = 1/10 secs
        count = count + 1
    return count
# loop until the user exits
# by pressing button b
# until then,
# wait a random time
# display a smile
# print out how long the user takes
# to press button a.
# if the user jumps the gun,
# tell them they are naughty
# and try again

while True:
    clear_button_a() # 
    display.show(Image.CLOCK1)
    if button_b.was_pressed():
        break
    sleep(random.randint(500, 4500)) # delay in ms
    if button_a.was_pressed():
        print('naughty')
        continue
    display.show(Image.HAPPY)
    print(time())
print('bye for now')
    