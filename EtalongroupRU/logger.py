"""
Author: Ajeet
Created: 1/19/2025
Description: This script scrapes apartment details from the Voxhall property page using Selenium and BeautifulSoup.
Project: automation
"""
import logging
import sys

# Create a logger
logger = logging.getLogger("Voxhall")
logger.setLevel(logging.INFO)

# Formatter for consistent log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# File handler
file_handler = logging.FileHandler("F:/automation/EtalongroupRU/debug.log", encoding="utf-8")
file_handler.setFormatter(formatter)

# Stream handler
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

# Add handlers to the logger
if not logger.handlers:  # Prevent adding handlers multiple times
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
