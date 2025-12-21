# NOTE: This problem only accepts JavaScript solutions on LeetCode.
# Below is the JavaScript solution:

"""
/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timeoutId = null;

    return function(...args) {
        // Clear any existing timeout
        if (timeoutId !== null) {
            clearTimeout(timeoutId);
        }

        // Set new timeout
        timeoutId = setTimeout(() => {
            fn(...args);
        }, t);
    };
};
"""
