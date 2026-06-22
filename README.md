# WhatsApp Bulk Sender

A small Python automation tool that sends a WhatsApp message to a list of phone
numbers using Selenium + WhatsApp Web.

## How it works
- Reads phone numbers from an Excel file (`numbers.xlsx`, column: `phone`)
- Opens WhatsApp Web in Chrome (scan the QR once)
- Sends the configured message to each number

## Setup
```bash
pip install pandas selenium openpyxl
```
- Download the matching `chromedriver.exe` for your Chrome version and place it
  in this folder.
- Create `numbers.xlsx` with a `phone` column (e.g. `923001234567`).

## Run
```bash
python send.py
```

> Note: `numbers.xlsx` and `PyWhatKit_DB.txt` are git-ignored so real phone
> numbers are never published. Use responsibly and only message people who have
> consented.
