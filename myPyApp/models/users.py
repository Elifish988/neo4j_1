from models.db import Database

def create_user_table():
    db = Database()
    db.execute_query('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    db.commit()
    db.close()

def seed_users():
    db = Database()
    cursor = db.execute_query('SELECT COUNT(*) FROM users')

    if cursor.fetchone()[0] == 0:
        users = [
            ('יוסי', 'yossi@example.com'),
            ('מיכל', 'michal@example.com'),
            ('דני', 'dani@example.com')
        ]
        db.execute_many('INSERT INTO users (name, email) VALUES (?, ?)', users)
        db.commit()

    db.close()

def add_user(name, email):
    db = Database()
    db.execute_query('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    db.commit()
    db.close()

def delete_user(user_id):
    db = Database()
    db.execute_query('DELETE FROM users WHERE id = ?', (user_id,))
    db.commit()
    db.close()

def get_all_users():
    db = Database()
    cursor = db.execute_query('SELECT * FROM users')
    users = cursor.fetchall()
    db.close()
    return users