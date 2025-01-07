import os

class Utils:
    
    @staticmethod
    def clean():
        os.system('cls')

    @staticmethod
    def find_by_id(array, id):
        for obj in array:
            if obj['id'] == id:
                return obj