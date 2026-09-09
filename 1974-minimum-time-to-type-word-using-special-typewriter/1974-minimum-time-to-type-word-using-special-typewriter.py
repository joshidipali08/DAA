class Solution:
    def minTimeToType(self, word: str) -> int:

        # Pointer starts at 'a'
        current = 'a'

        # Total time
        time = 0

        # Go through each character
        for ch in word:

            # Find the distance between current and target character
            distance = abs(ord(ch) - ord(current))

            # Since the letters are in a circle,
            # we can also go the other way
            shortest_distance = min(distance, 26 - distance)

            # Move the pointer + type the character
            time += shortest_distance + 1

            # Move pointer to the current character
            current = ch

        return time