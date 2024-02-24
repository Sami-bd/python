class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        newGain = [0]
        for i, v in enumerate(gain):
            newGain.append(newGain[i]+v)
            
        newGain = max(newGain)

        return newGain