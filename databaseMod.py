import tkinter as tk
import sqlite3 

class databaseClass():
    def __init__(self, dbName):

        self.dbName = dbName

        # Connect to database or create a new one
        self.conn = sqlite3.connect(self.dbName)

        
        # cur is used to execute commands in database
        self.cur = self.conn.cursor()


        # query to create a table named data in the database
        # Here ID has PRIMARY KEY constraint which means it is unique and does not have NULL value
        query = """
        CREATE TABLE IF NOT EXISTS data(
            ID INTEGER PRIMARY KEY,
            Name varchar(100), 
            Email varchar(100),
            Phone INTEGER
        )"""
        self.cur.execute(query)

        # Save the changes to the database
        self.conn.commit()


    def fetch(self):
        selectQuery = "SELECT *,oid from data"
        self.cur.execute(selectQuery)

        # fetchall returns a list of tuples of all the data present in the database
        records = self.cur.fetchall()
        return records

        
    def insert(self, id, name, email, phone):
        insertQuery = f"INSERT INTO data (ID,Name,Email,Phone) VALUES (?,?,?,?)"
        self.cur.execute(insertQuery,(id, name, email, phone))
        self.conn.commit()


    def delete(self, id):
        delQuery = """DELETE FROM data WHERE ID=?"""
        self.cur.execute(delQuery,(id,))
        self.conn.commit()

    def update(self, id, name, email, phone, id1):
        updQuery = """
            UPDATE data 
            SET ID=?, Name=?, Email=?, Phone=? 
            WHERE ID=?
            """
        self.cur.execute(updQuery,(id, name, email, phone, id1))
        self.conn.commit()
