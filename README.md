🏠 Gurgaon Real Estate Analysis using Python
📌 Project Overview
This project analyzes a Gurgaon real estate dataset using Python to discover valuable insights about property prices, localities, builders, property types, and RERA approvals. The project focuses on data cleaning, exploratory data analysis (EDA), and answering business-related questions using data visualization and statistical analysis.

The analysis helps identify pricing trends and factors that influence property values in Gurgaon.

🎯 Objectives
Clean and preprocess real estate data.
Analyze property prices across different localities.
Compare Ready-to-Move and Under Construction properties.
Study the impact of RERA approval on property prices.
Analyze the relationship between area and price.
Identify premium builders and expensive property types.
Visualize important trends using graphs.
📊 Dataset
The dataset contains information about residential properties in Gurgaon, including:

Property Type
Flat Type (BHK)
Locality
Society
Builder Name
Company Name
Price
Area (Sqft)
Rate Per Sqft
Property Status
RERA Approval
🛠️ Technologies Used
Python
Pandas
Matplotlib
Seaborn
📚 Python Libraries
pandas
matplotlib
seaborn
Install the required libraries:

pip install pandas matplotlib seaborn
📂 Project Structure
Gurgaon-Real-Estate-Analysis/
│
├── data.csv
├── real_estate_analysis.py
├── README.md
🔍 Data Cleaning
The project performs several preprocessing steps before analysis:

Removed duplicate records
Standardized column names
Converted numeric columns into proper data types
Cleaned categorical values
Converted RERA approval into Boolean values
📈 Business Questions Answered
The project answers the following analytical questions:

Which is the costliest flat in the dataset?
Which locality has the highest average property price?
Which locality has the highest rate per square foot?
Do Ready-to-Move properties cost more than Under Construction properties?
Do RERA-approved properties command a price premium?
How does property area impact price?
Which BHK configuration is the most expensive?
Which property type has the highest rate per square foot?
Which builders consistently price properties higher?
Are larger homes always more expensive per square foot?
📊 Visualizations
The project includes visualizations such as:

Area vs Price Scatter Plot
Area vs Rate Per Sqft Scatter Plot
These graphs help understand relationships between property size and pricing.

🚀 How to Run
Clone the repository
git clone https://github.com/yourusername/Gurgaon-Real-Estate-Analysis.git
Navigate to the project folder
cd Gurgaon-Real-Estate-Analysis
Install dependencies
pip install pandas matplotlib seaborn
Place the dataset (data.csv) inside the project folder.

Run the project

python real_estate_analysis.py
💡 Key Insights
Identifies the most expensive properties in Gurgaon.
Compares property prices across localities.
Evaluates pricing differences based on RERA approval.
Highlights premium builders.
Shows the relationship between area and pricing.
Provides useful visual insights for real estate analysis.
🔮 Future Improvements
Build an interactive dashboard using Power BI or Tableau.
Add predictive price modeling using Machine Learning.
Include interactive visualizations with Plotly.
Perform correlation analysis between multiple features.
Create a web application using Streamlit.
👨‍💻 Author
Kunal Rajput

Aspiring Data Analyst | Python | SQL | Excel | Power BI | Tableau

⭐ If you found this project helpful, consider giving it a Star on GitHub!
