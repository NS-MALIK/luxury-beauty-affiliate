import os
import sys

# Add your project's root directory to the sys.path
project_home = '/home/Naina009911/luxury-beauty-affiliate'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Now, import your Flask app from src.main
from src.main import app as application