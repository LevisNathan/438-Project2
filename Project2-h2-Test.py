import unittest
import app

class SocketIOTest(unittest.TestCase):
    def test_onConnect(self):
        client = app.socketio.test_client(app.app)
        r = client.get_received()
        server_msg =r[0]
        self.assertEqual(server_msg['name'], 'srver says hello')
        data = server_msg['args'][0]
        self.assertEqual(data['message'], 'Hello, client!')
        
    def test_emit(self):
        client = app.socketio.test_client(app.app)
        client.emit('new message', {
            'message':'this is a client massage'
        })
        r = client.get_received()
        for i in r:
            print i
            

if __name__ == '__main__':
    unittest.main