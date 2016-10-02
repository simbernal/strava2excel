__author__ = 'SimonBernal'


import pandas as pd
from stravalib import Client
from pandas import ExcelWriter
import sys

# access info for strava user
with open('Client_ID', 'r') as f:
    client_id = f.read().strip()
with open('Access_Token', 'r') as f:
    access_token = f.read().strip()
with open('Client_Secret', 'r') as f:
    client_secret = f.read().strip()


# get info from activity for pandas columns
def get_activity_info(client, activity):
    '''
    :param client:
    :param activity:
    :return:
    '''

    vals = {}
    vals['ID'] = activity.id

    start = activity.start_date
    vals['Date'] = start.date()
    vals['Start Time'] = start.time()

    vals['City'] = activity.location_city
    vals['Country'] = activity.location_country

    vals['Type'] = activity.type
    vals['Name'] = activity.name

    vals['Elapsed Time'] = activity.elapsed_time
    vals['Moving Time'] = activity.moving_time

    vals['Distance'] = float(activity.distance)
    vals['Total Elevation Gain'] = float(activity.total_elevation_gain)
    #vals['Elevation High'] = activity.elev_high
    #vals['Elevation Low'] = activity.elev_low

    gear = activity.gear_id
    if gear != None:
        vals['Gear'] = client.get_gear(gear).name

    vals['Avg Speed'] = float(activity.average_speed)
    vals['Max Speed'] = float(activity.max_speed)

    vals['Achievement Count'] = activity.achievement_count

    '''
    for key, value in vals.items():
        print('------------------------------------------------')
        print('key: ' + str(key) + ' -- value: ' + str(value))
        print('type: ' + str(type(value)))
    '''


    return vals



## create pandas DataFrame
col_names = ['ID', 'Date', 'Start Time', 'City', 'Country',
             'Type', 'Name','Elapsed Time', 'Moving Time',
             'Distance', 'Total Elevation Gain', 'Gear',
             'Avg Speed', 'Max Speed', 'Achievement Count']


if __name__ == '__main__':

    ## connect to client and get activities
    client = Client(access_token=access_token)
    activities = client.get_activities(limit=1)

    ## create DataFrame with all activity data
    act = pd.DataFrame(columns=col_names)
    for a in activities:
        act = act.append(get_activity_info(client, a), ignore_index=True)

    print(act)

    print('\n\n\n\n\n\n\n')
    print('segements:')
    ## create DataFrame with all segement data
    for a in activities:
        a.


    '''
    ## output DataFrame to Excel
    act = act.set_index('ID')
    writer = ExcelWriter('strava_data.xlsx')
    act.to_excel(writer, 'Activities')
    writer.save()
    '''