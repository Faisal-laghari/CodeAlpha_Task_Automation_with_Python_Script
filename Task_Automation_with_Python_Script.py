"""
=========================================================
        TASK AUTOMATION WITH PYTHON SCRIPTS
=========================================================

This program provides three automation tasks:

1. Organize image files into an "Images" folder
2. Extract email addresses from a text file
3. Scrape the title of a webpage

Key Concepts Used:
- os
- shutil
- re
- requests
- file handling
- functions
- exception handling

Author: Student Project
=========================================================
"""

import os
import shutil
import re
import requests
from datetime import datetime


# --------------------------------------------------------
# OPTION 1 : ORGANIZE IMAGE FILES
# --------------------------------------------------------
def organize_files():
    """Move image files into an Images folder."""

    print("\n========== ORGANIZE FILES ==========")

    folder_path = input("Enter folder path: ").strip()

    try:
        # Check whether folder exists
        if not os.path.exists(folder_path):
            print("Error: Folder not found.")
            return

        # Create Images folder
        image_folder = os.path.join(folder_path, "Images")

        if not os.path.exists(image_folder):
            os.makedirs(image_folder)

        # Image extensions
        image_extensions = (
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".bmp",
            ".webp"
        )

        moved_count = 0

        # Scan folder
        for file_name in os.listdir(folder_path):

            source_path = os.path.join(folder_path, file_name)

            if os.path.isfile(source_path):

                if file_name.lower().endswith(image_extensions):

                    destination_path = os.path.join(
                        image_folder,
                        file_name
                    )

                    try:
                        shutil.move(
                            source_path,
                            destination_path
                        )
                        moved_count += 1

                    except shutil.Error:
                        print(
                            f"File already exists: {file_name}"
                        )

        print("--------------------------------")
        print(f"Total files moved: {moved_count}")
        print("Task completed successfully.")

    except PermissionError:
        print("Permission denied.")

    except Exception as error:
        print("Unexpected Error:", error)


# --------------------------------------------------------
# OPTION 2 : EXTRACT EMAIL ADDRESSES
# --------------------------------------------------------
def extract_emails():
    """Extract emails from a text file."""

    print("\n========== EMAIL EXTRACTOR ==========")

    file_path = input("Enter text file path: ").strip()

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Regular Expression
        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

        emails = re.findall(pattern, content)

        # Remove duplicates
        unique_emails = sorted(set(emails))

        output_file = "extracted_emails.txt"

        with open(output_file, "w", encoding="utf-8") as file:
            for email in unique_emails:
                file.write(email + "\n")

        print("--------------------------------")
        print(f"Emails found: {len(unique_emails)}")
        print(
            f"Saved into file: {output_file}"
        )

    except FileNotFoundError:
        print("Error: File not found.")

    except Exception as error:
        print("Unexpected Error:", error)


# --------------------------------------------------------
# OPTION 3 : WEB PAGE TITLE SCRAPER
# --------------------------------------------------------
def scrape_title():
    """Fetch webpage title and save log."""

    print("\n========== WEB SCRAPER ==========")

    url = input(
        "Enter URL (Press Enter for example.com): "
    ).strip()

    if url == "":
        url = "https://example.com"

    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        html = response.text

        # Regex for title
        match = re.search(
            r"<title>(.*?)</title>",
            html,
            re.IGNORECASE | re.DOTALL
        )

        if match:
            title = match.group(1).strip()

        else:
            print("Title tag not found.")
            return

        # Current date and time
        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # Save in append mode
        with open(
            "website_titles.txt",
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                f"Date: {timestamp}\n"
            )

            file.write(
                f"URL: {url}\n"
            )

            file.write(
                f"Title: {title}\n"
            )

            file.write(
                "-" * 50 + "\n"
            )

        print("--------------------------------")
        print("Web page title fetched successfully.")
        print("Title :", title)
        print(
            "Saved in website_titles.txt"
        )

        # BeautifulSoup can also be used
        # for more advanced web scraping.

    except requests.exceptions.MissingSchema:
        print("Invalid URL.")

    except requests.exceptions.ConnectionError:
        print("Connection failed.")

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.RequestException:
        print("Error while fetching webpage.")

    except Exception as error:
        print("Unexpected Error:", error)


# --------------------------------------------------------
# MAIN MENU
# --------------------------------------------------------
def main():
    """Display menu and call functions."""

    while True:

        print("\n")
        print("=" * 50)
        print("     TASK AUTOMATION MENU")
        print("=" * 50)
        print("1. Organize Image Files")
        print("2. Extract Email Addresses")
        print("3. Scrape Web Page Title")
        print("4. Exit")
        print("=" * 50)

        choice = input(
            "Enter your choice (1-4): "
        )

        if choice == "1":
            organize_files()

        elif choice == "2":
            extract_emails()

        elif choice == "3":
            scrape_title()

        elif choice == "4":
            print("\nThank you for using the program.")
            break

        else:
            print(
                "Invalid choice. Please try again."
            )


# --------------------------------------------------------
# PROGRAM ENTRY POINT
# --------------------------------------------------------
if __name__ == "__main__":
    main()