from .extensions import db


class EmployeeModel(db.Model):
    # __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String())
    lastName = db.Column(db.String())
    email = db.Column(db.String(100))
    phone = db.Column(db.String(50))

    # def __init__(self, firstName, lastName, email, phone):
    #     self.firstName = firstName
    #     self.lastName = lastName
    #     self.email = email
    #     self.phone = phone
    
    def __repr__(self):
        return f"{self.firstName}:{self.lastName}"
