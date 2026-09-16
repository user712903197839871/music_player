# testing reading/writing to json
# tis' gonna look like a sql file actually

import src.utils.json_crud

# creating the initial schema
dataset = {}
id: int = 0


def add_song(song_name: str):
    dataset[id] = dict()
    dataset[id]["url"] = f"https://youtube.com/{song_name}"
    dataset[id]["full title"] = ""
    dataset[id]["stripped title"] = ""
    dataset[id]["song name"] = f"{song_name}"
    dataset[id]["authors"] = ["", ""]
    dataset[id]["channels"] = ["", ""]
    dataset[id]["audio"] = f"path_to_'{song_name}'"
    dataset[id]["image"] = f"path_to_'{song_name}'_thumbnail, if allowed"
    dataset[id]["metadata"] = dict()
    dataset[id]["metadata"]["listened"] = 0
    dataset[id]["metadata"]["skiped"] = 0
    dataset[id]["metadata"]["likes"] = 0
    dataset[id]["metadata"]["dislikes"] = 0


# arr = [
#     "Bohemian Rhapsody", "Like a Rolling Stone", "Billie Jean", "Stayin Alive", "Purple Rain",
#     "Heroes", "Superstition", "Dreams", "Gimme Shelter", "Blue Monday",
#     "Smells Like Teen Spirit", "Lose Yourself", "Hey Jude", "What is Love", "Born to Run",
#     "Imagine", "One More Time", "Creep", "Fast Car", "Bitter Sweet Symphony",
#     "Enjoy the Silence", "In the Air Tonight", "Seven Nation Army", "Killing in the Name",
#     "Clocks", "Take on Me", "Everybody Wants to Rule the World", "Sweet Child O Mine",
#     "Hotel California", "Space Oddity", "Good Vibrations", "God Only Knows", "Respect",
#     "What s Going On", "A Change Is Gonna Come", "Stand by Me", "Yesterday",
#     "Strawberry Fields Forever", "Sultans of Swing", "Wish You Were Here",
#     "Comfortably Numb", "Time", "Another Brick in the Wall", "Roxanne",
#     "Every Breath You Take", "Message in a Bottle", "Don t Stop Believin",
#     "Under Pressure", "Radio Ga Ga", "Mr Brightside", "Somebody Told Me", "Viva la Vida",
#     "Yellow", "Scientist", "Fix You", "Paranoid Android", "Karma Police",
#     "Fake Plastic Trees", "No Surprises", "Teardrop", "Unfinished Sympathy",
#     "Massive Attack", "Glory Box", "Sour Times", "Roads", "Protection", "Angel",
#     "Black Hole Sun", "Spoonman", "Fell on Black Days", "Jeremy", "Alive", "Black",
#     "Even Flow", "Plush", "Interstate Love Song", "Creep", "Vasoline", "Big Empty",
#     "Lithium", "Come as You Are", "In Bloom", "Heart Shaped Box", "All Apologies",
#     "About a Girl", "Where Is My Mind", "Monkey Gone to Heaven", "Debaser",
#     "Here Comes Your Man","Wave of Mutilation", "Hey", "Gouge Away", "Tame", "Gigantic",
#     "Velouria", "Allison","Dig for Fire", "Here Comes the Sun", "Something"
# ]
# real = [
#     "Try", "Captain", "Aura", "Look at the Scars", "Narrative", "Bismarck", "Tantra", 
#     "Prayers", "Hola Señorita", "Que que tu m'aimes ?", "Alors on danse", "Love Story",
#     "On The Floor", "Amazing", "In Da Club", "Chantaje", "No Lie", "Mi Gente",
#     "Taki Taki", "In Love", "Faded", "Angel", "Lean On", "Caliente",
#     "In And Out Of Love", "Rainy Day", "X.O", "Despacito", "Sorry", "URUS", "Banger",
#     "Весна", "When I Win", "Minor", "Marlboro", "DINERO", "Fire Man", "OneLove",
#     "Last of Us"
# ]
# for song in arr:
#     add_song(song)
#     id += 1
# for song in real:
#     add_song(song)
#     id += 1


