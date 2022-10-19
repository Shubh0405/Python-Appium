from pytest_bdd import *
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

scenarios("../Features/CheckAllCategories.feature")
scenarios("../Features/SearchBox.feature")

@given(u'Flipkart app opens')
def LaunchFlipkartApp(context):
    desired_cap = {
        "deviceName": "RZCT609NGNJ",
        "platformName": "Android",
        "appium:uiautomator2ServerInstallTimeout": "90000",
        "appium:appPackage": "com.flipkart.android",
        "appium:appActivity": ".SplashActivity"
    }

    context.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cap)
    context.driver.implicitly_wait(30)

@given(u'English Language Selected')
def SelectEnglishLanguage(context):
    context.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageView[1]").click()

    context.driver.find_element(AppiumBy.ID, "com.flipkart.android:id/select_btn").click()


@given(u'login flow skipped')
def SkipLoginFlow(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.google.android.gms:id/cancel")))
    context.driver.find_element(AppiumBy.ID, "com.google.android.gms:id/cancel").click()

    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.flipkart.android:id/custom_back_icon")))

    context.driver.find_element(AppiumBy.ID, "com.flipkart.android:id/custom_back_icon").click()


@when(u'category page opens')
def OpenCategoryPage(context):
    context.driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]").click()


@then(u'Verify all categories text')
def VerifyAllCategroiesText(context):
    category_header = context.driver.find_element(AppiumBy.ID, "com.flipkart.android:id/title_action_bar")
    print(category_header.text == "All Categories")

@then(u'Click on the seach icon and enter text iphone')
def SearchIphone(context):

    context.driver.find_element(AppiumBy.ID, "com.flipkart.android:id/search_icon").click()

    # WebDriverWait(context.driver, 10).until(
    #     EC.presence_of_element_located((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.EditText")))
    search_phone = context.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.EditText")
    search_phone.send_keys("iphone")

@then(u'close app')
def CloseApp(context):
    context.driver.quit()
