class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = []

        for i in range(len(gain)):

            if i == 0:
                altitude.append(0)

            altitude.append(altitude[i] + gain[i])

        return max(altitude)