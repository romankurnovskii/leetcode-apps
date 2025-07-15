## Description

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1. Return the highest altitude of a point.

Example:
```
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
```

Constraints:
```
- n == gain.length
- 1 <= n <= 100
- -100 <= gain[i] <= 100
```

> **Hint:**  Track the running sum and keep the maximum seen so far.

### Explanation

Let's imagine you're on a bike ride, and you start at sea level (altitude 0). Each number in the gain array tells you how much you go up or down at each step. We keep track of our current altitude as we go, and always remember the highest point we've reached so far.

We do this because it lets us find the maximum altitude in a single pass, without having to store all the altitudes. By updating the highest altitude as we go, we make our solution efficient and easy to understand.

### Solution

```python
def largestAltitude(gain):
    altitude = 0
    max_altitude = 0
    for g in gain:
        altitude += g
        max_altitude = max(max_altitude, altitude)
    return max_altitude
``` 