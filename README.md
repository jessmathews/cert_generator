# Certificate Generator

## Requirements
- Python3
- A template file in pdf format
- List of names to be added
- Fonts (as required)

## Setup

Open terminal and clone this repository

```bash
git clone https://github.com/jessmathews/cert_generator.git
cd cert_generator
```
Create and activate a python virtual environment
```bash
# creates a python environment with name "env" 
python3 -m venv env

#activate this environment
source env/bin/activate

```
Install Dependencies
```bash
pip install -r requirements.txt
```
## Running of the script

- A template file in pdf format should be put in a folder named "template" in the cert_generator directory

- For initial testing use the "test_data.csv" and populate with a few names of your choice (check line 29 of main.py)

