from behave import *
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')

use_step_matcher('re') #Nos permite recibir parametros de los Escenarios del archivo .feature

@given('I am on the homepage')
def step_impl(contex):
    #browser = webdriver.Chrome() Normal
    browser = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=chrome_options)
    browser.get('https://www.google.com/')
