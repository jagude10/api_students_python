from service.list_se_circle_service import ListSECService
from flask import Response,json,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder

app_list_sec = Blueprint("app_list_sec",__name__)
list_se_circle_service = ListSECService()

@app_list_sec.route('/list_sec/all')
def get_all_students():

    return Response(status=200,
                    response=json.dumps(list_se_circle_service.get_all_students()
                    ,cls=UtilEncoder),mimetype="application/json")
@app_list_sec.route('/list_sec',methods=['POST'])
def save_student():
    data = request.json
    try:

        list_se_circle_service.add_student(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")

    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}),
                    mimetype="application/json")