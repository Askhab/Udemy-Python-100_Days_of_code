import smtplib
import datetime as dt
from random import choice

my_email = "asmag86@gmail.com"
password = "hlodjwfuwbsbbrsu"
receiver_email = "asmag86@mail.ru"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt", mode="r") as quotes:
        data = quotes.readlines()
        quote = choice(data)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver_email,
            msg=f"Subject:Motivational quote!\n\n{quote}"
        )
