from flask import Flask, jsonify
from controller.student_controller import app_student
from controller.listse_controller import app_list_se
from controller.listsec_controller import app_list_sec
from controller.listdec_controller import app_list_dec

app = Flask(__name__)
app.register_blueprint(app_student)
app.register_blueprint(app_list_se)
app.register_blueprint(app_list_dec)
app.register_blueprint(app_list_sec)

if __name__ == '__main__':
    app.run()
