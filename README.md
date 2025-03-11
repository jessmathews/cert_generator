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

- Font files required should be kept in a folder named "fonts" in TrueType(.ttf) format. (check line 16 of main.py)

- In main.py the overlaytext() function has four parameters (check line 45 of main.py). The fourth parameter controls how high along the y axis the text should be placed. Adjust this value using trial and error (or any other method of your choice)


Once all these are done, run the script

```bash
python3 main.py
```
output pdfs will be stored in the "output" folder. 
Verify all details and you are good to go.

populate the participants list with the required values and run the script again. 
**NOTE**: remember to delete the output folder before running the script again to make sure there are no test pdfs in the folder

That's all. Enjoy certificate generating.

Made with ❤️ and python.