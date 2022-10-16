from assertpy import assert_that
from solution import Solution 
solution= Solution()

def test_that_anything_is_made():
    input_string = "cat"
    #  c
    #  a    
    #  t
    rows = 3
    assert_that(solution.convert(input_string,rows)).is_equal_to("cat")

def test_catdog():
    input_string = "catdog"
     # c   o
     # a d g
     # t
    rows = 3
    assert_that(solution.convert(input_string,rows)).is_equal_to("coadgt")

def test_catd():
    input_string = "catd"
    # c   
    # a d 
    # t
    rows = 3
    assert_that(solution.convert(input_string,rows)).is_equal_to("cadt")
    
def test_given_example_1():
    input_string = "PAYPALISHIRING"
    # P   A   H   N
    # A P L S I I G
    # Y   I   R
    rows = 3
    assert_that(solution.convert(input_string,rows)).is_equal_to("PAHNAPLSIIGYIR")

def test_larger_rows(): 
    input_string = "longercat"
    rows = 4
    # l     c
    # o   r a
    # n e   t
    # g
    assert_that(solution.convert(input_string, rows)).is_equal_to("lcoranetg")

def test_katie_hard_test_rows_6():
    input_string = "thistestisreallylong6"
    # t        r        6
    # h      s e      g
    # i     i  a     n
    # s   t    l   o
    # t s      l l
    # e        y
    rows = 6
    assert_that(solution.convert(input_string,rows)).is_equal_to("tr6hsegiianstlotslley")
    
    
def test_given_problem_2():
    input_string = "PAYPALISHIRING"
    rows = 4
    # P     I    N
    # A   L S  I G
    # Y A   H R
    # P     I
    assert_that(solution.convert(input_string,rows)).is_equal_to("PINALSIGYAHRPI")


def test_given_problem_3():
    input_string = "A"
    rows = 1
    # A
    assert_that(solution.convert(input_string,rows)).is_equal_to("A")
    


def test_long_thing_one_row():
    input_string = "ABCD"
    rows = 1
    # A B C D
    assert_that(solution.convert(input_string,rows)).is_equal_to("ABCD")


def test_long_thing_two_rows():
    input_string = "ABCD"
    rows = 2
    # A C
    # B D
    assert_that(solution.convert(input_string,rows)).is_equal_to("ACBD")