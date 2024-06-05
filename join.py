#!C:\Python\python.exe

import cgi
import cgitb
import mysql.connector

cgitb.enable()

print("Content-Type: text/html\r\n\r\n")
print()

form = cgi.FieldStorage()

username = form.getvalue("username")
name = form.getvalue("name")
address = form.getvalue("address")
country = form.getvalue("country")
state = form.getvalue("state")
city = form.getvalue("city")
postal_code = form.getvalue("postal-code")
phone = form.getvalue("phone")
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="marvel tv"
    )

    cursor = mydb.cursor()

    cursor.execute("""
        INSERT INTO info(username, name, address, country, state, city, postal_code, phone)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (username, name, address, country, state, city, postal_code, phone))

    mydb.commit()

except mysql.connector.Error as err:
    print(f"<p>Error: {err}</p>")
    mydb.rollback()

finally:
    cursor.close()
    mydb.close()

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Join</title>
    <style>
        body {{
            color: #ffffff;
            font-size: larger;
            display: flex;
            flex-direction: column;
            font-family: 'Poppins', Arial, Helvetica, sans-serif;
            margin: 0;
            padding: 0;
            min-height: 100vh;
            background-color: #02011a;
            overflow-x: hidden;
        }}
        header {{
            font-family: 'BentonSansCompBlack', sans-serif;
            background-color: #000000;
            color: #fff;
            padding: 20px 0;
            text-align: center;
            box-shadow: 0 4px 8px rgba(16, 92, 130, 0.5);
            font-size: 30px;
        }}
        nav {{
            display: flex;
            justify-content: center;
            background-color: #172b6f;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
            animation: fadeIn 0.5s ease-in-out;
        }}
        nav a {{
            color: #fff;
            padding: 14px 20px;
            text-decoration: none;
            text-align: center;
            transition: background-color 0.3s, transform 0.3s;
        }}
        nav a:hover {{
            background-color: #067573;
            transform: scale(1.1);
        }}
        main {{
            padding: 20px;
            margin: 20px 50px;
            flex: 2;
        }}
        footer {{
            background-color: #333;
            color: #fff;
            padding: 10px 0;
            text-align: center;
            width: 100%;
            bottom: 0;
            position: relative;
        }}
        p {{
            color: #ffffff;
            font-family: "DM Sans", sans-serif;
            font-weight: 300;
            font-style: normal;
            font-size: 20px;
            white-space: pre-wrap;
        }}
        form {{
            font-family: "DM Sans", sans-serif;
            background-color: #0e0335;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
            display: flex;
            flex-direction: column;
            gap: 15px;
            animation: slideUp 3.5s ease-in-out;
        }}
        label {{
            font-size: 18px;
            font-weight: bold;
        }}
        input, select {{
            padding: 10px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
        }}
        button {{
            padding: 10px;
            background-color: #067573;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 18px;
            transition: background-color 0.3s, transform 0.3s;
        }}
        b {{
            font-size:29px;
        }}
        button:hover {{
            background-color: #045a5a;
            transform: scale(1.05);
        }}
        @keyframes slideUp {{
            from {{
                transform: translateY(100px);
                opacity: 0;
            }}
            to {{
                transform: translateY(0);
                opacity: 1;
            }}
        }}
      section {{
            margin-bottom: 40px;
            padding: 20px;
            background: rgba(19, 28, 60, 0.8);
            border-radius: 50px;
            box-shadow: 0 4px 8px rgba(39, 53, 124, 0.5);
            animation: slideUp 3.5s ease-in-out;
            font-family: "DM Sans", sans-serif;
            font-size: 24px;
        }}
    </style>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900&display=swap" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&family=Andika:wght@400&family=Poppins:wght@400&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <img src="./img/marvellogo.png" alt="No Image" height="80px">
    </header>
    <nav>
        <a href="./index.html">Home</a>
        <a href="./characters.html">Characters</a>
        <a href="./shows.html">Shows</a>
        <a href="./join.html">Join Us</a>
        <a href="./contact.html">Contact</a>
        <a href="./about.html">About Us</a>
    </nav>
    <section>
    <h1>Form Submitted!!</h1>
     <ul><br>
    <li><b>Username:</b> {username}</li><br>
    <li><b>Name:</b> {name}</li><br>
    <li><b>Address:</b> {address}</li><br>
    <li><b>Country:</b> {country}</li><br>
    <li><b>State:</b> {state}</li><br>
    <li><b>City:</b> {city}</li><br>
    <li><b>Postal Code:</b> {postal_code}</li><br>
    <li><b>Phone Number:</b> {phone}</li></ul>
    <h2>We will Contact You soon!!</h2>
    </section>
</body>
<footer>
    <p>&copy; 2024 Marvel TV. All rights reserved.</p>
</footer>
</html>
""")
