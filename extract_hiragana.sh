#!/bin/bash

if [ ! -d "venv" ]; then
    # Create virtual environment
    echo "Creating virtual environment..."
    python3 -m venv venv

    # Activate virtual environment
    echo "Activating virtual environment..."
    . venv/bin/activate

    # Upgrade tools
    echo "Upgrading tools..."
    pip3 install --upgrade pip setuptools wheel

    # Install required packages
    echo "Installing required packages..."
    pip3 install -r requirements.txt
else
    # Activate virtual environment
    echo "Activating virtual environment..."
    . venv/bin/activate
fi

# Extract ETL database
echo "Extracting ETL database..."
python3 extract.py

# Extract hiragana dataset
# TODO

# Cleanup samples
# TODO

# Create standardized text-based dataset files
# TODO

