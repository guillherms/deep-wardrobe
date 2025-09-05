from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.shopyourtv.com/tag/the-bear-season-1/")

posts = driver.find_elements(By.CSS_SELECTOR, "div.grid-four-columns-button.post")

links = []
for post in posts:
    try:
        link = post.find_element(By.PARTIAL_LINK_TEXT, "OUTFIT DETAILS").get_attribute("href")
        links.append(link)
    except:
        pass

print("Total links:", len(links))

for link in links:
    driver.get(link)
    time.sleep(2)

    # --- Tratamento de anúncio ---
    try:
        ad_button = driver.find_element(By.ID, "dismiss-button")
        ad_button.click()
        print("Anúncio fechado ✅")
        time.sleep(1)
    except:
        pass  # se não tiver anúncio, segue

    # --- Coleta de dados ---
    try:
        character = driver.find_element(By.CSS_SELECTOR, "span.character").text
        episode = driver.find_element(By.CSS_SELECTOR, "span.episode").text
        brand_products = driver.find_element(By.CSS_SELECTOR, "span.brand-products").text
        buy_link = driver.find_element(By.LINK_TEXT, "BUY THE LOOK").get_attribute("href")
        image = driver.find_element(By.CSS_SELECTOR, "div.entry img").get_attribute("src")

        print("character:", character)
        print("episode:", episode)
        print("Detalhes:", image[:200], "...")
        print("-----")

    except Exception as e:
        print("Erro ao coletar:", e)

driver.quit()
