# DALEK poetry generator, by The Doctor
import speech
import random
from microbit import sleep

# Randomly select fragments to interpolate into the template.
location = random.choice(["brent", "trent", "kent", "tashkent"])
action = random.choice(["wrapped up", "covered", "sang to", "played games with"])
obj = random.choice(["head", "hand", "dog", "foot"])
prop = random.choice(["in a tent", "with cement", "with some scent",
                     "that was bent"])
result = random.choice(["it ran off", "it glowed", "it blew up",
                       "it turned blue"])
attitude = random.choice(["in the park", "like a shark", "for a lark",
                         "with a bark"])
conclusion = random.choice(["where it went", "its intent", "why it went",
                           "what it meant"])

# A template of the poem. The {} are replaced by the named fragments.
poem = [
    "there was a young man from {}".format(location),
    "who {} his {} {}".format(action, obj, prop),
    "one night after dark",
    "{} {}".format(result, attitude),
    "and he never worked out {}".format(conclusion),
    "EXTERMINATE",
]

# Loop over each line in the poem and use the speech module to recite it.
for line in poem:
    speech.say(line, speed=120, pitch=100, throat=100, mouth=200)
    sleep(500)