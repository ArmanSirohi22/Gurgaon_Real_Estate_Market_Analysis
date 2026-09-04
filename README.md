# Gurgaon Real Estate Market Analysis

## 📊 Project Overview

This project analyzes the Gurgaon/Gurugram real estate market using Python and exploratory data analysis (EDA). The analysis focuses on property prices, area, price per square foot, locality, BHK configuration, property type, builder/company, RERA approval, and construction status.

The dataset contains **19,515 property records** across **12 columns**.

## 🎯 Business Questions

The analysis answers the following questions:

1. Which is the costliest flat in the dataset?
2. Which locality has the highest average property price?
3. Which locality has the highest average rate per square foot?
4. Do ready-to-move properties cost more than under-construction properties?
5. Do RERA-approved properties command a price premium?
6. How does property area impact property price?
7. Which BHK configuration is the most expensive on average?
8. Which property type has the highest average price?
9. Do certain builders or companies consistently price properties higher?
10. Are larger homes always more expensive per square foot?

## 🛠️ Tools & Technologies

- **Python**
- **Pandas** – data loading, cleaning, and analysis
- **Matplotlib** – visualization
- **Seaborn** – visualization
- **VS Code** – development environment
- **Git & GitHub** – version control and project sharing

## 🔄 Project Workflow

```
Raw Real Estate Data
        ↓
Data Loading
        ↓
Data Cleaning & Standardization
        ↓
Duplicate Removal
        ↓
Numerical Data Conversion
        ↓
Categorical Data Cleaning
        ↓
Exploratory Analysis
        ↓
Business Questions
        ↓
Visual Analysis
        ↓
Real Estate Market Insights
```

## 🧹 Data Cleaning

The Python analysis includes:

- Standardizing column names
- Removing duplicate records
- Converting price values into numeric format
- Cleaning area values
- Cleaning rate-per-square-foot values
- Standardizing categorical text
- Converting RERA approval into a Boolean field
- Removing duplicates again after cleaning

## 📈 Analysis & Visualization

The project uses:

- GroupBy analysis for locality, BHK, property type, and builder/company comparisons
- Average price comparisons
- Price-per-square-foot comparisons
- Correlation analysis between area and price
- Scatter plots to examine the relationship between area and rate per square foot

**Area vs. Rate per Sqft:**

![Area vs Rate per Sqft](visualizations/area_vs_rate_per_sqft.png)

*Rate per sqft tends to fall as area increases — smaller units generally command a higher price per square foot than large plots.*

## 📁 Repository Structure

```
Gurgaon_Real_Estate_Market_Analysis/
│
├── data/
│   └── data of gurugram real Estate.csv
│
├── src/
│   └── gurgaon_real_estate_analysis.py
│
├── visualizations/
│   └── area_vs_rate_per_sqft.png
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

> **Note:** The dataset itself is excluded from version control via `.gitignore`. Add your own copy to the `data/` folder before running the script (see [Data Note](#️-data-note) below).

## ▶️ How to Run

**1. Clone the repository**

```bash
git clone https://github.com/ArmanSirohi22/Gurgaon_Real_Estate_Market_Analysis.git
cd Gurgaon_Real_Estate_Market_Analysis
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Place the dataset**

Put the dataset inside the `data/` folder. Make sure the filename matches the filename used in the script, or update the `pd.read_csv()` path in `src/gurgaon_real_estate_analysis.py` accordingly.

**4. Run the analysis**

```bash
python src/gurgaon_real_estate_analysis.py
```

This prints the answers to each business question to the console and saves a scatter plot to `visualizations/area_vs_rate_per_sqft.png`.

## 💡 Key Skills Demonstrated

This project demonstrates practical skills in:

- Data cleaning
- Exploratory Data Analysis (EDA)
- Data transformation
- Feature standardization
- GroupBy and aggregation
- Correlation analysis
- Data visualization
- Business-question-driven analysis
- Python-based data analysis

## ⚠️ Data Note

If the dataset is from a third party, verify that redistribution is permitted before committing it to a public repository. If redistribution is not allowed, keep the dataset out of GitHub (it is already excluded via `.gitignore`) and document the source here instead:

- **Source:** *(add source URL or description here)*
- **Usage restrictions:** *(note any restrictions here, if applicable)*

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Arman Sirohi**
GitHub: [ArmanSirohi22](https://github.com/ArmanSirohi22)
