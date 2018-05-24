import psycopg2


class yomtovnation_postgressql_db_manager:

    def __init__(self):
        connection_manager = psycopg2.connect(host='localhost', database='yomtovinvitations', user='postgres',
                                              password='mysecretpassword')
        self.connection_manager = connection_manager

    def insert_data_into_yomtovnation_db(self, employee_name, main_dish, add_on):
        self.connection_manager.cursor().execute("INSERT into InvitationRecord "
                                                 "values ('{}', '{}', '{}', CURRENT_DATE)".format(employee_name, main_dish, add_on))
        self.connection_manager.commit()
