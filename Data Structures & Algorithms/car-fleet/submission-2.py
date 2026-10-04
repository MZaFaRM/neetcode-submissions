class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = len(position)
        sorted_cars = sorted(
            range(fleets),
            key=position.__getitem__,
            reverse=True,
        )
        prev_time = None
        for car in sorted_cars:
            time = (target - position[car]) / speed[car]
            if prev_time and time <= prev_time:
                fleets -= 1
            else:
                prev_time = time
        return fleets

        