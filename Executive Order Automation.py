from sqlalchemy import create_engine
import time 
import openai
import pandas as pd


# Replace these values with your actual PostgreSQL credentials
user = 'jackstein'
password = 'stitch2'
host = 'localhost'  # Or your actual host
port = '5432'  # Default port for PostgreSQL
dbname = 'eo_database'

# Create a connection string
connection_string = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'

# Create an engine to connect to the database
engine = create_engine(connection_string)

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # Or the driver for your browser
driver.get("https://www.federalregister.gov/presidential-documents/executive-orders/donald-trump/2025")

# Wait for the page to load (optional)
driver.implicitly_wait(10)

# Extract executive orders
data = []
orders = driver.find_elements(By.CLASS_NAME, "row.presidential-document-wrapper")
for order in orders:
    title = order.find_element(By.TAG_NAME, "a").text
    Link = order.find_element(By.TAG_NAME, "a").get_attribute("href")
    EO_id = order.find_element(By.TAG_NAME, "h5").text
    data.append({"Title": title, "Link": Link, "EO_id": EO_id})

driver.quit()

current_data = pd.DataFrame(data)

from sqlalchemy import text

with engine.connect() as conn:
    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS current_eo_table (
        title TEXT,
        Link TEXT,
        EO_id TEXT PRIMARY KEY,
        full_text TEXT,
        summary TEXT
    );
    """))

current_data.to_sql('current_eo_table', engine, if_exists='replace', index=False)

def fetch_table_as_dataframe(table_name, engine):
    query = f"SELECT * FROM {table_name}"
    return pd.read_sql(query, engine)

# Function to compare two tables and find columns unique to the second table
def find_unique_columns(table1_name, table2_name, column_name, engine):
    # Load the tables into DataFrames
    table1 = fetch_table_as_dataframe(table1_name, engine)
    table2 = fetch_table_as_dataframe(table2_name, engine)

    # Filter the tables by the comparison column
    table1_values = set(table1[column_name])
    table2_values = set(table2[column_name])

    # Find values unique to the second table
    unique_values = table2_values - table1_values

    return unique_values

# Function to create a new table containing all rows from the second table where unique values occur
def create_filtered_table(unique_values, source_table_name, target_table_name, column_name, engine):
    # Check if unique_values is empty
    if not unique_values:
        print("No unique values provided. Skipping table creation.")
        return

    # Convert unique values to a comma-separated string for SQL query
    unique_values_str = ', '.join([f"'{value}'" for value in unique_values])

    # Create SQL query to select rows where the column matches unique values
    from sqlalchemy import text

    query = text(f"""
    CREATE TABLE {target_table_name} AS
    SELECT *
    FROM {source_table_name}
    WHERE {source_table_name}."{column_name}" IN ({unique_values_str});
    """)

    with engine.connect() as connection:
        connection.execute(query)

table1_name = "eo_table"  # First table name
table2_name = "current_eo_table"  # Second table name
comparison_column = "EO_id"  # Column for comparison
target_table_name = "filtered_current_eo_table"  # Name of the new table

unique_values = find_unique_columns(table1_name, table2_name, comparison_column, engine)

# Create a new table with the filtered rows
create_filtered_table(unique_values, table2_name, target_table_name, comparison_column, engine)

print(f"Table '{target_table_name}' created with rows from '{table2_name}' where {comparison_column} matches unique values.")

unique_values_str = ', '.join([f"'{value}'" for value in unique_values])

print(unique_values_str)

EO_ids = [eo.strip().strip("'") for eo in unique_values_str.split(',')]

print(EO_ids)

from sqlalchemy import text
import pandas as pd

query = text("""
SELECT * 
FROM current_eo_table
WHERE "EO_id" IN :EO_ids
""")

with engine.connect() as conn:
    result = conn.execute(query, {'EO_ids': tuple(EO_ids)})
    new_EOs = pd.DataFrame(result.fetchall(), columns=result.keys())


from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (adjust to your specific WebDriver setup)
driver = webdriver.Chrome()

# Iterate through the DataFrame rows
for index, row in new_EOs.iterrows():
    driver.get(row["Link"])
    driver.implicitly_wait(10)
    try:
        all_text = driver.find_element(By.CLASS_NAME, "content-col").text
        new_EOs.at[index, "all_text"] = all_text  # Add the summary to the DataFrame
    except Exception as e:
        print(f"Error extracting summary for {row['Title']}: {e}")
        new_EOs.at[index, "all_text"] = None  # Set to None if summary extraction fails

# Close the WebDriver
driver.quit()



# Replace YOUR_API_KEY with your actual API key
openai.api_key = "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"



def generate_summary(prompt, word_limit=100):
    completion = openai.ChatCompletion.create(
        model="gpt-4",  # Use the GPT model you prefer
        messages=[
            {"role": "system", "content": "You are a research assistant."},
            {
                "role": "user",
                "content": f"Write a {word_limit}-word summary of the following text: {prompt}"
            }
        ]
    )
    return completion.choices[0].message['content']

# Example DataFrame
# df = pd.DataFrame({'all': ['Text1', 'Text2', 'Text3']})  # Replace with your actual DataFrame

# Add a summary column to the DataFrame
new_EOs['summary'] = None

for index, row in new_EOs.iterrows():
    try:
        if not row['summary'] or pd.isna(row['summary']):
            text_to_summarize = row['all_text']
            summary = generate_summary(text_to_summarize)
            new_EOs.at[index, 'summary'] = summary
            print(f"Row {index} summarized.")
        
        # Add a delay to avoid hitting API rate limits
        time.sleep(2)  # Adjust the delay as needed
    except Exception as e:
        print(f"Error summarizing row {index}: {e}")


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email details
sender_email = "eonotificationsystem@gmail.com"
receiver_email = "Jodymstein@gmail.com"
password = "nmdv eute vgnu hgaj"  # App-specific password for Gmail


if new_EOs.empty:
    print("No new Executive Orders found.")
    exit()
else:
    for index, row in new_EOs.iterrows():
        title = row['Title'].strip()
        body = "Summary: " + row['summary'] + "\n\n View full Executive Order here: " + row['Link']
        subject = "New Executive Order: " + title
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                print("Email sent successfully!")
        except Exception as e:
            print(f"Error: {e}")

new_EOs.rename(columns={'Title': 'title'}, inplace=True)
new_EOs.rename(columns={'all_text': 'full_text'}, inplace=True)
new_EOs.to_sql('eo_table', engine, if_exists='append', index=False)