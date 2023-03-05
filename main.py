from flask import Flask, send_from_directory, render_template, Response, url_for, request
from flask_restful import Resource, Api, reqparse
from app.updater import UpdateTeams
import traceback
import os
import subprocess


app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
api = Api(app)


class MSTeamsUpdater(Resource):
    def get(self):
        html = render_template('index.html')
        return Response(html, mimetype='text/html')

class UpdateStatus(Resource):
    def post(self):
        print(request.form)

        try:
            updater = UpdateTeams()
            updater.update_status(status="Busy", message="Testing status update")

            return "Updating Status"

        except Exception as e:
            return traceback.format_exception(type(e), e, e.__traceback__)


api.add_resource(MSTeamsUpdater, '/')
api.add_resource(UpdateStatus, '/update')

if __name__ == '__main__':

    # subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe", '--remote-debugging-port=9222', '--user-data-dir=C:\\selenum\\ChromeProfile'])

    app.run(host="localhost", port=8003, debug=True)
