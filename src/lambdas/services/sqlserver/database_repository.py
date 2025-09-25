from contextlib import contextmanager
from typing import List, Dict, Any, Optional

from .database_connection_service import DatabaseConnectionService

class DatabaseRepository:
    """
    A generic repository class for handling CRUD operations for a specific database table.
    This class uses the DatabaseConnectionService to manage connections and ensures
    that all database interactions are safe from SQL injection by using parameterized queries.
    """

    def __init__(self, db_service: DatabaseConnectionService, primary_key_column: str = "Id"):
        """
        Initializes the repository for a specific table.

        Args:
            db_service (DatabaseConnectionService): The service used to get database connections.
            table_name (str): The name of the database table this repository will manage (e.g., 'dbo.Users').
            primary_key_column (str): The name of the primary key column for this table. Defaults to 'Id'.
        """
        """   if not table_name:
            raise ValueError("table_name cannot be empty.") """
        
        self._db_service = db_service
        #self._table_name = table_name
        self._primary_key_column = primary_key_column

    def get_all(self, table_name: str) -> List[Dict[str, Any]]:
        """Fetches all records from the table."""
        with self._db_service.get_connection() as conn:
            cursor = conn.cursor(as_dict=True)
            query = f"SELECT * FROM {table_name};"
            cursor.execute(query)
            return cursor.fetchall()

    def get_by_id(self, record_id: Any) -> Optional[Dict[str, Any]]:
        """
        Fetches a single record by its primary key.

        Args:
            record_id: The ID of the record to fetch.

        Returns:
            A dictionary representing the record, or None if not found.
        """
        with self._db_service.get_connection() as conn:
            cursor = conn.cursor(as_dict=True)
            # IMPORTANT: Use parameterized queries to prevent SQL injection
            query = f"SELECT * FROM {self._table_name} WHERE {self._primary_key_column} = %s;"
            cursor.execute(query, (record_id,))
            return cursor.fetchone()

    def create(self, data: Dict[str, Any], table_name: str) -> Any:
        """
        Inserts a new record into the table.

        Args:
            data (Dict[str, Any]): A dictionary where keys are column names and values are the data to insert.

        Returns:
            The ID of the newly created record.
        """
        with self._db_service.get_connection() as conn:
            cursor = conn.cursor()
            
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['%s'] * len(data))
            values = tuple(data.values())
            
            # Parameterized query for security
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"
            
            cursor.execute(query, values)

            # Retrieve the ID of the newly inserted row
            cursor.execute("SELECT SCOPE_IDENTITY() AS NewId;")
            new_id = cursor.fetchone()[0]

            conn.commit()
            return new_id

    def update(self, record_id: Any, data: Dict[str, Any]) -> bool:
        """
        Updates an existing record in the table.

        Args:
            record_id: The ID of the record to update.
            data (Dict[str, Any]): A dictionary of columns and new values to update.

        Returns:
            True if the update was successful (at least one row affected), False otherwise.
        """
        if not data:
            return False # Nothing to update
            
        with self._db_service.get_connection() as conn:
            cursor = conn.cursor()

            set_clause = ", ".join([f"{key} = %s" for key in data.keys()])
            values = tuple(data.values()) + (record_id,)

            query = f"UPDATE {self._table_name} SET {set_clause} WHERE {self._primary_key_column} = %s;"
            
            cursor.execute(query, values)
            conn.commit()
            
            return cursor.rowcount > 0

    def delete(self, record_id: Any) -> bool:
        """
        Deletes a record from the table.

        Args:
            record_id: The ID of the record to delete.

        Returns:
            True if the deletion was successful (at least one row affected), False otherwise.
        """
        with self._db_service.get_connection() as conn:
            cursor = conn.cursor()
            query = f"DELETE FROM {self._table_name} WHERE {self._primary_key_column} = %s;"
            cursor.execute(query, (record_id,))
            conn.commit()
            
            return cursor.rowcount > 0