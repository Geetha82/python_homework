import os
import sqlite3
import pandas as pd


def main():
    # Define the path to the lesson database
    db_path = os.path.join("..", "db", "lesson.db")

    if not os.path.exists(db_path):
        print(f"Error: The lesson database was not found at {db_path}.")
        return

    connection = None

    try:
        connection = sqlite3.connect(db_path)

        # SQL statement to JOIN line_items and products
        query = """
            SELECT 
                line_items.line_item_id, 
                line_items.quantity, 
                line_items.product_id, 
                products.product_name, 
                products.price
            FROM line_items
            JOIN products ON line_items.product_id = products.product_id;
        """

        # Read data into a DataFrame and print the first 5 lines
        df = pd.read_sql_query(query, connection)
        print("--- Step 1 & 2: First 5 lines of the initial JOIN DataFrame ---")
        print(df.head(5))
        print("\n" + "=" * 60 + "\n")

        # Add a column called 'total' (quantity * price) and print first 5 lines
        df["total"] = df["quantity"] * df["price"]
        print("--- Step 3: DataFrame with 'total' column added ---")
        print(df.head(5))
        print("\n" + "=" * 60 + "\n")

        # Groupby product_id and apply the required agg() aggregations
        # Aggregations: line_item_id -> count, total -> sum, product_name -> first
        summary_df = (
            df.groupby("product_id")
            .agg(
                {
                    "line_item_id": "count",
                    "total": "sum",
                    "product_name": "first",
                }
            )
            .reset_index()
        )

        print("--- Step 4: First 5 lines of the grouped/aggregated DataFrame ---")
        print(summary_df.head(5))
        print("\n" + "=" * 60 + "\n")

        #  Sort the DataFrame by the product_name column
        summary_df = summary_df.sort_values(by="product_name")

        # Write the final summary DataFrame to order_summary.csv
        csv_filename = "order_summary.csv"
        summary_df.to_csv(csv_filename, index=False)
        print(f"--- Step 5 & 6: Data successfully written to {csv_filename} ---")

    except (sqlite3.Error, Exception) as e:
        print(f"An error occurred during processing: {e}")

    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    main()
