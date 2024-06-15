# WhatsApp Bulk Messages Without Saving Contacts

It is a python script that sends WhatsApp message automatically from WhatsApp web application without saved contact numbers. It can be configured to send advertising messages to recipients. It read data from an excel sheet and send a configured message to people.

## Important Note
* WhatsApp Business released API on May 2022, no longer needed this repository. You can accomplish your same requirements through WhatsApp Business APIs.

## Prerequisites

In order to run the python script, your system must have the following programs/packages installed and the contact number not need to be saved in your phone (You can use bulk contact number saving procedure of email). It has limitation of sending attachment but you can refer to my another repo which has functionality to send document file like pdf, image, etc.
* Python 3: Download it from https://www.python.org/downloads
* Firefox: Download it from https://www.mozilla.org/en-US/firefox/
* Geckodriver: Download it from https://github.com/mozilla/geckodriver/releases and place geckodriver file in the same folder
* Pandas : Run in command prompt **pip install pandas**
* Xlrd : Run in command prompt **pip install xlrd**
* Selenium: Run in command prompt **pip install selenium** 
* Web Driver: Run in command prompt **pip install webdriver_manager**
* Openpyxl: Run in command prompt **pip install openpyxl**

## Approach
* First need to clone this respiratory
* Run python script script.py using py script.py in the terminal
* The script opens WhatsApp web using firefox.
* User needs to scan QR code from his/her phone.
* Enter in command prompt to execute further.
* The script hit url with contact number and message from excel sheet.
* Once all the message will be sent geckodriver will automatically closed.

## Known Issues/WIP
* Message sending doesn't work, needs user to press button
(used pynput for time being to spam enter button, will fix later)

Note: If you wish to send an image instead of text you can write attachment selection python code.

## Legal
* This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by WhatsApp or any of its affiliates or subsidiaries. This is an independent and unofficial software. Use at your own risk. Commercial use of this code/repo is strictly prohibited.