import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            name text,
            age text,
            surname text,
            email text,
            gender text,
            contact text,
            tc text,
            city text
            
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, age, surname, email, gender, contact, tc, city):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?,?)",
                         (name, age, surname, email, gender, contact, tc, city))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from employees")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from employees where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, age, surname, email, gender, contact, tc, city):
        self.cur.execute(
            "update employees set name=?, age=?, surname=?, email=?, gender=?, contact=?, tc=?, city=? where id=?",
            (name, age, surname, email, gender, contact, tc, city, id))
        self.con.commit()