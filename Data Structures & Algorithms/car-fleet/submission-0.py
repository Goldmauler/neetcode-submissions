class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        x = []
        for i in range(n):
            time = (target - position[i]) / speed[i]
            x.append((position[i], time))
        x.sort(reverse=True)
        fleet = 0
        prev_time = 0
        for pos, time in x:
            if time > prev_time:
                fleet += 1
                prev_time = time

        return fleet
        


