from typing import List, Optional


class SQLQueriesFactory:

    @staticmethod
    def generate_select_query(table: str, columns: Optional[List[str]], projection_fields: Optional[List[str]], order_column: Optional[str], order_ascending: bool = True, limit: Optional[int] = None, distinct: Optional[bool] = None) -> str:
        query = " SELECT "
        if distinct:
            query += " DISTINCT "
        query += ", ".join(columns) if columns else "*"
        query += f" FROM {table} "
        if projection_fields:
            query += " WHERE "
            query += " AND ".join(projection_fields)
        if order_column is not None:
            query += f" ORDER BY {order_column} "
            query += "ASC" if order_ascending else "DESC"
        if limit:
            query += f" LIMIT {limit} "
        return query