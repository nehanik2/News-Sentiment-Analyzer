#CREATING THE CONFIGURATION FILE 
"""
Project Configuration File
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# File Paths
DATA_DIR = 'data'
MODELS_DIR = 'models'
CACHE_DIR = 'cache'
VIZ_DIR = 'visualizations'
NOTEBOOKS_DIR = 'notebooks'

# Model Parameters
RANDOM_STATE = 42
TEST_SIZE = 0.2
N_FEATURES_TFIDF = 500
CV_FOLDS = 5

# Sentiment Thresholds
POSITIVE_THRESHOLD = 0.3
NEGATIVE_THRESHOLD = -0.3
TOXICITY_THRESHOLD = 0.5

# News Collection Settings
ARTICLES_PER_TOPIC = 100
TOPICS = [
    'politics', 
    'economy', 
    'health', 
    'technology', 
    'sports',
    'entertainment', 
    'climate', 
    'crime', 
    'education'
]

# Cache Settings
CACHE_EXPIRY_HOURS = 24

if __name__ == "__main__":
    print("Configuration loaded successfully!")
    print(f"API Key present: {NEWS_API_KEY is not None}")
    print(f"Topics: {TOPICS}")