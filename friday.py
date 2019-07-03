# Andrzej Kocielski, 2018-02-01
# Is it Friday?

import datetime

if datetime.datetime.today().weekday() == 4:
    print("Yay! It is Friday.")
else:
    print("Unfortunately it is not Friday.")
