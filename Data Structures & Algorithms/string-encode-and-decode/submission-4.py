from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        # Converts ["yes", "!@#$%^&*()"] -> "3#yes10#!@#$%^&*()"
        encoded = []
        for word in strs:
            encoded.append(f"{len(word)}#{word}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # Find where the '#' delimiter is
            j = i
            while s[j] != "#":
                j += 1

            # Get length of the word
            length = int(s[i:j])

            # Extract exact word based on recorded length
            start = j + 1
            end = start + length
            res.append(s[start:end])

            # Jump pointer past the extracted word
            i = end

        return res