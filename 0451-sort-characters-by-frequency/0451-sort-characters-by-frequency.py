class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        res = ""
        for ch, count in sorted_freq:
            res += ch * count

        return res