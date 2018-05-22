from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import logging



def authorize_access():
    """
    Authorizes the access to google spreadsheets API, if the connection has been authorized the function returns
    the service as an HTTP object
    :return returns an google spreadsheet connection object
    """
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    return service


def retrive_data_from_YomTovNation(connection_access: object) -> object:
    """
    @:param the function gets a google spreadsheet connection object as a parameter
    :return Returns a tuple that contains the name of the employee, his main dish For the current day, and his side-dish
    """
    SPREADSHEET_ID = '146RH3SMLhNFF55_n_EXEIQ9UqlFcsBErnEYr9Bmpg7w'
    RANGE_NAME = 'Yom Tov Menu!B4:D18'
    result = connection_access.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                           range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        logging.error('No data found.')
    else:
        logging.info("found data!")
        return values
