# Definition for a street.
# class Street:
#     def openDoor(self):
#         pass
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
#     def moveLeft(self):
#         pass


class Solution:
    def houseCount(self, street: "Street", k: int) -> int:
        # Close k doors moving right
        for _ in range(k):
            street.closeDoor()
            street.moveRight()

        # Open the current door
        street.openDoor()

        # Move left and count until we find the open door
        res = 0
        while not street.isDoorOpen():
            street.moveLeft()
            res += 1

        return res
