import unittest
from parse_graph import GraphParser
from expects import expect, equal


class TestParseGraph(unittest.TestCase):
    def test_parse_graph(self):
        graph_string = '''
        "conf.py" -> "requests";
        "conf.py" -> "sys";
        "conf.py" -> "os.py";
        "other" -> "conf.py";
        '''

        parser = GraphParser()
        graph = parser.parse(graph_string)

        expect(graph).to(equal({
            'conf.py': ['requests', 'sys', 'os.py'],
            'other': ['conf.py']
            }))

