"""<strong class="text-underline"><span class="table-ip4-home"> 217.138.216.60</span></strong>"""
import requests
import bs4
import fake_headers

headers = fake_headers.Headers(browser='firefox', os='win')
headers_dict = headers.generate()
url = "https://www.iplocation.net/"
responce = requests.get(url, headers=headers_dict)
html_data = responce.text
soup = bs4.BeautifulSoup(html_data, "lxml")
span_tag = soup.find('span', class_="table-ip4-home")
ip_address = span_tag.text
print(ip_address.strip())
