# UI Automation Tests

This project is a UI automation test suite using Playwright, pytest, and Allure.

## Setup


## Virtual Environment Setup

It is recommended to use a virtual environment to manage dependencies.

### Windows
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### MacOS/Linux
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
### Run tests and generate Allure report
1. Run tests:
   ```bash
   pytest --alluredir=reports
   ```

2. Generate Allure report:
   ```bash
   allure serve reports
   ```