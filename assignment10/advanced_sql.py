import sqlite3
import os


# ===== Database Path Configuration (Robust Absolute Path Discovery) =====

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "db", "lesson.db"))

def main():
    if not os.path.exists(DB_PATH):
        print(f" Error: Database file not found at: {DB_PATH}")
        return

    conn = None
    try:
        # Open database connection
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Enforce foreign key validation strings immediately after connecting
        conn.execute("PRAGMA foreign_keys = 1;")

        # ===== Task 1: Complex JOINs with Aggregation =====
        query_task1 = """
        SELECT 
            o.order_id, 
            SUM(p.price * l.quantity) AS total_price
        FROM orders o
        INNER JOIN line_items l ON o.order_id = l.order_id
        INNER JOIN products p ON l.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id ASC
        LIMIT 5;
        """
        
        print("\n===== Task 1: Total Price of the First 5 Orders =====\n")
        print(f"{'Order ID':<10} | {'Total Price':<12}")
        print("-" * 27)
        
        cursor.execute(query_task1)
        for row in cursor.fetchall():
            order_id, total_price = row
            print(f"{order_id:<10} | ${total_price:,.2f}")


        # ===== Task 2: Understanding Subqueries =====
        query_task2 = """
        SELECT 
            c.customer_name,
            AVG(sub.total_price) AS average_total_price
        FROM customers c
        LEFT JOIN (
            SELECT 
                o.customer_id AS customer_id_b, 
                SUM(p.price * l.quantity) AS total_price
            FROM orders o
            INNER JOIN line_items l ON o.order_id = l.order_id
            INNER JOIN products p ON l.product_id = p.product_id
            GROUP BY o.order_id
        ) sub ON c.customer_id = sub.customer_id_b
        GROUP BY c.customer_id
        ORDER BY average_total_price DESC;
        """
        
        print("\n===== Task 2: Average Order Price Per Customer =====\n")
        print(f"{'Customer Name':<35} | {'Avg Order Price':<15}")
        print("-" * 53)
        
        cursor.execute(query_task2)
        for row in cursor.fetchall():
            customer_name, avg_price = row
            display_price = f"${avg_price:,.2f}" if avg_price is not None else "$0.00"
            print(f"{customer_name:<35} | {display_price:<15}")


        # ===== Task 3: An Insert Transaction Based on Data =====
        print("\n===== Task 3: Transactional Order Processing =====\n")
        
        # 1. Fetch data variables dynamically using verified schemas (unpacking tuples)
        cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons';")
        customer_id_row = cursor.fetchone()
        customer_id = customer_id_row[0] if customer_id_row else None
        
        cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris';")
        employee_id_row = cursor.fetchone()
        employee_id = employee_id_row[0] if employee_id_row else None
        
        # Find the product_ids of the 5 least expensive products
        cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5;")
        product_ids = [row[0] for row in cursor.fetchall()]
        
        # Safety check to ensure lookups succeeded before starting the transaction
        if customer_id is None or employee_id is None or len(product_ids) < 5:
            print("Setup error: Could not locate necessary customer, employee, or product records.")
            conn.close()
            return

        # 2. Begin the unified context transaction block
        conn.execute("BEGIN TRANSACTION;")
        
        # Create order record utilizing RETURNING clause to fetch the auto-assigned key
        insert_order_query = """
        INSERT INTO orders (customer_id, employee_id) 
        VALUES (?, ?) 
        RETURNING order_id;
        """
        cursor.execute(insert_order_query, (customer_id, employee_id))
        new_order_id = cursor.fetchone()[0] # Unpack the auto-assigned integer ID
        
        # Insert the 5 separate line items for the target order
        insert_item_query = """
        INSERT INTO line_items (order_id, product_id, quantity) 
        VALUES (?, ?, 10);
        """
        for prod_id in product_ids:
            cursor.execute(insert_item_query, (new_order_id, prod_id))
            
        # Commit all changes permanently to disk
        conn.commit()
        print(f" Transaction successful! Created Order ID: {new_order_id}")
        
        # 3. Use SELECT with a JOIN to print out order metadata details (FIXED TO p.product_name)
        display_order_query = """
        SELECT l.line_item_id, l.quantity, p.product_name
        FROM line_items l
        INNER JOIN products p ON l.product_id = p.product_id
        WHERE l.order_id = ?
        ORDER BY l.line_item_id ASC;
        """
        cursor.execute(display_order_query, (new_order_id,))
        order_details = cursor.fetchall()
        
        print(f"\nManifest for Order #{new_order_id}:")
        print(f"{'Line Item ID':<12} | {'Quantity':<8} | {'Product Name':<25}")
        print("-" * 51)
        for item in order_details:
            li_id, qty, prod_name = item
            print(f"{li_id:<12} | {qty:<8} | {prod_name:<25}")


        # ===== Task 4: Aggregation with HAVING =====
        query_task4 = """
        SELECT 
            e.employee_id, 
            e.first_name, 
            e.last_name, 
            COUNT(o.order_id) AS order_count
        FROM employees e
        INNER JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.employee_id
        HAVING COUNT(o.order_id) > 5
        ORDER BY order_count DESC;
        """
        
        print("\n===== Task 4: Employees with More Than 5 Orders =====\n")
        print(f"{'Emp ID':<8} | {'First Name':<12} | {'Last Name':<15} | {'Order Count':<12}")
        print("-" * 55)
        
        cursor.execute(query_task4)
        for row in cursor.fetchall():
            emp_id, f_name, l_name, order_count = row
            print(f"{emp_id:<8} | {f_name:<12} | {l_name:<15} | {order_count:<12}")

        # Close database connection
        conn.close()
        
    except sqlite3.Error as e:
        if conn:
            try:
                conn.rollback()
                print("🔄 Transaction successfully rolled back.")
            except sqlite3.OperationalError:
                pass 
        print(f"❌ SQLite Error Encountered: {e}")

if __name__ == "__main__":
    main()