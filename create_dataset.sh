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
echo "Extracting hiragana dataset..."
python3 extract_hiragana.py

# Cleanup samples
echo "Cleaning samples..."
python3 samples_cleanup.py

# Unify samples
echo "Unifying size of samples..."
python3 unify_size_of_samples.py

# Create standardized text-based dataset files
# TODO

