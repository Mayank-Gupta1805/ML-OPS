from mytest import square
def test_square_gives_correct_value():
    subject=square(2)

    assert subject==4
    