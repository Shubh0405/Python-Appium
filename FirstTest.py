from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



desired_cap = {
  "deviceName": "RZCT609NGNJ",
  "platformName": "Android",
  "appium:uiautomator2ServerInstallTimeout": "90000",
  "appium:appPackage": "com.flipkart.android",
  "appium:appActivity": ".SplashActivity"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cap)
driver.implicitly_wait(30)


driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageView[1]").click()

driver.find_element(AppiumBy.ID, "com.flipkart.android:id/select_btn").click()

driver.find_element(AppiumBy.ID, "com.google.android.gms:id/cancel").click()

driver.find_element(AppiumBy.ID, "com.flipkart.android:id/custom_back_icon").click()

driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]").click()


category_header = driver.find_element(AppiumBy.ID, "com.flipkart.android:id/title_action_bar")
print(category_header.text == "All Categories")

driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.ImageView").click()

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, "search_icon")))

driver.find_element(AppiumBy.ID, "com.flipkart.android:id/search_icon").click()

search_phone = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.EditText")
search_phone.send_keys("iphone")

driver.quit()