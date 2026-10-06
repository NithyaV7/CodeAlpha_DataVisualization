import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load Titanic dataset
df = pd.read_csv("data/titanic.csv")

# Create output folder
os.makedirs("visualizations/output", exist_ok=True)

# Set visualization style
sns.set_theme(style="whitegrid")

# 1. Survival Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Survived")
plt.title("Titanic Passenger Survival Distribution")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("visualizations/output/survival_distribution.png")
plt.show()

# 2. Passenger Class Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Pclass")
plt.title("Passengers by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("visualizations/output/passenger_class.png")
plt.show()

# 3. Gender Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Sex")
plt.title("Passenger Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("visualizations/output/gender_distribution.png")
plt.show()

# 4. Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", bins=30, kde=True)
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("visualizations/output/age_distribution.png")
plt.show()

# 5. Fare Distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Fare", bins=30, kde=True)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("visualizations/output/fare_distribution.png")
plt.show()

# 6. Survival by Gender
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Sex", hue="Survived")
plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("visualizations/output/survival_by_gender.png")
plt.show()

# 7. Survival by Passenger Class
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Pclass", hue="Survived")
plt.title("Survival by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("visualizations/output/survival_by_class.png")
plt.show()

# 8. Age vs Fare
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Age", y="Fare", hue="Survived")
plt.title("Age vs Fare by Survival Status")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.tight_layout()
plt.savefig("visualizations/output/age_vs_fare.png")
plt.show()

print("All visualizations created successfully!")