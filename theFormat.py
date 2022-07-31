import requests
from bs4 import BeautifulSoup

# Set URL and get page content
urls = ["https://www.hellomerch.com/collections/the-format/products/dog-problems-standard-edition-12-double-black-vinyl",
       "https://www.hellomerch.com/collections/the-format/products/interventions-lullabies-standard-edition-12-black-vinyl"]

# Using User-Agent helps to avoid getting blocked - https://oxylabs.io/blog/5-key-http-headers-for-web-scraping
headers = {'User-Agent':'Mozilla/5.0 (Macintosh Intel Mac OS X 10_15_7) AppleWebKit/605.1.15'
    + '(KHTML, like Gecko) Version/15.5 Safari/605.1.15'}

for url in urls:
    # titles = []
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content, 'html.parser')
    title = soup.title.text
    # titles.append(title)
    # print(titles)
    if 'Dog' in title:
        dog_problems = title
    else:
        interventions = title

# # script_text = soup.find("p", class_="product-vendor").text
# script_text_before_split = soup.find("script", id="bold-subscriptions-platform-script")
# script_text_before_split = str(script_text_before_split)
# script_text = str.split(script_text_before_split, 'inventory_quantity":', 1)[1]
# # script_text = str.split(script_text, '\'subscriptions\'', 1)[0]
# script_text = str.split(script_text, ',"inventory_management"', 1)[0]

# print(script_text + " remain in stock.")


