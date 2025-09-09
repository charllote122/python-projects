# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset

def load_and_explore():
    try:
        # Load Iris dataset from sklearn
        iris = load_iris()
        
        # Convert to DataFrame
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
        
        print("First 5 rows of the dataset:")
        print(df.head())
        
        print("\nDataset info:")
        print(df.info())
        
        print("\nChecking for missing values:")
        print(df.isnull().sum())
        
        # No missing values in Iris dataset, but if there were, you could fill or drop them like this:
        # df = df.fillna(method='ffill')  # forward fill
        # or
        # df = df.dropna()
        
        return df
    
    except Exception as e:
        print(f"Error loading or exploring dataset: {e}")
        return None

# Task 2: Basic Data Analysis

def basic_analysis(df):
    try:
        print("\nBasic statistics for numerical columns:")
        print(df.describe())
        
        print("\nMean values grouped by species:")
        group_mean = df.groupby('species').mean()
        print(group_mean)
        
        # Observations example:
        print("\nObservations:")
        print(" - Setosa generally has smaller sepal and petal sizes compared to Versicolor and Virginica.")
        print(" - Virginica has the largest average petal length and width.")
        
        return group_mean
    
    except Exception as e:
        print(f"Error during analysis: {e}")

# Task 3: Data Visualization

def create_visualizations(df):
    try:
        sns.set(style="whitegrid")
        
        # 1. Line Chart: Plot sepal length trend across samples (just as example of line plot)
        plt.figure(figsize=(8, 5))
        plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length (cm)', color='blue')
        plt.title('Sepal Length Trend Across Samples')
        plt.xlabel('Sample Index')
        plt.ylabel('Sepal Length (cm)')
        plt.legend()
        plt.show()
        
        # 2. Bar Chart: Average petal length per species
        plt.figure(figsize=(8, 5))
        sns.barplot(x='species', y='petal length (cm)', data=df, palette='viridis')
        plt.title('Average Petal Length per Species')
        plt.xlabel('Species')
        plt.ylabel('Petal Length (cm)')
        plt.show()
        
        # 3. Histogram: Distribution of sepal width
        plt.figure(figsize=(8, 5))
        sns.histplot(df['sepal width (cm)'], bins=20, kde=True, color='green')
        plt.title('Distribution of Sepal Width')
        plt.xlabel('Sepal Width (cm)')
        plt.ylabel('Frequency')
        plt.show()
        
        # 4. Scatter Plot: Sepal length vs Petal length colored by species
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette='deep')
        plt.title('Sepal Length vs Petal Length by Species')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Petal Length (cm)')
        plt.legend(title='Species')
        plt.show()
        
    except Exception as e:
        print(f"Error during visualization: {e}")

# Main Execution

def main():
    df = load_and_explore()
    if df is not None:
        basic_analysis(df)
        create_visualizations(df)

if __name__ == "__main__":
    main()
