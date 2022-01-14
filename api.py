from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Any, Dict, List, Optional
from database.interface.sql_queries import SQLQueriesFactory
from database.interface.sql_operations import SQLOperations
from database.data_model.data_model import Ping

app = FastAPI()

# CORS authorization
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# As soon as it is quite a simple API we will use only one file

@app.get("/api/ping/")
async def get_all_pings() -> List[Dict[str, Any]]:
    """Retrieve the last entries of the ping table for all IP available.

    Returns:
        List[Dict[str, Any]]: A JSON based on SQL table data model for the needed ping
    """
    query_number_of_distinct_ips = f"SELECT COUNT(DISTINCT {Ping.Columns.IP}) FROM {Ping.TABLE}"
    number_of_distinct_ips = SQLOperations.execute_sql_query(query_number_of_distinct_ips, with_return = True)[0][0]
    query = SQLQueriesFactory.generate_select_query(
        table = Ping.TABLE,
        columns = Ping.Columns.ALL,
        projection_fields = None,
        order_column = Ping.Columns.EVENT_TIME,
        order_ascending = False,
        limit = number_of_distinct_ips
    )
    entries = SQLOperations.execute_sql_query(query, with_return = True)
    entries = [dict(zip(Ping.Columns.ALL, entry)) for entry in entries]
    for entry in entries:
        entry[Ping.Columns.PACKET_LOSS] = entry[Ping.Columns.PACKET_LOSS] == 1
    return entries

@app.get("/api/ping/{ip}")
async def get_ping(ip: str) -> List[Dict[str, Any]]:
    """Retrieve the last entry of the ping table for current asked IP if provided, else for all IP available

    Args:
        ip (Optional[str], optional): The IP to retrieve ping data from. Defaults to None.

    Returns:
        List[Dict[str, Any]]: A JSON based on SQL table data model for the needed ping
    """
    query = SQLQueriesFactory.generate_select_query(
        table = Ping.TABLE,
        columns = Ping.Columns.ALL,
        projection_fields = [f"{Ping.Columns.IP} = '{ip}'"],
        order_column = Ping.Columns.EVENT_TIME,
        order_ascending = False,
        limit = 1
    )
    entries = SQLOperations.execute_sql_query(query, with_return = True)
    entries = [dict(zip(Ping.Columns.ALL, entry)) for entry in entries]
    for entry in entries:
        entry[Ping.Columns.PACKET_LOSS] = entry[Ping.Columns.PACKET_LOSS] == 1
    return entries