[![Python API Tests](https://github.com/RuzanBagdasaryan/QA_API_Automatio/actions/workflows/python-app.yml/badge.svg)](https://github.com/RuzanBagdasaryan/QA_API_Automatio/actions/workflows/python-app.yml)

# QA API Automation Framework

## 📌 Project Description

This project demonstrates API test automation using Python and Pytest.

The framework includes:
- API client abstraction
- Config management
- Logging
- JSON structure validation
- HTML reporting
- CI/CD integration

---

## 🛠 Tech Stack

- Python 3.11+
- Pytest
- Requests
- Pytest-HTML
- GitHub Actions

---

## 📂 Project Structure

qa_api_automation/
│
├── config/
├── schemas/
├── tests/
├── utils/
├── .github/workflows/
├── pytest.ini
└── requirements.txt

---

## ▶ How to Run Tests

Install dependencies:

pip install -r requirements.txt

Run tests:

pytest --html=reports/report.html --self-contained-html

---

## 📊 Reporting

HTML report is generated in:

reports/report.html

---

## 🚀 CI/CD

Tests run automatically via GitHub Actions on every push.
