import json
from datetime import datetime

class Planner:
    
    PRIORITY_MAP = {'high': 1, 'medium': 2, 'low': 3}
    DATE_FORMAT = '%Y-%m-%d'

    def __init__(self):
        self.tasks = []

    def find(self, title):
        for task in self.tasks:
            if task['title'] == title:
                return task; 

    def add_task(self, title, priority, deadline):
        task = {
            'title': title,
            'priority': priority,
            'deadline': datetime.strptime(deadline, self.DATE_FORMAT),
            'completed': False
        }
        self.tasks.append(task)
        self.tasks.sort(key=self.task_sort_key)

    def remove_task(self, task):
        
        if task is None:
            return
        
        self.tasks.remove(task);
            
    def mark_completed(self, task):
        task['completed'] = True

    def clear_completed(self):
        self.tasks = [task for task in self.tasks if not task['completed']]

    @classmethod
    def task_sort_key(cls, task):
        return (cls.PRIORITY_MAP.get(task['priority'], float('inf')), task['deadline'])

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            tasks_with_string_dates = [
                {**task, 'deadline': task['deadline'].strftime(self.DATE_FORMAT)}
                for task in self.tasks
            ]
            json.dump(tasks_with_string_dates, file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            self.tasks = json.load(file)
            for task in self.tasks:
                task['deadline'] = datetime.strptime(task['deadline'], self.DATE_FORMAT)