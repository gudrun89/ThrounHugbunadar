class Account(object):
    def __init__(self, credit, deposit):
        self.credit = credit
        self.deposit = deposit


    def getName(self):
        return self.__class__.__name__

    def transfer(self, amount):
        self.credit += amount


# Inherits from Account
class Heidursmerki(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.042
        self.indexed = False
        self.fixed = 0.33
        super(Heidursmerki, self).__init__(credit, deposit)


# Inherits from Account
class Sparileid36(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.017
        self.indexed = True
        self.fixed = 36
        super(Sparileid36, self).__init__(credit, deposit)


# Inherits from Account
class Sparileid48(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.018
        self.indexed = True
        self.fixed = 48
        super(Sparileid48, self).__init__(credit, deposit)


# Inherits from Account
class Sparileid60(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.019
        self.indexed = True
        self.fixed = 60
        super(Sparileid60, self).__init__(credit, deposit)


if __name__ == "__main__":
    account = Heidursmerki(1000,100)
        
