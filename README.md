Policy Impact Simulator (India)
An interactive data science project that answers a practical policy question:
“Which districts are most affected if government welfare spending is reduced?”
Instead of just building a vulnerability index, this project simulates real-world policy cuts and shows their impact at the district level.

What This Project Does
Combines multiple public datasets (Census, NFHS, SC/ST, etc.)
Builds a district-level vulnerability score
Simulates policy cuts (e.g., MGNREGA, welfare spending)
Shows how vulnerability changes when support is reduced
Provides a simple web interface (Flask) to explore results

Key Features
District-level analysis (Maharashtra)
Composite vulnerability scoring using:
ST population %
SC population %
Literacy rate
Deprivation score (education + clean fuel access)
Policy simulation:
Adjust % cut in welfare spending
See updated vulnerability instantly
Clean and merged real-world datasets

Tech Stack
Python (Pandas, NumPy)
Flask (Web app)
Data Sources:
Census 2011
NFHS-5
SC/ST population data
Jupyter Notebook (data processing)


## Project Files

- app.py - Flask app for running the policy simulation
- final_dataset.csv - cleaned district-level dataset used for modeling
- templates/index.html - frontend interface (district selection + simulation)
- govt.ipynb - data cleaning, merging, and feature engineering


How to Run
1. Clone the repo
git clone https://github.com/your-username/policy-impact-simulator-india.git
cd policy-impact-simulator-india

2. Install dependencies
pip install pandas flask

3. Run the app
python app.py

4. Open in browser
http://127.0.0.1:5000/

Example Use Case
Select a district (e.g., Nagpur)
Enter a policy cut (e.g., 20%)
The model recalculates vulnerability based on reduced support

This helps answer:
Which districts are most sensitive to policy cuts?
Where should policymakers avoid reducing spending?
Which regions need targeted protection?

Why This Project Matters
Most data science projects stop at prediction.
This project goes further:
Connects policy → impact
Focuses on decision-making
Builds a tool that NGOs, analysts, or journalists could actually use

Limitations
Currently limited to Maharashtra
MGNREGA integration is basic (can be improved with richer data)
Uses proxy indicators for deprivation

Future Improvements
Add more states
Improve MGNREGA dependency modeling
Add time trends (NFHS-4 vs NFHS-5)
Deploy online (Render / Railway)
Add visual charts (SHAP, maps)

Author 
Nayanah Soju


