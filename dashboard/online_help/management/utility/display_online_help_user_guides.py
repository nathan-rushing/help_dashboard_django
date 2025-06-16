import pandas as pd

"""
Displays the sections from the Radiant 2025.1 help assignments dataset.
"""
# section_column = df['Section'].dropna()
# print(section_column)


# Load your Excel file
df = pd.read_excel('online_help/management/dataset/Radiant_2025.1_help_assignments_v3_copy.xlsx', sheet_name='online_help_user_guides')

# Drop rows where any of the key columns are missing
df = df.dropna(subset=['Section', 'Sub-sections', 'color'])

# Group data and convert to structured list
grouped = df.groupby('Section').apply(
    lambda x: list(zip(x['Sub-sections'], x['color']))
).reset_index(name='subsections')

# Convert to list of dicts for the template
section_data = grouped.to_dict(orient='records')


# Convert to list of dicts for the template
section_data = grouped.to_dict(orient='records')

# # Group by Section, and collect Sub-section + Color as tuples
# grouped = df.groupby('Section').apply(
#     lambda x: list(zip(x['Sub-sections'], x['color']))
# ).reset_index(name='Subsection_Color_Pairs')

# Display results
# for _, row in grouped.iterrows():
#     print(f"Section: {row['Section']}")
#     print("Sub-sections and Colors:")
#     for sub, color in row['Subsection_Color_Pairs']:
#         print(f" - {sub} (Color: {color})")
#     print()


# print(section_data)
# print(grouped['Section'])
# print(grouped)