class Date:
    def __init__(self,init_day,init_month,init_year):
        self.day=init_day
        self.month=init_month
        self.year=init_year

    def show(self):
        print(self.day,self.month,self.year)

independence_day = Date(15,8,1947)
independence_day.show()

print("type(independence_day):",type(independence_day))


