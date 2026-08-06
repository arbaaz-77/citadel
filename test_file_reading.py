from unittest.mock import mock_open, patch


def read_castle():
    with open("castle.txt") as file:
        return file.read()


def test_read_castle():
    # Arrange
    fake_file = mock_open(read_data="Winterfell")

    # Act
    with patch("builtins.open", fake_file):
        result = read_castle()

    # Assert
    assert result == "Winterfell"
