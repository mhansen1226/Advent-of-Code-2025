import re

pattern = re.compile(r"(\s)(\S)")


def split_add_zeros(s: str) -> list[str]:
    s = pattern.sub(r";\2", s)
    s = re.sub(" ", "0", s)
    return s.split(";")
