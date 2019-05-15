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
    browser.get('https://swapi.co/')


@when('I click on the link documetation')
def step_impl(context):
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get('https://swapi.co/documentation')