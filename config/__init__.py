import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Determine which environment configuration to load
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development').lower()

if ENVIRONMENT == 'development':
    from .development import CONFIG
elif ENVIRONMENT == 'production':
    from .production import CONFIG
elif ENVIRONMENT == 'testing':
    from .testing import CONFIG
else:
    raise ValueError("Invalid environment name. Ensure 'ENVIRONMENT' variable is set in the .env file.")
