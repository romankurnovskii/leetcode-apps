from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_freq = {}  # key -> frequency
        self.freq_to_keys = defaultdict(OrderedDict)  # frequency -> OrderedDict of keys
        self.key_to_val = {}  # key -> value

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1

        # Update frequency
        freq = self.key_to_freq[key]
        self.freq_to_keys[freq].pop(key)

        if not self.freq_to_keys[freq] and freq == self.min_freq:
            self.min_freq += 1

        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1][key] = None

        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val:
            # Update existing key
            self.key_to_val[key] = value
            self.get(key)  # Update frequency
            return

        # Remove LFU key if at capacity
        if len(self.key_to_val) >= self.capacity:
            # Remove least recently used key with min_freq
            lfu_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val[lfu_key]
            del self.key_to_freq[lfu_key]

        # Add new key
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = None
        self.min_freq = 1
