

# Problem : play script

Write a program which reads a play script into objects, with unit tests.
- [x] Define classes Actor, Line, Play
- [x] Define a construtor on Play which takes a filename as a parameter. The play can be read from that file name.
- [X] Define a method on Play called title() which returns the title of the play
- [x] Define a method on Play called url() which returns a string holding the URL of the play
- [x] Define a method on Actor called all_lines() which returns a list all the Lines for that Actor
- [ ] Define a method on Line called actor() to indicate which actor should say that line
- [ ] Define a method on Line called next() which gives next line in the play
- [ ] Define a method on Line called previous() which gives the previous line in the play
- [ ] Define a method on Play called cast() which gives a list of all the Actors. The Actors are sorted in descending order of the number of lines each actor has (importance)
- [ ] Define a method on Play called actors() which lists all the Actors in ascending alphabetical order.
- [ ] Define a method on Play called all_lines() which gives a list of all the Lines in the play
- [ ] Define a method on Play called first_line() which gives the first Line in the play
- [ ] Define a method on Play called last_line() which gives the last Line in the play
- [ ] Define a method on Play called who_has_the_most_lines() which returns the Actor with the most lines
- [ ] Define a method on Play called words_by_occurrance() which returns a dict, such that the key is a word in the play, and the value is an int showing how many times the word is used.
- [ ] Define a method on Play called render() which returns a huge string holding the entire play, with Actors and Lines in a similar way to how it was read in.
        Each line should be wrapped to 40 characters for easy reading.

Demonstrate that this all works with unit tests as best as you can.

You have two sample plays to work with
- play1.txt
- play2.txt






