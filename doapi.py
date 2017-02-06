#!/usr/bin/python

import random
import string
import skiff

TOKEN = '<YOUR-TOKEN>'
RAND_TEXT = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(7))
NAME = RAND_TEXT 
REGION = 'fra1'
size = '512mb'

s = skiff.rig(TOKEN)
droplets = s.Droplet.all()
myd = s.Droplet.get('<DROPLET-ID>')
print myd.snapshots()
