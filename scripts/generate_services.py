import yaml
import os
from datetime import datetime

# Define the path to the data file and the content directory
data_file_path = 'data/services.yaml'
content_dir = 'content/services'

# Ensure the content directory exists
os.makedirs(content_dir, exist_ok=True)

# Read the services data
with open(data_file_path, 'r', encoding='utf-8') as f:
    services = yaml.safe_load(f)

# Generate markdown files for each service
for service in services:
    title = service.get('title', 'Untitled Service')
    slug = service.get('slug', title.lower().replace(' ', '-'))
    description = service.get('description', '')
    category = service.get('category', 'General')
    overview = service.get('overview', '')
    features = service.get('features', [])
    why_us = service.get('why_us', '')

    # Get current date and format it for Hugo
    current_date = datetime.now().isoformat()

    # Construct the markdown content
    markdown_content = f"""---
title: "{title}"
date: {current_date}
draft: false
description: "{description}"
category: "{category}"
---

## Service Overview

{overview}

## Key Features

"""
    for feature in features:
        markdown_content += f"*   {feature}\n"
    
    markdown_content += f"""
## Why Choose Us for This Service?

{why_us}
"""

    # Write the markdown file
    file_name = os.path.join(content_dir, f"{slug}.md")
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    print(f"Generated: {file_name}")

print("Service markdown files generated successfully.")