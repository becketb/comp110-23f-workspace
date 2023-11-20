"""Test my zip function."""

__author__ = "730529193"

from lessons.zip import zip 


def test_empty_inputs():
    """Test when both input lists are empty."""
    massage: list[str] = []
    price: list[int] = []
    result = zip(massage, price)
    assert result == {}


def test_valid_inputs():
    """Test when both input lists have the same length."""
    massage: list[str] = ["Full Body Massage", "Deep Tissue Massage", "Swedish Massage"]
    price: list[int] = [60, 70, 65]
    result = zip(massage, price)
    expected_result = {
        "Full Body Massage": 60,
        "Deep Tissue Massage": 70,
        "Swedish Massage": 65
    }
    assert result == expected_result


def test_mismatched_lengths():
    """Test when input lists have different lengths."""
    massage: list[str] = ["Full Body Massage", "Deep Tissue Massage"]
    price: list[int] = [60, 70, 65]
    result = zip(massage, price)
    assert result == {}
