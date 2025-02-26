Executive Order Tracker
About This App
The Executive Order Tracker is a Python-based automation tool designed to track, summarize, and manage U.S. Presidential Executive Orders (EOs). It leverages web scraping, AI summarization, and database management to keep users informed of new EOs. This tool is particularly useful for researchers, analysts, and policy enthusiasts who want to stay updated on executive actions.

Key Features
Data Extraction: Scrapes the Federal Register for the latest EOs and their metadata (titles, IDs, links).
AI Summarization: Uses OpenAI GPT-4 to generate concise summaries of EO texts.
Database Management: Stores EO data in a PostgreSQL database and identifies newly issued orders.
Email Notifications: Sends alerts summarizing new EOs, complete with links to their full text.
Data Visualization Ready: Data is saved in a structured format for easy integration with dashboards or reports.
How to Run This App Locally
Prerequisites
Python: Version 3.8 or higher.
PostgreSQL: Installed and running.
Browser Driver: Selenium-compatible (e.g., ChromeDriver).
Step 1: Clone the Repository
Clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/your-repo/executive-order-tracker.git
cd executive-order-tracker
Step 2: Set Up a Virtual Environment
It is recommended to use a virtual environment for package management:

bash
Copy
Edit
python3 -m venv venv
On Unix:
bash
Copy
Edit
source venv/bin/activate
On Windows:
bash
Copy
Edit
venv\Scripts\activate
Step 3: Install Dependencies
Install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
Step 4: Set Up the Database
Create a PostgreSQL database and update the credentials in the script:

sql
Copy
Edit
CREATE DATABASE eo_database;
Update the user, password, host, and port values in the connection_string in the script.

Step 5: Run the Script
Start the EO tracker by running:

bash
Copy
Edit
python tracker.py
How to Use This App
Scrape New Data:

The script will scrape the Federal Register for the latest EOs and extract their details.
Database Update:

Existing EOs are compared to the newly scraped data to identify new entries.
Summarization:

The full text of new EOs is retrieved and summarized using GPT-4.
Email Notifications:

Notifications are sent to the configured email address with a summary and link for each new EO.
Data Management:

All EO data is saved to the PostgreSQL database for easy access and analysis.
Resources
Federal Register: Source for scraping EO data.
OpenAI GPT-4: For text summarization.
PostgreSQL: For data storage and management.
Selenium: For web scraping.
Future Improvements
Add a dashboard for visualizing trends in executive orders.
Incorporate categorization of EOs by topic or impact area.
Support notifications for multiple recipients.
License
This project is licensed under the MIT License.# EOnotificationsytem
