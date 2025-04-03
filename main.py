from view.start_ui import StartUI
from database.score_db import create_table

if __name__ == '__main__':
    create_table()
    StartUI()