<img width="965" height="375" alt="Screenshot 2026-07-17 204133" src="https://github.com/user-attachments/assets/3c5b1c2e-a610-4428-a654-ed0c3addd7a9" />

# Pak Wheels ETL Pipeline

Welcome to the **Pak Wheels ETL Project**! This repository contains an automated end-to-end data engineering pipeline designed to extract, process, and load automotive marketplace data for analytical use.

The project demonstrates a production-ready ETL workflow handling data scraping/API extraction, schema alignment, data cleaning, and final storage.

---

## 🏗️ Architecture & Workflow

The pipeline follows a structured data engineering lifecycle as shown in the project schema:

1. **Extraction:** Fetching raw car listing details from web sources or API endpoints using Python.
2. **Transformation:** 
   * Cleaning missing values and removing duplicate listings.
   * Standardizing column data types (prices, mileage, engine capacity).
   * Exporting staging checkpoints as CSV files.
3. **Loading:** Establishing a database connection to structured storage engines (SQL databases/Data Warehouses) to make the data query-ready.

---

## 📁 Repository Structure

* **`Pak-Wheels-ETL/`**: Contains the primary Jupyter Notebooks and Python scripts executing the extraction logic, data transformation workflows, and database connector scripts.

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.x
* **Data Engineering & Analysis:** `pandas`, `numpy`
* **Workflow Environment:** Jupyter Notebook
* **Storage Connectors:** SQL Integration Libraries

---
