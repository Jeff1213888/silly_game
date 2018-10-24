#! /usr/bin/python
# -*- coding : utf-8 -*-
# Filename: cacu.py
# Arthur: Hansson Ji
# Date: 10/23/2018
import time
from splinter import Browser
from selenium import webdriver
def splinter(url):
    browser = Browser()
    print('Opening browser\n')
    browser.visit(url)
    time.sleep(3)
    print('Selecting user type\n')
    browser.find_by_id('userTypeSelect').click()
    time.sleep(1)
    print('Click \"Student\"\n')
    browser.find_by_text('Student').click()
    time.sleep(1)
    print('Filling email and password\n')
    browser.find_by_id('inputEmail').fill('randomemail@mail.com')
    browser.find_by_id('inputPassword').fill('8C51B7')
    print('Submitting form\n')
    browser.find_by_id('submitForm').click()
    time.sleep(3)
    print('Continue courses\n')
    browser.find_link_by_href('CourseLogin.aspx?courseid=2360111').click()
    time.sleep(3)
    print('Click the lesson')
    browser.find_link_by_href('/mod/homepage/view.php?id=322&continue=true').click()
    for i in range(1, 100):

        try:
            for h in range(4):
                choice = 'multichoice_' + str(i) + '_' + str(h + 1)
                print('Click choice: ' + choice)
                browser.find_by_id(choice). click()
            for k in range(4):
                unclick = 'multichoice_' + str(i) + '_' + str(k + 1)
                browser.find_by_id(unclick).click()
                time.sleep(1)
                browser.find_by_value('Check Response').click()
                time.sleep(1)
                try:
                    browser.find_by_id('nextnavbutton').click()
                    print('Correct')
                except:
                    print('Not correct')
                    browser.find_by_id(unclick).click()
        except:
            for j in range(4):
                choice = 'multichoice_' + str(i) + '_' + str(j + 1)
                print('Looking for id: ' + choice)
                browser.find_by_id(choice).click()
                time.sleep(1)
                browser.find_by_value('Check Response').click()
                time.sleep(1)
                try:
                    browser.find_by_id('nextnavbutton').click()
                except:
                    print('Wrong choice')
            print('Done or not a multi choice question')
        finally:
            print('Countdown started: 60sec')
            time.sleep(60)
            print('Trying to click \"next\"')
            browser.find_by_id('nextnavbutton').click()
            # exit(0)


if __name__ == '__main__':
    websize ='https://web.3rdmil.com/login'
    splinter(websize)
