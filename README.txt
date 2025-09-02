Set Up Instructions for Legal and General Desk Booking System:

    1) Set up the Virtual Environment in the terminal one after another:
        a) python3 -m venv venv
        b) Set-ExecutionPolicy Unrestricted -Scope Process this maybe needed to bypass security restrictions
        c) source venv/bin/activate or venv\Scripts\activate (Windows)

    2) Install Dependencies from the requirements.txt file which downloads everything the application needs:
        a) pip3 install -r requirements.txt

    3) Start the Database = db.sqlite:
        a) Python3 run.py

    4) A link will come up in this sort of format with a HTTPS and some numbers, you can either copy and paste it into a web browser
        or you can command + click on the link in the terminal

    5) You will then be taken to the dashboard where you need to register your username, email, and password.
        or you can log into the admin dashboard which has the login details of Username: admin Password: AdminPass123!

    6) Once you login you will be able to create new bookings. As admin you can cancel or amend other users bookings as it has full access

    7) Once the booking is made you will then be able to edit to change the date, location, floor, or desk. Once you do this the booking
        is then booked out and no one else is able to book with the exact same details 

    8) If you don't want to do any of that you can cancel the booking. 

    9) You can flick through different dashboards with the navigation bar at the top of the website.
