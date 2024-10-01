from flask_restx import Resource, Namespace
from .extensions import db
from .models import EmployeeModel
from .api_models import employee_model, employee_input_model

ns = Namespace("api", description="Rest api")


@ns.route("/employees")
class EmployeeAPI(Resource):
    @ns.doc("Lists all employees")
    @ns.marshal_list_with(employee_model)
    def get(self):
        return EmployeeModel.query.all()

    @ns.expect(employee_input_model)
    @ns.marshal_with(employee_model)
    def post(self):
        print(ns.payload)
        employee = EmployeeModel(firstName=ns.payload["firstName"],
                                 lastName=ns.payload["lastName"],
                                 email=ns.payload["email"],
                                 phone=ns.payload["phone"])
        db.session.add(employee)
        db.session.commit()
        return employee, 201


@ns.route("/employees/<int:id>")
class EmployeeWithIdAPI(Resource):
    @ns.marshal_with(employee_model)
    def get(self, id):
        employee = EmployeeModel.query.get_or_404(id)
        return employee

    @ns.expect(employee_input_model)
    @ns.marshal_with(employee_model)
    def put(self, id):
        employee = EmployeeModel.query.get_or_404(id)
        employee.firstName = ns.payload["firstName"]
        employee.lastName = ns.payload["lastName"]
        employee.email = ns.payload["email"]
        employee.phone = ns.payload["phone"]
        db.session.commit()
        return employee

    def delete(self, id):
        employee = EmployeeModel.query.get_or_404(id)
        db.session.delete(employee)
        db.session.commit()
        return {}, 204

