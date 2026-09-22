import mysql.connector

# ================= SQL CONNECTION =================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2112",
    database="atm_db"
)

cursor = db.cursor()

# Get PIN and balance from SQL
cursor.execute("SELECT pin, balance FROM atm_account WHERE id=1")
data = cursor.fetchone()

correct_pin = data[0]
balance = data[1]

transaction = []


# ================= ATM LOGIN =================

for attempt in range(3):

    user_pin = int(input("enter your pin number:"))

    if user_pin == correct_pin:
        print("\nlogin successful")
        break
    else:
        print("incorrect_pin")
        break

else:
    print("your account is locked.attempt more than 3")
    exit()


# ================= ATM MENU =================

while True:

    print("\n---atm menu---")
    print("1.check balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.transaction history")
    print("5.pin change")
    print("6.exit")
    print("===============================")

    choice = int(input("enter your choice:"))


    # ================= CHECK BALANCE =================

    if choice == 1:

        print("\ncheck current balance:", balance)


    # ================= DEPOSIT =================

    elif choice == 2:

        deposit = int(input("enter your deposit amount:"))

        if deposit > 0:

            balance += deposit

            transaction.append("deposited:" + str(deposit))

            # Update balance in SQL
            cursor.execute(
                "UPDATE atm_account SET balance=%s WHERE id=1",
                (balance,)
            )

            # Store transaction in SQL
            cursor.execute(
                """
                INSERT INTO transactions
                (transaction_type, amount, balance)
                VALUES (%s, %s, %s)
                """,
                ("deposit", deposit, balance)
            )

            db.commit()

            print("your cash is deposited successfully")
            print("balance updated:", balance)

        else:

            print("enter your valid amount")


    # ================= WITHDRAW =================

    elif choice == 3:

        withdraw = int(input("enter your withdraw amount:"))

        if withdraw <= 0:

            print("enter your valid amount")

        elif withdraw > balance:

            print("insufficient balance")

        else:

            balance -= withdraw

            transaction.append("withdrawan:" + str(withdraw))

            # Update balance in SQL
            cursor.execute(
                "UPDATE atm_account SET balance=%s WHERE id=1",
                (balance,)
            )

            # Store transaction in SQL
            cursor.execute(
                """
                INSERT INTO transactions
                (transaction_type, amount, balance)
                VALUES (%s, %s, %s)
                """,
                ("withdraw", withdraw, balance)
            )

            db.commit()

            print("please receive your cash")
            print("remaining balance:", balance)


    # ================= TRANSACTION HISTORY =================

    elif choice == 4:

        print("\n======transactions history======")

        if transaction:

            for transactions in transaction:
                print("transactions")

        else:

            print("no transaction avalaible")

        print("current balance:", balance)

        # Also display transactions stored in SQL
        print("\n======SQL TRANSACTION HISTORY======")

        cursor.execute(
            """
            SELECT transaction_type, amount, balance
            FROM transactions
            ORDER BY id
            """
        )

        sql_transactions = cursor.fetchall()

        if sql_transactions:

            for trans in sql_transactions:
                print(
                    "Type:",
                    trans[0],
                    "| Amount:",
                    trans[1],
                    "| Balance:",
                    trans[2]
                )

        else:

            print("no transaction avalaible")


    # ================= PIN CHANGE =================

    elif choice == 5:

        old_pin = int(input("enter your current pin:"))

        if old_pin == correct_pin:

            new_pin = int(input("enter your new pin:"))

            correct_pin = new_pin

            # Update PIN in SQL
            cursor.execute(
                "UPDATE atm_account SET pin=%s WHERE id=1",
                (correct_pin,)
            )

            db.commit()

            print("successfully changed your pin")

        else:

            print("incorrect pin")


    # ================= EXIT =================

    elif choice == 6:

        print("\n thank you for using atm")
        print("have a nice day")
        print("visit again")

        break


    # ================= INVALID CHOICE =================

    else:

        print("invalid choice.please try again")


# ================= CLOSE SQL CONNECTION =================

cursor.close()
db.close()













        


