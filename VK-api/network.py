from api import get_friends
from igraph import Graph, plot, drawing
import time
from copy import deepcopy


def get_network(user_id):
	user_friends = get_friends(user_id, '')
	connections = []
	for i, friend in enumerate(user_friends):
		friends = get_friends(friend, '')
		time.sleep(0.3)
		for _, friend in enumerate(friends):
			for k, another_friend in enumerate(user_friends):
				if friend == another_friend:
					connections.append((i, k))
	return connections


def plot_graph(user_id):
	connections = get_network(user_id)
	user_friends = get_friends(user_id, 'last_name')
	last_names = []
	for friend in user_friends:
		last_names.append(friend['last_name'])
	graph = Graph(vertex_attrs={"label": last_names, "shape": "circle", "size": 10}, edges=connections, directed=False)
	N = len(last_names)
	visual_style = {"vertex_size": 20, "bbox": (3000, 3000), "margin": 70, "vertex_label_dist": 2,
					"edge_color": "#4F4F4F", "layout": graph.layout_fruchterman_reingold(
			maxiter=1000,
			area=N ** 2,
			repulserad=N ** 2)}
	graph.simplify(multiple=True, loops=True)
	clusters = graph.community_multilevel()
	pal = drawing.colors.ClusterColoringPalette(len(clusters))
	graph.vs['color'] = pal.get_many(clusters.membership)
	plot(graph, **visual_style)


if __name__ == '__main__':
	plot_graph(422277418)
	
