# Test the functions in the cleaning.py
from utils import assert_equals
from cleaning import FF_wave


def test_rename_col(object):
    """
    Test the rename_col function in cleaning.py (FF_wave class)
    """
    print("Testing rename_col")
    assert_equals(['a', 'b', 'c', 'd', 'e', 'f'],
                  object.rename_col(['a', 'b', 'c', 'd', 'e', 'f']).columns)


def test_replacement(object):
    """
    Test the replacement function in cleaning.py (FF_wave class)
    """
    print("Testing replacement")
    assert_equals(2, object.replacement('f', 1, 2).loc[3, 'f'])


def test_gender_response(object):
    """
    Test the gender_response function in cleaning.py (FF_wave class)
    """
    print("Testing gender_response")
    assert_equals(1, object.gender_response().loc[1, 'gender'])


def test_avg_subscale(object):
    """
    Test the avg_subscale function in cleaning.py (FF_wave class)
    """
    print("Testing avg_subscale")
    assert_equals(4.0, object.avg_subscale('f', 'agg', 1).loc[1, 'f_agg_avg'])


def test_sum_subscale(object):
    """
    Test the sum_subscale function in cleaning.py (FF_wave class)
    """
    print("Testing sum_subscale")
    assert_equals(2.0, object.sum_subscale('del', 1).loc[2, 'del_sum'])


def main():
    interest_col = ['m5k2c', 'f5k2c', 'k5f1c', 'ch5ppvtss']
    interest_col2 = ['m5k2a', 'm5k2b', 'f5k2a', 'f5k2b', 'k5f1a', 'k5f1b']
    t = FF_wave("FF_wave_test_5rows.csv", interest_col2)
    t2 = FF_wave("FF_wave_test_9rows.csv", interest_col)
    t2.rename_col(['m_agg_1', 'f_agg_1', 'del_1', 'ppvt_ss'])
    t2.fill_nas([-6, -3, -9, -5, -1, -2])
    test_rename_col(t)
    test_replacement(t)
    test_gender_response(t2)
    test_avg_subscale(t2)
    test_sum_subscale(t2)


if __name__ == '__main__':
    main()
