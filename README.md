    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install Flask

    pip freeze > requirements.txt
    pip install -r requirements.txt

    To Run: python app.py

v1.1:
    create a flask python app to wish birthday to my friends using whatsapp. Also create a ui to enter friends phone number, name, birthday, when_to_wish with default value as 00:00 and timezone with default timezone to IST. Using Selenium
    
        pip install selenium

v1.2: The time zones should be available as drop down.
mobile code prefix also should be changable.
also add a test button to send message now.

v1.3: Use sql alchemy and give option to edit friends entry

v1.x: Using Twilio
