import sys
# Add your project's directory to the sys.path
project_home = '/home/Naina009911/luxury-beauty-affiliate/src'  # Replace with your path
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Import and run your Flask app
from main import app as application