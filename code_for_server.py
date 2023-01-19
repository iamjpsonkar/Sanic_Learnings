from sanic import Sanic, text, Request

app = Sanic(__name__)

@app.post("/")
async def handler(request:Request):
  message = (
    request.head + b"\n\n" + request.body
  ).decode("utf-8")
  print("m:",message)
  return text("Done")

if __name__ == '__main__':
  app.run(port = 9999, debug = True)
  
'''
$ curl localhost:9999 -d '{"foo":"bar"}'
Done

============================================================

[2023-01-18 16:29:17 +0530] - (sanic.access)[INFO][127.0.0.1:62574]: POST http://localhost:9999/  200 4
POST / HTTP/1.1
Host: localhost:9999
User-Agent: curl/7.84.0
Accept: */*
Content-Length: 13
Content-Type: application/x-www-form-urlencoded

{"foo":"bar"}
'''