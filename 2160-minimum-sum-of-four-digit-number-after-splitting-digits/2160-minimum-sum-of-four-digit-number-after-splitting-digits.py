class Solution:
    def minimumSum(self, num: int) -> int:

        # Convert the number into a list of digits
        digits = [int(x) for x in str(num)]

        # Sort the digits from smallest to largest
        digits.sort()

        # Make the first number
        first = digits[0] * 10 + digits[2]

        # Make the second number
        second = digits[1] * 10 + digits[3]

        # Return the minimum sum
        return first + second