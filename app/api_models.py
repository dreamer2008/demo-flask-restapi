from flask_restx import fields
from .extensions import api

employee_model = api.model("Employee", {
    "id": fields.Integer,
    "firstName": fields.String,
    "lastName": fields.String,
    "email": fields.String,
    "phone": fields.String
})

employee_input_model = api.model("EmployeeAdd", {
    "firstName": fields.String,
    "lastName": fields.String,
    "email": fields.String,
    "phone": fields.String
})
