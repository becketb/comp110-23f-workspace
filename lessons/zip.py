"""Combining two lists into a dictionary."""

__author__ = "730529193"


def zip(massage: list[str], price: list[int]) -> dict[str, int]:
    """Zip has two paramaters 'massage' and 'price' which return a list of strings and a list of intgers respectively and the expected return value is a dict of string and integers."""
    if not massage or not price:
        return {}
    if len(massage) != len(price):
        return {}
    result_dict = {}
    for i in range(len(massage)):
        result_dict[massage[i]] = price[i]
        # maps the index of the massage list to the index of the price list.
    
    return result_dict


massage = ["Full Body Massage", "Deep Tissue Massage", "Swedish Massage"]
price = [60, 70, 65]
result_dict = zip(massage, price)
print(result_dict)
