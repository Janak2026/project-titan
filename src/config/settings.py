"""
Project TITAN Configuration
"""

from pathlib import Path

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASETS = PROJECT_ROOT / "datasets"

RAW_DATA = DATASETS / "raw"
BRONZE_DATA = DATASETS / "bronze"
SILVER_DATA = DATASETS / "silver"
GOLD_DATA = DATASETS / "gold"

# --------------------------------------------------
# Dataset
# --------------------------------------------------

DATASET_NAME = "Amazon Reviews 2023"

DATASET_URL = (
    "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/"
)

CATEGORY = "All_Beauty"

# --------------------------------------------------
# Fabric
# --------------------------------------------------

FABRIC_WORKSPACE = ""

LAKEHOUSE_NAME = ""

# --------------------------------------------------
# AI
# --------------------------------------------------

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

LLM_MODEL = "llama3"

# --------------------------------------------------
# Random Seed
# --------------------------------------------------

RANDOM_SEED = 42