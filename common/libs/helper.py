from flask import jsonify


def ops_renderJson(code=200, msg="success", data={}):
    resp = {"code": code, "msg": msg, "data": data}
    return jsonify(resp)


def ops_renderErrorJson(data={}):
    return ops_renderJson(code=-1, msg="fail", data=data)
