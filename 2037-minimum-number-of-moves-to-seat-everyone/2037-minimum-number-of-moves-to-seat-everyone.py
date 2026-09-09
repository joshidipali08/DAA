class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:

        # Sort the seats
        seats.sort()

        # Sort the students
        students.sort()

        # Store the total number of moves
        moves = 0

        # Match each student with the corresponding seat
        for i in range(len(seats)):

            # Calculate how far the student needs to move
            distance = abs(seats[i] - students[i])

            # Add the distance to the total moves
            moves += distance

        return moves