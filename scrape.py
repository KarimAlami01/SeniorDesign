from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

def get_html(url, driver_path):
    chrome_options = Options()
    #    chrome_options.add_argument("--headless")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    time.sleep(5) # 5 seconds wait to show im human
    html_content = driver.page_source
    driver.quit()
    return html_content

def scrape_data(url, driver_path):
    html_content = get_html(url, driver_path)
    soup = BeautifulSoup(html_content, 'html.parser')
    stats_div = soup.find('div', {'id': 'stats-pages'})
    game_stats_div = stats_div.find('div', {'class': 'ui container game-stats'})

    quarter_div = None
    if game_stats_div:
        quarter_div = game_stats_div.find('div', {'class': 'quarter-breakdown'})
    
    quarter_table = str(quarter_div.find('table')) if quarter_div else ''

    team_div = None
    if game_stats_div:
        team_div = game_stats_div.find('div', {'class': 'team-stats'})
    
    team_stats = str(team_div.find('table')) if team_div else ''

    stats_table_div = None
    if stats_div:
        stats_table_div = stats_div.find('div', {'class': 'stats-table'})

    stats_table = str(stats_table_div.find('table')) if stats_table_div else ''
    
    return quarter_table + team_stats + stats_table



def main():
    urls = [
        'https://theaudl.com/stats/game/2023-05-05-TOR-NY',
        'https://theaudl.com/stats/game/2023-05-05-CAR-ATL',
        'https://theaudl.com/stats/game/2023-05-05-COL-SD',
        'https://theaudl.com/stats/game/2023-05-05-SLC-POR',
        'https://theaudl.com/stats/game/2023-05-06-TOR-BOS',
        'https://theaudl.com/stats/game/2023-05-06-SLC-SEA',
        'https://theaudl.com/stats/game/2023-05-06-MIN-IND',
        'https://theaudl.com/stats/game/2023-05-06-DAL-ATX',
        'https://theaudl.com/stats/game/2023-05-06-COL-LA',
        'https://theaudl.com/stats/game/2023-05-07-PHI-DC'
    ]
    driver_path = '/Users/karimalami/Downloads/chromedriver_mac64'  
    
    for i, url in enumerate(urls):
        scraped_data = scrape_data(url, driver_path)
        with open(f"scraped_data_{i}.html", "w") as file:
            file.write(scraped_data)

if __name__ == '__main__':
    main()
