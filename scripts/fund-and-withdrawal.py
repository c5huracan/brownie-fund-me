from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entrance fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    # withdraw_amount = fund_me.withdraw()
    # print(withdraw_amount)
    # print(f"The current withdraw amount is {withdraw_amount}")
    fund_me.withdraw({"from": account})
    # fund_me.withdraw({"from": account, "value": withdraw_amount})


def main():
    fund()
    withdraw()
