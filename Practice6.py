from datetime import datetime, timezone, timedelta

class BankAccount:
    transaction_id = 0

    def __init__(self, account_number, first_name, last_name, timezone_offset, initial_balance=0):
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.timezone_offset = timezone_offset
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            BankAccount.transaction_id += 1
            confirmation_number = f'D-{self.account_number}-{datetime.utcnow().strftime("%Y%m%d%H%M%S")}-{BankAccount.transaction_id}'
            return confirmation_number
        else:
            return None

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            BankAccount.transaction_id += 1
            confirmation_number = f'W-{self.account_number}-{datetime.utcnow().strftime("%Y%m%d%H%M%S")}-{BankAccount.transaction_id}'
            return confirmation_number
        else:
            return None

    def deposit_interest(self, interest_rate):
        interest = self.balance * (interest_rate / 100)
        self.balance += interest
        BankAccount.transaction_id += 1
        confirmation_number = f'I-{self.account_number}-{datetime.utcnow().strftime("%Y%m%d%H%M%S")}-{BankAccount.transaction_id}'
        return confirmation_number

    def get_transaction_details(self, confirmation_number, timezone_arg):
        parts = confirmation_number.split('-')
        transaction_type = parts[0]
        account_number = parts[1]
        transaction_time_utc = datetime.strptime(parts[2], "%Y%m%d%H%M%S").replace(tzinfo=timezone.utc)
        transaction_id = int(parts[3])

        transaction_time = transaction_time_utc.astimezone(timezone(timedelta(hours=timezone_arg)))
        transaction_time_str = transaction_time.strftime('%Y-%m-%d %H:%M:%S')

        return {
            'account_number': account_number,
            'transaction_code': transaction_type,
            'transaction_id': transaction_id,
            'time': transaction_time_str,
            'time_utc': transaction_time_utc.strftime('%Y-%m-%dT%H:%M:%S')
        }

# Example usage
account = BankAccount(140568, "John", "Doe", -7, initial_balance=100.00)
print("Initial balance:", account.balance)

confirmation_number_deposit = account.deposit(50.00)
print("Confirmation number for deposit:", confirmation_number_deposit)
print("New balance after deposit:", account.balance)

confirmation_number_withdraw = account.withdraw(30.00)
print("Confirmation number for withdrawal:", confirmation_number_withdraw)
print("New balance after withdrawal:", account.balance)

confirmation_number_interest = account.deposit_interest(0.5)
print("Confirmation number for interest deposit:", confirmation_number_interest)
print("New balance after interest deposit:", account.balance)

transaction_details = account.get_transaction_details(confirmation_number_deposit, -7)
print("\nTransaction details for deposit:")
for key, value in transaction_details.items():
    print(key, ":", value)
