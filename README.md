# 🚀 API Automation Framework  

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)  
![Pytest](https://img.shields.io/badge/Test_Framework-Pytest-green?logo=pytest)  
![Requests](https://img.shields.io/badge/HTTP_Library-Requests-orange?logo=fastapi)  
![Status](https://img.shields.io/badge/Status-Active-success)  

---

## 📌 Overview  
This project is a **Python-based API Automation Framework** built with **Pytest** and the **Requests** library.  
It helps validate RESTful API endpoints for response codes, payloads, and business logic, with reports for tracking execution.  

---

## 🛠️ Tech Stack  
- 🐍 **Python 3.11+**  
- ⚡ **Pytest** – test runner & fixtures  
- 🌐 **Requests** – API HTTP client  
- 📊 **Pytest HTML Reports** – execution results  

---

## 📂 Project Structure  

API Automation Framework/
│── reports/ # Test execution reports
│── tests/ # Test cases (GET, POST, PUT, DELETE)
│ ├── test_getuser.py
│ ├── test_postuser.py
│ ├── test_putuser.py
│ ├── test_deleteuser.py
│── utils/ # Utility and helper modules
│ ├── apis.py # API methods (GET, POST, PUT, DELETE)
│── test_data.json # Sample test data
│── pytest.ini # Pytest configuration
│── conftest.py # Fixtures and reusable configs
│── requirements.txt # Project dependencies

---

## ⚡ Features  
- ✅ GET, POST, PUT, DELETE API automation  
- ✅ Data-driven testing with JSON  
- ✅ Pytest fixtures for reusable setup  
- ✅ Terminal & HTML reports  
- ✅ Extensible for more APIs  

