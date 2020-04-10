"""
Author: Joe Cranney
Project Title: Whatbot Helper
Project Description: Makes bulk task creation with What Bot a little more efficient
Date Created: 4/9/2020
Last Edited: 4/9/2020
"""

import os
import xlrd
import random
import string
import json


# Returns all tasks in provided xlsx file
def parse_tasks_from_spreadsheet(file_name):
    if ".xlsx" not in file_name:
        raise Exception("File name does not have .xlsx")
    else:
        workbook = xlrd.open_workbook("./config/" + file_name).sheet_by_index(0)
        items = []
        for row in range(1, workbook.nrows):
            name = workbook.cell(row, 0).value
            site = workbook.cell(row, 1).value
            sku = workbook.cell(row, 2).value
            one_checkout = workbook.cell(row, 3).value
            head_start = workbook.cell(row, 4).value
            size = workbook.cell(row, 5).value
            profile_name = workbook.cell(row, 6).value

            data = {
                "name": name,
                "site": site,
                "sku": sku,
                "one_checkout": one_checkout,
                "head_start": head_start,
                "size": size,
                "profile_name": profile_name
            }

            items.append(data)

        return items


def validate_files():
    if not os.path.exists("./config/billing.db"):
        raise Exception("billing.db does not exist in config, read instructions.")
    if os.path.exists("./config/groups.db"):
        os.remove("./config/groups.db")
    if os.path.exists("./config/tasks.db"):
        os.remove("./config/tasks.db")
    if os.path.exists("./config/groups.txt"):
        os.remove("./config/groups.txt")
    if os.path.exists("./config/tasks.txt"):
        os.remove("./config/tasks.txt")

    os.rename("./config/billing.db", "./config/billing.txt")


def rename_files():
    os.rename("./config/billing.txt", "./config/billing.db")
    os.rename("./config/groups.txt", "./config/groups.db")
    os.rename("./config/tasks.txt", "./config/tasks.db")


class Helper:

    def __init__(self, billing_db_path="./config/billing.txt", groups_db_path="./config/groups.txt",
                 tasks_db_path="./config/tasks.txt"):
        self.billing_db = billing_db_path
        self.groups_db = groups_db_path
        self.tasks_db = tasks_db_path
        open(self.groups_db, "w+")
        open(self.tasks_db, "w+")

    def get_billing_id(self, billing_name):
        for profile in open(self.billing_db):
            p = json.loads(profile)
            if p["name"] == billing_name:
                return p["_id"]

        raise Exception("Provided billing name does not exist in billing.db")

    def create_group(self, task):
        name = task["name"]
        head_start = task["head_start"]
        one_checkout = task["one_checkout"]
        site = task["site"]
        sku = task["sku"]

        group = {
            "_id": ''.join(random.choices(string.ascii_letters + string.digits, k=16)),
            "advanced": False,
            "customScrapers": [],
            "keywordsLink": sku,
            "name": name,
            "oneCheckoutPerProfile": eval(one_checkout),
            "preloadHeadstart": str(int(head_start)),
            "restockMode": "BRUTE",
            "scrapers": [],
            "siteId": site,
            "proxySetId": "none"
        }

        with open(self.groups_db, "a+") as f:
            json.dump(group, f)
            f.write("\n")

        return group["_id"]

    def write_tasks_to_files(self, data):
        for task in data:
            group_found = False

            # Check to see if the group is already made
            for group in open(self.groups_db):
                g = json.loads(group)
                if task["name"] == g["name"]:
                    group_found = True

                    task_data = {
                        "_id": ''.join(random.choices(string.ascii_letters + string.digits, k=16)),
                        "groupId": g["_id"],
                        "size": task["size"],
                        "billing": self.get_billing_id(task["profile_name"]),
                        "username": "",
                        "password": "",
                        "flavor": "base",
                        "preload": True,
                        "enabled": True
                    }

                    with open(self.tasks_db, "a+") as f:
                        json.dump(task_data, f)
                        f.write("\n")

            if not group_found:
                # The group has not been made, therefore it needs to be
                group_id = self.create_group(task)

                task_data = {
                    "_id": ''.join(random.choices(string.ascii_letters + string.digits, k=16)),
                    "groupId": group_id,
                    "size": task["size"],
                    "billing": self.get_billing_id(task["profile_name"]),
                    "username": "",
                    "password": "",
                    "flavor": "base",
                    "preload": True,
                    "enabled": True
                }

                with open(self.tasks_db, "a+") as f:
                    json.dump(task_data, f)
                    f.write("\n")
