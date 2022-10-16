import pandas
import matplotlib.pyplot as plt 
import pytest
from assertpy import assert_that

# The test data looks like this:
#	    A	B	C	D
# one	5	4	2	6
# two 	4	6	4	3
# three	8	6	4	9
# four	1	3	8	4


@pytest.fixture  # this is an annotation that pytest understands. 
def df():
    df= pandas.read_excel("play-data.XLSX")
    return df 

    # print (df)
    # print(df['A'])


    # a = df['A']  #this makes a variable in the form of a series, so the function to find the average and stuff id different from 
    # # when you are doing things with a dataframe. 


def test_we_can_get_mean_value_of_a_column(df : pandas.DataFrame ):
    a : pandas.Series = df['A'] # Take the column A from the data frame.
    mean_of_column = a.mean()
    expected_value : float = 4.5
    assert_that(mean_of_column).is_equal_to(expected_value)


def test_we_can_find_sum_of_a_column(df : pandas.DataFrame ):
    a : pandas.Series = df['A'] # Take the column A from the data frame.
    sum_of_column = a.sum()
    expected_value : float = 18.0
    assert_that(sum_of_column).is_equal_to(expected_value)
    
def test_for_mean_in_different_way(df : pandas.DataFrame ):
    a : pandas.Series = df['A'] # Take the column A from the data frame.
    sum_of_column = a.sum()
    row_number = a.count()
    hand_mean= sum_of_column/row_number
    assert_that(hand_mean).is_equal_to(4.5)

def test_for_mean_in_dumb_way(df : pandas.DataFrame ):
    a : pandas.Series = df['A'] # Take the column A from the data frame.
    total = 0 
    count = 0
    for value in a:
        total += value
        count +=1 
    mean = total / count
    assert_that(mean).is_equal_to(4.5)

def test_we_can_rotate_the_whole_dataframe( df : pandas.DataFrame ):
    transposed_df : pandas.DataFrame = df.transpose()
    #print(transposed_df)
    # Transposed_df looks like this:
    #               0     1      2     3
    # Unnamed: 0  one  two   three  four
    # A             5     4      8     1
    # B             4     6      6     3
    # C             2     4      4     8
    # D             6     3      9     4

    assert_that(transposed_df[2][1]).is_equal_to(8)

#def test_we_can_multiply_all_elements_in_a_dataframe(df : pandas.DataFrame ):
    # The test data looks like this:
    #	    A	B	C	D
    # one	5	4	2	6
    # two 	4	6	4	3
    # three	8	6	4	9
    # four	1	3	8	4
    COLUMNS=1
    
    #multiplied_df=df.iloc[1:4,1:4]#.mul(3,axis=COLUMNS)  # Multiple it all by 3.
    # The multiplied data looks like this:
    # Unnamed: 0   A   B   C   D
    # 0        oneoneone  15  12   6  18
    # 1     two two two   12  18  12   9
    # 2  threethreethree  24  18  12  27
    # 3     fourfourfour   3   9  24  12
    print(multiplied_df)

    sample_value= df[2][1] 
    assert_that(sample_value).is_equal_to(44)

df= pandas.read_excel("play-data.XLSX")
print(df.at[0,'A'])

print(df.loc[])
