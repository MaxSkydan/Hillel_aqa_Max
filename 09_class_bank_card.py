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
import logging
import random

_log = logging.getLogger()


class Creditcard:
    """The class represent of Credit cards."""

    PIN_LENGTH = 4
    CVV_RANGE = (100, 999)
    BANK_ID = '4441'
    BANK_NUMBER_RANGE = (100000000000, 999999999999)
    EXP_DATE_YEAR = 5
    START_EXP_MONTH_DAY = 1
    OPENING_BALANCE = 0
    USD_TO_UAH_RATE = 40.1

    def __init__(self, pin, client_name, client_surname):
        """Initialize an instance of the Credit card.

        param pin: An integer representing the pin code.
        param name: A string representing the name of the client.
        param surname: A string representing the surname of the client.
        param cvv: Automatic generation of CVV code in integer format.
        param exp_date: Automatically create a date from today + 5 years.
        param card_num: Automatic generation of card number in integer format.
        param balance: An integer representing the balance on card.
        """
        self.__pin = pin
        self.name = client_name
        self.surname = client_surname
        self.__cvv = random.randint(*self.CVV_RANGE)
        self.__exp_date = datetime.date.today().replace(
            year=datetime.date.today().year + self.EXP_DATE_YEAR,
            day=self.START_EXP_MONTH_DAY)
        self.__card_num = int(self.BANK_ID + str(random.randint(
            *self.BANK_NUMBER_RANGE)))
        self.__balance = self.OPENING_BALANCE

    def __str__(self):
        """Human-readable string representation of the Credit card."""
        return (f'This credit card is in the name of '
                f'{self.name} {self.surname}.\n'
                f'Credit card number {self.__card_num}\n'
                f'Card exp date {self.__exp_date}')

    @classmethod
    def validate_length_pin(cls, pin):
        """Check the pin code have a length of 4 characters long."""
        return len(str(pin)) == cls.PIN_LENGTH

    @classmethod
    def _usd_to_uah(cls, usd_value):
        """Convert USD to UAH."""
        return usd_value * cls.USD_TO_UAH_RATE

    @staticmethod
    def validate_expired_card(end_date):
        """Check the card exp date is greater than or equal to current date."""
        return end_date >= datetime.date.today()

    @property
    def pin_code(self):
        """Getter for Pin code."""
        return self.__pin

    @pin_code.setter
    def pin_code(self, pin):
        """Setter for Pin code."""
        self.__pin = pin

    @property
    def balance(self):
        """Getter for credit card balance."""
        return format(self.__balance, '.2f')

    @property
    def cvv_code(self):
        """Getter for CVV code."""
        return self.__cvv

    @property
    def card_number(self):
        """Getter for Card number."""
        return self.__card_num

    @property
    def exp_date(self):
        """Getter for expiration card date."""
        return self.__exp_date

    def check_pin_code(self, current_pin):
        """Check if pin code is correct."""
        return current_pin == self.__pin

    def check_cvv_code(self, cvv):
        """Check if cvv code is correct."""
        return cvv == self.__cvv

    def check_card_number(self, current_card_num):
        """Check if card number is correct."""
        return current_card_num == self.__card_num

    def __income(self, new_sum, usd=False):
        """Balance increase.

        params new_sum: An integer representing the amount of money.
        params usd: A bool representing if sum in usd.
        """
        operation = self._usd_to_uah(new_sum) if usd else new_sum
        self.__balance += operation
        return self.balance

    def __expenses(self, new_sum, usd=False):
        """Decrease in balance. With balance check for negative value.

        params new_sum: An integer representing the amount of money.
        params usd: A bool representing if sum in usd.
        """
        operation = self._usd_to_uah(new_sum) if usd else new_sum
        if self.__balance - operation >= 0:
            self.__balance -= operation
            return self.balance
        else:
            raise ValueError('Not enough money')

    def check_balance(self, pin):
        """Check balance in credit card.

        params pin: An integer representing the pin code.
        """
        if self.check_pin_code(pin):
            _log.info(f'Hello {self.name} {self.surname}.\n'
                      f'Your balance is {self.balance} UAH.')
            return self.balance
        else:
            raise PermissionError('Wrong credentials')

    def put_money_to_card(self, card_num, cur_sum, usd=False):
        """Top up credit card balance.

        params card_num: An integer representing the card number.
        params cur_sum: An integer representing the amount of money.
        params usd: A bool representing if sum in usd.
        """
        if self.check_card_number(card_num):
            if usd:
                self.__income(cur_sum, usd=True)
                _log.info(f'Operation was successfully completed.\n'
                          f'{cur_sum} USD was depositing from your card.')
            else:
                self.__income(cur_sum)
                _log.info(f'Operation was successfully completed.\n'
                          f'{cur_sum} UAH was depositing from your card.')
            return True
        else:
            raise KeyError("Card number isn't correct.")

    def buy_new_item(self, cvv, cur_sum, usd=False):
        """Reducing the balance on the card after purchasing an item.

        params cvv: An integer representing the cvv code.
        params cur_sum: An integer representing the amount of money.
        params usd: A bool representing if sum in usd.
        """
        if self.check_cvv_code(cvv):
            if self.validate_expired_card(self.__exp_date):
                if usd:
                    if self.__expenses(cur_sum, usd=True):
                        _log.info(f'Operation was successfully completed.\n'
                                  f'{cur_sum} USD was withdrawn '
                                  f'from your card.')
                        return True
                    else:
                        raise ValueError
                else:
                    if self.__expenses(cur_sum):
                        _log.info(f'Operation was successfully completed.\n'
                                  f'{cur_sum} UAH was withdrawn '
                                  f'from your card.')
                        return True
                    else:
                        raise ValueError
            else:
                raise AssertionError('Card is expired.')
        else:
            raise PermissionError


if __name__ == '__main__':

    log_formatter = logging.Formatter('%(asctime)s '
                                      '[%(levelname)s]  %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    _log.addHandler(console_handler)
    _log.setLevel(logging.INFO)

    max_cred = (3344, 'Max', 'Skydan')
    john_cred = (2112, 'John', 'Dou')

    def check_balance_of_card(card, pin):
        """Check balance on card.

        params card: class instance.
        params pin: card pin code in integer format.
        """
        try:
            card.check_balance(pin)
        except PermissionError as per_er:
            _log.info(per_er)

    def change_pin_code(card, new_pin):
        """Change pin code for card.

        params card: class instance.
        params new_pin: new card pin code in integer format.
        """
        if card.validate_length_pin(new_pin):
            card.pin_code = new_pin
            _log.info('PIN code was successfully changed.')
            return True
        else:
            _log.info('The PIN code must be 4 characters long.')
            return False

    def put_money_on_the_card_in_uah(card, cur_sum):
        """Put money on the card in uah.

        params card: class instance.
        params cur_sum: An integer representing the amount of money.
        """
        try:
            card.put_money_to_card(card.card_number, cur_sum)
        except KeyError as key_er:
            _log.info(key_er)

    def put_money_on_the_card_in_usd(card, cur_sum):
        """Put money on the card in usd.

        The exchanged money will be sent to the card
        according to the exchange rate.

        params card: class instance.
        params cur_sum: An integer representing the amount of money.
        """
        try:
            card.put_money_to_card(card.card_number, cur_sum, usd=True)
        except KeyError as key_er:
            _log.info(key_er)

    def spend_money_online_in_uah(card, cur_sum):
        """Spend money in uah.

        params card: class instance.
        params cur_sum: An integer representing the amount of money.
        """
        try:
            card.buy_new_item(card.cvv_code, cur_sum)
        except ValueError as val_er:
            _log.info(val_er)
        except PermissionError as per_er:
            _log.info(per_er)
        except AssertionError as asser_er:
            _log.info(asser_er)

    def spend_money_online_in_usd(card, cur_sum):
        """Spend money in usd.

        The amount in uah will be withdrawn from the card
        according to the exchange rate.

        params card: class instance.
        params cur_sum: An integer representing the amount of money.
        """
        try:
            card.buy_new_item(card.cvv_code, cur_sum, usd=True)
        except ValueError as val_er:
            _log.info(val_er)
        except PermissionError as per_er:
            _log.info(per_er)
        except AssertionError as asser_er:
            _log.info(asser_er)

    max_card = Creditcard(*max_cred)
    john_card = Creditcard(*john_cred)

    _log.info(max_card)
    _log.info(john_card)
    check_balance_of_card(max_card, 3344)
    check_balance_of_card(john_card, 2112)
    change_pin_code(max_card, 33333)
    change_pin_code(max_card, 3333)
    spend_money_online_in_uah(max_card, 3)
    put_money_on_the_card_in_uah(max_card, 10)
    check_balance_of_card(max_card, 3333)
    put_money_on_the_card_in_usd(max_card, 100)
    spend_money_online_in_usd(max_card, 1)
    check_balance_of_card(max_card, 333)
