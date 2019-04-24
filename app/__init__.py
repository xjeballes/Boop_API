from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.pet_controller import api as pet_ns
from .main.controller.specie_controller import api as specie_ns
from .main.controller.breed_controller import api as breed_ns
from .main.controller.business_controller import api as business_ns
from .main.controller.circle_controller import api as circle_ns

blueprint = Blueprint("api", __name__)

api = Api(blueprint,
          title = "BOOP API WITH JWT",
          version = "1.0",
          description = "a flask restplus web service for BOOP"
          )

api.add_namespace(user_ns, path="/user")
api.add_namespace(auth_ns, path="/auth")
api.add_namespace(pet_ns, path="/pet")
api.add_namespace(specie_ns, path="/specie")
api.add_namespace(breed_ns, path="/breed")
api.add_namespace(business_ns, path="/business")
api.add_namespace(circle_ns, path="/circle")