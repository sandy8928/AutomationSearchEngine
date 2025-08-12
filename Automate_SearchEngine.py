# Chrome Automation 
import webbrowser as wb  # This module provides a high-level interface to allow displaying web pages in the browser.

def open_chrome(url): # This function opens a URL in the default browser.
    """
    Opens the specified URL in the default web browser.
    Args:
    url (str): The URL to open.
    """
    try: # Try to open the URL
        wb.open(url)  # Open the URL
        print(f"Opening {url} in your web browser.") # Print a message to the console.
    except Exception as e: # If there is an error, print the error message.
        print(f"An error occurred while trying to open the URL: {e}") # Print the error message.

# Example usage
if __name__ == "__main__": # This is a guard clause to ensure the code only runs when the script is run directly.
    url1 = "https://www.yahoo.com" # Replace with your desired URL
    url2 = "https://www.chrome.com"  # Replace with your desired URL
    url3 = "https://www.google.com"  # Replace with your desired URL
    url4 = "https://www.bing.com"  # Replace with your desired URL
    open_chrome(url1) # Open the first URL
    open_chrome(url2) # Open the second URL
    open_chrome(url3) # Open the third URL.
    open_chrome(url4) # Open the fourth URL.


"""
This script opens a specified URL in the default web browser.
You can replace 'https://www.example.com' with any URL you wish to open.
Note: Ensure that the web browser is installed and configured correctly on your system.
This script uses the webbrowser module to handle the opening of URLs.
You can run this script directly to test the functionality.
Make sure to have Python installed on your machine to execute this script.
This script is designed to automate the process of opening a URL in Chrome.
It is a simple automation task that can be expanded for more complex browser interactions in the future."""
