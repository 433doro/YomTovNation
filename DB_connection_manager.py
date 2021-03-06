import sqlite3
import logging


class sqlite3_database_manager:

    def __init__(self):
        try:

            self.db_connection_setup = sqlite3.connect('YomTovInvitationRecord.db')
            self.db_transaction_controller = self.db_connection_setup.cursor()
            logging.info("Successfuly connected to the postgresDB")

        except:
            logging.exception("Couldn't connect to the postgresDB")

    def transaction_controller(self, employee_name, main_dish, add_on):
        """
        The function creates the SQL queries to the SQLiteDB. sends the information about what each employee ate,
        on the current date date.
        :param employee_name: The name of cognigos employee stands for the table name. Each employee got a separated
        table in order to list easily and efficiently his orders
        :param main_dish: The main dish as specified in YomTovNation file in google spreadsheet
        :param add_on: The Add-on as specified in YomTovNation file in google spreadsheet
        """
        self.db_transaction_controller.execute("INSERT into 'InvitationRecord' "
                                               "values ('{}', '{}', '{}', STRFTIME('%d-%m-%Y'))"
                                               .format(employee_name, main_dish, add_on))
        self.db_connection_setup.commit()
