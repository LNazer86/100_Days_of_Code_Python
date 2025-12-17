import datetime as dt
import pandas as pd
import random
import smtplib
from email.mime.text import MIMEText

now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)
random_letter = random.randint(1, 3)

data = pd.read_csv("birthdays.csv")

birth_dict = {(row["month"], row["day"]): (row["name"], row["email"], row["year"]) for (index, row) in data.iterrows()}

if today in birth_dict:
    person = birth_dict[today]
    name = person[0]
    email = person[1]

    with open(f"letter_templates/letter_{random_letter}.txt") as letter:
        letter_text = letter.read()
    personalized_letter = letter_text.replace("[NAME]", name)

    msg = MIMEText(personalized_letter, "plain", "utf-8")
    msg["Subject"] = "Birth Wish"
    msg["From"] = "email"
    msg["To"] = email

    with smtplib.SMTP("smtp.seznam.cz", 587) as connection:
        connection.starttls()
        connection.login(user="email", password="password")
        connection.send_message(msg)