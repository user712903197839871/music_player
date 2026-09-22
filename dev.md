

[ ] we stopped at validating test (emtpy ones) adding err codes, editing output where needed, note where output is altered

# first phase
- ## planned deadline: 10 days, ~1.5 weeks, due date 25/09/26
- ## features to be implemented:
    - ### schafolding of the project done, architecture, file structure
    - ### tests schafolding, a decent test pipeline and test architecture/logic 

    - ### a string matching function assembly
        - [X] add a basic string matching using levenshtein's algorithm
        - [X] add checking for full titles
            - [X] strip useless stuff
            - [X] parse format defined stuff, return status for a unrecognized format
            - [X] check for author, song names return according status
        - [X] in future: make exclude patterns a set, the rest need a loop for control over length

        - [ ] #1 add a check for channel name in author not found
        - [ ] #2 not really an issue, but make `collect_feats` in `str_match.py` return a struct not magic numbers
        - [ ] #3 make a webcrawler+claude and expand your testing dataset to 10k songs
        - [ ] !!!#4 in future: refactor the title->data functions in `str_match.py` to be more proffesional, reusable, efficient, and return more specific error codes
            - [ ] in future: think of a better way to check for featurings in ()
            - [ ] add more return err_codes in `SongTitleData`

    - ### a db object/the whole db logic implemented

