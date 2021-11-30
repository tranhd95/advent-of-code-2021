#!/usr/bin/env python
import sys
import requests
import os

from dotenv import load_dotenv


def download_input(day, year=2020, suffix="in"):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    load_dotenv()
    req = requests.get(url, cookies={"session": os.getenv("COOKIE")})
    if req.status_code != 200:
        raise Exception(req.content.decode("utf-8"))
    fname = f"data/{str(day).zfill(2)}.{suffix}"
    print(f"Saving {fname}...")
    save_file(req.content.decode("utf-8"), fname)


def save_file(content, filename):
    with open(filename, "w") as f:
        f.write(content)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid arguments", sys.argv)
        exit()
    day = sys.argv[1]
    download_input(day)
