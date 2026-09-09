class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:

        # Sort box types by units per box
        # Highest units should come first
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        total_units = 0

        # Go through each type of box
        for boxes, units in boxTypes:

            # Find how many boxes we can take
            boxes_to_take = min(boxes, truckSize)

            # Add their units
            total_units += boxes_to_take * units

            # Reduce the available space in the truck
            truckSize -= boxes_to_take

            # If the truck is full, stop
            if truckSize == 0:
                break

        return total_units