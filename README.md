# CodeAlpha Data Visualization – Titanic Dataset

## Project Overview

This project was completed as part of the **CodeAlpha Data Visualization** task. The objective is to explore the Titanic passenger dataset, identify important patterns, and communicate the findings through clear and meaningful data visualizations.

Python libraries including **Pandas, Matplotlib, and Seaborn** were used for data analysis and visualization.

## Objectives

* Explore and understand the Titanic dataset.
* Analyze passenger survival patterns.
* Examine passenger class and gender distributions.
* Investigate age and fare distributions.
* Compare survival across passenger classes and genders.
* Create professional and easy-to-understand visualizations.
* Identify key insights from the dataset.

## Dataset

The dataset contains **418 passenger records** and **12 variables**.

### Main Variables

| Variable    | Description                       |
| ----------- | --------------------------------- |
| PassengerId | Unique passenger identifier       |
| Survived    | Survival status                   |
| Pclass      | Passenger class                   |
| Name        | Passenger name                    |
| Sex         | Passenger gender                  |
| Age         | Passenger age                     |
| SibSp       | Number of siblings/spouses aboard |
| Parch       | Number of parents/children aboard |
| Ticket      | Ticket number                     |
| Fare        | Passenger fare                    |
| Cabin       | Cabin information                 |
| Embarked    | Port of embarkation               |

The dataset contains missing values, particularly in the **Age, Fare, and Cabin** columns.

## Technologies and Libraries

* **Python 3**
* **Pandas** – data loading and analysis
* **Matplotlib** – data visualization
* **Seaborn** – statistical visualization
* **Git & GitHub** – version control and project sharing

## Project Structure

```text
CodeAlpha_DataVisualization/
│
├── data/
│   └── titanic.csv
│
├── notebooks/
│
├── visualizations/
│   ├── titanic_visualizations.py
│   └── output/
│       ├── age_distribution.png
│       ├── age_vs_fare.png
│       ├── fare_distribution.png
│       ├── gender_distribution.png
│       ├── passenger_class.png
│       ├── survival_by_class.png
│       ├── survival_by_gender.png
│       └── survival_distribution.png
│
├── .gitignore
└── README.md
```

## Visualizations Created

The project includes eight visualizations:

1. **Survival Distribution** – shows the number of passengers who survived and did not survive.
2. **Passenger Class Distribution** – shows the distribution of passengers across first, second, and third class.
3. **Gender Distribution** – compares the number of male and female passengers.
4. **Age Distribution** – shows the distribution of passenger ages.
5. **Fare Distribution** – displays the distribution of passenger fares.
6. **Survival by Gender** – compares survival status across gender.
7. **Survival by Passenger Class** – compares survival status across passenger classes.
8. **Age vs Fare** – explores the relationship between passenger age and fare, with survival status represented in the visualization.

## Key Findings

### Overall Survival

The dataset contains **418 passengers**:

* **152 passengers survived**
* **266 passengers did not survive**
* Survival rate: approximately **36.36%**
* Non-survival rate: approximately **63.64%**

### Passenger Class

Passenger distribution by class:

* **1st Class:** 107 passengers
* **2nd Class:** 93 passengers
* **3rd Class:** 218 passengers

The third-class group contains the largest number of passengers.

### Survival by Passenger Class

The supplied dataset shows:

| Passenger Class | Did Not Survive | Survived | Survival Rate |
| --------------- | --------------: | -------: | ------------: |
| 1st Class       |              57 |       50 |        46.73% |
| 2nd Class       |              63 |       30 |        32.26% |
| 3rd Class       |             146 |       72 |        33.03% |

First-class passengers have the highest survival rate among the three classes in this dataset.

### Age

The average passenger age is approximately:

**30.27 years**

The dataset contains passengers ranging from approximately **0.17 to 76 years old**.

### Fare

The average passenger fare is approximately:

**35.63**

The fare values range from **0 to approximately 512.33**.

### Gender

In the supplied dataset, the survival column shows a highly unusual pattern:

* Female records: **152 survived**
* Male records: **266 did not survive**

This pattern should be interpreted specifically as a characteristic of the **supplied dataset**, rather than as a general historical conclusion about Titanic survival.

## Data Visualization Approach

The project uses different visualization techniques depending on the type of information being analyzed:

* **Count plots** for categorical variables.
* **Histograms** for numerical distributions.
* **Scatter plots** for relationships between numerical variables.
* **Grouped count plots** for comparing survival across categories.

The visualizations were designed to make patterns and comparisons easier to understand.

## How to Run the Project

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project

```bash
cd CodeAlpha_DataVisualization
```

### 3. Install the required libraries

```bash
pip3 install pandas matplotlib seaborn
```

### 4. Run the visualization script

```bash
python3 visualizations/titanic_visualizations.py
```

The generated visualization images will be saved inside:

```text
visualizations/output/
```

## Results

The project successfully demonstrates how Python-based data visualization can be used to explore a real-world passenger dataset and communicate important patterns.

The analysis provides insights into:

* Passenger survival
* Passenger class
* Gender
* Age
* Fare
* Relationships between variables
* Survival patterns across different categories

## Future Improvements

Future versions of the project could include:

* Additional statistical analysis.
* More advanced interactive visualizations.
* Correlation analysis.
* Feature engineering.
* Interactive dashboards using Plotly or Power BI.
* A more detailed analysis of missing values.
* Comparison with additional Titanic datasets.

## Author

**Nithya**

Data Visualization Project
**CodeAlpha Internship / Task**
