

import pytest
from assertpy import assert_that
from play_scripts import Actor,Play,Line

# tests for the code. 

#def test_that_actor_has_a_name():
    # citizen1 = Actor("citizen1")
    # assert_that( citizen1.name ).is_equal_to("citizen1")

# def test_that_two_actors_with_same_name_cant_be_added_to_a_set():
#     # Given...
#     citizen1 = Actor("citizen1")
#     citizen1_again = Actor("citizen1")
#     test_set = set()
#     test_set.add(citizen1)

#     # When ...
#     test_set.add(citizen1_again)

#     # Then...
#     assert_that( len(test_set) ).is_equal_to(1)

#def test_that_two_actors_with_same_name_are_equal():
    # # Given...
    # citizen1 = Actor("citizen1")
    # citizen1_again = Actor("citizen1")

    # # Then...
    # is_equal = False
    # if citizen1 == citizen1_again:
    #     is_equal = True
    # assert_that(is_equal).is_true()

def test_that_play_reads_in_actors():
    play1 = Play("play1.txt")

    assert_that( play1.actors ).is_not_empty()
    assert_that( play1.actors['CITIZEN 1']).is_not_none()

def test_that_play_reads_the_title():
    play1 = Play("play1.txt")

    assert_that( play1.title ).is_equal_to("The Legend of Lightning Larry")

def test_that_play_reads_the_url():
    play1 = Play("play1.txt")

    assert_that( play1.url ).is_equal_to("http://www.aaronshep.com/rt/RTE01.html")

def test_that_actor_lines_are_returned():
    play1 = Play("play1.txt")
    # Want to ask the programme what lines the actor has
    actor_name_we_want = "CITIZEN 1"
    actor : Actor = play1.get_actor(actor_name_we_want)
    assert_that( actor.lines) .is_not_empty()
    
    first_line_obj : Line = actor.lines[0]
    first_line_obj_in_text : str = first_line_obj.text
    sections_of_first_line = first_line_obj_in_text.split(" ")
    first_word_of_line = sections_of_first_line[0]
    assert_that(first_word_of_line).is_equal_to("Well,")

    expected_text = "Well, you've heard about gunfighting good guys like Wild Bill Hickok and Wyatt Earp."
    print(expected_text)
    print(first_line_obj_in_text)
    assert_that( first_line_obj_in_text).is_equal_to(expected_text)
   # The .text shows the proggramme that it needs to look at the text not the object

# Define a method on Actor called all_lines() which returns a list all the Lines for that Actor
def test_that_all_linbes_are_given_4_actor():
    play1 = Play("play1.txt")
    actor_name = "CITIZEN 1"
    citizen1 = play1.get_actor(actor_name)
    
    lines_got_back = citizen1.all_lines()
    assert_that( len(lines_got_back)).is_greater_than(0)
    assert_that( lines_got_back[0] ).is_equal_to("Well, you've heard about gunfighting good guys like Wild Bill Hickok and Wyatt Earp.")
