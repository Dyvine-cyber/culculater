import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"
url = "https://www.kaggle.com/datasets/himanshunakrani/iris-dataset"
df = pd.read_csv(url)

print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())



for column in df.select_dtypes(include=['float64']).columns:
    df[column].fillna(df[column].median(), inplace=True)


print("\nBasic Statistics:")
print(df.describe())


print("\nMean values by Species:")
group_means = df.groupby('species').mean()
print(group_means)


print("\nObservations from Analysis:")
print("- The dataset has 150 rows and 5 columns (4 numerical, 1 categorical).")
print("- No missing values were found in the Iris dataset.")
print(f"- {group_means.index[0]} has the largest average sepal length ({group_means['sepal_length'].max():.2f}).")
print(f"- {group_means.index[2]} has the largest average petal length ({group_means['petal_length'].max():.2f}).")


sns.set(style="whitegrid")

# 1. Line chart: Average sepal length per species (simulating a trend)
plt.figure(figsize=(8, 6))
for species in df['species'].unique():
    species_data = df[df['species'] == species]
    plt.plot(species_data.index, species_data['sepal_length'], label=species)
plt.title('Sepal Length Trend Across Species')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.show()


plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='petal_length', data=df)
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()


plt.figure(figsize=(8, 6))
sns.histplot(df['sepal_width'], bins=20, kde=True)
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', size='species', data=df)
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.show()