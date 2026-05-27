# RefferBot


RefferBot is a Python script designed to automate the process of submitting referrals to a program. It uses Selenium to navigate the web form, populate fields, and submit entries based on data provided in an Excel spreadsheet. This project was created to efficiently submit multiple referrals for a contest.

## How It Works

The script launches a Chrome browser instance, navigates to the referral page, and iterates through a list of contacts from an Excel file. For each contact, it completes the form with both static referrer information and the dynamic contact details before submitting it. The script is configured to process the first 10 entries from the specified data file.

## Features

-   Automates submissions to the web form.
-   Reads referral contact information (name, email, phone) from an Excel (`.xlsx`) file.
-   Fills in static referrer details automatically.
-   Handles various form elements including text inputs, dropdown menus, and checkboxes.
-   Includes delays to ensure the page loads correctly before interacting with elements.

## Prerequisites

Before running this script, ensure you have the following installed:

-   Python 3.x
-   Google Chrome
-   [ChromeDriver](https://chromedriver.chromium.org/downloads) (The version must match your installed Google Chrome version).
-   The required Python libraries: `selenium`, `pandas`, and `openpyxl`.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/speghetimafia/refferbot.git
    cd refferbot
    ```

2.  **Install Python dependencies:**
    ```bash
    pip install selenium pandas openpyxl
    ```

3.  **Ensure ChromeDriver is accessible:**
    Make sure the `chromedriver` executable is placed in a directory included in your system's PATH.

4.  **Prepare the Data File:**
    Create an Excel file (e.g., `datag.xlsx`). The script expects the file to contain the following columns:
    -   `serial`
    -   `first_name`
    -   `last_name`
    -   `email`
    -   `phone`

## Usage

1.  **Configure the script:**
    Open `form_bot.py` in a text editor and update the `file_path` variable to the absolute path of your Excel data file.

    ```python
    # Change to your file path
    file_path = "/path/to/your/datag.xlsx" 
    ```

2.  **Run the script:**
    Execute the script from your terminal.

    ```bash
    python form_bot.py
    ```

The script will open a Chrome window and begin submitting entries from your Excel file.

## Disclaimer

This script was built for a specific version of the referral form. If the website's HTML structure, element IDs, or class names change, the script will likely fail and will require updates to function correctly.
