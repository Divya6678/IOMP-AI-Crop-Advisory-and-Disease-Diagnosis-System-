import sqlite3
import traceback

def migrate():
    try:
        conn = sqlite3.connect("history.db")
        cursor = conn.cursor()
        cursor.execute("ALTER TABLE history ADD COLUMN user_id INTEGER")
        conn.commit()
        print("Successfully added user_id column")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("Column already exists")
        else:
            print("Error:", e)
            traceback.print_exc()
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    migrate()
