import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

url = "https://dilutiontracker.com/login"
driver.get(url)


email = driver.find_element('xpath', '//*[@id="email"]')
email.send_keys("desitrader2020@gmail.com")

password = driver.find_element('xpath', '//*[@id="password"]')
password.send_keys("Test12345")

submit_button = driver.find_element(
    'xpath', '//*[@id="form_wrapper__login"]/form/button')

submit_button.click()

time.sleep(2)
print("logged in")


def get_dilution_data(ticker):
    print("getting dilution data for "+ticker)
    ticker_url = "https://dilutiontracker.com/app/search/"+ticker
    driver.get(ticker_url)

    time.sleep(7)
    try:
        cash_need = driver.find_element(
            "xpath", '//*[@id="dashContentWrapper"]/div[2]/div[5]/span[2]')
        cash_need = cash_need.text
    except:
        cash_need = None
    try:
        dt_overall_risk = driver.find_element(
            "xpath", '//*[@id="dashContentWrapper"]/div[2]/div[1]/span[2]')
        dt_overall_risk = dt_overall_risk.text
    except:
        dt_overall_risk = None

    try:
        dt_offering_ability = driver.find_element(
            "xpath", '//*[@id="dashContentWrapper"]/div[2]/div[2]/span[2]')
        dt_offering_ability = dt_offering_ability.text
    except:
        dt_offering_ability = None
    try:
        dt_amount_exceeding_shelf = driver.find_element(
            "xpath", '//*[@id="dashContentWrapper"]/div[2]/div[3]/span[2]')
        dt_amount_exceeding_shelf = dt_amount_exceeding_shelf.text
    except:
        dt_amount_exceeding_shelf = None
    try:
        dt_historical = driver.find_element(
            "xpath", '//*[@id="dashContentWrapper"]/div[2]/div[4]/span[2]')
        dt_historical = dt_historical.text
    except:
        dt_historical = None
    cash_in_hand = None
    try:
        cash_in_hand = driver.find_element(
            "xpath", '//*[@id="dashContentWrapper"]/p[3]/strong[1]')
        if "months" not in cash_in_hand.text:
            cash_in_hand = None
    except:
        pass

    if not cash_in_hand:  # cash in hand is None
        try:
            cash_in_hand = driver.find_element(
                "xpath", '//*[@id="dashContentWrapper"]/p[4]/strong[1]')
            if "months" not in cash_in_hand.text:
                cash_in_hand = None
        except:
            pass

    if cash_in_hand and cash_in_hand.text:
        cash_in_hand = cash_in_hand.text.replace("months", "").strip()
    return cash_in_hand, cash_need, dt_overall_risk, dt_offering_ability, dt_amount_exceeding_shelf, dt_historical
