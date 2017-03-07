import unittest
import app

class unit_test(unittest.TestCase):
    def test_hello(self):
        client = app.chatbot('!!hello')
        self.assertEqual(r, 'Chatbot: Hi i\'m chatbot')
    def test_about(self):
        client = app.chatbot('!!about')
        self.assertEqual(r, 'Chatbot: This is a chat room created by Nathan Levis')

if __name__ == '__main__':
    unittest.main