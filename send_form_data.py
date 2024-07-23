import os
import mysql.connector
from mysql.connector import Error

def connect_to_database():
    """Establishes a connection to the MySQL database using mysql-connector-python."""
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'vzleadgen.cma1wzfub9dh.us-west-2.rds.amazonaws.com'),
            database=os.getenv('DB_NAME', 'vizleads'),
            user=os.getenv('DB_USER', 'tlubben'),
            password=os.getenv('DB_PASSWORD', 'VizualLead21!')
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def store_form_data(data):
    """Inserts form data into the form_data table."""
    connection = connect_to_database()
    if connection is not None:
        try:
            data_tuple = tuple(data.values())
            cursor = connection.cursor()
            query = """
                INSERT INTO form_data (
                    full_name, job_title, department_ai, linkedin_industry,
                    lvl1_industry, lvl2_industry, long_input1, long_input2,
                    long_input3, long_input4
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                )
            """
            print(data_tuple)
            cursor.execute(query, data_tuple)
            connection.commit()
            print("Data inserted successfully")
            cursor.close()
        except Error as e:
            print(f"Error while inserting data: {e}")
        finally:
            connection.close()
            print("MySQL connection is closed")
    else:
        print("Failed to connect to the database")