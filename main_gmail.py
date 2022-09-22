from simplegmail import Gmail
import email_template as E

place_holder_text = 'preheader text'

def sendMail(gmail):
    new_template = E.text_replace("Hello Sir,", "I will develop a new Website & customize your Website as you want.", "I will rank your Website on the 1st page of Google and you will be getting more calls")
    print(new_template)
    params = {
    "to": "uttorpurus@gmail.com",
    "sender": "mislam162013@bscse.uiu.ac.bd",
    "subject": "Test Mail",
    "msg_html": F"{new_template}",
    "msg_plain": "Hi\nThis is a plain text email.",
    "signature": False  # use my account signature
    }
    message = gmail.send_message(**params)  # equivalent to send_message(to="you@youremail.com", sender=...)


def receiveMail(gmail):
    # Unread messages in your inbox
    messages = gmail.get_unread_inbox()

    # Starred messages
    messages = gmail.get_starred_messages()

    # ...and many more easy to use functions can be found in gmail.py!

    # Print them out!
    for message in messages:
        print("To: " + message.recipient)
        print("From: " + message.sender)
        print("Subject: " + message.subject)
        print("Date: " + message.date)
        print("Preview: " + message.snippet)
        
        print("Message Body: " + message.plain)  # or message.html


gmail = Gmail() # will open a browser window to ask you to log in and authenticate

#receiveMail(gmail)
sendMail(gmail)















