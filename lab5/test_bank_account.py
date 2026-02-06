import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def test_deposit_increases_balance(self):
        account = BankAccount(0)
        account.deposit(100)
        self.assertEqual(account.get_balance(), 100)
        account.deposit(50)
        self.assertEqual(account.get_balance(), 150)

    def test_withdraw_decreases_balance(self):
        account = BankAccount(100)
        account.withdraw(30)
        self.assertEqual(account.get_balance(), 70)
        account.withdraw(70)
        self.assertEqual(account.get_balance(), 0)

    def test_withdraw_more_than_balance_raises(self):
        account = BankAccount(50)
        with self.assertRaises(ValueError):
            account.withdraw(100)

    def test_deposit_negative_raises(self):
        account = BankAccount(0)
        with self.assertRaises(ValueError):
            account.deposit(-10)
        with self.assertRaises(ValueError):
            account.deposit(0)

    def test_withdraw_negative_raises(self):
        account = BankAccount(100)
        with self.assertRaises(ValueError):
            account.withdraw(-5)
        with self.assertRaises(ValueError):
            account.withdraw(0)

    def test_deposit_invalid_type_raises(self):
        account = BankAccount(0)
        with self.assertRaises(ValueError):
            account.deposit("sto")

    def test_withdraw_invalid_type_raises(self):
        account = BankAccount(100)
        with self.assertRaises(ValueError):
            account.withdraw("piecdziesiat")

    def test_initial_balance(self):
        account = BankAccount(200)
        self.assertEqual(account.get_balance(), 200)


if __name__ == "__main__":
    unittest.main()
