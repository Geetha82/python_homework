import os
import sqlite3

# Task 2: Relationship Analysis:
# Which table has the foreign key in the one-to-many relationship?
# The magazines table holds the foreign key that points to the primary key of the publishers table.
# What foreign keys does
# The subscriptions table is a join table for a many-to-many relationship
# It requires two foreign keys:One pointing to the primary key of the subscribers table.One pointing to the primary key of the magazines table.

# Task 3: Helper Functions to populate date
def add_publisher_data(cursor,name):
    try:
        cursor.execute(
            "INSERT OR IGNORE INTO publishers (name) VALUES (?);", (name,)
            )
    except sqlite3.Error as e:
        print(f"Error inserting publisher '{name}': {e}")

def add_magazine_data(cursor,name, publisher_name):
    try:
        # Task 2 Concept: Follow foreign key relationship back to publishers table
        cursor.execute(
            "SELECT id FROM publishers WHERE name = ?;", (publisher_name,)
        )
        row = cursor.fetchone()

        if row is None:
            print(
                f"Cannot add magazine '{name}': Publisher '{publisher_name}' not found."

            )
            return
        publisher_id = row[0]

        # Use INSERT or IGNORE to respect the UNIQUE constraint on magazine name
        cursor.execute(
            "INSERT OR IGNORE INTO magazines (name, publisher_id) VALUES (?, ?);",
            (name, publisher_id)
            )
        
    except sqlite3.Error as e:
        print(f"Error inserting magazine '{name}': {e}")

def add_subscriber_data(cursor,name, address):
    try:
        # Task 3 Constraint: Check that BOTH name and address aren't identical duplicates
        cursor.execute(
            "SELECT id FROM subscribers WHERE name = ? AND address = ?;",
            (name, address),
        )

        if cursor.fetchone() is not None:
            return
    
        cursor.execute(
            "INSERT INTO subscribers (name, address) VALUES (?, ?);",
            (name, address)
            )
        
    except sqlite3.Error as e:
        print(f"Error inserting subscriber '{name}': {e}")


def add_subscription_data(cursor, subscriber_name, magazine_name, expiration_date):
# Inserts a join table connection between a subscriber and a magazine.   
    try:
        # find subscriber ID
        cursor.execute(
            "SELECT id FROM subscribers WHERE name = ?;", (subscriber_name,)
            )
        sub_row = cursor.fetchone()

        # find magazine ID
        cursor.execute(
            "SELECT id FROM magazines WHERE name = ?;", (magazine_name,)
            )
        mag_row = cursor.fetchone()

        if not sub_row or not mag_row:
            print(
                f"Cannot link subscription for '{subscriber_name}' to {magazine_name}: Record missing."
            )
            return
        
        subscriber_id = sub_row[0]
        magazine_id = mag_row[0]
 
        # Avoid Duplicate Subscriptions: Prevent linking the exact same sub-to-mag mapping again
        cursor.execute(
            "SELECT id FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?;",
            (subscriber_id, magazine_id),
        )
        if cursor.fetchone() is not None:
            return
    
        cursor.execute(
            """INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date)
            VALUES (?, ?, ?);""",
             (subscriber_id, magazine_id, expiration_date),
            )
        
    except sqlite3.Error as e:
        print(f"Error inserting subscriptiom: {e}")



def main():
    # Task1: Define the relative database path
    db_path = os.path.join("..", "db", "magazines.db")

    # Ensure the parent directory (../db) exists before connecting
    db_dir = os.path.dirname(db_path)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir)

    connection = None

    # Task 1: Execute all SQL-related operations inside a try block
    try:
        print(f"Connecting to database at: {db_path}")
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # TASK 3 REQUIREMENT: Force SQLite to actively monitor and enforce foreign keys
        connection.execute("PRAGMA foreign_keys = 1")

        print("Defining Database Structures...")


        # Task 2: Define Database Structure

        # Create Publisher table
        cursor.execute("""
                       
                       CREATE TABLE IF NOT EXISTS publishers (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL UNIQUE
                       );
        """)

        # Create magazines table
        cursor.execute("""
                       
                       CREATE TABLE IF NOT EXISTS magazines (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL UNIQUE,
                       publisher_id INTEGER NOT NULL,
                       FOREIGN KEY (publisher_id) REFERENCES publishers(id)
                       );
        """)

        # Create subscribers table
        cursor.execute("""
                       
                       CREATE TABLE IF NOT EXISTS subscribers (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       address TEXT NOT NULL
                       );
        """)

        # Create subscriptions table
        cursor.execute("""
                       
                       CREATE TABLE IF NOT EXISTS subscriptions (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       subscriber_id INTEGER NOT NULL,
                       magazine_id INTEGER NOT NULL,
                       expiration_date TEXT NOT NULL,
                       FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
                        FOREIGN KEY (magazine_id) REFERENCES magazines(id)
                       );
        """)

        # TASK 3: Add at least 3 entries to Publishers table
        add_publisher_data(cursor, "Condé Nast")
        add_publisher_data(cursor, "Hearst Communications")
        add_publisher_data(cursor, "Dotdash Meredith")

        # TASK 3: Add at least 3 entries to Magazines table
        add_magazine_data(cursor, "Vogue", "Condé Nast")
        add_magazine_data(cursor, "Cosmopolitan", "Hearst Communications")
        add_magazine_data(cursor, "Better Homes & Gardens", "Dotdash Meredith")

        # TASK 3: Add at least 3 entries to Subscribers table
        add_subscriber_data(cursor, "Alice Smith", "123 Maple St")
        add_subscriber_data(cursor, "Bob Jones", "456 Oak Ave")
        add_subscriber_data(cursor, "Charlie Brown", "789 Pine Rd")

        # TASK 3: Add at least 3 entries to Subscriptions table
        add_subscription_data(cursor, "Alice Smith", "Vogue", "2027-12-31")
        add_subscription_data(cursor, "Bob Jones", "Cosmopolitan", "2026-11-30")
        add_subscription_data(cursor, "Charlie Brown", "Better Homes & Gardens", "2028-06-15")


        # Task 3: Commit to save the structural changes
        connection.commit()
        print("Database successfully populated and saved.")

        # Task 4: Write SQL Queries
        print("Task 4: Execute SQL Queries")
        # Write a query to retrieve all information from the subscribers table.
        print("Query 1: All Subscribers Information")
        cursor.execute("SELECT * FROM subscribers;")
        for row in cursor.fetchall():
            print(row)
        print("_" * 50)
        
        # Write a query to retrieve all magazines sorted by name.
        print("Query 2: All Magazines sorted by name ")
        cursor.execute("SELECT * FROM magazines ORDER BY name ASC;")
        for row in cursor.fetchall():
            print(row)
        print("_" * 50)

        # Write a query to find magazines for a particular publisher, one of the publishers you created. This requires a JOIN.
        selected_publisher = "Condé Nast"
        print("Query 3: Magazines publishes by '{selected_publisher}'")
        cursor.execute("""
            SELECT magazines.id, magazines.name
            FROM magazines
            JOIN publishers ON magazines.publisher_id = publishers.id
            WHERE publishers.name = ?;
        """, (selected_publisher,))
        for row in cursor.fetchall():
            print(row)
        print("_" * 50)

    except sqlite3.Error as e:
        # Task 1: Catch and report any database-related exceptions
        print(f"An error occurred while handling the database: {e}")

    finally:
        # Task 1: Ensure the connection is always closed to prevent memory leaks
        if connection:
            connection.close()
            print("Database connection closed successfully.")

if __name__ == "__main__":
    main()
