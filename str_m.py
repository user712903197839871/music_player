# a file where i test string match functions

# lets define what we need for this one:
# we need strings to match even though the lengths are different and characters are arranged differently
# eg:
# 'track' matches 'treak'
# 'truck' matches 'track'
# 'truck slowed & reveb' matches 'track'
# 'crutk' matches 'truck'
# 'crater' not matches 'truck'
# lenghts can be different
# case insensitive, with numbers and special characters included, do not count spaces

# further down the line translate characters from languages

# in json we will have the frequency dict and the original name, 
# freq dict will be made once once on download of song
# it will lowercase, strip spaces dahses underlines

# from enum import Enum, auto  # aparently enums in python need to be imported
from bst import BST  # i had to build my own bst


SKIP_CHARACTERS = {" ", "-", "_"}

# below this one, strings are marked as not matched
# we also add [0.0, 0.1] to this depending on length
MATCHING_CHARACTERS_PROPORTION = 0.5


# meaning add 100% more score for each words that matches perfectly
WORD_MATCH_MULTIPLIER = 1
# meaning that if a str matches all of its words, 
# multiply by additional (WORD_MATCH_MULTIPLIER*2)%
FULL_STRING_WORD_MATCH_BUFF = WORD_MATCH_MULTIPLIER * 2


# LENGHT_EQUAL_RANGE = 3     # max difference between lengths to be considered a weak match
# both below used to calibrate proportion on different lengths
# cannot add more than 0.1 to proportion, regardless of length
# LENGTH_DEBUFF_CALIBER = -5     # subtracting from smaller length 
# LENGTH_DIVISOR_CALIBER = 10    # dividing adaos by this


def get_frequencies(string: str) -> dict[str, int]:
    """
    gets the frequencies of letters from a string
    ignores SKIP_CHARACTERS

    Args:
        takes a string

    Returns:
        a dict of character: appearences
    """

    if len(string) == 0:
        return {}

    frequencies: dict[str, int] = {}

    for c in string:
        if c not in SKIP_CHARACTERS:
            if c not in frequencies:
                frequencies[c] = 0

            frequencies[c] += 1

    return frequencies


def get_matching_words(s1: str, s2: str) -> float:
    """
    counts word matches between s1&s2 in O(n)
    if all words from s1 or s2 match with the other, we give a FULL_STRING_WORD_MATCH_BUFF buff

    Returns:
        a float [1, 1+min_words] 
        where each WORD_MATCH_MULTIPLIER step represents a word match
        it is a number representing %, multiplies score at the end
    """
    # we start the counter at 0, but add 1 at the end!
    # we multiply the score by this number, 
    # 1 means no change 1.1 means +10% score, 2 means +200% score etc.
    words_match: float = 0

    set_1: set[str] = set(s1.split(' '))
    set_2: set[str] = set(s2.split(' '))

    for word in set_1:
        if word in set_2:
            words_match += 1

    if words_match == len(set_1) or words_match == len(set_2):
        words_match += FULL_STRING_WORD_MATCH_BUFF

    # convert into % or in however we buff words mathces
    words_match /= WORD_MATCH_MULTIPLIER

    # we add 1, meaning if no matches we multiply by 1
    return words_match + 1
    

def strings_match(string1: str, string2: str, proportion: float=MATCHING_CHARACTERS_PROPORTION) -> float:
    """
    uses a algorithm to smartly match the strings given a proportion [0, 1]
    (default=MATCHING_CHARACTERS_PROPORTION)
    gets the strings' matching proportion from the smallest string length
    something like 'track1' will match 'track1: reveb slowed & speed up' matches

    Args:
        string1 & string2 strings to compare
        proportion: the proportion that need to match
        (Deprecated, using a match formula now)

    Returns:
        true if they match, 
        false otherwise
    """

    len_str1: int = len(string1)
    len_str2: int = len(string2)

    matching_characters: int = 0

    # we check case insensitive
    string1 = string1.lower()
    string2 = string2.lower()


    frequencies_str1 = get_frequencies(string1)
    frequencies_str2 = get_frequencies(string2)
    

    # get how many characters match, indiferent on position
    for c in frequencies_str1:
        if c in frequencies_str2:
            matching_characters += min(frequencies_str1[c], frequencies_str2[c])


    # proportion = proportion + (max(min(0, comparing_length - LENGTH_DEBUFF_CALIBER), LENGTH_DIVISOR_CALIBER) / LENGTH_DIVISOR_CALIBER**2)
    # (matching_characters / comparing_length) >= proportion

    matching_score = (matching_characters / max(len_str1, len_str2))
    length_penalty = (min(len_str1, len_str2) / max(len_str1, len_str2))
    word_match_buff = get_matching_words(string1, string2)

    return matching_score * length_penalty * word_match_buff



# "lost souls"
# "Baby Shark",
# "Friday",
# "The Hamster Dance Song",
# "Axel F",
# "Barbie Girl",
# "Macarena",
# "Who Let the Dogs Out",
# "My Humps",
# "Achy Breaky Heart",
# "Ice Ice Baby"

test: str = "Imagene"

arr = [
    "Bohemian Rhapsody", "Like a Rolling Stone", "Billie Jean", "Stayin Alive", "Purple Rain",
    "Heroes", "Superstition", "Dreams", "Gimme Shelter", "Blue Monday",
    "Smells Like Teen Spirit", "Lose Yourself", "Hey Jude", "What is Love", "Born to Run",
    "Imagine", "One More Time", "Creep", "Fast Car", "Bitter Sweet Symphony",
    "Enjoy the Silence", "In the Air Tonight", "Seven Nation Army", "Killing in the Name",
    "Clocks", "Take on Me", "Everybody Wants to Rule the World", "Sweet Child O Mine",
    "Hotel California", "Space Oddity", "Good Vibrations", "God Only Knows", "Respect",
    "What s Going On", "A Change Is Gonna Come", "Stand by Me", "Yesterday",
    "Strawberry Fields Forever", "Sultans of Swing", "Wish You Were Here",
    "Comfortably Numb", "Time", "Another Brick in the Wall", "Roxanne",
    "Every Breath You Take", "Message in a Bottle", "Don t Stop Believin",
    "Under Pressure", "Radio Ga Ga", "Mr Brightside", "Somebody Told Me", "Viva la Vida",
    "Yellow", "Scientist", "Fix You", "Paranoid Android", "Karma Police",
    "Fake Plastic Trees", "No Surprises", "Teardrop", "Unfinished Sympathy",
    "Massive Attack", "Glory Box", "Sour Times", "Roads", "Protection", "Angel",
    "Black Hole Sun", "Spoonman", "Fell on Black Days", "Jeremy", "Alive", "Black",
    "Even Flow", "Plush", "Interstate Love Song", "Creep", "Vasoline", "Big Empty",
    "Lithium", "Come as You Are", "In Bloom", "Heart Shaped Box", "All Apologies",
    "About a Girl", "Where Is My Mind", "Monkey Gone to Heaven", "Debaser",
    "Here Comes Your Man","Wave of Mutilation", "Hey", "Gouge Away", "Tame", "Gigantic",
    "Velouria", "Allison","Dig for Fire", "Here Comes the Sun", "Something"
]

real = [
    "Try", "Captain", "Aura", "Look at the Scars", "Narrative", "Bismarck", "Tantra", 
    "Prayers", "Hola Señorita", "Que que tu m'aimes ?", "Alors on danse", "Love Story",
    "On The Floor", "Amazing", "In Da Club", "Chantaje", "No Lie", "Mi Gente",
    "Taki Taki", "In Love", "Faded", "Angel", "Lean On", "Caliente",
    "In And Out Of Love", "Rainy Day", "X.O", "Despacito", "Sorry", "URUS", "Banger",
    "Весна", "When I Win", "Minor", "Marlboro", "DINERO", "Fire Man", "OneLove",
    "Last of Us"
]

sorted_matches: BST = BST(comparator=lambda a, b: a[0] < b[0])

for s in real:
    match_score: float = strings_match(test, s)

    sorted_matches.insert([match_score, s])

for s in arr:
    match_score: float = strings_match(test, s)

    sorted_matches.insert([match_score, s])


sorted_matches.in_order(func=sorted_matches.print_node, limit=10)

print(f"\ncompared for '{test}' in both")




"""
Miyagi feat. HLOY - Try (Official Audio)
Miyagi - Sorry (Official Audio)
Miyagi & Эндшпиль - Дама (Official Audio)
Miyagi & Эндшпиль - When I Win (Official Audio)
Miyagi feat. Ollane - Весна (Official Audio)
Miyagi - Captain (Official Audio)
Miyagi & Эндшпиль - Колизей (Official Audio)
Эндшпиль feat. onna badvibes - Aura (Official Audio)
Miyagi & Эндшпиль - Голгофа (Official Audio)
Гуф - Письмо домой (Альбом Сам и)
Miyagi & Эндшпиль - Я хочу любить (Official Audio)
Miyagi & Эндшпиль - Look at the Scars (Official Audio)
Miyagi - Marlboro (Official Audio)
Miyagi & Andy Panda - Minor (Mood Video)
Miyagi & Эндшпиль - Fire Man (Official Audio)
Miyagi & Эндшпиль feat. Oiseau & Papillon - Banger (Official Audio)
Miyagi & Andy Panda - Патрон (Official Audio)
Miyagi & Эндшпиль - Last of Us (Official Audio)
Miyagi & Эндшпиль - Narrative (Official Audio)
Miyagi feat. TumaniYO, KADI - Bismarck (Official Audio)
Miyagi feat. TumaniYO, KADI - Bismarck (Official Audio)
Miyagi & Andy Panda - Tantra (Official Audio)
TumaniYO feat. HLOY - Rainy Day (Official Audio)
KADI feat. Miyagi - Prayers (Official Audio)
Miyagi feat. KADI - Родная Пой (Official Audio)




GIMS, Maluma - Hola Señorita (Maria) [Official Video]
Konfuz — Ратата (Mood video)
Сергей Лазарев - Это все она (Official video)
Дима Билан - Держи
Miyagi & Эндшпиль & N.E.R.A.K. - Именно та (Audio)🎧 /Andy Panda
Сати Казанова feat. Arsenium - До рассвета
Тимати feat. Рекорд Оркестр - Баклажан (Лада Седан)
Тима Белорусских - Витаминка (Премьера официального клипа)
Эльбрус Джанмирзоев "Бродяга"
INNA - Caliente (by Play & Win) | Lyrics Video
Тима Белорусских - МОКРЫЕ КРОССЫ /OFFICIAL (трек)/
GIMS - Est-ce que tu m'aimes ? (Clip officiel)
Тима Белорусских - Незабудка
IOWA - Улыбайся
JONY - Титры
Dabro - Юность (премьера песни, 2020) | Звук поставим на всю
Егор Крид feat. Филипп Киркоров - Цвет настроения черный (премьера трека, 2018)
ФАБРИКА - Не родись красивой
NYUSHA / НЮША - Наедине (Official Clip) HD
Stromae - Alors on danse (Official Music Video)
Чёрные глаза
Егор Крид - Потрачу (премьера клипа, 2017)
HammAli & Navai - Птичка (Премьера клипа)
Indila - Love Story (Official Music Video)




Jennifer Lopez, Pitbull - On The Floor (Official Music Video)
INNA - Amazing (Official Video)
Jah Khalib - Лейла
Miyagi - Captain (Official Audio)
Miyagi & Andy Panda - Minor (Mood Video)
50 Cent - In Da Club (Official Music Video)
Shakira - Chantaje (Official Video) ft. Maluma
Элджей & Кравц - Дисконнект
Miyagi & Эндшпиль feat. Oiseau & Papillon - Banger (Official Audio)
Miyagi & Эндшпиль - Fire Man (Official Audio)
Sean Paul - No Lie ft. Dua Lipa
J Balvin, Willy William - Mi Gente (Official Video)
DJ Snake - Taki Taki ft. Selena Gomez, Ozuna, Cardi B (Official Music Video)
Miyagi & Эндшпиль feat. KADI - In Love (Official Audio)
Miyagi & Andy Panda - Tantra (Official Audio)
Alan Walker - Faded
Miyagi - Angel (Official Audio)
Miyagi & Эндшпиль & N.E.R.A.K. - Именно та (Audio)🎧 /Andy Panda
Major Lazer & DJ Snake - Lean On (feat. MØ) [Official 4K Music Video]
Major Lazer Official
INNA - Caliente | Official Music Video
NYUSHA / НЮША - Выше (Official clip) HD
In And Out Of Love (Slowed Version)
TumaniYO feat. HLOY - Rainy Day (Official Audio)
The Limba & Andro - X.O (Mood video)
Luis Fonsi - Despacito ft. Daddy Yankee




MORGENSHTERN - ПОЙДЕТ (Веселый Клип, 2023)
Miyagi - Sorry (Official Audio)
Miyagi - Captain (Official Audio)
Элджей & Rakhim - URUS (Official Video)
Miyagi & Эндшпиль feat. Oiseau & Papillon - Banger (Official Audio)
Каспийский Груз - На белом (feat. Гио Пика)
Miyagi feat. Ollane - Весна (Official Audio)
Miyagi & Эндшпиль - When I Win (Official Audio)
Miyagi & Эндшпиль - Колизей (Official Audio)
Гуф - Письмо домой (Альбом Сам и)
Miyagi & Эндшпиль - Санавабич (Music Clip)
Miyagi & Эндшпиль - В последний раз (Lyric Video) | YouTube Exclusive
104 - НЕ ЖАЛЬ (ft. Скриптонит, MiyaGi) [Official Audio]
Miyagi & Andy Panda - Minor (Mood Video)
Miyagi - Marlboro (Official Audio)
Наследство
THRILL PILL, Егор Крид & MORGENSHTERN - Грустная Песня
MORGENSHTERN - DINERO (Official Video, 2021)
Miyagi feat. KADI - Родная Пой (Official Audio)
Miyagi & Эндшпиль - Fire Man (Official Audio)
Miyagi & Andy Panda - Там Ревели Горы (Mood Video)
Miyagi & Эндшпиль - OneLove (Lyric video)/ Andy Panda
Miyagi - Настырный (Lyric video)
Miyagi & Эндшпиль - Last of Us (Official Audio)
Элджей & Кравц - Дисконнект








Дама
Весна
Колизей
Голгофа
Письмо домой
Я хочу любить
Патрон
Родная Пой
Ратата
Это все она
Держи
Именно та
До рассвета
Баклажан
Витаминка
Бродяга
МОКРЫЕ КРОССЫ
Незабудка
Улыбайся
Титры
Юность
Цвет настроения черный
Не родись красивой
Наедине
Чёрные глаза
Потрачу
Птичка
Дисконнект
Лейла
Выше
ПОЙДЕТ
На белом
Санавабич
В последний раз
НЕ ЖАЛЬ
Наследство
Грустная Песня
Родная Пой
Там Ревели Горы 
Настырный
Дисконнект




"""
