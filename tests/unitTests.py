import unittest
import app

class unit_test(unittest.TestCase):
    def test_hello(self):
        client = app.chatbot('!!hello')
        r = client.responce
        self.assertEqual(r, 'Chatbot: Hi i\'m chatbot')
    def test_about(self):
        client = app.chatbot('!!about')
        r = client.responce
        self.assertEqual(r, 'Chatbot: This is a chat room created by Nathan Levis')
    def test_sing(self):
        client = app.chatbot('!!sing')
        r=client.responce
        self.assertEqual(r, 'Chatbot: laydal laydal laydal!!!!!')
    def test_help(self):
        client = app.chatbot('!!help')
        r =  client.responce 
        self.assertEqual(r, "Chatbot have a couple of commands:" )
if __name__ == '__main__':
    unittest.main