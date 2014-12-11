""" Account Module """


class Account(object):
    """ Create Account Class """
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def existing_account(self, account_number):
        """ Check if account exists """
        self.account_number = account_number
        account_number != 'None'
