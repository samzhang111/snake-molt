from server import app
import unittest


class IntegrationTest(unittest.TestCase):
    def setUp(self):
        app.run(port=8001)

    def tearDown(self):
        app.stop()

