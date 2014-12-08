"""This is a docstring"""
from flask import Flask, render_template, request
from bank.bank import Bank
from bank.account import Account

APP = Flask(__name__)
BANK = Bank()

@APP.route('/')
def hello_world():
    """Missing function docstring"""
    account_number = request.args.get('account_number')
    balance = BANK.get_account_balance(account_number)
    return render_template('index.html', balance=balance)

if __name__ == '__main__':
    import cProfile

    #account = Account('1111', 50)
    BANK.add_account(Account('1111', 50))
    cProfile.run('APP.run(debug=True)', sort='time')

