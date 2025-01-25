import unittest
from scp_client import SCPClient

class TestSCPClient(unittest.TestCase):

    def setUp(self):
        self.client = SCPClient(hostname='example.com', username='user', password='password')

    def test_upload(self):
        result = self.client.upload('local_file.txt', 'remote_file.txt')
        self.assertTrue(result)

    def test_download(self):
        result = self.client.download('remote_file.txt', 'local_file.txt')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
