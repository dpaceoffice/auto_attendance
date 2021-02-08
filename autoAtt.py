"""
Author David Pace

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
