""" wrapper for mailtrap client
"""

import json
import requests


class MailtrapClient:
    """client for dealing with mailtrap"""

    mailtrap_url = "https://mailtrap.io/api"
    account_id = "887445"
    inbox_id = "0"

    def __init__(self, token):
        self.headers = {"Accept": "application/json", "Api-Token": token}

    def get_inboxes(self):
        """return inboxes availables"""
        url = self.mailtrap_url + "/accounts/" + self.account_id + "/inboxes"
        return requests.get(url, headers=self.headers, timeout=15)

    def set_inbox(self, inbox_name):
        """set inbox id to search for use on further requests"""
        inboxes_response = self.get_inboxes()
        if inboxes_response.status_code != 200:
            raise FileNotFoundError("Could not access inboxes")

        for inbox in json.loads(inboxes_response.text):
            if inbox["name"] == inbox_name:
                self.inbox_id = str(inbox["id"])
                return

        raise FileNotFoundError("requested inbox does not exist")

    def get_messages(self):
        """get all messages"""
        url = (
            self.mailtrap_url
            + "/accounts/"
            + self.account_id
            + "/inboxes/"
            + self.inbox_id
            + "/messages"
        )
        return requests.get(url, headers=self.headers, timeout=15)


def search_messages(searched_messages, subject_search):
    """search given message subjects for a search string"""
    result = []
    if isinstance(searched_messages, str):
        searched_messages = json.loads(searched_messages)
    for message in searched_messages:
        if subject_search in message["subject"]:
            result.append(message)
    return result
