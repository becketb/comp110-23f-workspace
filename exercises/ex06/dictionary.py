"""Ex06- Practice With Dictionary Functions."""

__author__ = "730529193"


def invert(teams: dict[str, str]) -> dict[str, str]:
    """Defines the function of invert has the parameter of colors which is a dict of two string values and expects to return the same."""
    teams_invert = {}
    for key in teams:
        value = teams[key]
        if value in teams_invert:
            raise KeyError("Duplicate value encountered")
        teams_invert[value] = key
    return teams_invert


def favorite_color(colors: dict[str, str]) -> str:
    """Defines the function of favorite colors, takes colors as a dict of strings and returns a string (inverts values)."""
    color_count: dict[str, int] = {}
    most_popular_color = None

    for color in colors.values():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
        
        if most_popular_color is None or color_count[color] > color_count[most_popular_color]:
            most_popular_color = color

    return most_popular_color or "No favorite color"


def count(count_list: list[str]) -> dict[str, int]:
    """Defines the function of count, takes the count list a list of strings and returns a dictionary of strings and integers (correctly recognizes and updates favorite colors)."""
    count_result: dict[str, int] = {}
    
    for item in count_list:
        if item in count_result:
            count_result[item] += 1
        else:
            count_result[item] = 1
    
    return count_result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Defines alphabetizer which takes a list of words and produces a dictionary of strings and a list of strings (corresponding keys of letters to values of words that correspond to those letters)."""
    result: dict[str, list[str]] = {}
    for word in words:
        word_lower = word.lower()
        if word_lower and 'a' <= word_lower[0] <= 'z':
            first_letter = word_lower[0]
            if first_letter in result:
                result[first_letter] += [word]
            else:
                result[first_letter] = [word]
    
    return result


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Update attendance takes three parameters and uses the attendance log to update the attendance of students on a particular day."""
    if day in attendance_log:
        if student not in attendance_log[day]:
            attendance_log[day] = attendance_log[day] + [student]
    else:
        attendance_log[day] = [student]

    return attendance_log


attendance_log = {"Monday": ["Jackson", "Derek"], "Tuesday": ["Emily"]}
updated_log = update_attendance(attendance_log, "Tuesday", "Miranda")
expected_updated_log = {
    "Monday": ["Jackson", "Derek"],
    "Tuesday": ["Emily", "Miranda"],
}
assert updated_log == expected_updated_log