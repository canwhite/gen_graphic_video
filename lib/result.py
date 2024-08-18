class Response:
    @staticmethod
    def set_response(msg="", code=200, data=None):
        return {
            "msg": msg,
            "code": code,
            "data": data
        }

    @staticmethod
    def get_response(response):
        return response


if __name__ == "__main__":
    #静态方法的调用直接用类名调用就ok
    response = Response.set_response(msg="操作成功", code=200, data={"result": "这是一个示例响应"})
    print(Response.get_response(response))