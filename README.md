
markdown
# Executive Order Tracker

## About This App

The **Executive Order Tracker** is a Python-based automation tool that tracks, summarizes, and manages U.S. Presidential Executive Orders (EOs). It leverages web scraping, AI summarization, and database management to keep users informed of new EOs. 

This app is ideal for researchers, analysts, and policy enthusiasts who want to stay updated on executive actions in real-time.

### Key Features
- **Web Scraping**: Automatically scrapes the Federal Register for the latest EOs.
- **AI-Powered Summarization**: Uses OpenAI GPT-4 to create concise summaries of EO texts.
- **Database Management**: Stores EO data in a PostgreSQL database and identifies new entries.
- **Email Notifications**: Sends email alerts summarizing new EOs, with links to their full text.
- **Structured Data**: Saves data in a format ready for integration with visualizations or reports.

---

## How to Run This App Locally

### Prerequisites
- **Python**: Version 3.8 or higher.
- **PostgreSQL**: Ensure it is installed and running on your machine.
- **Browser Driver**: Compatible with Selenium (e.g., ChromeDriver).

### Step 1: Clone the Repository
```bash
git clone https://github.com/autumnmist26017/EOnotificationsytem.git
cd executive-order-tracker
```

### Step 2: Set Up a Virtual Environment
It is recommended to use a virtual environment for package management:
```bash
python3 -m venv venv
```

#### On Unix:
```bash
source venv/bin/activate
```

#### On Windows:
```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies
Install the required packages:
```bash
pip install -r requirements.txt
```

### Step 4: Set Up the Database
Create a PostgreSQL database:
```sql
CREATE DATABASE eo_database;
```

Update the database credentials in the `connection_string` variable in the script.

### Step 5: Run the Script
Start the EO Tracker:
```bash
python tracker.py
```

---

## How to Use This App

1. **Scrape New Data**:
   - The app scrapes the Federal Register for the latest EOs and extracts their details.

2. **Database Update**:
   - Existing EOs are compared with new data to identify fresh entries.

3. **AI Summarization**:
   - The full text of new EOs is retrieved and summarized using OpenAI GPT-4.

4. **Email Notifications**:
   - Summary notifications are sent to the configured email address.

5. **Data Storage**:
   - All EO data is stored in a PostgreSQL database for easy access and analysis.

---

## Resources
- [Federal Register](https://www.federalregister.gov/) - Source for scraping EO data.
- [OpenAI GPT-4](https://openai.com/) - For text summarization.
- [PostgreSQL](https://www.postgresql.org/) - For database management.
- [Selenium](https://www.selenium.dev/) - For web scraping.

---

## Future Improvements
- Add a web-based dashboard for visualizing EO trends.
- Incorporate categorization of EOs by topics and impacts.
- Support multiple email recipients for notifications.

---

## License
This project is licensed under the MIT License.
```
