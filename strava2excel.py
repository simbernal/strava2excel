__author__ = 'SimonBernal'


import pandas as pd
from pandas import ExcelWriter
from stravalib import Client
import datetime
import os



_col_names = ['ID', 'Date', 'Start Time', 'City', 'Country',
             'Type', 'Name','Elapsed Time', 'Moving Time',
             'Distance', 'Total Elevation Gain', 'Gear',
             'Avg Speed', 'Max Speed', 'Achievement Count']



def export(access_token=None, values=[], ignore=[], filename='strava2excel_export.xlsx', limit=None):

    # check that access token is valid
    if access_token == None:
        with open('Access_Token', 'r') as f:
            access_token = f.read().strip()
    elif type(access_token) == str:
        if os.path.isfile(access_token):
            with open(access_token, 'r') as f:
                access_token = f.read().strip()
    else:
        raise TypeError('argument <access_token> must be a string or None')

    # try and load client with access token
    try:
        client = Client(access_token=access_token)
    except:
        raise ValueError('access_token is not valid')

    # check that values are valid®
    if values == []:
        values = _col_names
    if type(values) != list:
        raise TypeError('argument <values> must be a list')
    for val in values:
        if val not in _col_names:
            raise ValueError(str(val) + ' is not an option, valid options are:\n' + str(col_names))

    # check that ignore is valid
    if type(ignore) != list:
        raise TypeError('argument <ignore> must be a list')
    for val in ignore:
        if val not in _col_names:
            raise ValueError(str(val) + ' is not a valid option, valid options to ignore are:\n' + str(values))

    # remove values in ignore form values
    to_del = []
    for i, val in enumerate(values):
        if val in ignore:
            to_del.append(i)
    for i in to_del[::-1]:
        del values[i]

    # check that limit is valid
    if limit != None and type(limit) != int:
        raise TypeError('argument <limit> must be an int or None')

    # check that filename is valid
    if type(filename) != str:
        raise TypeError('argument <filename> must be a string')


    ### inputs are valid -- now get all the information ###

    ## get user activities
    activities = client.get_activities(limit=limit)

    # create DataFrame to store activity data
    df = pd.DataFrame(columns=values)
    for a in activities:
        df = df.append(_get_activity_info(client, a, values), ignore_index=True)

    ## output DataFrame to Excel spreadsheet
    df = df.set_index('ID')
    writer = ExcelWriter(filename)
    df.to_excel(writer, 'Activities')
    writer.save()


# get info from activity for pandas columns
def _get_activity_info(client, activity, cols):


    vals = {}

    if 'ID' in cols:
        vals['ID'] = activity.id

    start = activity.start_date
    if 'Date' in cols:
        vals['Date'] = start.date()
    if 'Start Time' in cols:
        vals['Start Time'] = start.time()

    if 'City' in cols:
        vals['City'] = activity.location_city
    if 'Country' in cols:
        vals['Country'] = activity.location_country

    if 'Type' in cols:
        vals['Type'] = activity.type
    if 'Name' in cols:
        vals['Name'] = activity.name

    if 'Elapsed Time' in cols:
        vals['Elapsed Time'] = str(activity.elapsed_time)
    if 'Moving Time' in cols:
        vals['Moving Time'] = str(activity.moving_time)

    if 'Distance' in cols:
        vals['Distance'] = float(activity.distance)
    if 'Total Elevation Gain'  in cols:
        vals['Total Elevation Gain'] = float(activity.total_elevation_gain)
    #vals['Elevation High'] = activity.elev_high
    #vals['Elevation Low'] = activity.elev_low
    
    if 'Gear' in cols:
        gear = activity.gear_id
        if gear != None:
            vals['Gear'] = client.get_gear(gear).name

    if 'Avg Speed' in cols:
        vals['Avg Speed'] = float(activity.average_speed)
    if 'Max Speed' in cols:
        vals['Max Speed'] = float(activity.max_speed)

    if 'Achievement Count' in cols:
        vals['Achievement Count'] = activity.achievement_count

    return vals


if __name__ == '__main__':

    export(filename='output_08102016.xls')
