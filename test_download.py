from os import path, remove
from time import sleep

import time
from driver_builder import DriverBuilder
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import datetime
import glob
import pandas as pd
from xlsxwriter.workbook import Workbook
from pandas.io.excel import ExcelWriter
import time
import numpy as np

class TestDownload:
    def test_download(self):

        driver_builder = DriverBuilder()

        download_path = "."

        # expected_download = path.join(download_path, "5MB.zip")

        # # clean downloaded file
        # try:
        #     remove(expected_download)
        # except OSError:
        #     pass

        # assert (not path.isfile(expected_download))

        browser = driver_builder.get_driver(download_path, headless=True)

        browser.get('https://www.funtoot.com/funtoot/#/app/login')
        time.sleep(2)

        browser.find_element_by_id('username').send_keys("ebl01t001")
        browser.find_element_by_id('password').send_keys("funtoot")
        browser.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[1]/div/div[2]/div[2]/form/div/div[5]/div[1]/div/div/button").send_keys(Keys.RETURN)
        time.sleep(10)


        def convert_xlsx_to_csv():
            files = glob.glob('*.xlsx')
            for file in files:
                os.system('ssconvert ' + file + ' ' + str(file.split('.')[0]) + '.csv')

        def convert_to_old_data():
            pass

        def pre_process_data(cls):
            files = glob.glob('*.csv')
            df = []

            for file in files:
                if file[0] != 'a':
                    temp_df = pd.read_csv(file)
                    Time_stamp = []
                    for i in range(len(temp_df)):
                        Time_stamp.append(str(datetime.datetime.now().strftime("'%d-%b-%Y %H:%M:%S")))
                    temp_df.insert(0, "Time Stamp", Time_stamp, True)
                    temp_df.rename(columns = {"Subj Progress": "Subj Progress (%)", "Concept Progress": "Concept Progress (%)", "SubConcept Progress": "SubConcept Progress (%)"}, inplace = True)
                    df.append(temp_df)

            df[0].drop(['Start Date', 'End Date'], axis=1, inplace=True)
            df[0].drop([], axis=1, inplace=True)
            os.system('rm ./reports/time_series_data_' + cls + '.csv')
            # old_data = pd.read_csv('./reports/old_data_' + cls + '.csv')
            # new_df = pd.concat([df[0], old_data]) 
            df[0].to_csv('./reports/time_series_data_' + cls + '.csv', index=False)

        def stitch_all_classes():
            files = glob.glob('./reports/*.csv')
            files.sort()
            df = []
            for file in files:
                base = os.path.basename(file).split('.')
                if base[0][0] == 't':
                    temp_df = pd.read_csv(file)
                    df.append(temp_df)


            final_df = pd.concat([df[0], df[1]]) 
            for i in range(2, len(df)):
                final_df = pd.concat([final_df, df[i]])

            os.system('rm ./reports/stitched_time_series_data.csv')
            
            final_df.to_csv('./reports/stitched_time_series_data.csv', index = False)



        browser.get('https://www.funtoot.com/funtoot/#/app/teacher/reports/curriculum-progress')
        browser.implicitly_wait(8)
        time.sleep(10)

        for j in range(2, 6):
            # date = (datetime.datetime(2019, 5, 15, 15, 48, 10, 680809) + datetime.timedelta(days=0)).strftime('%d-%b-%Y')
            date = str(datetime.datetime.now().strftime('%d-%b-%Y'))
            print(date)
            browser.find_element_by_xpath('//input[@placeholder = "To"]').clear() 
            browser.find_element_by_xpath('//input[@placeholder = "From"]').clear() 
            ActionChains(browser).move_to_element(browser.find_element_by_xpath('//input[@placeholder = "To"]')).click().send_keys(str(date)).perform()
            ActionChains(browser).move_to_element(browser.find_element_by_xpath('//input[@placeholder = "From"]')).click().send_keys(str(date)).perform()
            browser.find_element_by_xpath('//button[@class="btn btn-default ng-binding"]').click()
            time.sleep(10)
            select_class = browser.find_element_by_id('Select1')
            select = Select(select_class)
            select.select_by_index(j)
            time.sleep(10)
            print("to be downloaded")
            browser.find_element_by_xpath("//download-report-btn/div/i").click()
            time.sleep(4)
            os.system('mv ' + str(j + 3) + 'AMathematicsreport.xlsx ' + str(date) + '.xlsx')
            time.sleep(8)
            convert_xlsx_to_csv()
            os.system('rm *.xlsx')
            pre_process_data(str(j + 3))
            files = glob.glob('*.csv')
            for file in files:
                if file[0] != 'a':
                    os.system('rm ' + file)
        
            os.system('rm *.csv')
            if (j == 5):
                time.sleep(2)
                browser.quit()


        stitch_all_classes()

        print("done")

    # def wait_until_file_exists(self, actual_file, wait_time_in_seconds=5):
    #     waits = 0
    #     while not path.isfile(actual_file) and waits < wait_time_in_seconds:
    #         print("sleeping...." + str(waits))
    #         sleep(.5)  # make sure file completes downloading
    #         waits += .5

t = TestDownload()
t.test_download()