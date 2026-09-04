Gurgaon Real Estate Market Analysis

📊 Project Overview

This project analyzes the Gurgaon/Gurugram real estate market using Python and exploratory data analysis (EDA).

The analysis focuses on property prices, area, price per square foot, locality, BHK configuration, property type, builder/company, RERA approval, and construction status.

The dataset contains 19,515 property records and 12 columns.

🎯 Business Questions

The analysis answers the following questions:

Which is the costliest flat in the dataset?

Which locality has the highest average property price?

Which locality has the highest average rate per square foot?

Do ready-to-move properties cost more than under-construction properties?

Do RERA-approved properties command a price premium?

How does property area impact property price?

Which BHK configuration is the most expensive on average?

Which property type has the highest average price?

Do certain builders or companies consistently price properties higher?

Are larger homes always more expensive per square foot?

🛠️ Tools & Technologies

Python

Pandas – data loading, cleaning and analysis

Matplotlib – visualization

Seaborn – visualization

Jupyter Notebook / VS Code – development environment

Git & GitHub – version control and project sharing

🔄 Project Workflow

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

🧹 Data Cleaning

The Python analysis includes:

Standardizing column names

Removing duplicate records

Converting price values into numeric format

Cleaning area values

Cleaning rate-per-square-foot values

Standardizing categorical text

Converting RERA approval into a Boolean field

Removing duplicates again after cleaning

📈 Analysis & Visualization

The project uses:

GroupBy analysis for locality, BHK, property type and builder/company comparisons

Average price comparisons

Price-per-square-foot comparisons

Correlation analysis between area and price

Scatter plots to examine the relationship between area and rate per square foot

📁 Suggested Repository Structure

Gurgaon_Real_Estate_Market_Analysis/
│
├── data/
│   └── data of gurugram real Estate.csv
│
├── notebooks/
│   └── Gurgaon_Real_Estate_Analysis.ipynb
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

If the dataset is from a third party, verify that you are allowed to redistribute it before committing it to a public repository. If redistribution is not allowed, keep the dataset out of GitHub and document where it came from.

▶️ How to Run

1. Clone the repository

git clone https://github.com/ArmanSirohi22/Gurgaon_Real_Estate_Market_Analysis.git
cd Gurgaon_Real_Estate_Market_Analysis

2. Install dependencies

pip install -r requirements.txt

3. Place the dataset

Put the dataset inside the data/ folder.

Make sure the filename matches the filename used in the Python script, or update the pd.read_csv() path accordingly.

4. Run the analysis

python src/gurgaon_real_estate_analysis.py

💡 Key Skills Demonstrated

This project demonstrates practical skills in:

Data cleaning

Exploratory Data Analysis (EDA)

Data transformation

Feature standardization

GroupBy and aggregation

Correlation analysis

Data visualization

Business-question-driven analysis

Python-based data analysis

⚠️ Data Note

The repository should clearly mention the original source of the dataset and any applicable usage restrictions. Add the source URL or source description here before publishing the repository if available.

👤 Author
Arman Sirohi
GitHub: ArmanSirohi22
