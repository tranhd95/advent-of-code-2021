import requests
import os
from dotenv import load_dotenv


def iter_inp(day, year=2021):
    yield from iter_lines(puzzle_input(day, year))


def iter_lines(inp):
    for line in inp.split("\n"):
        if line:
            yield line


def puzzle_input(day, year=2021):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    load_dotenv()
    r = requests.get(url, cookies={"session": os.getenv("COOKIE")})
    return r.content.decode("utf-8")
