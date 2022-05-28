from service.list_se_service import ListSEService
from flask import Response,json,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder

app_list_se = Blueprint("app_list_se",__name__)

list_se_service = ListSEService()

@app_list_se.route('/list_se/all')
def get_all_students():

    return Response(status=200,
                    response=json.dumps(list_se_service.get_all_students()
                    ,cls=UtilEncoder),mimetype="application/json")

@app_list_se.route('/list_se',methods=['POST'])
def save_student():
    data = request.json
    try:

        list_se_service.add_student(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")

    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}),
                    mimetype="application/json")

@app_list_se.route("/listse/tostart",methods=["POST"])
def create_pet_to_start():
    return Response(status=200,
                    response=json.dumps(list_se_service.add_to_start(request.json)),
                    mimetype="application/json")

@app_list_se.route("/listse/toposition/<position>",methods=["POST"])
def create_pet_to_position(position):
    return Response(status=200,
                    response=json.dumps(list_se_service.add_to_position(int(position),request.json)),
                    mimetype="application/json")

