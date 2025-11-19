#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Setting up Pylings environment...${NC}"

# Check for python3
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install it first."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo -e "${BLUE}Creating virtual environment...${NC}"
    python3 -m venv .venv
else
    echo -e "${GREEN}Virtual environment already exists.${NC}"
fi

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
echo -e "${BLUE}Installing dependencies...${NC}"
pip install -r requirements.txt

echo -e "${GREEN}Setup complete!${NC}"
echo -e "To start learning, run:"
echo -e "${BLUE}source .venv/bin/activate${NC}"
echo -e "${BLUE}python3 pylings.py watch${NC}"
