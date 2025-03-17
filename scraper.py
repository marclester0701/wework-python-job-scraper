from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

def fetch_jobs():
    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (no UI)
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://weworkremotely.com/categories/remote-programming-jobs")
    
    time.sleep(10)  # Increased wait time for JavaScript to load fully
    
    print(driver.page_source[:1000])  # Print first 1000 characters

    jobs = []
    job_elements = driver.find_elements(By.CSS_SELECTOR, "section.jobs li")  # Updated CSS selector
    
    for job in job_elements:
        try:
            company = job.find_element(By.CLASS_NAME, "company").text.strip()
            title = job.find_element(By.CLASS_NAME, "title").text.strip()
            location = job.find_element(By.CLASS_NAME, "region").text.strip() if job.find_elements(By.CLASS_NAME, "region") else "Worldwide"
            link = job.find_element(By.TAG_NAME, "a").get_attribute("href")
            
            jobs.append([company, title, location, link])
        except:
            continue
    
    driver.quit()
    return jobs

def save_to_csv(jobs, filename="remote_jobs.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Company", "Title", "Location", "Link"])
        writer.writerows(jobs)
    print(f"Saved {len(jobs)} jobs to {filename}")

if __name__ == "__main__":
    job_list = fetch_jobs()
    if job_list:
        save_to_csv(job_list)
    else:
        print("No jobs found.")