import unittest
from parse_graph import GraphParser
from expects import expect, equal, be_a


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

    def test_get_d3_node_edge_representation_from_graph(self):
        parser = GraphParser()
        graph = {
                'a': ['b', 'c'],
                'b': ['a']
                }

        nodes, edges = parser.d3_representation(graph)

        expect(nodes).to(be_a(list))
        expect(set(nodes)).to(equal({'a', 'b', 'c'}))
        expect(edges).to(equal([('a', 'b'), ('a', 'c'), ('b', 'a')]))
