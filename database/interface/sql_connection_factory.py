import sqlite3
import logging

# Create logger here
logger = logging.getLogger(__name__)

# Keep it relative to stay in "all services in folder" logic
SQLITE_DATABASE_FILE = "../home-network-monitoring-database/NetworkMonitoring.db"

class SQLConnectionFactory:

    def create_connection() -> sqlite3.Connection:
        try:
            return sqlite3.connect(SQLITE_DATABASE_FILE)
        except sqlite3.Error as error:
            logger.exception(error)