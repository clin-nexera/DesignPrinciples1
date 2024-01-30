### Temporary Field ###
# https://refactoring.guru/smells/temporary-field



@dataclass
class MyDateTime:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.full_date = f"{year}, {month}, {day}"

    def foo(self):
        ...

    def goo(self):
        ...

    def hoo(self):
        ...

    def __str__(self):
        return self.full_date 
        # we can replace this with return f"{year}, {month}, {day}" and delete self.full_date from the init if self.full_date is only being used in one function.