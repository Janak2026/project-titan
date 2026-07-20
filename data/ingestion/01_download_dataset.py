"""
Project TITAN

Step 1:
Download Amazon Reviews Dataset

Author: Janardhana Rao Komanapalli
"""

from pathlib import Path
import logging

from src.config.settings import (
    RAW_DATA,
    DATASET_NAME,
    CATEGORY,
)

# --------------------------------------------------
# Logging
# --------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


# --------------------------------------------------
# Create Directories
# --------------------------------------------------

def create_directories():

    RAW_DATA.mkdir(parents=True, exist_ok=True)

    logger.info("Directory verified : %s", RAW_DATA)


# --------------------------------------------------
# Download Dataset
# --------------------------------------------------

def download_dataset():

    logger.info("------------------------------------------")
    logger.info("Project TITAN")
    logger.info("------------------------------------------")

    logger.info("Dataset : %s", DATASET_NAME)
    logger.info("Category : %s", CATEGORY)

    logger.info("")
    logger.info(
        "Dataset download implementation will be added in the next step."
    )

    logger.info("Raw data location : %s", RAW_DATA)


# --------------------------------------------------
# Main
# --------------------------------------------------

def main():

    create_directories()

    download_dataset()

    logger.info("")
    logger.info("Step completed successfully.")


if __name__ == "__main__":
    main()