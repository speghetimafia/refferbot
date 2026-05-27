from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

# Load data from spreadsheet
file_path = "path"  # Change to your file path
df = pd.read_excel(file_path)

# Setup WebDriver (Ensure chromedriver is installed)
driver = webdriver.Chrome()
driver.get("link")
time.sleep(7)  # Wait for the page to load

def apply_zoom():
    driver.execute_script("""
        window.onload = function() {
            document.body.style.zoom='60%';
        };
        document.body.style.zoom='60%'; // Apply immediately in case onload fails
    """)
    time.sleep(2)  # Ensure zoom effect takes place

# Loop through the first 10 serial numbers
for index, row in df.iterrows():
    serial_number = int(row["serial"])  # Convert serial to integer
    if serial_number > 10:
        break  # Stop after serial number 10

    try:
        # Refresh the page before each entry
        driver.refresh()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Wait for page load

        # Apply Zoom every time after reload
        apply_zoom()

        # Fill "Your Information" (Static details)
        driver.find_element(By.ID, "form_c5a19cb2-5266-4a49-a52e-8d7383533b2f").send_keys("first name")
        driver.find_element(By.ID, "form_91248d6d-029b-45a4-8b73-b9d1967d3c0f").send_keys("last name")
        driver.find_element(By.ID, "form_19673c5a-b298-4f33-9299-d372a6158def").send_keys("email")
        driver.find_element(By.ID, "form_dacb24f2-b974-47cf-a724-e1c20d853490").send_keys("+number")

        # Select Country: India
        country_dropdown = Select(driver.find_element(By.ID, "form_54624d86-325e-4ce5-ac0c-310bdcec5f06"))
        country_dropdown.select_by_visible_text("India")

        # Select "An alum of any of our programs"
        driver.find_element(By.XPATH, "//label[contains(text(), 'An alum of any of our programs')]").click()

        # Select Programs
        programs = [
            "1",
            "2",
            "3"
        ]
        for program in programs:
            driver.find_element(By.XPATH, f"//label[contains(text(), '{program}')]").click()

        # Fill Friend's Information (Dynamic details from Excel)
        driver.find_element(By.ID, "form_1c9328dc-7bf9-4f26-a519-3253dcf71a08").send_keys(row["first_name"])
        driver.find_element(By.ID, "form_4f820be6-ecd1-4f26-9ce9-d129aa94bb2d").send_keys(row["last_name"])
        driver.find_element(By.ID, "form_d094c584-ee71-46f8-8a7b-17feec5b9dd9").send_keys(row["email"])
        driver.find_element(By.ID, "form_76745b72-3c6a-4343-bc1f-e0e60ff0a5ba").send_keys(row["phone"])

        # Select Friend's Country: India
        friend_country_dropdown = Select(driver.find_element(By.ID, "form_e91ac838-5d28-4fd6-8839-5fa5a869aa00"))
        friend_country_dropdown.select_by_visible_text("India")

        # Submit the form
        time.sleep(5)  # Short delay before clicking submit
        submit_button = driver.find_element(By.CLASS_NAME, "form_button_submit")
        submit_button.click()

        # Wait for form submission
        time.sleep(39)  # Adjust if needed

    except Exception as e:
        print(f"Error on Serial {serial_number}: {e}")

# Close the browser after all entries are completed
driver.quit()
