import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Replace with the path to your JSON credentials file
json_keyfile_path = "../../google api credential/credentials.json"

# Initialize the Google Sheets API client
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile_path, scope)
client = gspread.authorize(credentials)

# Open the Google Sheets document by its title or URL
spreadsheet = client.open('Monday Motivational Messages (Responses)')  # Replace with your Google Sheet name or URL

# Select the worksheet by name
worksheet = spreadsheet.worksheet('Sheet1')  # Replace with your sheet name

# Get all values in the worksheet
data = worksheet.get_all_values()

# Create a Pandas DataFrame from the data
subscribers_list = pd.DataFrame(data[1:], columns=data[0])

# Now 'df' contains your data as a Pandas DataFrame
print(subscribers_list)
