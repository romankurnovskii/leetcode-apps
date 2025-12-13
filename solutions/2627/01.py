class Solution:
    def debounce(self, fn: 'Callable', t: int) -> 'Callable':
        timeout_id = None
        
        def debounced(*args):
            nonlocal timeout_id
            # Clear any existing timeout
            if timeout_id is not None:
                clearTimeout(timeout_id)
            
            # Set new timeout
            timeout_id = setTimeout(lambda: fn(*args), t)
        
        return debounced
