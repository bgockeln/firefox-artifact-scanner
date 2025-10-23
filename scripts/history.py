import sqlite3
from datetime import datetime, timedelta
import csv
import os 
import sys 

# Helper Functions
def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

def wait():
    input("Press any key")

# Main Function
def analyze_history(db_path):
    
    # Check if file exists
    if not os.path.exists(db_path):
        print("Error: places.sqlite not found in ./browser_profile.")
        sys.exit(1)

    print("File found. Proceeding...")

    # Connect to SQLite DB and create a cursor to execute queries
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # SQL query to retrieve the most visited URLs and their metadata
    # Edit "Limit 50;" to change the amount of results
    query = """
    SELECT url, title, visit_count, last_visit_date
    FROM moz_places
    ORDER BY visit_count DESC
    LIMIT 50; 
    """

    # Execute the SQL query
    cursor.execute(query)

    # Create the CSV file and writes the results into it
    with open("history_export.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Timestamp", "Visit Count", "Title", "URL"])

        # Loop through all results returned by the query
        for row in cursor.fetchall():
            url = row[0]
            title = row[1]
            count = row[2]
            timestamp = row[3]
  
            # Convert Firefox timestamp to a datetime object
            # If there is no last visit date, use "N/A"
            if timestamp: 
                ts = datetime(1970, 1, 1) + timedelta(microseconds=timestamp)
            else:
                ts = "N/A"
    
            # Write each row of actual browsing data to the CSV file
            writer.writerow([ts, count, title, url])

    print("Analysis Complete")
    wait()
    clear_screen()

    # Close DB connection
    conn.close()
