import sqlite3

conn = sqlite3.connect("signin_login_page.db")
cur = conn.cursor()

loop = True
domainBlacklist = []

while loop:
    print("Signin [S] & Login [L]")
    value = input("Input: ")

    try:
        choice = str(value)
    except ValueError:
        continue

    if str.lower(choice) == "s":
        print("")
        print("SIGNIN")

        email = input("Email: ")
        if len(email) < 4:
            print("")
            print("Invalid Email")
            print("")
            continue

        domain = email.split("@")

        if domain[1] in domainBlacklist:
            print("")
            print("Invalid Email")
            print("")
            continue

        cur.execute(f"SELECT (email) FROM details")
        output = cur.fetchall()
        print(output)
        
        if email not in output:
            cur.execute(f"INSERT INTO details (email) VALUES ('{email}')")

            password = input("Password (Min 8 Characters): ")
            if len(password) < 8:
                print("Password too Short")
                continue
            
            cur.execute(f"INSERT INTO details (password) VALUES ('{password}')")

        else:
            print("Email already in use.")
            continue
        
        print("")

    elif str.lower(choice) == "l":
        print("")
        print("LOGIN")
        email = input("Email: ")
        password = input("Password: ")
        print("")

    else:
        print("")
        print("*INVALID VALUE*")
        print("")
        continue

cur.close()
conn.close()