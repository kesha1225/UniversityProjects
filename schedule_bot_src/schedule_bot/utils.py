import datetime
import os
import json
import random
from typing import List, Dict


def create_text_schedule(schedule: List[Dict[str, str]]) -> str:
    response = ""
    old_times = []
    i = 1
    for subject in schedule:
        group_info = subject["group"] + "\n" if subject["group"] else ""
        if group_info == "ИС-29 б\n" and not subject["link"].strip():
            continue
        response += (
            f"Пара №{i}:\n{subject['time']}\n{subject['title']}\n"
            f"{subject['teacher']}"
        )
        old_times.append(subject["time"])
        if subject["classroom"]:
            if group_info == "ИС-29 а\n":
                isb_classroom = schedule[schedule.index(subject) + 1]["classroom"]
                response += (
                    f"\nИС-29 а - {subject['classroom']}\nИС-29 б - {isb_classroom}"
                )
            else:
                response += f"\nИС-29 - {subject['classroom']}"
        if subject["link"].strip():
            response += f"\n{group_info} - {subject['link']}"
        if subject["note"]:
            response += f"\nПримечание - {subject['note']}"
        response += "\n--------------------\n"
        i += 1
    return response


def create_percent(user_id: int, now: datetime.datetime) -> int:
    random_data_file = os.path.dirname(__file__) + "/random_data.json"
    with open(random_data_file) as f:
        data: dict = json.loads(f.read())

    key = now.strftime("%d%m%Y") + str(user_id)
    if data.get(key) is not None:
        percent = data[key]
    else:
        percent = random.randint(0, 100)
        data[key] = percent
        with open(random_data_file, "w") as f:
            f.write(json.dumps(data))
    return percent
