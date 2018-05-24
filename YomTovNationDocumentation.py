import google_sheets_api
from db_connection_manager_postgres import yomtovnation_postgressql_db_manager
from time import strftime, gmtime, localtime
import logging


def employee_data_validation(employee_data):
    """
    this functions checks if there are at least three fields in the list that contains the data of the employees.
    if there are'nt at least three of them, it is adding them in order to avoid not enough arguments when sending the
    information on each employee to the database. if there are at least three fields the function then returns a list
    which contains the info of the employee
    :param employee_data:
    :return: List<str>
    """
    try:
        if len(employee_data) < 3:
            employee_data.append("-----")
            employee_data_validation(employee_data)

    finally:
        return employee_data


def is_it_not_a_weekend_day(weekday):
    if weekday == '5' or weekday == '6':  # in the strftmie format, the days count is zero based
        return False
    else:
        return True


def did_a_day_pass(last_time_where_data_got_collected, current_local_time):
    result = False
    if current_local_time == last_time_where_data_got_collected:
        result = True
    return result


if __name__ == '__main__':
    time_when_invitation_information_was_collected = strftime("%H: %M: %S", localtime())
    weekday_as_decimal_number = strftime("%w", localtime())
    try:
        while True:
            current_time = strftime("%H: %M: %S", localtime())
            try:
                if did_a_day_pass(current_time, time_when_invitation_information_was_collected) and \
                        is_it_not_a_weekend_day(weekday_as_decimal_number):
                    connection_authorization_key = google_sheets_api.authorize_access()  # type: object
                    # You must use a connection access key to make requests to Googlesheets
                    cognigo_employees_lunch_requests = google_sheets_api.retrive_data_from_YomTovNation(
                        connection_authorization_key)

                    specific_employee_request_details = cognigo_employees_lunch_requests[0]  # type: object

                    for employee in cognigo_employees_lunch_requests:
                        employee_data_validation(employee)
                        employee_name, main_dish, add_on = employee[0], employee[1], employee[2]
                        yomtovnation_postgressql_db_manager().insert_data_into_yomtovnation_db(employee_name, main_dish,
                                                                                               add_on)
            except:
                raise
    except:
        logging.exception("Some error occurred")
        raise
