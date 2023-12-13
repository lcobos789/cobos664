import requests
from bs4 import BeautifulSoup

for i in range(0, 3):
    url = f"https://www.phillipscollection.org/collection?on_view=1&has_image=1&field_period_target_id[86]=86&page={i}"
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    
    item_containers = soup.find_all("div", class_="card grid__item")
    
    for item_container in item_containers:
        titles = item_container.find_all("span")
        time = item_container.find_all("p")
        
        for title, t in zip(titles, time):
            print(title.text.strip(), t.text.strip())
