class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's cycle detection (tortoise and hare)
        slow = fast = nums[0]

        # Find the intersection point in the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Find the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
