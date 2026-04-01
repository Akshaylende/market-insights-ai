# Configuration settings for Different APIs 

import os
from dotenv import load_dotenv


#Instantiating dotenv to load environment variables
load_dotenv()


# Fetching API keys from env variables
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")
