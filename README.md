
Policy Impact Simulator (India)

An interactive data science project that answers a simple but important question:

Which districts are most affected if government welfare spending is reduced?

Instead of just building a vulnerability index, this project simulates policy cuts and shows their impact at the district level.

What This Project Does
Combines multiple public datasets (Census, NFHS, SC/ST, etc.)
Builds a district-level vulnerability score
Simulates policy cuts (e.g., MGNREGA, welfare spending)
Shows how vulnerability changes after the cut
Provides a simple Flask-based web interface

Key Features
District-level analysis (Maharashtra)
Composite vulnerability score using:
ST population %
SC population %
Literacy rate
Deprivation score (education + clean fuel access)

Policy simulation:
Adjust % cut in welfare spending
Instantly see updated vulnerability
Cleaned and merged real-world datasets

Tech Stack
Python (Pandas, NumPy)
Flask (web app)
Data sources:
Census 2011
NFHS-5
SC/ST datasets
Jupyter Notebook (data processing)

Project Files
app.py – Flask backend for simulation
final_dataset.csv – merged district dataset
templates/index.html – user interface
govt.ipynb – data cleaning and feature engineering

How to Run
git clone https://github.com/your-username/policy-impact-simulator-india.git
cd policy-impact-simulator-india
pip install pandas flask
python app.py
Open in browser:
http://127.0.0.1:5000/

Example Use Case
Select a district (e.g., Nagpur)
Enter a policy cut (e.g., 20%)
View updated vulnerability score

This helps answer:
Which districts are most sensitive to cuts?
Where should spending not be reduced?
Which areas need protection?

Why This Project Matters
Most data science projects stop at prediction.
This one focuses on decision-making:
connects policy → impact
provides an interactive tool
has a real-world use case

Limitations
Currently limited to Maharashtra
MGNREGA integration is basic
Uses proxy indicators for deprivation

Future Improvements
Expand to other states
Improve MGNREGA modeling
Add time trends (NFHS-4 vs NFHS-5)
Deploy online
Add visualizations (charts, maps)

Author
Nayanah Soju
