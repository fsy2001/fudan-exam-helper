import json
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

driver = webdriver.Safari()

def login():
    driver.get('https://uis.fudan.edu.cn/authserver/login?service=https%3A%2F%2Felearning.fudan.edu.cn%2Flogin%2Fcas')
    driver.find_element(By.ID, 'username').send_keys(os.getenv('UIS_USERNAME'))
    driver.find_element(By.ID, 'password').send_keys(os.getenv('UIS_PASSWORD'))
    driver.find_element(By.ID, 'password').send_keys(Keys.RETURN)
    sleep(2)

def send_content(url, title, content):
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@id="right_nav"]/a[2]').click()
    sleep(2)
    driver.find_element(By.ID, 'compose-message-subject').send_keys(title)
    driver.find_element(By.XPATH, '//*[@id="compose-new-message"]/form/div[2]/textarea').send_keys(content)
    driver.find_element(By.XPATH, '/html/body/div[4]/div[4]/div[2]/button[2]').click()
    sleep(1)

def process_student(row, students):
    id = str(row['学号'])
    url = None
    for student in students:
        if student['sortable_name'] == id:
            url = student['enrollments'][0]['html_url']
            break
    if url is not None:
        title = "期中考试成绩"
        content = None
        if row['总分'] != 0:
            content = \
f"""{row['姓名']}（{row['学号']}）同学：

在本次期中考试中，你的总成绩为{row['总分']}分，位次为第{row['位次']}名。其中各项得分如下：

填空题：{int(row['填空'])}分
11题：{int(row['11'])}分
12题：{int(row['12'])}分
13题：{int(row['13'])}分
14题：{int(row['14'])}分
15题：{int(row['15'])}分
16题：{int(row['16'])}分

本次考试的试题将会在下周的习题课上讲评。如对成绩有疑问，请在讲评后询问助教。"""
        else:
            content = \
f"""{row['姓名']}（{row['学号']}）同学：
在本次期中考试中，你的总成绩为0分（缺考）。"""

        send_content(url, title, content)
    else:
        print('student mismatch')

if __name__ ==  '__main__':
    login()
    with open('students.json', 'r') as file:
        students = json.load(file)

        df = pd.read_csv('score.csv')
        for row in df.iterrows():
            process_student(row[1], students)