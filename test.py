import graphviz

dot = graphviz.Digraph(comment='Test Graph')
dot.node('A', 'Start')
dot.node('B', 'End')
dot.edge('A', 'B', 'connection')

dot.render(filename='test_graph', format='png', cleanup=True)
