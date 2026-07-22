import pytest

from archive import Archive
from character import Character
from house import House


# Fixtures
@pytest.fixture
def archive():
    return Archive()


@pytest.fixture
def stark():
    return House("Stark", "Winter is Coming", "Direwolf", "The North")


@pytest.fixture
def jon(stark):
    return Character("Jon Snow", stark, "King in the North")


def test_add_character(archive, jon):
    # Act
    archive.add_character(jon)

    # Assert
    assert jon in archive.characters


def test_duplicate_character_is_not_added(archive, jon, stark):
    # Arrange
    duplicate_jon = Character("Jon Snow", stark, "Lord Commander")

    # Act
    archive.add_character(jon)
    archive.add_character(duplicate_jon)

    # Assert
    assert archive.characters == [jon]


def test_find_character_is_case_insensitive(archive, jon):
    # Arrange
    archive.add_character(jon)

    # Act
    result = archive.find_character("jOn sNoW")

    # Assert
    assert result == jon


def test_remove_character(archive, jon):
    # Arrange
    archive.add_character(jon)

    # Act
    archive.remove_character("Jon Snow")

    # Assert
    assert archive.characters == []
