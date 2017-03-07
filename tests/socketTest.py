import unittest
import socketio
import app

class socket_tests(unittest.TestCase):
    def test_connect(self):
        client = app.socketio.test_client(app.app)
        received = client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(received[0]['args'], [{'numbers': ['Chatbot: A user has joined the chat.']}])
        client.disconnect()
    def test_hello(self):
        client = app.socketio.test_client(app.app)
        responce = client.get_received()
    def test_disconnect(self):
        global disconnected
        disconnected = None
        client =app.socketio.test_client(app.app)
        client.disconnect()
        
        
if __name__ == '__main__':
    unittest.main()