import time
import pyautogui
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

time.sleep(2)

question = pyautogui.screenshot(region=(30, 80, 1310, 260))

answer1 = pyautogui.screenshot(region=(30, 355, 310, 375)).convert('L')
answer2 = pyautogui.screenshot(region=(363, 355, 310, 375)).convert('L')
answer3 = pyautogui.screenshot(region=(696, 355, 310, 375)).convert('L')
answer4 = pyautogui.screenshot(region=(1029, 355, 310, 375)).convert('L')
print("Screenshot tooked")

que_text = pytesseract.image_to_string(question, lang='rus')
ans1_text = pytesseract.image_to_string(answer1, lang='rus')
ans2_text = pytesseract.image_to_string(answer2, lang='rus')
ans3_text = pytesseract.image_to_string(answer3, lang='rus')
ans4_text = pytesseract.image_to_string(answer4, lang='rus')
print("Text identifieled")

### 2 ###

driver_path = '/mnt/python/image/geckodriver'
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get('https://www.bing.com/chat?q=Microsoft+Copilot&FORM=hpcodx')
input_box = driver.find_element(By.XPATH, '//*[@id="input"]')
input_box.send_keys(f"Вот вопрос: {que_text}. Вот варианты ответа {ans1_text}, {ans2_text}, {ans3_text}, {ans4_text}."
f" Дай исключительно вариант ответа и ничего более")
input_box.send_keys(Keys.RETURN)

time.sleep(5)

results = driver.find_element(By.XPATH, '//*[@id="response"]').text

if results == ans1_text:
    pyautogui.doubleClick(30, 355)
elif results == ans2_text:
    pyautogui.doubleClick(363, 355)
elif results == ans3_text:
    pyautogui.doubleClick(696, 355)
elif results == ans4_text:
    pyautogui.doubleClick(1029, 355)
else:
    print("Don't have right answer.")
    quit()

