import time
import pyautogui
import webbrowser

def click_button(x, y):
	pyautogui.click(x, y)
	pyautogui.mouseDown()
	pyautogui.mouseUp()
 
def half_sec():
	time.sleep(.5)

# Remove cookies
def clean_cookies():
	webbrowser.open("https://google.com")
	time.sleep(3)
	pyautogui.click(1661, 72)  # to settings
	half_sec()
	pyautogui.moveTo(1481, 236)  # history hover
	half_sec()
	pyautogui.click(1264, 236)  # click history
	time.sleep(6)
	pyautogui.click(88, 388)  # click delete
	time.sleep(10)
	pyautogui.click(868, 398)  # click drop for time
	time.sleep(3)
	pyautogui.click(712, 515)  # select alltime
	time.sleep(3)
	pyautogui.click(1125, 860)  # delete cookies


if __name__=='__main__':
	clean_cookies()