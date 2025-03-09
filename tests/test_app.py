import unittest
import socket
from app import app  

class FlaskTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world_success(self):
        response = self.app.get('/')
        
        self.assertEqual(response.status_code, 200)
        
        expected = 'Hello AWS! This is my Hello World CICD running on host %s\n' % socket.gethostname()
        self.assertEqual(response.data.decode(), expected)

if __name__ == '__main__':
    unittest.main()
