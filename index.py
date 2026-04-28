python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    # Load the dataset
    return pd.read_excel(file_path)

def create_dashboard(data):
    # Create a summary of data
    data_summary = data.groupby(['Quarter', 'Gender']).sum().reset_index()

    # Plot gender distribution by quarter
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Quarter', y='Count', hue='Gender', data=data_summary)
    plt.title('Pensioners Distribution by Gender and Quarter')
    plt.xlabel('Quarter')
    plt.ylabel('Number of Pensioners')
    plt.legend(title='Gender')
    plt.show()

    # Generate a heatmap for demographic trends
    pivot_table = data.pivot_table(index='Quarter', columns='Gender', values='Percentage')
    plt.figure(figsize=(8, 6))
    sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='.1f')
    plt.title('Heatmap of Gender Distribution (%) by Quarter')
    plt.show()

if __name__ == "__main__":
    # File path to the dataset
    file_path = 'Distribution of Pensioners 2022.xlsx'

    # Load the data
    pension_data = load_data(file_path)

    # Create and display the dashboard
    create_dashboard(pension_data)
