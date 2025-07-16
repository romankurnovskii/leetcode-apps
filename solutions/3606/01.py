from typing import List


def validateCoupons(
    code: List[str], businessLine: List[str], isActive: List[bool]
) -> List[str]:
    allowed_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
    priority = {line: i for i, line in enumerate(allowed_lines)}

    def is_valid_code(s):
        return s and all(c.isalnum() or c == "_" for c in s)

    valid = []
    for c, b, a in zip(code, businessLine, isActive):
        if is_valid_code(c) and b in allowed_lines and a:
            valid.append((priority[b], b, c))
    valid.sort()  # sorts by businessLine priority, then code lex
    return [c for _, _, c in valid]
