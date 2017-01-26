from microbit import *
import random

# see blog

def waiting():
    return not(button_a.is_pressed() or button_b.is_pressed())
    
def clear_buttons():
    button_a.was_pressed() # clear the button_a flag
    button_b.was_pressed() # clear the button_b flag
    
def time():
    # returns the time until waiting is over, in 1/10 secs
    count = 0
    while waiting():
        sleep(100) # 100 ms = 1/10 secs
        count = count + 1
    return count
    
while True:
    clear_buttons()
    display.show(Image.CLOCK1)
    if button_b.was_pressed():
        break
    sleep(random.randint(500, 4500)) # delay in ms
    if button_a.was_pressed():
        print('naughty!')
        continue
    if button_b.was_pressed():
        break
    display.show(Image.HAPPY)
    print(time())
print('bye for now')
while True:
    display.scroll('bye! ')