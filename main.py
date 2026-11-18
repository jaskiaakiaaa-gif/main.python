import time
import sys

lyrics = [
    ("You know it's true", 0.12, 2.1),
    ("Yeah, I miss you", 0.12, 2.9),
    ("You know it's true", 0.12, 3.0),
    ("So, what if I call", 0.10, 1.6),
    ("And you pick up the phone?", 0.09, 2.5),
    ("And I use this holiday", 0.12, 1.5),
    ("To make my way to your ghost", 0.09, 2.9),
    ("Oh, what if you're lonely", 0.12, 2.6)
]

for text, delay, pause in lyrics:
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    time.sleep(pause)