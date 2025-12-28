class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        # First button's time is just its time value
        res = events[0][0]
        max_time = events[0][1]
        prev_time = events[0][1]

        # Iterate through remaining events
        for i in range(1, len(events)):
            button_idx, curr_time = events[i]
            # Time taken is the difference between consecutive presses
            press_time = curr_time - prev_time

            # Update if we found a longer press time
            # Or if equal, choose the button with smaller index
            if press_time > max_time or (press_time == max_time and button_idx < res):
                max_time = press_time
                res = button_idx

            prev_time = curr_time

        return res
