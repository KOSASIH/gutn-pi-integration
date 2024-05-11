# main.py
import logging
from config import Config
from modules.gutn_pi_integration import GutnPIntegration

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load configuration
config = Config('config.json')

# Initialize Gutn PI Integration
gutn_pi_integration = GutnPIntegration(config)

# Start Gutn PI Integration
gutn_pi_integration.start()
