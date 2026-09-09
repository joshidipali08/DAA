class Solution:
    def minimumMoves(self, s: str) -> int:

        moves = 0
        i = 0

        while i < len(s):

            # If we find X, we need one move
            if s[i] == 'X':
                moves += 1

                # One move changes 3 characters to O
                i += 3

            else:
                # If it is already O, move to the next character
                i += 1

        return moves