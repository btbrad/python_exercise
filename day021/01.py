from datetime import datetime
from time import sleep
from random import randint

odds = [x for x in range(60) if x % 2 != 0]

for i in range(5):

    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")

    wait_time = randint(1, 60)

    sleep(wait_time)
