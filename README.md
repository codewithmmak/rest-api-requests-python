# RESTful API Testing in Python with requests

## To Get Started

### Pre-requisites
* Download and install Python:
  * [Install Python](https://www.python.org/downloads/ "Install Python")
* Download and install any Text Editor like Visual Code/Sublime/Brackets
  * [Install Visual Studio Code](https://code.visualstudio.com/download "Install Visual Studio Code")

### Setup 
* Clone the repository into a folder
* Go to Project root directory and install Dependency: `pip install -r requirements.txt`
* All the dependencies from requirements.txt will be installed.

### Run Test
1. Open Terminal
2. Go to project location
3. Enter `pytest` and hit enter key

### Capture stdout
1. Open Terminal
2. Go to project location
3. Enter `pytest -sv --capture=sys` and hit enter key

### Generate HTML Report using pytest-html
1. Open Terminal
2. Go to project location
3. Enter `pytest -sv --capture=sys --html=report.html` and hit enter key

#### HTML Report
![HTML Test Report](./img/report.png?raw=true "HTML Test Report")