from selenium import webdriver
import urllib.request
import json
from datetime import datetime

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.metacritic.com/browse/movies/score/metascore/all/filtered")

now = datetime.now()
movielist = []
i = 1
while i<=100:
    for movie in driver.find_elements_by_tag_name("tr"):
        print(movie.text)
        for tag in movie.find_elements_by_tag_name("a"):
            for img in tag.find_elements_by_tag_name("img"):
                print(img.get_attribute("src"))
                urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
                i = i+1
                movielist.append(
                    {"No": movie.text.split("\n")[1],
                     "Skor": movie.text.split("\n")[0],
                     "Judul": movie.text.split("\n")[2],
                     "Rilis": movie.text.split("\n")[3],
                     "Image": img.get_attribute("src"),
                     "waktu_scraping":now.strftime("%Y-%m-%d %H:%M:%S"),
                     }
                )

hasil_scraping = open("hasilscraping.json", "w")
json.dump(movielist, hasil_scraping, indent=6)
hasil_scraping.close()

driver.quit()