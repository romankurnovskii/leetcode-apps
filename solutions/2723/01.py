# JavaScript solution - Python wrapper
# Note: This is a JavaScript problem, but we provide a Python wrapper for consistency

"""
async function addTwoPromises(promise1, promise2) {
    const [val1, val2] = await Promise.all([promise1, promise2]);
    return val1 + val2;
}
"""

# For Python, we can simulate this with asyncio
import asyncio


class Solution:
    async def addTwoPromises(self, promise1, promise2):
        val1 = await promise1
        val2 = await promise2
        res = val1 + val2
        return res
