from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

api = Api(version='1.0', title='OpenAPI doc with RestX',
          description='Contact the dev team: dev@xxx.com',
          contact="dev@xxx.com"
          )
db = SQLAlchemy()
