class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=0, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, rest_days, hours=None):
        if hours is None:
            hours = (7 - rest_days) * 8
        return hours

    @classmethod
    def get_email(cls, name, email=None):
        if email is None:
            email = f"{name}@email.com"
        return email

    @classmethod
    def set_hourly_payment(cls, value):
        cls.hourly_payment = value

    def salary(self):
        hours = self.get_hours(self.rest_days, self.hours)
        return hours * self.hourly_payment
