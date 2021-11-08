"""
Hackathon project
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from tinydb import TinyDB, Query

db = TinyDB('database.json')
user = Query()
users = db.table('User')

class mm(toga.App):


    def startup(self):

        if users.all() != '':
            print('signed in')

            main_box = toga.Box()

            self.main_window = toga.MainWindow(title=self.formal_name)
            self.main_window.content = main_box
            self.main_window.show()

        elif users.all() == ' ':
            print('new user')
            main_box = toga.Box()

            self.main_window = toga.MainWindow(title=self.formal_name)
            self.main_window.content = main_box
            self.main_window.show()







def main():
    return mm()
