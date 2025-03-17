# wework-python-job-scraper

We Work Remotely Python Job Scraper

📌 Project Description

This project is a Python web scraper that extracts remote Python job listings from We Work Remotely. It uses Selenium to navigate the site, wait for JavaScript-loaded content, and filter out jobs specifically related to Python.

🚀 Features

Scrapes remote Python jobs from We Work Remotely.

Uses Selenium WebDriver to handle dynamic JavaScript content.

Filters jobs based on 'Python' in the title or company name.

Saves extracted data into a CSV file.

Runs in headless mode for efficiency.

🛠️ Requirements

Ensure you have Python installed. Then install the dependencies:

pip install selenium webdriver-manager

⚙️ How to Run the Scraper

Clone the repository:

git clone https://github.com/your-username/wework-python-job-scraper.git
cd wework-python-job-scraper

Run the script:

python scraper.py

Check the output file (remote_jobs.csv) for the extracted job listings.

📂 Output Example (remote_jobs.csv)

Company

Title

Location

Link

Example Co

Python Developer

Remote

https://weworkremotely.com/...

📝 Future Enhancements

Automate daily job alerts via email.

Add filtering options (e.g., experience level, salary).

Convert CSV data into a web dashboard using Flask/Streamlit.

💡 Contributions & Feedback

Feel free to fork, submit PRs, or open issues! 🚀

