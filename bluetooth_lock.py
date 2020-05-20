from public.common.desired_caps import desired
from public.po.login_page import LoginPage
from selenium.webdriver.common.by import By
from time import sleep

driver = desired()
Login = LoginPage(driver)
Login.login()


unlock_text = driver.wait_find_element(By.XPATH, "//*[@text='立即开锁']")

unlock_count_num = 3
succ_num = 0
for t in range(unlock_count_num):
    try:
        unlock_text.click()
        sleep(15)
        succ_num += 1
        print(succ_num)
    except:
        confirm_btn_text = driver.wait_find_element(By.XPATH, "//*[@text='确定']")
        confirm_btn_text.click()
        unlock_text.click()
        sleep(15)

succ ='%.2f%%' % (succ_num / unlock_count_num)
print(succ)






