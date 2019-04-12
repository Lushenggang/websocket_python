from bottle import get, run
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket

users = set()
@get('/websocket/', apply=[websocket])
def chat(ws):
  users.add(ws)
  while True:
    msg = ws.receive()  # 接客户端的消息
    if msg:
      print(msg)
      for user in users:
        user.send(msg) # 发送信息给所有的客户端
      else:
        break
  print('退出聊天')
  users.remove(ws)

run(host='127.0.0.1', port=8000, server=GeventWebSocketServer)