Policy Cut Impact Simulator
Data-driven analysis of how budget cuts affect vulnerable populations
Abstract
The Policy Cut Impact Simulator is a web-based analytical tool that models the consequences of reductions in public welfare spending. It provides a structured way to evaluate how different socio-economic groups are affected when funding for government programs is reduced.

The system combines demographic indicators with a weighted scoring model to produce a clear measure of vulnerability and highlight the most impacted communities within a district.

Problem Statement
Public policy decisions often involve budget reallocations or cuts. However, the downstream impact on vulnerable populations is rarely transparent or quantified in an accessible way.

This project addresses that gap by providing:

A quantitative framework for assessing vulnerability

A visual interface for exploring policy outcomes

Immediate insights into which groups are most affected

System Overview
The application is built as a lightweight web system with a clear separation between data processing and user interaction.

User Flow:

Select a district

Choose a welfare program

Adjust the budget cut percentage

View computed impact and insights

The system responds instantly with:

A vulnerability score

Risk classification

Demographic breakdown of impact

Contextual explanation

Methodology
The simulation is based on a weighted vulnerability model derived from key socio-economic indicators.

Core Indicators
Scheduled Tribe (ST) population share

Scheduled Caste (SC) population share

Literacy rate

Deprivation index

MGNREGA dependency

Scoring Model
Each indicator contributes to the final vulnerability score with predefined weights:

Indicator	Weight
ST Population	0.25
SC Population	0.15
Literacy	0.20
Deprivation	0.20
MGNREGA Dependency	0.20

Budget cuts amplify certain factors (deprivation and dependency), reflecting real-world sensitivity to funding changes.

Risk Classification
Score Range	Interpretation
< 0.2	Low Risk
< 0.4	Moderate Risk
< 0.6	High Risk
≥ 0.6	Very High Risk

Technical Architecture
Backend
Flask-based web server

Pandas for data processing and transformation

Custom simulation function for impact computation

Frontend
Server-rendered HTML (Jinja templating)

Responsive CSS layout

Vanilla JavaScript for interactivity

Data Layer
CSV-based dataset containing district-level indicators

Preprocessing includes normalization and cleaning

Key Features
Real-time simulation of budget cuts

Multi-factor vulnerability scoring

Interactive UI with dynamic controls

Visual breakdown of impact across demographic groups

Context-aware insights generated from data

Project Structure

├── app1.py              # Application logic and simulation engine
├── index.html           # User interface (Jinja template)
├── final_dataset.csv    # Source dataset
├── .gitignore
Setup Instructions
Clone the Repository
Bash

git clone https://github.com/your-username/policy-cut-simulator.git
cd policy-cut-simulator
Install Dependencies
Bash

pip install flask pandas
Run the Application
Bash

python app1.py
Access the Application
Open a browser and navigate to:


http://127.0.0.1:5000/
Sample Output Interpretation
A higher vulnerability score indicates that a district is more sensitive to funding reductions. The simulator identifies the dominant contributing factor, enabling targeted policy analysis.

For example:

High ST population → greater reliance on public employment programs

High deprivation → limited fallback options

Low literacy → reduced adaptability to economic shocks

Design Principles
Clarity over complexity

Data transparency

Immediate feedback for user actions

Minimal yet informative visual design

Potential Extensions
Integration with geospatial mapping

Scenario comparison across multiple districts

Machine learning-based impact prediction

Inclusion of additional welfare schemes

Exportable analytical reports

Use Cases
Policy analysis and research

Academic projects in public policy or data science

Demonstration of data-driven decision tools

Portfolio project for showcasing full-stack and analytical skills

License
This project is released under the MIT License.

Author Note
This project reflects an effort to combine data science with public policy analysis, focusing on interpretability and real-world relevance. It is designed to demonstrate both technical implementation and the ability to model complex societal problems in a structured way.