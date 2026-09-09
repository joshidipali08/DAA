class Solution:
    def maxDistance(self, colors: list[int]) -> int:

        # Store the maximum distance
        max_distance = 0

        # Check every house
        for i in range(len(colors)):

            # Compare it with every house after it
            for j in range(i + 1, len(colors)):

                # We need houses with different colors
                if colors[i] != colors[j]:

                    # Calculate the distance
                    distance = j - i

                    # Update maximum distance
                    max_distance = max(max_distance, distance)

        return max_distance