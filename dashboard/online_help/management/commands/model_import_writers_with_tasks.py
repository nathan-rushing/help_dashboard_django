from django.core.management.base import BaseCommand
from online_help.models import Task, Writers, TaskWriter
import pandas as pd

class Command(BaseCommand):
    help = 'Import unique writers from a CSV or Excel file'
    def handle(self, *args, **kwargs):
        df = pd.read_excel('online_help/management/dataset/Radiant_2025.1_help_assignments_v3_cleaned.xlsx', sheet_name='2025.1')

        task_count = 0
        writer_set = set()

        for _, row in df.iterrows():
            task = Task.objects.create(
                document=row['Documentation'],
                section=row['Section'],
                sub_section=row['Sub-sections'],
                comments=row.get('Comments', ''),
                SME=row.get('Subject Matter Expert/Engineering', ''),
                color=row.get('color', ''),
                completion=row.get('completion', ''),
            )
            task_count += 1

            writers = str(row.get('Writer', '')).split('\n')
            for writer_name in writers:
                writer_name = writer_name.strip()
                if writer_name:
                    writer, _ = Writers.objects.get_or_create(writer_name=writer_name)
                    writer_set.add(writer.pk)
                    TaskWriter.objects.get_or_create(task=task, writer=writer)

        self.stdout.write(self.style.SUCCESS(
            f'Imported {task_count} tasks and {len(writer_set)} unique writers with tasks successfully!'
        ))
