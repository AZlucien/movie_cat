from controllers.indexController import index_page
from controllers.member import member_page
from application import app
from common.libs.UrlManager import UrlManager
from flask_debugtoolbar import DebugToolbarExtension
# DEBUG工具栏初始化

# 拦截器初始化
from interceptors.auth import *

# 错误处理器初始化
from interceptors.errorHandler import *

toolbar = DebugToolbarExtension(app)


# blueprint初始化
app.register_blueprint(index_page, url_prefix="/")
app.register_blueprint(member_page, url_prefix="/member")

# 模板函数

app.add_template_global(UrlManager.buildUrl, "buildUrl")
app.add_template_global(UrlManager.buildStaticUrl, "buildStaticUrl")
