"""
Author: Joe Cranney
Project Title: Whatbot Helper
Project Description: Makes bulk task creation with What Bot a little more efficient
Date Created: 4/9/2020
Last Edited: 4/9/2020
"""

import sys
from whatbot import helper
from datetime import datetime

if __name__ == "__main__":
    print(f"[{datetime.now().strftime('%H:%M:%S.%f')}] - WHATBOT HELPER")
    print(f"[{datetime.now().strftime('%H:%M:%S.%f')}] - Created by @atcbackdoor")

    try:
        helper.validate_files()
    except Exception as e:
        print(f"[{datetime.now().strftime('%H:%M:%S.%f')}] - {e}")
        sys.exit()

    file_name = input(f"[{datetime.now().strftime('%H:%M:%S.%f')}] - Enter spreadsheet filename: ")

    try:
        tasks = helper.parse_tasks_from_spreadsheet(file_name)
        h = helper.Helper()
        h.write_tasks_to_files(tasks)
    except Exception as e:
        helper.rename_files()
        print(f"[{datetime.now().strftime('%H:%M:%S.%f')}] - {e}")
        sys.exit()

    helper.rename_files()
    print(f"[{datetime.now().strftime('%H:%M:%S.%f')}] - Done. Read instructions for next steps.")
