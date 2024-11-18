import pytest
import mt
import mt_credentials


def test_example_found():
    example_order_number = "305508971VAX20"
    client = mt.MailtrapClient(mt_credentials.get_token())
    client.set_inbox(mt_credentials.get_inbox_name())
    messages = client.get_messages().text
    found_result = mt.search_messages(messages, example_order_number)
    assert len(found_result) > 0


def test_example_not_found():
    example_order_number= "shouldNotBeFound"
    client = mt.MailtrapClient(mt_credentials.get_token())
    client.set_inbox(mt_credentials.get_inbox_name())
    messages = client.get_messages().text
    found_result = mt.search_messages(messages, example_order_number)
    assert len(found_result) == 0
