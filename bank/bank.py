""" Bank Module """


class Bank(object):
    """ Created Bank Class"""
    def __init__(self):
        """ Initializer """
        self.accounts = {}
        
    def add_account(self, account):
        """ Account Adding Method """
        self.accounts[account.account_number] = account.balance

    def get_account_balance(self, account_number):
        """ Method that returns account balance """
        return self.accounts.get(account_number)
