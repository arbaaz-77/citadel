from unittest.mock import MagicMock, call


def send_raven(send):
    send("Winter is Coming")
    send("The North Remembers")


def test_send_raven():
    fake_send = MagicMock()

    send_raven(fake_send)

    assert fake_send.call_count == 2

    fake_send.assert_has_calls(
        [
            call("Winter is Coming"),
            call("The North Remembers"),
        ]
    )
