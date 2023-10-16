import random
import os
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup as BS


def login():
    driver = uc.Chrome(version_main=117)
    url = 'https://www.upwork.com/nx/find-work/most-recent'

    driver.get(url)
    time.sleep(random.uniform(2.6, 3.9))
    email_field = driver.find_element(By.XPATH,
                                      '/html/body/div[4]/div/div/div/main/div/div[2]/div[2]/form/div/div/div[1]/div['
                                      '3]/div/div/div/div/input')
    email_field.send_keys('your email')
    time.sleep(random.uniform(0.6, 1.9))
    continue_button = driver.find_element(By.XPATH,
                                          "/html/body/div[4]/div/div/div/main/div/div[2]/div[2]/form/div/div/div["
                                          "1]/button")
    continue_button.click()
    time.sleep(random.uniform(1.6, 2.9))
    password_field = driver.find_element(By.XPATH,
                                         '/html/body/div[4]/div/div/div/main/div/div[2]/div[2]/form/div/div/div['
                                         '1]/div[3]/div/div/div/input')
    password_field.send_keys('your password')
    time.sleep(random.uniform(1.4, 2.1))
    login_button = driver.find_element(By.XPATH,
                                       "/html/body/div[4]/div/div/div/main/div"
                                       "/div[2]/div[2]/form/div/div/div[1]/button")
    login_button.click()
    time.sleep(random.uniform(1.1, 2.56))
    try:
        security_answer = driver.find_element(By.XPATH,
                                              "/html/body/div[4]/div/div/div/main/div/div[2]/di"
                                              "v[2]/form/div/div/div[1]/div[2]/div[1]/div/div/input")
        security_answer.send_keys('mazda')
        finish_login = driver.find_element(By.XPATH,
                                           "/html/body/div[4]/div/div/div/main/div/div[2]/div[2]/form/d"
                                           "iv/div/footer/div/div[1]/div/button")
        finish_login.click()
    except Exception:
        print('No security question')
    while True:
        file_to_delete = 'recent_job.txt'
        driver.refresh()
        if os.path.exists(file_to_delete):
            os.remove(file_to_delete)
            print(f'{file_to_delete} has been deleted.')
        else:
            print(f'{file_to_delete} does not exist in the directory.')
        print('Getting new job...')
        scrap_recent_jobs(driver.page_source)
        time.sleep(30)


def scrap_recent_jobs(page_source):
    recent_jobs = ''
    soup = BS(page_source, "html.parser")
    jobs_list = soup.find_all('div', {'data-test': 'job-tile-list'})

    for jobs in jobs_list:
        h2_elements = jobs.find('h2')
        description = jobs.find('span', {'data-test': 'job-description-text'})
        job_type = jobs.find('strong', {'data-test': "job-type"})
        posted_on = jobs.find('span', {'data-test': 'posted-on'})
        print(description.text.strip())
        print(h2_elements.text.strip())
        print(job_type.text.strip())
        print(posted_on.text.strip())
        recent_jobs = f'{h2_elements.text.strip()}\n{description.text.strip()}\n{job_type.text.strip()}' \
                      f'\n{posted_on.text.strip()}'
    with open('recent_job.txt', 'w', encoding='utf-8') as file:
        file.write(recent_jobs)


if __name__ == '__main__':
    login()
