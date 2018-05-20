import google_sheets_api
from DB_connection_manager import sqlite3_database_manager

if __name__ == '__main__':
    connection_authorization_key = google_sheets_api.authorize_access()  # type: object
    # You must use a connection access key to make requests to Googlesheets
    cognigo_employees_lunch_requests = google_sheets_api.retrive_data_from_YomTovNation(
        connection_authorization_key)
    specific_employee_request_details = cognigo_employees_lunch_requests[0]
    employee_name, main_dish, add_on = specific_employee_request_details[0], \
                                       specific_employee_request_details[1], specific_employee_request_details[2]

sqlite3_database_manager().transaction_controller(employee_name, main_dish, add_on)
