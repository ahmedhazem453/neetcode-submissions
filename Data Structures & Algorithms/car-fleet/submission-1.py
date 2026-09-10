class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(
            [(target - p, (target - p) / s) for p, s in zip(position, speed)],
            key=lambda x: x[0]
        )

        last = cars[0][1]
        ans = 1

        for car in cars[1:]:
            if car[1] <= last:
                continue
            else:
                last = car[1]
                ans += 1

        return ans