# Program to send bulk messages through WhatsApp web from an excel sheet without saving Contact numbers
# Original author @inforkgodara

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from time import sleep
import pandas

excel_data = pandas.read_excel('Recipients data.xlsx', sheet_name='Recipients')

count = 0

# Use Firefox instead of Chrome
# Replace '/path/to/geckodriver' with the actual path to your geckodriver executable
service = Service('geckodriver') # Place Geckodriver in same folder 
driver = webdriver.Firefox(service=service)

driver.get('https://web.whatsapp.com')
input("Press ENTER after login into Whatsapp Web and your chats are visible.")

for column in excel_data['Contact'].tolist():
    try:
        url = 'https://web.whatsapp.com/send?phone={}&text={}'.format(excel_data['Contact'][count], excel_data['Message'][count])
        sent = False
        # It tries 3 times to send a message in case if there any error occurred
        driver.get(url)
        try:
            click_btn = WebDriverWait(driver, 35).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[title="{}"]'.format(excel_data['Contact'][count])))
            )
            sleep(2)
            click_btn.click()
            sent = True
            sleep(5)
            print('Message sent to: ', str(excel_data['Contact'][count]))
        except Exception as e:
            print('Failed to send message to ', str(excel_data['Contact'][count]) + str(e))
    except Exception as e:
        print('Failed to send message to ', str(excel_data['Contact'][count]) + str(e))
    count = count + 1

driver.quit()
print("The script executed successfully.")