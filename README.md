<p><img src="https://whatbot.club/manual/images/logo.png" width="200" alt="whatbot logo"></p>

__whatbot-helper__ is a lightweight script that makes creating bulk tasks and groups more efficient and allows you to save time setting up. They are currently working on v1.0 which I assume will have something like this, however in the meantime feel free to use this. We are in no way affiliated with What Bot, you can find their official twitter page [here.](https://www.twitter.com/whatbotisthis)

# Getting Started

### Prerequisites

1. Fill out the task sheet [here](https://docs.google.com/spreadsheets/d/1kQetYxE-hNpLmeTGfuG9--M7yNo2JRNHYLdF3ws247c/edit?usp=sharing) and download as .xlsx
2. Install Python 3 [here](https://www.python.org/downloads/release/python-368/) and be sure to add to path during installation.
Once you have installed Python, download the repository.

The task sheet is pretty self-explanatory however if you would like to have multiple tasks in the same group, simply make the ``group name`` the same and when you run the script it will automatically group the tasks.


### Install
```python
pip install -r requirements.txt
```

### Usage
There are 3 main files that are involved within the whatbot task creation process. These files are billing.db, groups.db, and tasks.db

###### **billing.db**
Contains all of your profiles

###### **groups.db**
Contains all of the task groups

###### **tasks.db**
Contains all of your tasks

I mention this because it is important to understand what is needed for whatbot to understand your info. You will need to locate the billing.db file because it is needed in order to create your tasks.

#### Finding billing.db
Operating System | Path
---------------- | ----
MacOS | Library/Application Support/WhatBot/billing.db
Windows | %appdata%/WhatBot

_This folder is very important so make sure you can locate it, you will need it again._

Drag the billing.db and your task xlsx files into the ``config`` folder and open you terminal or cmd and type:
```python
python3 main.py
```

This will run the program. If you missed a step, you will get an error message telling you what is needed.

#### After script successfully runs
After it runs you will get a message saying: ``Done. Read instructions for next steps.`` At this point you need to navigate to the ``config`` folder and you will see 3 files. ``billing.db``, ``tasks.db``, and ``groups.db``. You will need to copy and paste these files into the whatbot folder from earlier where you got your original ``billing.db`` folder.

---

### Support

Feel free to contact me on Twitter [@atcbackdoor](https://www.twitter.com/atcbackdoor) if you are facing any issues or bugs. Please do NOT DM if you have not read the instructions, I will ignore.