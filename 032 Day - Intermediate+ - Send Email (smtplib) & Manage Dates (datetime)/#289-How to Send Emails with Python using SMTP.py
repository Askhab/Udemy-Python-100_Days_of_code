import smtplib

my_email = "asmag86@gmail.com"
password = "hlodjwfuwbsbbrsu"

receiver_email = "asmag86@mail.ru"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=receiver_email,
        msg="Subject:Another SMTP email \n\nHello, this is testing email for SMTP sendings."
    )
