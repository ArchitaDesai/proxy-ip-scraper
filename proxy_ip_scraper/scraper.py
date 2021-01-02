from selenium import webdriver
from bs4 import BeautifulSoup
import time, re

from .proxyconfig import *


def extract_data(data, url_index):
    if data:  # if data isn't empty (data exists)
        iseq = ip_seq[url_index]
        ps = port_seq[url_index]
        cs = country_seq[url_index]
        aseq = anon_seq[url_index]
        hs = https_seq[url_index]
        i = 0
        while (i < len(data)):
            if data[i] and len(data[i]) > 3:  # length>3 to avoid adsbygoogle/ads

                ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', data[i][iseq])[0]  # [0] to avoid having ip list
                
                # Note: 20 is the code used to differentiate exceptional data
                if ps == 20:
                    # Different data format -> "128.34.66.1:8080" -> "IP:port" 
                    s = data[i][iseq].split(":")
                    port = s[len(s) - 1]
                else:
                    port = data[i][ps]

                country = data[i][cs] if cs != 20 else "Not specified"
                anon = data[i][aseq] if aseq != 20 else "Not specified"
                
                if hs != 20:
                    upper = data[i][hs].upper()
                    https = "yes" if upper.find("HTTPS") != -1 or upper.find("YES") != -1 else "no"
                else:
                    https = "Not specified"

                print(ip, port, country, anon, https)
                
                # Write in CSV file
                # writer.writerow([ip, country, port, anon, https, datetime.now()]) # Will be written in DB with Django ORM

            i += 1


def parse(browser, url_index):
    time.sleep(7)
    soup = BeautifulSoup(browser.page_source, "html.parser")

    if id_tags_name[url_index]:
        attrib = "id"
        value = id_tags_name[url_index]
    else:
        attrib = "class"
        value = class_name[url_index]

    table = soup.find('table', attrs={attrib: value})
    table_body = table.find('tbody')
    rows = table_body.find_all("tr")

    data = []  # to store table here
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols])

    return data


def call_browser(url_index):

    browser = webdriver.Chrome()
    browser.get(urls[url_index])
    data = parse(browser, url_index)

    extract_data(data, url_index)

    page_index = 2
    while (page_index <= pages[url_index]):
        try:
            if (url_index == 9):
                # Simulate "Load more" button click
                browser.find_element_by_link_text('Load more').click()
            else:
                # Simulate page number click on website - in bottom
                browser.find_element_by_link_text(str(page_index)).click()

            data = parse(browser, url_index)
            extract_data(data, url_index)
        except:
            print("Error: No such element exception.")

        page_index += 1

    browser.quit()


def main():
    url_index = 0
    while url_index < len(urls):
        call_browser(url_index)
        url_index += 1
