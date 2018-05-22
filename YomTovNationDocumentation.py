import google_sheets_api
from DB_connection_manager import sqlite3_database_manager
from db_connection_manager_postgres import yomtovnation_postgressql_db_manager

def employee_data_validation(employee_data):
    """
    this functions checks if there are at least three fields in the list that contains the data of the employees.
    if there are'nt at least three of them, it is adding them in order to avoid not enough arguments when sending the
    information on each employee to the database. if there are at least three fields the function then returns a list
    which contains the info of the employee
    :param employee_data:
    :return: List<str>
    """
    if len(employee_data) < 3:
        employee_data.append("-----")
        employee_data_validation(employee_data)
        return employee_data
    else:
        return employee_data


if __name__ == '__main__':
    connection_authorization_key = google_sheets_api.authorize_access()  # type: object
    # You must use a connection access key to make requests to Googlesheets
    cognigo_employees_lunch_requests = google_sheets_api.retrive_data_from_YomTovNation(connection_authorization_key)

    specific_employee_request_details = cognigo_employees_lunch_requests[0]  # type: object

for employee in cognigo_employees_lunch_requests:
    employee_data_validation(employee)
    employee_name, main_dish, add_on = employee[0], employee[1], employee[2]
    yomtovnation_postgressql_db_manager().insert_data_into_yomtovnationdb(employee_name, main_dish, add_on)
