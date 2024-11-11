# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:41:34 2022

@author: Savage33

Instagram automation for login and search functionality using Selenium
"""
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import warnings
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Suppress warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def setup_driver():
    """Sets up and returns the Chrome WebDriver."""
    chrome_options = Options()
    # You can add any additional Chrome options here if needed
    prefs = {"excludeSwitches": ["enable-automation"],
             'credentials_enable_service': False,
             'profile.password_manager_enabled': False,
             'useAutomationExtension': False}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver

def login_instagram(driver, username, password):
    """Logs into Instagram using the provided username and password."""
    driver.get("https://www.instagram.com/")
    time.sleep(3)

    # Locate the username, password fields, and login button
    Element_KullaniciAdi = driver.find_element(By.XPATH, "//input[@name='username']")
    Element_Sifre = driver.find_element(By.XPATH, "//input[@name='password']")
    Element_ButtonGiris = driver.find_element(By.XPATH, "//button[@type='submit']")

    Element_KullaniciAdi.send_keys(username)
    Element_Sifre.send_keys(password)
    Element_ButtonGiris.click()
    time.sleep(5)

def handle_notifications(driver):
    """Handles pop-up notifications if they appear after login."""
    try:
        Element_ButtonBilgiKayit = driver.find_element(By.XPATH, "//div[@class='_ac8f']")
        Element_ButtonBilgiKayit.click()
        time.sleep(1)
        Element_ButtonBildirim = driver.find_element(By.XPATH, "//button[@class='_a9-- _a9_1']")
        Element_ButtonBildirim.click()
    except:
        print("No notification pop-up appeared.")
    time.sleep(3)

def go_to_explorer_page(driver):
    """Navigates to the Explorer page."""
    try:
        Element_ButtonexplorerSayfasi = driver.find_elements(By.XPATH, "//div[@class='_acut']")
        Element_ButtonexplorerSayfasi[3].click()
    except:
        print("Could not click the explorer button.")
    time.sleep(5)

def search_topic(driver, topic):
    """Searches for a specific topic on Instagram."""
    try:
        # Locate and click the search button
        Element_AramaKutusu = driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Ara"]')
        ActionChains(driver).move_to_element(Element_AramaKutusu).click().perform()
        time.sleep(1)

        # Input search text
        Element_AramaKutusutextgirisi = driver.find_element(By.XPATH, "//input[@aria-label='Arama Girdisi']")
        Element_AramaKutusutextgirisi.send_keys(topic)
        time.sleep(1)

        # Return a list of search results
        Eliement_KonuElemanlariListesi = driver.find_elements(By.XPATH, "//div[@class='_abm4']")
        return Eliement_KonuElemanlariListesi
    except:
        print("Could not interact with the search bar.")
        return []

def main():
    """Main function to run the Instagram automation."""
    # It's recommended to load sensitive information like username and password from environment variables
    username = "savage331"  # Replace with your Instagram username or load from environment
    password = "Parolasavage33."  # Replace with your Instagram password or load from environment

    driver = setup_driver()

    login_instagram(driver, username, password)
    handle_notifications(driver)
    go_to_explorer_page(driver)
    
    # Search for a topic
    search_results = search_topic(driver, "gsb mersin")
    if search_results:
        print(f"Found {len(search_results)} results for 'gsb mersin'.")
    else:
        print("No results found.")

    driver.quit()

if __name__ == "__main__":
    main()
