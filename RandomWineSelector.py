# IMPORT MODULES
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import pandas as pd

# Google Sheets API Client ID
# 200447405488-aaa1fohr47ctptuf1p6p9oj37uajinm9.apps.googleusercontent.com

# Google Sheets API Client Secret
# QErfeRrivnA53DAQ3I47BNMm

# Define spreadsheet name and ID
BeerWineList = 'Beer & Wine Inventory'
Wine = 'Wine'

# Call Google API
def get_google_sheet(BeerWineList, Wine):
    """ Retrieve sheet data using OAuth credentials and Google Python API. """
    scopes = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    # Setup the Sheets API
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', scopes)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))
# Call the Sheets API
    gsheet = service.spreadsheets().values().get(spreadsheetId=BeerWineList, range=Wine)
    return gsheet

def gsheet2df(gsheet):
    """ Converts Google sheet data to a Pandas DataFrame.
    Note: This script assumes that your data contains a header file on the first row!
    Also note that the Google API returns 'none' from empty cells - in order for the code
    below to work, you'll need to make sure your sheet doesn't contain empty cells,
    or update the code to account for such instances.
    """
    header = gsheet.get('values', [])[0]   # Assumes first line is header!
    values = gsheet.get('values', [])[1:]  # Everything else is data.
    if not values:
        print('No data found.')
    else:
        all_data = []
        for col_id, col_name in enumerate(header):
            column_data = []
            for row in values:
                column_data.append(row[col_id])
            ds = pd.Series(data=column_data, name=col_name)
            all_data.append(ds)
        df = pd.concat(all_data, axis=1)
        return df


gsheet = get_google_sheet(BeerWineList, Wine)
df = gsheet2df(gsheet)
print('Dataframe size = ', df.shape)
print(df.head())
