from behave import *
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')

use_step_matcher('re') #Nos permite recibir parametros de los Escenarios del archivo .feature

@given('I am on the homepage')
def step_impl(contex):
    #browser = webdriver.Chrome() Normal
    #browser = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=chrome_options)
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get('http://127.0.0.1:5000')


@when('I click on the link with id "(.*)"')
def step_impl(context, link_id):
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get('http://127.0.0.1:5000')
    link = browser.find_element_by_id(link_id)
    link.click()
