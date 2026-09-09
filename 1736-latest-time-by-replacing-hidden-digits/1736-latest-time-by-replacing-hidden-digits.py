class Solution:
    def maximumTime(self, time: str) -> str:

        # Convert string into a list
        time = list(time)

        # Check the first hour digit
        if time[0] == '?':
            if time[1] == '?' or time[1] <= '3':
                time[0] = '2'
            else:
                time[0] = '1'

        # Check the second hour digit
        if time[1] == '?':
            if time[0] == '2':
                time[1] = '3'
            else:
                time[1] = '9'

        # Check the first minute digit
        if time[3] == '?':
            time[3] = '5'

        # Check the second minute digit
        if time[4] == '?':
            time[4] = '9'

        # Convert list back to string
        return ''.join(time)