# WhatsApp Message Sender - Documentation

## Overview
This script automates sending WhatsApp messages to multiple contacts using the `pywhatkit` library. It reads contact details from a CSV file and sends a specified message to each recipient. A delay is added between messages to prevent rate limits.

## Dependencies
Ensure you have the required libraries installed:
```sh
pip install pywhatkit pandas
```

The script imports the following modules:
```python
import pywhatkit  # For sending WhatsApp messages
import pandas as pd  # For reading the CSV file
import time  # For adding delays between messages
```

## Data Input
- The script reads a CSV file (`contacts.csv`) containing contact details.
- Expected CSV format:
  ```csv
  phone,message
  712345678,Hello, how are you?
  798765432,Good morning!
  ```
- The `phone` column should contain recipient numbers (with or without a country code).
- The `message` column should contain the message to be sent.

## Functionality
1. **Reading Data**
   ```python
   data = pd.read_csv("contacts.csv")
   ```
   - Reads the contact list from the CSV file.
   
2. **Processing and Sending Messages**
   ```python
   for index, row in data.iterrows():
       try:
           receiver = str(row["phone"]).strip()
           if not receiver.startswith("+"):
               receiver = "+254" + receiver  # Adds the country code if missing
           message = str(row["message"])
           pywhatkit.sendwhatmsg_instantly(receiver, message)
           print(f"Message sent successfully to {receiver}")
           time.sleep(60)  # Adds a delay of 60 seconds
       except Exception as e:
           print(f"Error: {e}")
   ```
   - Iterates through each contact.
   - Ensures the phone number has the correct format.
   - Sends the message using `pywhatkit.sendwhatmsg_instantly()`.
   - Waits 60 seconds before sending the next message.

## Issues and Recommendations
1. **Phone Number Format:** Ensure the `phone` column contains valid numbers. Missing country codes are automatically prefixed with `+254`.
2. **Rate Limiting:** A 60-second delay is added to prevent spam detection.
3. **Error Handling:** Errors are caught and printed instead of stopping execution.
4. **File Path:** Ensure `contacts.csv` is in the correct directory or provide an absolute path.

## Usage
1. **Prepare the CSV File** with valid phone numbers and messages.
2. **Run the Script**
   ```sh
   python whatsapp_message_sender.py
   ```
3. **Monitor the Output** to ensure messages are sent successfully.

This script simplifies bulk messaging via WhatsApp, automating the process efficiently. 🚀

