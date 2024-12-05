import time
import pytz
import schedule
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from threading import Thread

app = Flask(__name__)

# Global variable to store friends
friends = []

# Path to your ChromeDriver
CHROMEDRIVER_PATH = "/path/to/chromedriver"

# Initialize WebDriver (Selenium)
driver = None

# List of timezones for the dropdown
TIMEZONES = [
    "Asia/Kolkata", "America/New_York", "Europe/London", "Europe/Paris",
    "Asia/Tokyo", "Australia/Sydney", "America/Los_Angeles", "Africa/Johannesburg"
]

# List of mobile code prefixes for different countries
COUNTRY_CODES = [
    ("+1", "United States"), ("+44", "United Kingdom"), ("+91", "India"),
    ("+61", "Australia"), ("+81", "Japan"), ("+33", "France"), ("+49", "Germany")
]

# Function to send WhatsApp message using Selenium
def send_whatsapp_message(phone_number, message):
    global driver
    # Open WhatsApp Web (in incognito mode to avoid caching issues)
    if driver is None:
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
        driver.get("https://web.whatsapp.com/")
        print("Scan the QR code to login.")
        time.sleep(15)  # Wait for QR scan

    # Locate the chat based on the phone number and send a message
    try:
        # Search for the contact using phone number
        search_box = driver.find_element(By.XPATH, '//*[@title="Search input textbox"]')
        search_box.clear()
        search_box.send_keys(phone_number)
        time.sleep(2)  # Wait for the search to complete

        # Click on the contact to open the chat
        contact = driver.find_element(By.XPATH, f'//span[@title="{phone_number}"]')
        contact.click()

        # Type the message
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
        message_box.send_keys(message + Keys.ENTER)
        print(f"Sent message to {phone_number}")
    except Exception as e:
        print(f"Error sending message to {phone_number}: {e}")

# Function to schedule the birthday wish
def schedule_birthday_wish(friend):
    birthday_datetime = friend['birthday']
    timezone = pytz.timezone(friend['timezone'])
    birthday_datetime = timezone.localize(birthday_datetime)  # Localize to the user's timezone

    # If the scheduled time is 00:00, send the wish exactly at midnight
    if friend['when_to_wish'] == "00:00":
        wish_time = birthday_datetime.replace(hour=0, minute=0, second=0)
    else:
        # Parse the custom time and set it
        wish_time = datetime.strptime(friend['birthday'].strftime('%Y-%m-%d') + ' ' + friend['when_to_wish'], '%Y-%m-%d %H:%M')
        wish_time = timezone.localize(wish_time)

    # Scheduling the task
    schedule.every().day.at(wish_time.strftime('%H:%M')).do(send_whatsapp_message, phone_number=friend['phone_number'], message=f"Happy Birthday {friend['name']}!")

# Route to add a friend to the schedule
@app.route('/add_friend', methods=['GET', 'POST'])
def add_friend():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        phone_number = request.form['phone_number']
        country_code = request.form['country_code']
        birthday = request.form['birthday']
        when_to_wish = request.form['when_to_wish']
        timezone = request.form['timezone']

        # Combine the country code with phone number
        full_phone_number = country_code + phone_number

        # Parse the birthday into datetime object
        birthday = datetime.strptime(birthday, '%Y-%m-%d')

        # Store friend information
        friend = {
            'name': name,
            'phone_number': full_phone_number,
            'birthday': birthday,
            'when_to_wish': when_to_wish,
            'timezone': timezone
        }

        friends.append(friend)
        
        # Schedule birthday wish
        schedule_birthday_wish(friend)

        return redirect(url_for('index'))

    return render_template('add_friend.html', timezones=TIMEZONES, country_codes=COUNTRY_CODES)

# Home route to show the list of friends
@app.route('/')
def index():
    return render_template('index.html', friends=friends)

# Function to run the scheduler in a separate thread
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Route to test sending a message
@app.route('/send_test', methods=['POST'])
def send_test():
    phone_number = request.form['phone_number']
    message = request.form['message']
    send_whatsapp_message(phone_number, message)
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Start the scheduler in a separate thread
    scheduler_thread = Thread(target=run_scheduler)
    scheduler_thread.start()

    # Run the Flask app
    app.run(debug=True)
