import pyodbc

conn = None
mycursor = None

def connect_database():
    """Connect to the SQL Server database."""
    global mycursor, conn
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-S6R1KLA;' 
            'DATABASE=bank_data;'
            'Trusted_Connection=yes;'
            'TrustServerCertificate=yes;'
        )
        mycursor = conn.cursor()
        print(" Database connection successful.")
    except pyodbc.Error as e:
        print(f" Error connecting to database: {e}")

def insert(id, name, phone, gender, salary):
    """Insert a new record into Table_1."""
    try:
        mycursor.execute(
            "INSERT INTO Table_1 (id, name, phone, gender, salary) VALUES (?, ?, ?, ?, ?)",
            (id, name, phone, gender, salary)
        )
        conn.commit()
        print(f" Record inserted successfully: {id}, {name}.")
    except pyodbc.Error as e:
        print(f" Error inserting record: {e}")

def id_exists(id):
    """Check if a record with a given ID exists."""
    try:
        mycursor.execute('SELECT COUNT(*) FROM Table_1 WHERE id = ?', (id,))
        result = mycursor.fetchone()
        return result[0] > 0
    except pyodbc.Error as e:
        print(f" Error checking ID existence: {e}")
        return False

def fetch_customer():
    """Fetch all customer records."""
    try:
        mycursor.execute('SELECT * FROM Table_1')
        result = mycursor.fetchall()
        return result
    except pyodbc.Error as e:
        print(f" Error fetching customers: {e}")
        return []

def update(id, new_name, new_phone, new_gender, new_salary):
    """Update a customer's record."""
    try:
        mycursor.execute(
            'UPDATE Table_1 SET name = ?, phone = ?, gender = ?, salary = ? WHERE id = ?',
            (new_name, new_phone, new_gender, new_salary, id)
        )
        conn.commit()
        print(f" Record updated successfully for ID: {id}.")
    except pyodbc.Error as e:
        print(f" Error updating record: {e}")

def delete(id):
    """Delete a customer's record."""
    try:
        mycursor.execute('DELETE FROM Table_1 WHERE id = ?', (id,))
        conn.commit()
        print(f" Record deleted successfully for ID: {id}.")
    except pyodbc.Error as e:
        print(f" Error deleting record: {e}")

def search(option, value):
    """Search for records by a specific column and value."""
    try:
        query = f'SELECT * FROM Table_1 WHERE {option} = ?'
        mycursor.execute(query, (value,))
        result = mycursor.fetchall()
        return result
    except pyodbc.Error as e:
        print(f" Error searching records: {e}")
        return []

#  Connect to the database
connect_database()
