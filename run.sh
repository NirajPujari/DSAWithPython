#!/bin/bash
echo "Creating virtual environment if it does not exist..."

# Create virtual environment if not exists
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

echo
echo "Activating environment..."
source venv/bin/activate

echo
echo "Installing dependencies..."
pip install -r requirements.txt

echo
echo "Starting Application..."
python3 src/main.py
