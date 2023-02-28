from flask import Flask, send_from_directory, render_template, Response, url_for, request
from flask_restful import Resource, Api, reqparse


app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
api = Api(app)


class MSTeamsUpdater(Resource):
    def get(self):
        html = render_template('index.html')
        return Response(html, mimetype='text/html')


api.add_resource(MSTeamsUpdater, '/')

if __name__ == '__main__':
    app.run(host="localhost", port=8003, debug=True)