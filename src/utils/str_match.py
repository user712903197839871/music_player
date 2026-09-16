"""
a file where i write string match functions

expected functionality
eg:
  'track' matches 'treak'
  'truck' matches 'track'
  'truck slowed & reveb' matches 'track'
  'crutk' matches 'truck'
  'crater' not matches 'truck'
case insensitive, with numbers and special characters included, do not count spaces
"""



from enum import Enum, auto  # aparently enums in python need to be imported

from Levenshtein import distance


class MatchStatus(Enum):
    # 1:1 match
    MATCH = auto()
    # 1-3 distance
    CLOSE = auto()
    # 4-5
    FAR_MATCH = auto()
    # a mismatch, strings are different
    MISSMATCH = auto()


def get_frequency(s: str) -> dict[str, int]:
    """gets the frequency of each character in s

    ?optimise using:
    ```
    from collections import Counter
    return Counter(s)
    ```

    Args:
        s (str)

    Returns:
        dict[str, int]: char and times it appeared
    """
    fr: dict[str, int] = {}
    
    for c in s:
        fr[c] = fr.get(c, 0) + 1

    return fr


def anagram(s1: str, s2: str) -> bool:
    """checks if s2 is anagram of s1

    Returns:
        bool: s1 is anagram of s2 or s2 is anagram of s1
    """
    return get_frequency(s1) == get_frequency(s2)


def str_match(str1: str, str2: str) -> MatchStatus:
    """checks (using Levenshteins distance algorithm) if str1 matches str2

    Args:
        str1 (str): jus a string
        str2 (str): jus a string

    Returns:
        int: the higher the number the less they match
    """

    # get levenshtein distance
    dist: int = distance(str1.lower(), str2.lower())

    # direct match
    if dist == 0:
        return MatchStatus.MATCH

    # here a check for anagrams is needed
    elif 0 < dist <= 5:
        if anagram(str1, str2):
            return MatchStatus.MISSMATCH

        # [1, 3]
        elif dist <=3:
            return MatchStatus.CLOSE

        # [4, 5]
        else:
            return MatchStatus.FAR_MATCH

    # everything else is a missmatch
    return MatchStatus.MISSMATCH

