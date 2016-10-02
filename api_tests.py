__author__ = 'SimonBernal'


import stravalib
from stravalib import Client
import time
import inspect

with open('Client_ID', 'r') as f:
    client_id = f.read().strip()
with open('Access_Token', 'r') as f:
    access_token = f.read().strip()
with open('Client_Secret', 'r') as f:
    client_secret = f.read().strip()

'''
print(access_token)
print(client_id)
print(client_secret)
'''

client = Client(access_token=access_token)
athlete = client.get_athlete()

time.sleep(1)

print('first name: ' + athlete.firstname)
print('last name: ' + athlete.lastname)
print('email: ' + athlete.email)

act = client.get_activities(limit=1)
for a in act:
    print(type(a))
    print('name: ' + str(a.name))
    print('dist: ' + str(a.distance))
    print('gear: ' + str(a.gear_id))
    print('id: ' + str(a.id))
    g = client.get_gear(a.gear_id)
    print(g.name)
#print(athlete)


attr = inspect.getmembers(stravalib.model.Activity, lambda a: not(inspect.isroutine(a)))
vals =  [a for a in attr if not(a[0].startswith('__') and a[0].endswith('__'))]
for v in vals:
    print(v)
### approach
# crear pandas con el gear
# crear el pandas con todas las actividades
