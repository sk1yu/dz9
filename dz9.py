class Task:
    def __init__(self, title, description, deadline, status="Не выполнено"):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = status

    def __str__(self):
        return f"Название: {self.title}\nОписание: {self.description}\nСрок выполнения: {self.deadline}\nСтатус: {self.status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Задача '{task.title}' добавлена.")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Задача '{title}' удалена.")
                return True
        print(f"Задача '{title}' не найдена.")
        return False

    def mark_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.status = "Выполнено"
                print(f"Задача '{title}' отмечена как выполненная.")
                return True
        print(f"Задача '{title}' не найдена.")
        return False

    def display_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
        else:
            print("Список задач:")
            for task in self.tasks:
                print(task)
                print("-" * 20)