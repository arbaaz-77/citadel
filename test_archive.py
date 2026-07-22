from archive import Archive
from character import Character
from house import House


def test_add_character():

    # Arrange
    stark = House("Stark", "Winter is Coming", "Direwolf", "The North")

    jon = Character("Jon Snow", stark, "King in the North")

    archive = Archive()

    # Act
    archive.add_character(jon)

    # Assert
    assert jon in archive.characters


def test_duplicate_character_is_not_added():

    # Arrange
    stark = House("Stark", "Winter is Coming", "Direwolf", "The North")

    jon = Character("Jon Snow", stark, "King in the North")
    duplicate_jon = Character("Jon Snow", stark, "Lord Commander")

    archive = Archive()

    # Act
    archive.add_character(jon)
    archive.add_character(duplicate_jon)

    # Assert
    assert archive.characters == [jon]


def test_find_character_is_case_insensitive():

    # Arrange
    stark = House("Stark", "Winter is Coming", "Direwolf", "The North")

    jon = Character("Jon Snow", stark, "King in the North")

    archive = Archive()

    # Act
    archive.add_character(jon)
    result = archive.find_character("jOn sNoW")

    # Assert
    assert result == jon


def test_remove_character():

    # Arrange
    stark = House("Stark", "Winter is Coming", "Direwolf", "The North")

    jon = Character("Jon Snow", stark, "King in the North")

    archive = Archive()

    # Act
    archive.add_character(jon)
    archive.remove_character("Jon Snow")

    # Assert
    assert archive.characters == []
