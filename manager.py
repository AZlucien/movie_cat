from www import *
from flask_script import Server,Command
from application import manager

# 启动参数为runserver(default)
manager.add_command("runserver", Server(host="127.0.0.1", use_debugger=True, use_reloader=True))


# 启动参数为init_db(初始化user db)
@Command
def init_db():
    from application import db
    from common.models.user import User
    db.create_all()


manager.add_command("init_db", init_db)


def main():
    manager.run()


# 启动
if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()
