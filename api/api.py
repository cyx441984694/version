from flask import jsonify
from flask_restful import Resource, Api

from .models import Version as VersionModel, to_dict

api = Api()

class Version(Resource):
    def get(self):
        return jsonify([to_dict(version) for version in VersionModel.query.all()])

api.add_resource(Version, '/version')