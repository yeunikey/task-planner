
#######################################################
#                                                     #
#                DEVELOPED BY YEUNIKEY                #
#               Task 1 / Python planner               #
#                                                     #
#                                                     #
#                     MIT License                     #
#         Copyright (c) 2025 Yerassyl Unerbek         #
#                                                     #
#######################################################

from utils import Utils
from pages import Page
from task_planner import Planner

class Application:

    def __init__(self):
        self.currentPage = Page.MENU
        self.planner = Planner()

    def start(self):
        self.menu()

    def add_task(self):
        
        print('')
        print('Add task')
        print('')

        title = input('Title: ')
        priority = input('Priority (high, medium, low): ')
        deadline = input('Deadline (2025-01-07): ')

        while True:
            print()
            confirm = input('Are you sure? (yes / no): ')
            
            if confirm == 'yes':
                self.planner.add_task(title, priority, deadline)

            self.menu()
            break
    
    def remove_task(self):

        print()
        print("Remove task")
        print()

        while True:
            title = input('Task title (or cancel): ')

            if title == 'cancel':
                self.menu()

            task = self.planner.find(title)

            if task is None:
                print('Task not found. Try again!')
                print()
                continue

            self.planner.remove_task(task)
            
            print()
            print('Task deleted!')
            print('Write something to go Menu')
            input('$: ')

            self.menu()
            
    def complete_task(self):
        print()
        print("Complete task")
        print()

        while True:
            title = input('Task title (or cancel): ')

            if title == 'cancel':
                self.menu()

            task = self.planner.find(title)

            if task is None:
                print('Task not found. Try again!')
                print()
                continue

            self.planner.mark_completed(task)
            
            print()
            print('Task completed!')
            print('Write something to go Menu')
            input('$: ')

            self.menu()

    def display_tasks(self):

        print()
        print("All tasks")
        print()

        for task in self.planner.tasks:
            deadline = task['deadline'].strftime(self.planner.DATE_FORMAT)

            print('')
            print(f"{task['title']}")
            print(f"  Priority: {task['priority']}");
            print(f"  Deadline: {deadline}");
            print(f"  Completed: {task['completed']}");
    
        while True:
            print()
            print('Write something to go Menu')
            input('$: ')

            self.menu()
            break;
    
    def save(self):
        
        print()
        print("Save tasks")
        print()

        while True:
            
            print('All tasks successfully saved to tasks.py')
            self.planner.save_to_file('out/tasks.json')

            print()
            print('Write something to go Menu')
            input('$: ')

            self.menu()
            break;
    
    def load(self):
        
        print()
        print("Load tasks")
        print()

        while True:
            
            print('All tasks successfully loaded from tasks.py')
            self.planner.load_from_file('out/tasks.json')

            print()
            print('Write something to go Menu')
            input('$: ')

            self.menu()
            break;
    
    def clear_completed(self):
        
        print()
        print("Clear completed tasks")
        print()

        while True:
            
            print('All completed tasks successfully remove')
            self.planner.clear_completed()

            print()
            print('Write something to go Menu')
            input('$: ')

            self.menu()
            break;

    def menu(self):
        Utils.clean()

        pages = [
            {
                "id": 1,
                "text": "Add task",
                "callback": self.add_task 
            },
            {
                "id": 2,
                "text": "Remove task",
                "callback": self.remove_task
            },
            {
                "id": 3,
                "text": "Complete task",
                "callback": self.complete_task 
            },
            {
                "id": 4,
                "text": "Display tasks",
                "callback":  self.display_tasks
            },
            {
                "id": 5,
                "text": "Save tasks",
                "callback":  self.save
            },
            {
                "id": 6,
                "text": "Load tasks",
                "callback":  self.load
            },
            {
                "id": 7,
                "text": "Clear completed",
                "callback":  self.clear_completed
            },
        ]

        print()
        print("Menu")
        print()

        for page in pages:
            print(f"  {page['id']}) {page['text']}")

        print()

        while True:
            id = int(input('Select: '))
            page = Utils.find_by_id(pages, id)

            if page is None:
                print("Page not found. Try again!")
                continue

            Utils.clean()
            callback = page['callback']
            callback()
            break

application = Application()
application.start()
