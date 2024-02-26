"""Home task. Bank card operations.

write class for bank card.
Class should reflect card lifecycle, card operations etc.
use CVV, PIN, Name, Surname , end date, card_num as initial params
class should have in addition to common logic some class attributes,
as minimum one classmethod and as minimum  one staticmethod,
two or more getters/setters, __str_ magic method
do not forget about block "if __name__ == '__main__':"
and code there to check your class written logic.
"""

import datetime


class Creditcard:
    """The class represent of Credit cards."""

    CURRENT_DATE = datetime.date.today()

    def __init__(self, cvv, pin, name, surname,
                 year, month, day, card_num, balance=0):
        """Initialize an instance of the Credit card.

        param cvv: An integer representing the cvv code.
        param pin: An integer representing the pin code.
        param name: A string representing the name of the client.
        param surname: A string representing the surname of the client.
        param year: An integer representing the end of year.
        param month: An integer representing the end of month.
        param day: An integer representing the end of day.
        param card_num: An integer representing the card number.
        param balance: An integer representing the balance on card.
        """
        self.__cvv = cvv
        self.__pin = pin
        self.__name = name
        self.__surname = surname
        self.__end_date = datetime.date(year, month, day)
        self.__card_num = card_num
        self.__balance = balance

    def __str__(self):
        """Human-readable string representation of the Credit card."""
        return (f'This credit card is in the name of '
                f'{self.__name} {self.__surname}\n'
                f'Credit card number {self.__card_num}\n'
                f'Card end date {self.__end_date}')

    @classmethod
    def validate_date(cls, end_date):
        """Check the date is greater than or equal to current date."""
        return end_date >= cls.CURRENT_DATE

    @staticmethod
    def _uah_to_usd(uah_value):
        """Convert USD to UAH."""
        dollar_exchange_rate = 40.1
        return uah_value * dollar_exchange_rate

    @property
    def pin_code(self):
        """Getter for Pin code."""
        return self.__pin

    @pin_code.setter
    def pin_code(self, num):
        """Setter for Pin code."""
        self.__pin = num

    @property
    def balance(self):
        """Getter for credit card balance."""
        return format(self.__balance, '.2f')

    def check_pin_code(self):
        """Check if pin code is correct."""
        current_pin = int(input('Please enter your PIN: \n'))
        if current_pin == self.__pin:
            return True
        else:
            return False

    def check_cvv_code(self):
        """Check if cvv code is correct."""
        current_cvv = int(input('Please enter your cvv code: \n'))
        if current_cvv == self.__cvv:
            return True
        else:
            return False

    def check_card_number(self):
        """Check if card number is correct."""
        current_card_num = int(input('Please enter your card number: \n'))
        if current_card_num == self.__card_num:
            return True
        else:
            return False

    def validate_expired_card(self, end_date):
        """Check the card expiration date."""
        if self.validate_date(end_date):
            return True

    def __income(self, new_sum, usd=False):
        """Balance increase.

        params new_sum: An integer representing the amount of money.
        params usd: A bool representing if sum in usd.
        """
        operation = self._uah_to_usd(new_sum) if usd else new_sum
        self.__balance += operation
        return self.__balance

    def __expenses(self, new_sum, usd=False):
        """Decrease in balance.

        params new_sum: An integer representing the amount of money.
        params usd: A bool representing if sum in usd.
        """
        operation = self._uah_to_usd(new_sum) if usd else new_sum
        self.__balance -= operation
        return self.__balance

    def check_balance(self):
        """Check balance in credit card."""
        if self.check_pin_code():
            return (f'Hello {self.__name} {self.__surname}.'
                    f'Your balance is {self.balance} UAH')
        else:
            return "PIN isn't correct"

    def put_money_to_card(self, usd=False):
        """Top up credit card balance.

        params usd: A bool representing if sum in usd.
        """
        if self.check_card_number():
            cur_sum = int(input('Enter amount: \n'))
            self.__income(cur_sum, usd=True) if usd else self.__income(cur_sum)
            return 'Operation was successfully completed'
        else:
            return "Card number isn't correct"

    def buy_new_item(self, num, usd=False):
        """Reducing the balance on the card after purchasing an item.

        params num: An integer representing the amount of money.
        params usd: A bool representing if sum in usd.
        """
        if self.check_cvv_code():
            if self.validate_expired_card(self.__end_date):
                self.__expenses(num, usd=True) if usd else self.__expenses(num)
                return 'Operation was successfully completed'
            else:
                return 'Your card is expired'
        else:
            return 'Incorrect code'


if __name__ == '__main__':

    my_card = Creditcard(cvv=333, pin=3344, name='Max', surname='Skydan',
                         year=2025, month=2, day=25, card_num=44332233)

    print(my_card)
    print(my_card.pin_code)
    my_card.pin_code = 4444
    print(my_card.pin_code)
    print(my_card.check_balance())
    print(my_card.put_money_to_card())
    print(my_card.balance)
    print(my_card.put_money_to_card(usd=True))
    print(my_card.balance)
    print(my_card.buy_new_item(321))
    print(my_card.balance)
    print(my_card.buy_new_item(1, usd=True))
    print(my_card.balance)
