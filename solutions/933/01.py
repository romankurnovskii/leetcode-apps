from collections import deque


class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        # Add current request time
        self.queue.append(t)

        # Remove requests outside the 3000ms window
        while self.queue[0] < t - 3000:
            self.queue.popleft()

        # Return number of requests in the window
        return len(self.queue)
