import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize(("name", "email", "subject", "message"),
                         [
                             ("Alla", "alla@gmail.com", "Demo Submission", "I want to submit by music to your label!"),
                             ("Alina", "alina@yahoo.com", "Test Test", "I don't want to write a message")
                         ])
@pytest.mark.alhymrecordstest
def test_alhymrec_contact(browser_chrome, name, email, subject, message):
    browser_chrome.get("https://fyl.vqr.mybluehost.me/")
    contact_link = WebDriverWait(browser_chrome, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "CONTACT")))
    contact_link.click()
    page_title = WebDriverWait(browser_chrome, 10).until(EC.title_contains("Contact"))
    name_field = WebDriverWait(browser_chrome, 10).until(EC.element_to_be_clickable((By.NAME, "your-name")))
    name_field.send_keys(name)
    browser_chrome.find_element(By.NAME, "your-email").send_keys(email)

    browser_chrome.find_element(By.NAME, "your-subject").send_keys(subject)
    browser_chrome.find_element(By.NAME, "your-message").send_keys(message)