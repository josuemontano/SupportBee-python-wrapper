class Requester:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Ticket:
    def __init__(self, id, subject, content, requester, starred=False, spam=False):
        """
        :param ticket_id: ID of the ticket
        :param subject: Subject of the ticket. REQUIRED for posting data
        :param starred: Starred
        :param requester_email:  Specifies the email of the requester of the ticket. REQUIRED for posting data
        :param content: Specifies the content of the ticket. Either text or html must be present.
                        Please look at the example above. REQUIRED for posting data
        :return:
        """
        self.id = id
        self.subject = subject
        self.content = content
        self.requester = requester
        self.starred = starred
        self.spam = spam

    def __eq__(self, other):
        return self.id == other.id
