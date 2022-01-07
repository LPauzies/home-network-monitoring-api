from typing import Optional, List, Any
from database.interface.sql_connection_factory import SQLConnectionFactory

class SQLOperations:

    # Regarding queries
    @staticmethod
    def execute_sql_query(sql_query: str, with_return: bool) -> Optional[List[Any]]:
        connection = SQLConnectionFactory.create_connection()
        cursor = connection.cursor()
        cursor.execute(sql_query)
        if with_return:
            return cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()

    # Regarding SQL files
    @staticmethod
    def execute_sql_script(sql_script_path: str) -> None:
        with open(sql_script_path, "r") as sql_descriptor:
            sql_script = sql_descriptor.read()
            SQLOperations.execute_sql_query(sql_script)