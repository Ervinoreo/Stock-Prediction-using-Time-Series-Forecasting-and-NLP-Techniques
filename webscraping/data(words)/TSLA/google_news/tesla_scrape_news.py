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
pagination_url = 'https://www.google.com/search?q=tesla&sca_esv=52b056e1a97f92b3&rlz=1C5CHFA_enSG1018SG1018&tbas=0&tbs=cdr:1,cd_min:{},cd_max:{}&tbm=nws&sxsrf=ACQVn0-gtYk4ooQe-Csm7M9ydGNiFB3QLw:1710308598863&ei=9jzxZaOoNMHWseMPhfSriA4&start={}&sa=N&ved=2ahUKEwij-_aDxPCEAxVBa2wGHQX6CuE4ChDy0wN6BAgEEAQ&biw=1034&bih=749&dpr=2'
max_iter_pgs = 30


info_list = [] 
dates_dict = [['12/31/2011','10/1/2011'],['9/30/2011', '7/1/2011'], ['6/31/2011', '4/1/2011'], ['3/31/2011', '1/1/2011']]

 
for dates in dates_dict:
    start_date = dates[1]
    end_date = dates[0]
    for i in range(0, max_iter_pgs):
        driver.get(pagination_url.format(start_date, end_date, i*10))
        # driver.refresh()
        time.sleep(3)
        wait = WebDriverWait(driver, 10)
    
        try:
            news_page = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dURPMd")))
            sections = news_page.find_elements(By.CLASS_NAME, "SoAPf")
            print("found sections")
            for ss in sections:
                try:
                    headline = ''
                    desc = ''
                    date = ''
                    div_elements = ss.find_elements(By.TAG_NAME, 'div')
                    headline = div_elements[1].text
                    date = div_elements[3].text
                    desc = div_elements[2].text
                    
                    info_list.append([headline, date, desc])

                except NoSuchElementException:
                    # Handle missing elements for this job posting
                    print("No element")
        except TimeoutException:
            # Handle the case where the job page or jobs are not loaded
            print(f"Timed out waiting for jobs to load on page {i}")
    
    

driver.quit()

end = time.time()
print(f"{end - start} seconds to complete Query!")
csv_file_path = '/Users/ervinyeoh/desktop/unimods/cs3244/tesla/tesla_google_2011.csv'  # Specify your desired path

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Optionally write headers, depending on your requirement
    writer.writerow(['Headlines', "Dates", "Descriptions"])
    writer.writerows(info_list)

print(f"Tesla listings saved to {csv_file_path}")

# import requests
# import csv
# from bs4 import BeautifulSoup

# url = 'https://www.google.com/search?q=tesla&sca_esv=52b056e1a97f92b3&rlz=1C5CHFA_enSG1018SG1018&tbas=0&tbs=cdr:1,cd_min:{},cd_max:{}&tbm=nws&sxsrf=ACQVn095gDrK7y6r0HuXnScAJrsw_gPeZg:1710298170350&ei=OhTxZZH-FKWW4-EPqM-vwAg&start={}&sa=N&ved=2ahUKEwiRg52XnfCEAxUlyzgGHajnC4g4FBDy0wN6BAgFEAQ&biw=1034&bih=749&dpr=2'
# info_list = [] 
# max_iter_pgs = 30
# dates_dict_2023 = [['9/30/2021', '7/1/2023'], ['6/31/2023', '4/1/2023'], ['3/31/2023', '1/1/2023']]

# for dates in dates_dict_2023:
#     start_date = dates[0]
#     end_date = dates[1]
#     for i in range(0, max_iter_pgs):
#         url = url.format(start_date, end_date,i * 10)
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')

#         try:
#             title_div = soup.find('div', class_='n0jPhd ynAwRc MBeu0 nDgy9d')
#             if title_div:
#                 title_text = title_div.get_text(strip=True)
#                 print(title_text)
#             else:
#                 print('Title div not found')
#             # news_page = soup.find('div', class_="SoAPf")
#             # print(news_page)
#             # sections = news_page.find_all('div', class_="SoAPf")
#             # print(sections)
#             # for ss in sections:
#             #     print("hello")
#             #     try:
#             #         print("1")
#             #         headline = ''
#             #         desc = ''
#             #         date = ''
#             #         div_elements = ss.find_all('div')
#             #         headline = div_elements[1].text
#             #         date = div_elements[3].text
#             #         desc = div_elements[2].text
#             #         print(headline)
                    
#             #         info_list.append([headline, date, desc])

#                 # except:
#                 #     # Handle missing elements for this job posting
#                 #     print("error")
#         except:
#             # Handle the case where the job page or jobs are not loaded
#             print("error")
#     break
