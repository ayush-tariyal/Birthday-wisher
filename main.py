import pandas
import random
import smtplib
import datetime as dt

data = pandas.read_csv("birthdays.csv")

birthday_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}

today = dt.datetime.now()
today_tuple = (today.month, today.day)

birthday_person = birthday_dict[today_tuple]

MY_EMAIL = "pythontocode007@gmail.com"
MY_PASSWORD = "hgqxfobrxieqydpu"
RECEIVER_EMAIL = birthday_person["email"]

with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt", "r") as letters:
    letter = letters.read()

birthday_letter = letter.replace("[NAME]", birthday_person["name"])


if today_tuple in birthday_dict:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f"Subject:Happy Birthday!!\n\n{birthday_letter}",
        )
