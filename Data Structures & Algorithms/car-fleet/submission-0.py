class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position,speed))
        position,speed = map(list,zip(*pairs))
        time = []
        n = len(position)

        for i in range(n):
            curr = (target - position[i]) / speed[i]
            time.append(curr)
        
        fleet = 0
        while time:
            curr = time[-1]
            while time and time[-1] <= curr:
                time.pop()
            fleet += 1

        return fleet
        
