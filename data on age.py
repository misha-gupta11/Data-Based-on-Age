import pandas as pd
import matplotlib.pyplot as plt

# Load the survey data
file_path = r'C:\Users\hp\Downloads\Perceptions on the Ohio River Waterway Survey.csv~'
survey_data = pd.read_csv(file_path)

# Extract relevant columns
columns_to_drop = ['Timestamp', 'What gender do you identify as?', 'What is your race?', 'Enter your zip code.']
survey_data_cleaned = survey_data.drop(columns=columns_to_drop)

# Rename columns for clarity
survey_data_cleaned.columns = [
    'Age', 
    'Cleanliness', 
    'Governmental Awareness', 
    'Resources Availability', 
    'Fun Activities Ease', 
    'Safety', 
    'Activities Rating', 
    'Pollution Control', 
    'Conservation Awareness', 
    'Parks and Boat Ramps'
]

# Plot histogram for each question based on Age
fig, axs = plt.subplots(len(survey_data_cleaned.columns) - 1, 1, figsize=(10, 30))

for i, column in enumerate(survey_data_cleaned.columns[1:]):
    axs[i].hist([survey_data_cleaned[survey_data_cleaned['Age'] == age][column].dropna() for age in survey_data_cleaned['Age'].unique()],
                label=survey_data_cleaned['Age'].unique(), bins=10, alpha=0.75)
    axs[i].set_title(f'{column} by Age')
    axs[i].set_xlabel(column)
    axs[i].set_ylabel('Frequency')
    axs[i].legend(title='Age Group')

plt.tight_layout()
plt.show()
