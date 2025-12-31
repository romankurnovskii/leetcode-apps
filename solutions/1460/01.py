from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}  # id -> (station, time)
        self.times = defaultdict(lambda: [0, 0])  # (start, end) -> [total_time, count]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins.pop(id)
        route = (start_station, stationName)
        self.times[route][0] += t - start_time
        self.times[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        total_time, count = self.times[route]
        return total_time / count
