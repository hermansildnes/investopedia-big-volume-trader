from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from getpass import getpass
import chromedriver_binary
import time


def load(url):
    options = webdriver.ChromeOptions()
    options.binary_location = (
        r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    )
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(10)

    driver.get(url)
    return driver


def login(driver, username, password):
    ufield = driver.find_element_by_name("username")
    pfield = driver.find_element_by_name("password")
    login = driver.find_element_by_name("login")

    ufield.clear()
    pfield.clear()

    ufield.send_keys(username)
    time.sleep(0.5)

    pfield.send_keys(password)
    time.sleep(0.5)

    login.click()


def buy(driver, ticker, quantity, trade_url):
    driver.get(trade_url)
    symbolfield = driver.find_element_by_name("symbolTextbox")
    symbolfield.send_keys(ticker)
    time.sleep(0.5)
    quantityfield = driver.find_element_by_name("quantityTextbox")
    quantityfield.send_keys(quantity)
    time.sleep(0.5)
    confirm = driver.find_element_by_id("sendConfirmationEmailCheckBox")
    confirm.click()
    time.sleep(0.5)
    previewButton = driver.find_element_by_id("previewButton")
    previewButton.click()
    time.sleep(1)
    submit = driver.find_element_by_name("submitOrder")
    submit.click()
    time.sleep(1)


def sell(driver, ticker, quantity, trade_url):
    driver.get(trade_url)
    symbolfield = driver.find_element_by_name("symbolTextbox")
    symbolfield.send_keys(ticker)
    time.sleep(0.5)
    select = Select(driver.find_element_by_name("transactionTypeDropDown"))
    time.sleep(0.5)
    select.select_by_visible_text("Sell")
    time.sleep(0.5)
    quantityfield = driver.find_element_by_name("quantityTextbox")
    quantityfield.send_keys(quantity)
    time.sleep(0.5)
    confirm = driver.find_element_by_id("sendConfirmationEmailCheckBox")
    confirm.click()
    time.sleep(0.5)
    previewButton = driver.find_element_by_id("previewButton")
    previewButton.click()
    time.sleep(1)
    submit = driver.find_element_by_name("submitOrder")
    submit.click()
    time.sleep(1)


def sellall(driver, ticker, trade_url):
    tosell = int(input("Stocks to sell: "))

    while True:
        if tosell > 999999:
            tempsell = 999999
        else:
            tempsell = tosell
        driver.get(trade_url)
        symbolfield = driver.find_element_by_name("symbolTextbox")
        symbolfield.send_keys(ticker)
        time.sleep(0.5)
        select = Select(driver.find_element_by_name("transactionTypeDropDown"))
        time.sleep(0.5)
        select.select_by_visible_text("Sell")
        time.sleep(0.5)
        quantityfield = driver.find_element_by_name("quantityTextbox")
        quantityfield.send_keys(tempsell)
        time.sleep(0.5)
        confirm = driver.find_element_by_id("sendConfirmationEmailCheckBox")
        confirm.click()
        time.sleep(0.5)
        previewButton = driver.find_element_by_id("previewButton")
        previewButton.click()
        time.sleep(1)
        submit = driver.find_element_by_name("submitOrder")
        submit.click()
        time.sleep(1)
        tosell -= tempsell
        if tosell <= 0:
            break


URL = "https://www.investopedia.com/auth/realms/investopedia/protocol/openid-connect/auth?response_type=code&approval_prompt=auto&redirect_uri=https%3A%2F%2Fwww.investopedia.com%2Fsimulator%2Fhome.aspx&client_id=inv-simulator-conf"
TRADE_URL = "https://www.investopedia.com/simulator/trade/tradestock.aspx"
PORTFOLIO_URL = "https://www.investopedia.com/simulator/portfolio/"
USERNAME = input("Username: ")
PASSWORD = getpass()
TICKER = input("Ticker: ")
ACTION = input("Buy/Sell/Sell all: ")
if ACTION.upper() != "SELL ALL":
    QUANTITY = input("Quantity: ")
    AMOUNT = input("Amount of times to run: ")


driver = load(URL)
time.sleep(3)
login(driver, USERNAME, PASSWORD)
time.sleep(5)

if ACTION.upper() == "BUY":
    for i in range(int(AMOUNT)):
        buy(driver, TICKER, QUANTITY, TRADE_URL)

elif ACTION.upper() == "SELL":
    for i in range(int(AMOUNT)):
        sell(driver, TICKER, QUANTITY, TRADE_URL)

elif ACTION.upper() == "SELL ALL":
    sellall(driver, TICKER, TRADE_URL)

else:
    driver.quit()
    raise Exception("Illegal action submitted! Try again...")
