# JavaScript solution - Python wrapper
# Note: This is a JavaScript problem, but we provide a Python wrapper for consistency

"""
function debounce(fn, t) {
    let timeoutId;
    return function(...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => fn.apply(this, args), t);
    };
}
"""

# For Python, we can simulate this
from threading import Timer

class Solution:
    def debounce(self, fn, t):
        timeout_id = None
        
        def debounced(*args, **kwargs):
            nonlocal timeout_id
            if timeout_id:
                timeout_id.cancel()
            timeout_id = Timer(t / 1000.0, lambda: fn(*args, **kwargs))
            timeout_id.start()
        
        return debounced

