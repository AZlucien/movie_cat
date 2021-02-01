from application import app


@app.before_request
def before_act():
    app.logger.info("request start")
    return


@app.after_request
def after_act(request):
    app.logger.info("request end")
    return request
