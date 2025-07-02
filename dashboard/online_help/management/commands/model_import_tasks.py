from django.core.management.base import BaseCommand
from online_help.models import Task
import pandas as pd

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # print(">>> Import command started")
        df = pd.read_excel('online_help/management/dataset/Radiant_2025.1_help_assignments_v3_cleaned.xlsx', sheet_name='2025.1')

        # Assuming you've already read the Excel file into a DataFrame called df
        filtered_df = df[[
            'Documentation',
            'Section',
            'Sub-sections',
            'Comments',
            'Subject Matter Expert/Engineering',
            'color'
        ]]

        # Optional: Rename columns to match Django model fields
        filtered_df.columns = ['document', 'section', 'sub_section', 'comments', 'SME', 'color']

        
        # print(f"Filtered rows: {filtered_df.shape[0]}")


        # Insert into the database
        for _, row in filtered_df.iterrows():
            Task.objects.create(
                document=row['document'],
                section=row['section'],
                sub_section=row['sub_section'],
                comments=row['comments'],
                SME=row['SME'],
                color=row['color']
            )

        
        # print("Running import command...")


        self.stdout.write(self.style.SUCCESS('Task imported successfully!'))





# If you want to delete all rows in the Task table before importing new data:
# You should place this in a separate management command file (e.g., delete_tasks.py) to avoid duplicate class names.

# class Command(BaseCommand):
#     help = 'Deletes all Task entries from the database'

#     def handle(self, *args, **options):
#         Task.objects.all().delete()
#         self.stdout.write(self.style.SUCCESS('All Task entries deleted successfully!'))

