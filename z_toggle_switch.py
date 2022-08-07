import board
from digitalio import DigitalInOut, Direction, Pull

btn = DigitalInOut(board.D4)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

prev_state = btn.value

while True:
    cur_state = btn.value
    if cur_state != prev_state:
        if not cur_state:
            print("BTN is up")
        else:
            print("BTN is down")

    prev_state = cur_state
