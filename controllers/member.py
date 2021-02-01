from application import app
from flask import Blueprint, render_template, request, jsonify
from common.libs.helper import ops_renderJson, ops_renderErrorJson
from common.models.user import User
from common.libs.UserService import UserService


member_page = Blueprint("member_page", __name__)


@member_page.route("/reg", methods=['GET', 'POST'])
def reg():
    if request.method == "GET":
        return render_template("member/reg.html")

    req = request.values

    reg_name = req['reg_name'] if "reg_name" in req else ""
    reg_pwd = req['reg_pwd'] if "reg_pwd" in req else ""

    if reg_name is None or len(reg_name) < 4:
        return ops_renderErrorJson()

    if reg_pwd is None or len(reg_pwd) < 6:
        return ops_renderErrorJson()

    user_info = User.query.filter_by(login_name=reg_name).first()
    if user_info:
        return ops_renderErrorJson(msg="用户名已被注册")

    model_user = User()
    model_user.login_name = reg_name
    model_user.login_salt = UserService.geneSalt(8)
    model_user.login_pwd = UserService.genePwd(reg_pwd, model_user.login_salt)

    return ops_renderJson()


@member_page.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("member/login.html")
