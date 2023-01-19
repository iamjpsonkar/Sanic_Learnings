from sanic import Sanic, Request
from sanic.response import text
from sanic.views import HTTPMethodView


app = Sanic("CBVs")

class SingleProfileView(HTTPMethodView, attach=app, uri="/<username>"):
  async def get(self,request: Request, username: str):
    return text("I am get method")

  async def put(self,request: Request, username: str):
    return text("I am put method")

  async def patch(self,request: Request, username: str):
    return text("I am patch method")

  async def delete(self,request: Request, username: str):
    return text("I am delete method")


if __name__ == '__main__':
  app.run()