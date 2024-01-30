### Feature Envy ###
# https://refactoring.guru/smells/feature-envy

from dataclasses import dataclass
@dataclass(frozen=True)
class ShoppingItem:
    name: str
    price: float
    tax: float


class Order:
    def get_bill_total(self, items: list[ShoppingItem]) -> float:
        return sum([item.price * item.tax for item in items])

    def get_receipt_string(self, items: list[ShoppingItem]) -> list[str]:
        return [f"{item.name}: {item.price * item.tax}$" for item in items]

    def create_receipt(self, items: list[ShoppingItem]) -> float:
        bill = self.get_bill_total(items)
        receipt = self.get_receipt_string(items).join('\n')
        return f"{receipt}\nBill {bill}"
    



# Signs of feature envy are when a method accesses the data of another object more than its own
# In this case get_bill_total and get_receipt_string are accessign price and tax a lot from a Shopping Item
# The suggestion would be to have a calculate_tax() function in ShoppingItem and use that method
# inside get_bill_total and get_receipt_string