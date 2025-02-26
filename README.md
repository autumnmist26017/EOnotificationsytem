# Executive Order Tracker

## About This App

The **Executive Order Tracker** is a Python-based automation tool designed to track, summarize, and manage U.S. Presidential Executive Orders (EOs). It leverages web scraping, AI summarization, and database management to keep users informed of new EOs. 

This app is ideal for researchers, analysts, and policy enthusiasts who want to stay updated on executive actions in real time.

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
git clone https://github.com/your-repo/executive-order-tracker.git
cd executive-order-tracker
