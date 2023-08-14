import requests
import datetime
import os

# Calculate the date range for the last 365 days
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=365)

# Construct the URL base
base_url = "https://archives.nseindia.com/products/content/sec_bhavdata_full_"

# Create a target folder for saving the files
target_folder = "Bhavcopy"
os.makedirs(target_folder, exist_ok=True)

# Loop through each day in the date range
current_date = start_date
while current_date <= end_date:
    # Skip weekends (Saturday and Sunday)
    if current_date.weekday() < 5:
        date_str = current_date.strftime("%d%m%Y")
        file_name = f"{date_str}.csv"
        download_file = os.path.join(target_folder, f"bhavcopy{current_date.strftime('%Y-%m-%d')}.csv")
        download_url = base_url + file_name

        # Check if the file already exists, if not, proceed with downloading
        if not os.path.exists(download_file):
            response = requests.get(download_url)

            # Save the content to a local file if the request was successful
            if response.status_code == 200:
                with open(download_file, "wb") as file:
                    file.write(response.content)
                print(f"Downloaded {download_file}")
            else:
                print(f"File not found for {date_str}, skipping...")
    else:
        print(f"Skipping weekend: {current_date}")

    # Move to the next day
    current_date += datetime.timedelta(days=1)
