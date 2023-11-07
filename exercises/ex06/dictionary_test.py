"""EX07-'dict' Unit Tests."""
from dictionary import invert, favorite_color, count, alphabetizer, update_attendance 

__author__ = "730529193"


def test_invert_use_case1() -> None:
    """Test invert function which should invert teams."""
    test_dict: dict[str, str] = {"Warriors": "Gold", "Wizards": "Blue", "Bucks": "Green"}
    result = invert(test_dict)
    expected_result = {"Gold": "Warriors", "Blue": "Wizards", "Green": "Bucks"}
    assert result == expected_result


def test_invert_use_case2() -> None:
    """Test invert function which should invert teams."""
    test_dict: dict[str, str] = {"Wizards": "Lakers", "Nuggets": "Pacers", "Heat": "Bulls"}
    result = invert(test_dict)
    expected_result = {"Lakers": "Wizards", "Pacers": "Nuggets", "Bulls": "Heat"}
    assert result == expected_result


def test_invert_edge_case() -> None:
    """Test invert function with a duplicate value, which should overwrite the existing value."""
    test_dict: dict[str, str] = {"Duke": "UNC", "Clemson": "UNC", "NCSU": "Wake"}
    result = invert(test_dict)
    assert result == {"UNC": "Clemson", "Wake": "NCSU"}


def test_favorite_color_use_case1() -> None:
    """Test favorite color function which should return Blue."""
    test_dict: dict[str, str] = {"Frederico": "Blue", "Bontanious": "Red", "Skyle": "Blue", "Drevoid": "Green"}
    result = favorite_color(test_dict)
    assert result == "Blue"


def test_favorite_color_use_case2() -> None:
    """Test favorite color function, which should return Red."""
    test_dict: dict[str, str] = {"Jon-John": "Red", "Janicious": "Red", "Jeolus": "Green", "Jilli": "Blue"}
    result = favorite_color(test_dict)
    assert result == "Red"


def test_favorite_color_edge_case() -> None:
    """Test favorite color function with an empty input, which should return 'No favorite color'."""
    test_dict: dict[str, str] = {}
    result = favorite_color(test_dict)
    assert result == "No favorite color"


def test_count_use_case1() -> None:
    """Test count function which should return the amount of times a color was referenced."""
    test_list: list[str] = ["Red", "Blue", "Red", "Green", "Blue"]
    result = count(test_list)
    expected_result = {"Red": 2, "Blue": 2, "Green": 1}
    assert result == expected_result


def test_count_use_case2() -> None:
    """Test count function which should return the amount of times a fruit was referenced."""
    test_list: list[str] = ["Pear", "Banana", "Mango", "Pear"]
    result = count(test_list)
    expected_result = {"Pear": 2, "Banana": 1, "Mango": 1}
    assert result == expected_result


def test_count_edge_case() -> None:
    """Test count function with an empty input, which should return an empty dictionary."""
    test_list: list[str] = []
    result = count(test_list)
    assert result == {}


def test_alphabetizer_use_case1() -> None:
    """Test alphabetizer function which should return the fruits in alphabetical order."""
    test_list: list[str] = ["apple", "banana", "cherry", "apricot", "blueberry"]
    result = alphabetizer(test_list)
    expected_result = {
        "a": ["apple", "apricot"],
        "b": ["banana", "blueberry"],
        "c": ["cherry"]
    }
    assert result == expected_result


def test_alphabetizer_use_case2() -> None:
    """Test alphabetizer function which should return the animals in alphabetical order."""
    test_list: list[str] = ["dog", "caiman", "elephant", "dingo"]
    result = alphabetizer(test_list)
    expected_result = {
        "c": ["caiman"],
        "d": ["dog", "dingo"],
        "e": ["elephant"]
    }
    assert result == expected_result


def test_alphabetizer_edge_case() -> None:
    """Test alphabetizer function with input containing numeric characters, which should return an empty dictionary."""
    test_list: list[str] = ["123", "456", "789", "101112"]
    result = alphabetizer(test_list)
    assert result == {}


def test_update_attendance_use_case1() -> None:
    """Test update attendance function which should add Miranda to Tuesday."""
    test_dict: dict[str, list[str]] = {"Monday": ["Jackson", "Derek"], "Tuesday": ["Emily"]}
    updated_log = update_attendance(test_dict, "Tuesday", "Miranda")
    expected_updated_log = {
        "Monday": ["Jackson", "Derek"],
        "Tuesday": ["Emily", "Miranda"],
    }
    assert updated_log == expected_updated_log


def test_update_attendance_use_case2() -> None:
    """Test update attendance function which should add Alitorion to Wednesday."""
    test_dict: dict[str, list[str]] = {}
    updated_log = update_attendance(test_dict, "Wednesday", "Alitorion")
    expected_updated_log = {"Wednesday": ["Alitorion"]}
    assert updated_log == expected_updated_log


def test_update_attendance_edge_case() -> None:
    """Test update attendance function with updating an existing day's attendance."""
    test_dict: dict[str, list[str]] = {"Monday": ["Jackson", "Derek"], "Tuesday": ["Emily"]}
    updated_log = update_attendance(test_dict, "Tuesday", "Derek")
    expected_updated_log = {
        "Monday": ["Jackson", "Derek"],
        "Tuesday": ["Emily", "Derek"],
    }
    assert updated_log == expected_updated_log