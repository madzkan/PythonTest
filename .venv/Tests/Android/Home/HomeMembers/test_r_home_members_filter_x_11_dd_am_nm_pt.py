import time

from selenium.webdriver.common.by import By

from appium import webdriver
from Tests.Android.Login.login_admin import login_admin_loop
from src.testproject.decorator import report_assertion_errors
from addons.swipe_and_find_element import SwipeAndFindElement
import pytest
import allure


def test_home_members_filter_1(driver):

    driver.reset()
    time.sleep(20)

    login_admin_loop(driver)

    # 1. Swipe 'Up' to 'Groups - Home'
    # groups_home = (
    #     By.XPATH, "//android.view.ViewGroup/android.widget.TextView[@text = 'Groups']")
    # driver.addons().execute(
    #     SwipeAndFindElement.verticalswipeandroid(
    #         swipeDirection="Up",
    #         bottomMarginPercent=0,
    #         topMarginPercent=0,
    #         maxSwipes=0,
    #         timeoutMilliseconds=0), *groups_home)

    driver.swipe(start_x=1023, start_y=1183, end_x=945, end_y=466, duration=300)

    # 2. Click 'See all - im1'
    see_all4 = driver.find_element(By.XPATH,
                                    "//android.widget.TextView[@text = 'Members']/following::android.widget.TextView[@text = 'See all']")
    see_all4.click()

    time.sleep(10)

    # 3. Click 'Recently Active3'
    recently_active3 = driver.find_element(By.XPATH,
                                            "//android.widget.TextView[@text = 'Recently Active']")
    recently_active3.click()

    # 4. Click 'Newest Members1'
    newest_members1 = driver.find_element(By.XPATH,
                                            "//android.widget.TextView[@text = 'Newest Members']")
    newest_members1.click()

    # 5. Click 'ANDROID.WIDGET.IMAGEVIEW41'
    close_btn = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '']")
    close_btn.click()

    # 6. Is 'ANDROID.VIEW.VIEWGROUP18' is clickable?
    android_view_viewgroup18 = driver.find_element(By.XPATH,
                                                    "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]")
    assert android_view_viewgroup18.is_enabled()