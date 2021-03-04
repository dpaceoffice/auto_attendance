"""

Purpose:
This script is designed to automatically take roll on moodle for software engineering, and start zoom after. 
The configuations must be set below or adjusted to your system to properly work. I.E timeout may need to be extended for slower internet, or lowered for faster internet
The driver must also be set to use the broswer installed on your system. This script has yet to go through rigourus testing so if any bugs may be encounted please report those.  

"""

import time
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#############################CONFIGURATIONS##############################
#Moodle email
email = ''

#Moodle password
password = ''

#Enable to launch zoom after processing attendence
using_zoom = True

#Time pages are allowed to load in seconds
timeout = 10

#Use the correct browser driver
driver = webdriver.Firefox(executable_path='drivers\geckodriver.exe')
#driver = webdriver.Chrome(executable_path='drivers\geckodriver.exe')
#driver = webdriver.Ie(executable_path='drivers\geckodriver.exe')

#########################################################################

#Waits 10 seconds for page to load before timing out, may need to be longer for slower internet
driver.implicitly_wait(timeout)

def checkInfo():
    if(email == '' or password == ''):
        return False
    return True

def init():
    driver.get('https://moodle.uno.edu/mod/attendance/view.php?id=1283452')
    sign_box = driver.find_element_by_link_text('UNO Sign In')
    sign_box.click()

def log_email(username):
    email_field = driver.find_element_by_id('i0116')
    email_field.send_keys(''+username+'' + Keys.RETURN)

def log_pass(password):
    password_field = driver.find_element_by_id('i0118')
    signIn_button = driver.find_element_by_id('idSIButton9')
    password_field.send_keys(''+password)
    signIn_button.click()

def att_gateway():
    try:
        att_button = driver.find_element_by_partial_link_text('Submit attendance')
        att_button.location_once_scrolled_into_view
        att_button.click()
    except NoSuchElementException:
        print('Attendance not avaliable or the username/password may be wrong')
        print('Closing in 5 seconds...')
        driver.quit()
        time.sleep(5)
        sys.exit()

def mark_attendence():
    present_button = driver.find_element_by_id('id_status_9601')
    save_button = driver.find_element_by_id('id_submitbutton')
    present_button.click()
    save_button.click()

def startup(username, password):
    init()
    log_email(username)
    time.sleep(2)#necessary
    log_pass(password)
    att_gateway()
    mark_attendence()
    return True

#Python cant automatically start the application through the browser for obvious reasons
def start_zoom():
    driver.get('https://uno.zoom.us/j/86818604192?pwd=c3FpSXR6a3FPSENKVTUyNFdSWmFsUT09#success')
    #driver.get('https://uno.zoom.us/j/86818604192?pwd=c3FpSXR6a3FPSENKVTUyNFdSWmFsUT09')
    launch_meeting = driver.find_element_by_class_name('_1FvRrPS6')
    launch_meeting.click()

def main():
    if(startup(email, password)):
        print('Sign in successful.')
    if(using_zoom):
        start_zoom()
        print('Zoom started - script will automatically self-destruct in 15 seconds.')
        time.sleep(15)
    driver.quit()
    sys.exit

if(__name__ == "__main__"):
    if(checkInfo() == False):
        print('Moodle email and password must be configured to run this script directly.')
        print('Closing in 5 seconds...')
        driver.close()
        time.sleep(5)
        sys.exit
    else:
        main()
