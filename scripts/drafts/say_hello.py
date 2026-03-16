"""
Script to generate personalised greetings for course participants.

Reads people data from a JSON file and course configuration from a YAML file.
Filters people enrolled in the configured course and writes greetings to an
output file. The output directory is read from the environment variable
OUTPUT_DIR, defaulting to 'data/final' if not set.

Usage:
    uv run --env-file .env scripts/drafts/say_hello.py
"""

import json
import os

import yaml
from dotenv import load_dotenv

from exohw import get_greetings, write_greetings

# Load environment variables from .env file (Pillar 1)
load_dotenv('.env')
output_dir = os.environ.get('OUTPUT_DIR', 'data/final')

# Load input data (Pillar 4)
with open('data/people.json', 'r') as f:
    data = json.load(f)

# Load configuration (Pillar 2)
with open('config/config.yaml', 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

# Run core logic (Pillar 3)
greetings = get_greetings(data['people'], config)
write_greetings(greetings, output_dir, config)