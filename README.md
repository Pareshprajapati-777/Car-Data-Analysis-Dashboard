# 🚗 Car Data Analysis Dashboard

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Pandas-Analysis-150458?logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly&logoColor=white" alt="Plotly">
</p>

> 📊 An interactive dashboard for exploring car specifications, prices, brands, fuel types, and market patterns.

## 🌟 Overview

The **Car Data Analysis Dashboard** is built with Python and Streamlit. It presents car dataset information through summary metrics, filters, interactive charts, and comparisons to help users explore vehicle characteristics and pricing patterns.

## ✨ Features

### 🏠 Summary Dashboard
- 🚘 Total cars and brands
- ⛽ Fuel-type overview
- 🌍 Country and model-year summaries
- 📋 Dataset preview and quick insights

### 🔎 Data Exploration
- 🏷️ Brand comparisons
- 📅 Year-wise filtering
- ⚙️ Fuel type, body type, and transmission analysis
- 💰 Price statistics
- 🔧 Engine and power comparisons
- 🛡️ Safety-feature exploration
- 🛣️ Mileage analysis

### 📈 Interactive Visualizations
- Price distribution histogram
- Top expensive brands
- Engine capacity vs. power
- Power vs. price
- Average price by year
- Mileage by fuel type
- Body-type distribution
- Average price by country
- Correlation heatmap

### 🏎️ Popular Car Gallery
Browse a curated visual section featuring brands such as BMW, Mercedes-Benz, Lamborghini, Ferrari, Porsche, and Tesla.

## 🛠️ Tech Stack

| Technology | Purpose |
| --- | --- |
| 🐍 Python | Application logic |
| 🎈 Streamlit | Dashboard interface |
| 🐼 Pandas | Data loading and manipulation |
| 🔢 NumPy | Numerical calculations |
| 📊 Plotly Express / Graph Objects | Interactive charts |

## 📂 Project Structure

```text
Car-Data-Analysis-Dashboard/
├── Car.py
├── requirements.txt
├── README.md
└── dataset file(s)
```

The dataset filename may vary; use the file included in the repository and confirm the expected path in `Car.py`.

## 🚀 Installation & Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Pareshprajapati-777/Car-Data-Analysis-Dashboard.git
cd Car-Data-Analysis-Dashboard
```

### 2️⃣ Install dependencies

```bash
python -m pip install -r requirements.txt
```

If no `requirements.txt` is present in your checkout, install the main libraries:

```bash
python -m pip install streamlit pandas numpy plotly
```

### 3️⃣ Start the dashboard

```bash
python -m streamlit run Car.py
```

Open the local URL printed in the terminal. Ensure the dataset is placed at the path expected by the app.

## 📊 Analysis Questions You Can Explore

- Which brands have the highest average prices in the dataset?
- How do prices vary across model years?
- What relationships appear between engine capacity, power, and price?
- How does mileage vary by fuel type?
- Which vehicle characteristics show stronger correlations?

These are exploratory questions; results depend on the dataset and its quality.

## ⚠️ Data Notes

- 📅 The years and values reflect the bundled dataset, not necessarily the current vehicle market.
- 🧹 Check for missing values, inconsistent units, and outliers before drawing conclusions.
- 💰 Prices are dataset values and should not be treated as current dealer quotations.
- 📷 Add screenshots to the repository if you want a visual preview directly in this README.

## 🔮 Future Improvements

- 🤖 Add a machine-learning price prediction module
- 📥 Enable CSV or Excel report downloads
- 🔍 Add advanced filters and search
- 🧪 Add data validation and tests
- 🔄 Support regularly refreshed datasets

## 👨‍💻 Author

**Paresh Prajapati**

Data Analytics · Python · Streamlit

🔗 [GitHub Profile](https://github.com/Pareshprajapati-777) · [LinkedIn](https://linkedin.com/in/pareshprajapati-co)

---

⭐ Explore the data, compare vehicle characteristics, and uncover useful patterns.
