from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date
from .models import Project, Task, Tasklog


class ProjectTest(TestCase):

    def setUp(self):
      
        self.user = User.objects.create_user(username="testuser", password="12345")

        self.project = Project.objects.create(
            name="Project Alpha",
            description="Test Project Description",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 2, 1),
            status="In_progress",
            user=self.user
        )

        self.task1 = Task.objects.create(
            name="Task 1",
            description="First task",
            status="Not_Started",
            start_date=date(2025, 1, 5),
            end_date=date(2025, 1, 7),
            project=self.project
        )

        self.task2 = Task.objects.create(
            name="Task 2",
            description="Second task",
            status="Completed",
            start_date=date(2025, 1, 10),
            end_date=date(2025, 1, 12),
            project=self.project
        )

        self.log1 = Tasklog.objects.create(task=self.task1, msg="Started working...")
        self.log2 = Tasklog.objects.create(task=self.task1, msg="Halfway done")


    def test_user_create(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_project_create(self):
        self.assertEqual(str(self.project), "Project Alpha")
        self.assertEqual(self.project.status, "In_progress")

    def test_task_create(self):
        self.assertEqual(str(self.task1), "Task 1")
        self.assertEqual(self.task1.status, "Not_Started")
        self.assertEqual(str(self.task2), "Task 2")

    def test_tasklog_create(self):
        self.assertEqual(str(self.log1), "Log for Task 1")
        self.assertEqual(self.log1.msg, "Started working...")
        self.assertEqual(self.log2.msg, "Halfway done")

    def test_project_user_relationship(self):
        self.assertEqual(self.project.user.username, "testuser")

    def test_project_tasks_relationship(self):
        self.assertEqual(self.project.tasks.count(), 2)
        self.assertIn(self.task1, self.project.tasks.all())
        self.assertIn(self.task2, self.project.tasks.all())

    def test_task_tasklog_relationship(self):
        self.assertEqual(self.task1.logs.count(), 2)
        self.assertIn(self.log1, self.task1.logs.all())

    def test_deleting_user_cascades_to_project(self):
        self.user.delete()
        self.assertEqual(Project.objects.count(), 0)

    def test_deleting_project_cascades_to_tasks(self):
        self.project.delete()
        self.assertEqual(Task.objects.count(), 0)

    def test_deleting_task_cascades_to_tasklogs(self):
        self.task1.delete()
        self.assertEqual(Tasklog.objects.count(), 0)
