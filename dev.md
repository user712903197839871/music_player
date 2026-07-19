
## project plan
an alternative to Tmusic built from scratch by me for me;

alternatively, if i cant do the backend download audio from link thing, then it will just be a storing downloaded songs utility.



## what we need to implement
first things off

- [X] a string matching function, with the ability to check how many characters match in %
    - kinda done, but its not in % it's from 1-1+min-words

- remove remixes slowed  and other shi

- matching function should match intra-languages (translate characters) 

- a way to store stuff: music name; author(s); channel(s); urls;


## architecture

after some thought, and tradeoffs i decided to make the backend in **python**,

we will use json to store metadata + a url to original, and a path to the actual downloaded song

in json we will have the frequency dict and the original name, 
freq dict will be made once on download of song
it will lowercase, strip spaces dahses underlines

in that mini-database we will also store likes dislikes and other shi for our prefferences, though this is questionable but should be added, most of the times i will use the mandatory `shuffle` functionality

now another thing to keep in mind are the playlists;

and keeping track if a music/playlist is downloaded or is present (60% check);

i wanna make a separate json file each playlist will be a object with its own metadata and prefferences, and with a list what list for now should sustain operations like `downloaded_songs[playlist_array[song]]` -> a pointer to song or something, basically the values should be usable for the songs json object to easily access a song;

i opt for an array for easy sequential play and for easy randomized play, though i consider something like a custom mix of an array + map, storing index and value as keys and value as value, some tangled thing but working and efficient, though that could be an overkill

i also want playlists to be like able to flow into each other like cascades, not mandatory or default behaviour but as a feature, so arrays can store pointers to other playlist objects' arrays

also a feature like, download playlist as formated, like if you have a formated organized playlist on yt, you can download it as a playlist; also downloading not only individual tracks but all tracks from a playlist; organize and drag folders arrange them like you want

for no tho, i gotta do 

another thing is, we mannually input stuff, put slowed reveb and other shi, into a sepparate field (like modifier)


## a big problem (read about tis)
so we have a huge problem, there is no reliable way to get the author(s) and song name from the title, that's almost impossible;

### we have 3 ways:
- **we insert the full title** get fast downloads, playlist downloads, but search by author is sometimes incorrect and is deadly slow, no stats with authors & so on (which is not that bad actually if i think about this now)

- **we manually do everything** painfully slow, no playlist downloads, slow in developement, but we get 100% correct stuff, author stats, clean stats (no dirty full title text) is cleaner and more preffered, but again painfully slow in insertion

- **we make ai work** insert the full title make an opensource ai model parse them for you, slow a lil, needs to be double checked, still faster than the previous, + all its features, same complexity in developement, problem is it is also much much heavier (idk but a normal ai model should be at least 200MB which is kinda a lot)


so we have trade-offs, 

either great UX easy developement, not all functionalities, or partially

either painfull insertion of song (not that painfull actually but kinda slow for ~500-600 songs at once) but all included

either a middle-ground, easy insert (UX) though still should be slow (ai is slow) full functionalities, but will need double checking (still easier to fix ~50-100 songs then to insert ~500 manually) and much bigger, maybe too big, after some research, defenitelly too big, at least 4 GB RAM at least 1GB (defenetelly more than i expected), and speed wouldn't be that big of an improvement (like 100 songs per 10/15 minutes, i can do that myself)

absolute cinema; absolute trade-offs; we'll go with second variant for now

nuh uh, i decided to coombine, 1 & 2, we will have an automatic script run, but when in encounteres patterns it does not know flag it and stop, also flag a little when it encounteres 



## version control
i will add stuff here sometimes, maybe

initial commit
