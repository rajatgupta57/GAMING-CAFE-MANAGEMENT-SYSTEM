# Importing MySQL Connector
import mysql.connector as mysql

# Taking MySQL Password as Input
password = input("Enter your MySQL password:")

# Function to Create Database
def DataBaseCreation():
    try:
        # Establishing Connection
        mydb = mysql.connect(host="localhost", user="root", passwd=password)
        cursor = mydb.cursor()
        
        # Creating Database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS Gaming_Cafe")
        print("Created Database Successfully")
    except Exception as e:
        print("Failed to establish connection:", e)

# Printing Title of System
print("*" * 70)
print("\tGAMING CAFE MANAGEMENT SYSTEM")
print("*" * 70)

# Function to Create Tables
def TablesCreation():
    try:
        # Connecting to the Gaming_Cafe Database
        mydb = mysql.connect(host="localhost", user="root", passwd=password, database="Gaming_Cafe")
        cursor = mydb.cursor()

        # Creating Players Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Players (
                Player_ID INT(10) PRIMARY KEY,
                Player_Name VARCHAR(15),
                Player_Age INT(10),
                Phone_No VARCHAR(20),  # Changed from INT to VARCHAR to store phone numbers correctly
                Subs VARCHAR(20),
                Reg_Date DATE
            )
        """)

        # Creating Games Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Games (
                G_ID INT(10) PRIMARY KEY,
                G_Type VARCHAR(15),
                G_Name VARCHAR(15),
                G_Mode VARCHAR(25),
                G_Size INT(5),
                G_Rate INT(5)
            )
        """)

        # Creating Subscriptions Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Subscriptions (
                Subs_ID INT(10) PRIMARY KEY,
                Subs_Name VARCHAR(15),
                Val INT(5),
                Subs_Amt INT(5),
                Hours INT(4),
                P_Limit INT(4)
            )
        """)

        # Creating Payments Table with Foreign Key Reference to Players Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Payments (
                Payment_ID INT AUTO_INCREMENT PRIMARY KEY,  # Added auto-increment ID
                Player_ID INT(10),
                Player_Name VARCHAR(15),
                Amount INT(10),
                Mode_Of_Payment VARCHAR(15),
                Date_Of_Payment DATE,
                T_Played INT(4),
                FOREIGN KEY (Player_ID) REFERENCES Players(Player_ID) ON DELETE CASCADE  # Added foreign key
            )
        """)

        # Creating Devices Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Devices (
                Dev_ID INT(10) PRIMARY KEY,
                Dev_Type VARCHAR(15),
                Dev_Name VARCHAR(15),
                Price INT(10),
                Date_of_Purchase DATE,
                Warranty INT(5)
            )
        """)

        print("Required Tables Created")
    except Exception as e:
        print("Failed to establish connection:", e)

# Calling Functions to Create Database and Tables
DataBaseCreation()
TablesCreation()

# Establishing Global Connection
mydb = mysql.connect(host="localhost", user="root", passwd=password, database="Gaming_Cafe")
cursor = mydb.cursor()

# Function to Manage Player Details
def player_details():
    
    # Function to Add a New Player
    def add():
        Player_ID = int(input("Enter Player's ID:"))
        Player_Name = input("Enter Player's Name:")
        Player_Age = int(input("Enter Player's Age:"))
        Phone_No = input("Enter Their Phone Number:")  # Changed input type to string
        Subs = input("Enter Their Subscription:")
        Reg_Date = input("Enter Their Registration Date (YYYY-MM-DD):")
        try:
            # Inserting Data into Players Table
            cursor.execute(f"INSERT INTO Players VALUES ({Player_ID}, '{Player_Name}', {Player_Age}, '{Phone_No}', '{Subs}', '{Reg_Date}')")
            mydb.commit()
            print("Data Added Successfully.")
        except Exception as e:
            print("Failed to establish connection:", e)

    # Function to Display All Players
    def display():
        try:
            cursor.execute("SELECT * FROM Players")
            results = cursor.fetchall()
            for i in results:
                print(i)
        except Exception as e:
            print("Failed to establish connection:", e)

    # Function to Update Player Details
    def update():
        Old_Player_ID = int(input("Enter Current Player's ID:"))
        New_Player_ID = int(input("Enter New Player's ID:"))
        Player_Name = input("Enter Player's Name:")
        Player_Age = int(input("Enter Player's Age:"))
        Phone_No = input("Enter Their Phone Number:")
        Subs = input("Enter Their Subscription:")
        Reg_Date = input("Enter Their Registration Date (YYYY-MM-DD):")
        try:
            cursor.execute(f"UPDATE Players SET Player_ID={New_Player_ID}, Player_Name='{Player_Name}', Player_Age={Player_Age}, Phone_No='{Phone_No}', Subs='{Subs}', Reg_Date='{Reg_Date}' WHERE Player_ID={Old_Player_ID}")
            mydb.commit()
            print("Data Updated Successfully.")
        except Exception as e:
            print("Failed to establish connection:", e)

    # Function to Search for a Player
    def search():
        Player_ID = int(input("Enter Player ID to Search:"))
        try:
            cursor.execute(f"SELECT * FROM Players WHERE Player_ID={Player_ID}")
            results = cursor.fetchall()
            for i in results:
                print(i)
        except Exception as e:
            print("Failed to establish connection:", e)

    # Function to Delete a Player
    def delete():
        print("Proceed with caution.")
        Player_ID = int(input("Enter Player ID to Delete:"))
        try:
            cursor.execute(f"DELETE FROM Players WHERE Player_ID={Player_ID}")
            mydb.commit()
            print("Data Deleted Successfully.")
        except Exception as e:
            print("Failed to establish connection:", e)

    # Menu for Managing Players
    while True:
        print("A:Add, D:Display, U:Update, S:Search, X:Delete, E:Exit")
        choice = input("Enter Choice:")
        if choice == "A":
            add()
        elif choice == "D":
            display()
        elif choice == "U":
            update()
        elif choice == "S":
            search()
        elif choice == "X":
            delete()
        else:
            break

# Main Menu of the System
while True:
    print("1. Manage Players")
    print("2. Manage Games")
    print("3. Manage Subscriptions")
    print("4. Manage Payments")
    print("5. Manage Devices")
    print("6. Exit")
    choice = input("Enter Choice:")

    # Calling Corresponding Functions Based on User Input
    if choice == "1":
        player_details()
    elif choice == "2":
        game_details()
    elif choice == "3":
        subscription_details()
    elif choice == "4":
        payment_log()
    elif choice == "5":
        device_details()
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

# Logging Out Message
print("*" * 70)
print("\tYOU HAVE LOGGED OUT")
print("\tTHANK YOU FOR CHECKING IN")
print("*" * 70)
