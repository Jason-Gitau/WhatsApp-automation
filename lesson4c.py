# Description: This script sends messages to multiple contacts using the pywhatkit library
# 
# The script reads the contacts from a CSV file and sends a message to each contact.
#
# The script reads the contacts from a CSV file and sends a message to each contact.

# Import the required libraries

# import the pywhatkit library to send WhatsApp messages
import pywhatkit
# import the pandas library to read the CSV file
import pandas as pd
# import the time module to add a delay between messages
import time 

# Read the data from the CSV file
data = pd.read_csv("contacts.csv")

# Loop through the data and send messages to each contact
for index, row  in data.iterrows():
    # Extract the receiver's phone number and message from the row
    try:
        receiver = str(row["phone"]).strip()
        # Check if the phone number starts with a "+"
        if not receiver.startswith("+"):
            # Add the country code if it is missing
            receiver = "+254" + receiver 

        # meassage to be sent
        message = str(row["message"])

        # Send the message to the receiver
        pywhatkit.sendwhatmsg_instantly(receiver, message)

        # Print a success message
        print(f"Message sent successfully to {receiver}")

        # Add a delay of 60 seconds between messages
        time.sleep(60)

    # Handle any errors that occur during the process
    except Exception as e:
        print(f"Error: {e}")


        