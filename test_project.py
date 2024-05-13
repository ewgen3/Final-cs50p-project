from project import get_name, check_stock_exists, check_login
import pytest

def main():
    test_get_name()
    test_check_stock_exists()
    test_check_login()


def test_get_name():
    assert get_name("AAPL") == "Apple Inc."
    assert get_name("MSFT") == "Microsoft Corporation"
    with pytest.raises(ValueError):
        assert get_name("1234")
        assert get_name("BRUH")

def test_check_stock_exists():
    assert check_stock_exists("AAPL") == True
    assert check_stock_exists("TSLA") == True
    assert check_stock_exists("MICROSOFT") == False
    assert check_stock_exists("1234") == False
    assert check_stock_exists("BRUH") == False

def test_check_login():
    assert check_login("eugene") == True
    assert check_login("test") == True
    assert check_login("I_wont_ever_use_this_username") == False

if __name__ == "__main__":
    main()
