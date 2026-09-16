# import pytest
from src.utils.str_match import str_match, MatchStatus


class SongNames:
    short: str = "Clava"
    medium: str = "La Calavasa"
    long: str = "La pulga normala clava"

def test_match():
    assert str_match(SongNames.short, "Clava") == MatchStatus.MATCH

def test_match_long():
    assert str_match(SongNames.long, SongNames.long) == MatchStatus.MATCH

def test_typo():
    assert str_match(SongNames.short, "Ckava") == MatchStatus.CLOSE

def test_aditional_letter():
    assert str_match(SongNames.short, "Cleava") == MatchStatus.CLOSE

def test_letters_reorder():
    assert str_match(SongNames.short, "lavaC") == MatchStatus.MISSMATCH

def test_multiple_typos():
    assert str_match(SongNames.long, "La puga normal ckaaa") == MatchStatus.FAR_MATCH

def test_different_str():
    assert str_match(SongNames.long, "bruhh what are these names") == MatchStatus.MISSMATCH

def test_str_missmatch():
    assert str_match(SongNames.medium, SongNames.short) == MatchStatus.MISSMATCH

def test_different_str_lens():
    assert str_match(SongNames.short, "bruhh what are these names") == MatchStatus.MISSMATCH

def test_small_difference():
    # notice how case sensitivity does not matter
    assert str_match(SongNames.medium, "calavasa") == MatchStatus.CLOSE

def test_real_case():
    assert str_match("lost soul", "lost souls") == MatchStatus.CLOSE


# add a big test to test speed
