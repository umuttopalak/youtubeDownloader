import re

def link_checker(text):
    pattern = r"(https?://)?(www\.)?youtube\.com/watch\?v=\w+"
    match = re.search(pattern, text)

    if match:
        return True

    return False