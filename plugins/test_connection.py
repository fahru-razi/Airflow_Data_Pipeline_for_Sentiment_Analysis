from sqlalchemy import create_engine

def test_connection():
    conn_string = 'postgresql://airflow:airflow@postgres:5432/data_warehouse'
    try:
        engine = create_engine(conn_string)
        connection = engine.connect()
        print("Connection to PostgreSQL successful")
        connection.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_connection()
