from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import csv
import concurrent.futures

PATH = "/Users/ervinyeoh/desktop/unimods/bt4222/chromedriver-mac-arm64/chromedriver"
service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)
start = time.time()
pagination_url = 'https://www.tesla.com/blog#list_id=tcl-list-1&page={}'
max_iter_pgs = 46
info_list = []

for i in range(0, max_iter_pgs + 1):
    driver.get(pagination_url.format(i))
    driver.refresh()
    time.sleep(10)
    wait = WebDriverWait(driver, 10)
    
    try:
        news_page = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tcl-list__content")))
        sections = news_page.find_elements(By.CLASS_NAME, "tcl-article-teaser")
        for ss in sections:
            try:
                headline = ''
                date = ''
                span_elements = ss.find_elements(By.TAG_NAME, 'span')
                headline = span_elements[0].text
                date = span_elements[1].text
                desc = ss.find_elements(By.TAG_NAME, 'p')
                info_list.append([headline, date, desc[0].text])

            except NoSuchElementException:
                # Handle missing elements for this job posting
                print("No element")
    except TimeoutException:
        # Handle the case where the job page or jobs are not loaded
        print(f"Timed out waiting for jobs to load on page {i}")

driver.quit()

end = time.time()
print(f"{end - start} seconds to complete Query!")
csv_file_path = '/Users/ervinyeoh/desktop/unimods/cs3244/tesla.csv'  # Specify your desired path

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Optionally write headers, depending on your requirement
    writer.writerow(['Headlines', "Dates", "Descriptions"])
    writer.writerows(info_list)

print(f"Tesla listings saved to {csv_file_path}")

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, TimeoutException
# import time
# import csv
# import concurrent.futures

# PATH = "/Users/ervinyeoh/desktop/unimods/bt4222/chromedriver-mac-arm64/chromedriver"
# service = Service(executable_path=PATH)
# driver = webdriver.Chrome(service=service)
# start = time.time()
# pagination_url = 'https://www.tesla.com/blog#list_id=tcl-list-1&page=1'
# max_iter_pgs = 46
# info_list = []

# driver.get(pagination_url)
# wait = WebDriverWait(driver, 10)
    
# try:
#     news_page = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tcl-list__content")))
#     sections = news_page.find_elements(By.CLASS_NAME, "tcl-article-teaser")
#     for ss in sections:
#         try:
#             headline = ''
#             date = ''
#             span_elements = ss.find_elements(By.TAG_NAME, 'span')
#             headline = span_elements[0].text
#             date = span_elements[1].text
#             desc = ss.find_elements(By.TAG_NAME, 'p')
#             info_list.append([headline, date, desc[0].text])

#         except NoSuchElementException:
#             # Handle missing elements for this job posting
#             print("No element")
# except TimeoutException:
#     # Handle the case where the job page or jobs are not loaded
#     print(f"Timed out waiting for jobs to load on page {1}")

# driver.quit()

# end = time.time()
# print(f"{end - start} seconds to complete Query!")
# csv_file_path = '/Users/ervinyeoh/desktop/unimods/cs3244/tesla.csv'  # Specify your desired path

# with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     # Optionally write headers, depending on your requirement
#     writer.writerow(['Headlines', "Dates", "Descriptions"])
#     writer.writerows(info_list)

# print(f"Tesla listings saved to {csv_file_path}")
