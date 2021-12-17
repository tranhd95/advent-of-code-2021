from dataclasses import dataclass

from utils import rinput


@dataclass
class Probe:
    position: tuple[int, int]
    velocity: tuple[int, int]

    def move(self):
        x, y = self.position
        vel_x, vel_y = self.velocity
        self.position = (x + vel_x, y + vel_y)
        if vel_x > 0:
            vel_x -= 1
        elif vel_x < 0:
            vel_x += 1
        vel_y -= 1
        self.velocity = (vel_x, vel_y)
        return self.position


def parse(inp):
    x_raw, y_raw = inp.split(", ")
    x_from, x_to = tuple(map(int, x_raw.split("=")[1].split("..")))
    y_from, y_to = tuple(map(int, y_raw.split("=")[1].split("..")))
    return (x_from, x_to), (y_from, y_to)


def is_overshot(y, y_min):
    return y < y_min


def is_within(x, y, x_min, x_max, y_min, y_max):
    return (x_min <= x <= x_max) and (y_min <= y <= y_max)


def solve1(inp):
    (x_min, x_max), (y_min, y_max) = parse(inp)
    records = []
    for x_vel in range(1, x_max):
        for y_vel in range(1, 100):  # 200 IQ heuristics
            probe = Probe((0, 0), (x_vel, y_vel))
            x, y = probe.position
            highest = y
            while not is_overshot(y, y_min):
                x, y = probe.move()
                highest = max(y, highest)
                if is_within(x, y, x_min, x_max, y_min, y_max):
                    records.append(highest)
                    break
    return max(records)


def solve2(inp):
    (x_min, x_max), (y_min, y_max) = parse(inp)
    distinct_cnt = 0
    for x_vel in range(1, x_max * 2):
        for y_vel in range(y_min, abs(y_max * 2)):  # 300 IQ heuristics
            probe = Probe((0, 0), (x_vel, y_vel))
            x, y = probe.position
            while not is_overshot(y, y_min):
                x, y = probe.move()
                if is_within(x, y, x_min, x_max, y_min, y_max):
                    distinct_cnt += 1
                    break
    return distinct_cnt


print(solve1(rinput(17)))
print(solve2(rinput(17)))
