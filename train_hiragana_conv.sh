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

# Train CNN models
echo "Training CNN models..."
python3 train_hiragana_conv.py
