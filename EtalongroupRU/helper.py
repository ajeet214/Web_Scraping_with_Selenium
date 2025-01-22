"""
Author: Ajeet
Created: 1/19/2025
Description: This script scrapes apartment details from the Voxhall property page using Selenium and BeautifulSoup.
Project: automation
"""
import os
import json
from typing import List, Dict
from logger import logger


def save_file(path: str, data: List) -> None:
    """
       Saves the provided data to a file at the specified path.
       If the file already exists, it is deleted before saving the new data.

       Args:
           path (str): The file path where the data will be saved.
           data (List): The data to be saved in JSON format.

       Returns:
           None: The function performs an action (saving a file) and does not return a value.

       Side Effects:
           - If the file exists at the specified path, it is removed before saving the new data.
           - A log message is generated after successfully saving the data.
       """

    # Check if the file exists
    if os.path.exists(path):
        # If the file exists, delete it
        os.remove(path)

    # Open the file in write mode and save the data in JSON format
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

        # Log a message indicating the file was successfully created
        logger.info(f"New {path} has been created with the data.")
