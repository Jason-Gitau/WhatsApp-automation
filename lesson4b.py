# Send a WhatsApp message using Python
# #
# # The pywhatkit library allows you to send WhatsApp messages using Python.
# #
# # To send a WhatsApp message, you can use the sendwhatmsg() function.
# #
# # The sendwhatmsg() function takes four arguments:
# #
# # sendwhatmsg() function requires 2 mins to send the message to allow the web.whatsapp.com to load
# # The receiver's phone number
# # The message to send
# # The hour to send the message
# # The minute to send the message
# # Here's an example of how to send a WhatsApp message using Python:
import pywhatkit as kit
import datetime

receiver = "+254791774217"

message = "Hello, this is a test message from Python"

now=datetime.datetime.now()
send_hour=now.hour
send_minute=now.minute+2

kit.sendwhatmsg(receiver,message,send_hour,send_minute)
print("Message sent successfully")