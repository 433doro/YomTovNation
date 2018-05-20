import sqlite3


def set_up_connection():
    db_connection_setup = sqlite3.connect('YomTovInvitationRecord.db')
    db_transaction_controller = db_connection_setup.cursor()
    return db_transaction_controller

def create_db_table_for_each_of_cognigos_employees(employees_names):
    db_transaction_controller = set_up_connection()
    if employees_names != 'Dima':
        if employees_names != 'Golan':
            db_transaction_controller.execute("CREATE TABLE '{}' AS select * FROM Golan".format(employees_names))
    db_connection_setup.commit()



def clear_all_data_from_all_tables():

