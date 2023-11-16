import mysql.connector
import xml.etree.ElementTree as ET

# Function to connect to the database
def connect_to_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="OnlineBookstore"
    )
    return conn

# Function to parse XML and populate the database
def populate_database(xml_file_path):
    conn = connect_to_database()
    cursor = conn.cursor()

    # Parse the XML file
    xml_tree = ET.parse(xml_file_path)
    xml_root = xml_tree.getroot()

    # Iterate over the child elements of the root element
    for child_element in xml_root:
        table_name = child_element.tag
        for row_element in child_element:
            # Get the data from each child element
            data = {}
            for attr_element in row_element:
                data[attr_element.tag] = attr_element.text

            # Generate the SQL query to insert the data into the table
            columns = ', '.join(data.keys())
            values = ', '.join([f"'{value}'" for value in data.values()])
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

            # Execute the SQL query
            cursor.execute(query)

    # Commit the changes and close the cursor and connection
    conn.commit()
    cursor.close()
    conn.close()

# Function to update a book in the database
def update_book(xml_file_path):
    conn = connect_to_database()
    cursor = conn.cursor()

    # Parse the XML file
    xml_tree = ET.parse(xml_file_path)
    xml_root = xml_tree.getroot()

    # Get the updated details for the book
    updated_details = {}
    for child_element in xml_root:
        if child_element.tag == 'books':
            for row_element in child_element:
                for attr_element in row_element:
                    updated_details[attr_element.tag] = attr_element.text

    # Check if the BookID is present in the updated details
    if 'BookID' in updated_details:
        # Generate the SQL query to update the book
        set_clause = ', '.join([f"{key} = '{value}'" for key, value in updated_details.items() if key != 'BookID'])
        query = f"UPDATE Books SET {set_clause} WHERE BookID = {updated_details['BookID']}"

        # Execute the SQL query
        cursor.execute(query)

        # Commit the changes and close the cursor and connection
        conn.commit()
        cursor.close()
        conn.close()
        print("Book updated successfully!")
    else:
        print("BookID not found in the XML file. Please make sure the XML file contains the BookID tag.")



# Function to delete a book from the cart
def delete_book(cart_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    # Generate the SQL query to delete the book from the cart
    query = f"DELETE FROM carts WHERE CartID = {cart_id}"

    # Execute the SQL query
    cursor.execute(query)

    # Commit the changes and close the cursor and connection
    conn.commit()
    cursor.close()
    conn.close()
    
def main():
    while True:
        print("Menu:")
        print("1. Insert XML data")
        print("2. View all tables")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            xml_file_path = r"C:\Users\vaish\Downloads\update.xml"
            populate_database(xml_file_path)
            print("Data inserted successfully!")
        elif choice == "2":
            conn = connect_to_database()
            cursor = conn.cursor()

            # Get the table names
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()

            # Fetch and display the data from each table
            for table in tables:
                table_name = table[0]
                cursor.execute(f"SELECT * FROM {table_name}")
                data = cursor.fetchall()
                print(f"\n{table_name}:")
                for row in data:
                    print(row)

            cursor.close()
            conn.close()
        elif choice == "3":
            xml_file_path = r"C:\Users\vaish\Downloads\populate.xml"
            update_book(xml_file_path)
            print("Book updated successfully!")
        elif choice == "4":
            cart_id = input("Enter the CartID of the book to be deleted: ")
            delete_book(cart_id)
            print("Book deleted successfully!")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()