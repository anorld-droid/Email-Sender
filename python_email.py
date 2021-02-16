import smtplib
import socket
import sys


def check_network_connection():
    """Returns True if there is no internet connection,false otherwise"""
    try:
        socket.gethostbyname("www.gmail.com")
        return False
    except:
        return True


def send_email(myemail, password):
    emailObj = smtplib.SMTP("smtp.gmail.com", 587)
    emailObj.ehlo()
    emailObj.starttls()
    try:
        emailObj.login(myemail, password)
    except Exception as err:
        print(err, "incorrect password")
    toemail = input("Enter recipients email: ")
    message = input("Enter the message: ")
    emailObj.sendmail(myemail, toemail, message)


if __name__ == "__main__":

    if check_network_connection():
        print("Check your internet connection then try again.")
        sys.exit(1)
    myemail = input("Enter your email: ")
    password = input("Enter the password: ")
    send_email(myemail, password)
