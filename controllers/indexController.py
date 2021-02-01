from flask import Blueprint, request, make_response, jsonify, render_template
from common.models.user import User

index_page = Blueprint("index_page ", __name__)


@index_page.route("/index")
def template():
    # 字典传值
    context = {}
    # 通过Model查询数据库

    result = User.query.all()
    context['sql_result'] = result

    return render_template("index.html", **context)
