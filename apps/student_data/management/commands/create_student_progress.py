from django.core.management.base import BaseCommand
from apps.student_data.models import StudentData, StudentProgress


class Command(BaseCommand):
    def handle(self, *args, **options):
        students = StudentData.objects.all()
        for student in students.iterator():
            try:
                print(student.progress)
            except StudentProgress.DoesNotExist:
                student_progress = StudentProgress.objects.create(
                    student_data=student, account_creation=2)
                student_progress.save()
