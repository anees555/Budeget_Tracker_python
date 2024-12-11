import psycopg2

def get_connection():
    connec = psycopg2.connect(
        dbname = "budget_tracker",
        user = "budget_user",
        password = 'mypassword',
        host = 'localhost',
        port = "5432" 
    )
    return connec
def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL,
            category VARCHAR(50) NOT NULL,
            amount NUMERIC(10, 2) NOT NULL,
            description TEXT
        );
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()