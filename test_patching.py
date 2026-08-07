from unittest.mock import patch


def announce():
    print("Winter is Coming")


def test_announce():
    with patch("builtins.print") as mock_print:
        announce()

        mock_print.assert_called_once_with("Winter is Coming")
