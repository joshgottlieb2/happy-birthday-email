import datetime as dt
import pandas
import random
import smtplib

my_email = "pythontesting246@gmail.com"
password = "Y6383*ZtT"

today = (dt.datetime.now().month, dt.datetime.now().day)

# Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")

# Use dictionary comprehension
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}


# compare and see if today's month/day tuple matches one of the keys in birthday_dict
# If there is a match, pick random letter from letter_templates and replace the [NAME] with actual name

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    letter_number = random.randint(1,3)
    with open(f"letter_templates/letter_{letter_number}.txt") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

# Send the letter to that person's email address.

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person['email'],
            msg=f"Subject: Happy Birthday!\n\n{contents}")


