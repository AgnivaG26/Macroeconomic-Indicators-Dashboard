---
tags: [Import-c816]
title: World Economic Dashboard
created: '2025-08-15T05:26:19.200Z'
modified: '2025-08-15T15:42:01.887Z'
---

-----

### Macroeconomic Indicators Dashboard

This project is a dynamic and interactive dashboard built with **Python** and **Streamlit** that visualizes key macroeconomic indicators for countries around the world, using data from the World Bank. The dashboard provides enhanced data analysis and visualization capabilities beyond the standard World Bank website, making economic trends easier to explore, compare, and export.

### 🚀 Features

  * **Multi-Country Comparison:** Compare the performance of multiple countries side-by-side on a single chart for any key indicator (GDP Growth, Trade, etc.).
  * **Dynamic Filters:** Use interactive sliders and dropdowns to filter data by country and year range, instantly updating all charts and metrics.
  * **Choropleth Maps:** Visualize a selected indicator on an interactive world map for any year, allowing for quick identification of global and regional trends.
  * **Data Export:** Easily download the filtered data for a single country, a multi-country comparison, or a specific indicator for all countries with a single click.
  * **Clean and Robust Data:** The backend script, `data_cleaning.py`, handles data cleaning, including fixing missing values and preparing the data for seamless use in the dashboard.

### 💡 How This Dashboard Enhances the World Bank's Data

The World Bank's website is a powerful source of raw data, but its tools for analysis and visualization can be limited. This project addresses those limitations by providing a more user-friendly and feature-rich experience.

| Feature | This Dashboard | World Bank Website |
| :--- | :--- | :--- |
| **Direct Multi-Country Comparison** | ✅ Easily compares multiple countries on one chart | ❌ Requires manual data download and plotting |
| **Export Filtered Data** | ✅ Downloads only the data you see and need | ❌ Requires downloading a large, raw dataset |
| **Interactive Choropleth Maps** | ✅ Provides quick global visualization for a selected year | ❌ Requires navigating to a separate tool and extensive filtering |
| **Seamless User Experience** | ✅ Single-page, interactive, no-code required | ❌ Requires navigating through multiple pages and menus |

### 🛠️ How to Use

#### Prerequisites

  * Python 3.8+
  * Streamlit, pandas, and plotly libraries. Install them using:
    ```bash
    pip install streamlit pandas plotly
    ```
  * The raw CSV data files from the World Bank. Download the six required CSVs (GDP Growth, Exports, Imports, Agriculture, Industry, Services) and save them in your project folder.

#### Steps

1.  **Run the Data Cleaner:** This script will load and prepare your raw CSV data, saving a cleaned file named `cleaned_data.pkl`. Run it once from your terminal:

    ```bash
    python data_cleaner.py
    ```

2.  **Run the Dashboard:** Once the cleaned data file is generated, you can start the Streamlit app from your terminal:

    ```bash
    streamlit run dashboard.py
    ```

This will open the interactive dashboard in your web browser. You can use the sidebar filters to explore the data and download your custom filtered data.

### 📄 Project Files

  * `data_cleaning.py`: The script for cleaning and preparing the data.
  * `dashboard.py`: The main Streamlit application script.
  * `cleaned_data.pkl`: The cleaned, ready-to-use data file created by `data_cleaner.py`.
  * `gdp_growth.csv`, `exports.csv`, etc.: The raw data files downloaded from the World Bank.
