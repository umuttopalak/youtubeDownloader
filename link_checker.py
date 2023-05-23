import re

def link_checker(text):
    pattern = r"(https?://)?(www\.)?youtube\.com/watch\?v=\w+"
    match = re.search(pattern, text)

    if match:
        print("Bu bir YouTube bağlantısı içeriyor.")
        return True

    return False