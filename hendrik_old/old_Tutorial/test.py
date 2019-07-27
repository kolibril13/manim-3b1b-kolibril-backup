from manimlib.imports import *

class Node(Circle):
    CONFIG = {
        "radius" : 0.15,
        "stroke_color" : BLUE,
        "stroke_width" : 3,
        "fill_color" : GREEN,
        "fill_opacity" : 0,
    }
    def __init__(self, name="", identity=-1, data=None, **kwargs):
        Circle.__init__(self, **kwargs)
        self._name = name
        self._id = identity
        self._data = data
        self._fpointers = []
        self._bpointers = []



class Network(object):
    def __init__(self, **kwargs):
        #Network.__init__(self, **kwargs)
        self.root = None
        self.network = [[]]
        self.layer_sizes = []
        self.num_layers = 0

    def __str__(self):
        name_str = "["
        id_str = "["
        for node in self.iter_network():
            name_str += node._name +  ", "
            id_str += str(node._id) + ", "
        name_str = name_str[:-2] + "]"
        id_str = id_str[:-2] + "]"
        return name_str + "\n" + id_str

    def __iter__(self):
        return self

    def __next__(self):
        for layer in self.network:
            for node in layer:
                return node

    def add_node(self, _n_name="", _bp_name=None):
        n_node = Node()
        if self.root is None:
            n_node._name = _n_name
            n_node._id = 0
            n_node._layer = 0
            self.root = n_node
            self.root._bpointers = [None]
            self.network = [[self.root]]
        else:
            __bp = self._fetch_bp(_bp_name)
            self._add_node(n_node, _n_name, __bp)

    def _add_node(self, node, _n_name, bpointer):
        node._name = _n_name
        node._bpointers.append(bpointer)
        if bpointer is not None: bpointer._fpointers.append(node)
        self._update_network(self.root, [[self.root]])
        if bpointer is not None: self._update_ids(bpointer._id)

    def iter_network(self):
        for layer in self.network:
            for node in layer:
                yield node

    def _fetch_bp(self, _bp_name=""):
        __bp = None
        for layer in self.network:
            for node in layer:
                if _bp_name is "None":
                    __bp = None
                    break
                elif node._name == _bp_name:
                    __bp = node
                    break
        return __bp

    def import_network(self, layout):
        for layer_num, layer in layout.items():
            for n_name, bp in layer.items():
                self.add_node(_n_name=n_name, _bp_name=bp)

    def export_network(self):
        layout = {}
        i=0
        for layer in self.network:
            temp_dict = {}
            for node in layer:
                temp_dict.update( {node._name : node._bpointers[0]} )
            layout[i] = temp_dict
            i += 1
        return layout

    def _update_network(self, node, network=[[]], __flag=0):
        __layer = __flag+1
        __temp_network = network

        for fp in node._fpointers:
            if fp._fpointers is not []:
                fp._layer = __layer
                if fp is node._fpointers[0]: __temp_network.append([])
                __temp_network[__layer].append(fp)
                self._update_network(fp, __temp_network, __layer)
            else:
                fp._layer = __layer
                __temp_network[__layer].append(fp)

        if __flag is 0:
            self.network = __temp_network
        else:
            return __temp_network

    def _update_ids(self, new_id):
        __layer_sizes = []
        for layer in self.network:
            __layer_size = 0
            for node in layer:
                __layer_size += 1
                if node._id is -1:
                    node._id = new_id
                elif node._id >= new_id:
                    node._id += 1
            if __layer_size is not 0: __layer_sizes.append(__layer_size)
        self.layer_sizes = __layer_sizes
        self.num_layers = len(self.layer_sizes)


class NetworkMobject(VGroup):
    CONFIG = {
        "node_radius" : 0.15,
        "node_buff" : MED_SMALL_BUFF,
        "layer_buff" : LARGE_BUFF,
        "node_stroke_color" : BLUE,
        "node_stroke_width" : 3,
        "node_fill_color" : GREEN,
        "edge_color" : LIGHT_GREY,
        "edge_stroke_width" : 2,
        "edge_propogation_color" : YELLOW,
        "edge_propogation_time" : 1,
        "max_shown_nodes" : 16,
        "brace_for_large_layers" : True,
        "average_shown_activation_of_large_layer" : True,
        "include_output_labels" : False,
    }

    def __init__(self, network, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.network = network
        self.layer_sizes = network.layer_sizes
        self.add_nodes()
        self.add_edges()

    def add_nodes(self):
        layers = VGroup(*[
            self.get_layer(size)
            for size in self.layer_sizes
        ])

        layers.arrange(RIGHT, buff = self.layer_buff)

        self.layers = layers
        self.add(self.layers)

        if self.include_output_labels:
            self.add_output_labels()

    def get_layer(self, sizes):
        layer = VGroup()
        n_nodes = sizes

        if n_nodes > self.max_shown_nodes:
            n_nodes = self.max_shown_nodes

        #Instantiate a VGroup of 'nodes'(circles)
        nodes = VGroup(*[
        Circle(
            radius = self.node_radius,
            stroke_color = self.node_stroke_color,
            stroke_width = self.node_stroke_width,
            fill_color = self.node_fill_color,
            fill_opacity = 0,
        )
        for x in range(n_nodes)
        ])

        nodes.arrange(DOWN, buff = self.node_buff)

        #Itteratively adds edge attributes to each node
        for node in nodes:
            node.edges_in = VGroup()
            node.edges_out = VGroup()
        layer.nodes = nodes
        layer.add(nodes)

        #This adds an ellipsis ("...") between nodes if there are more in the
        # layer than the layer size allows, effectively 'abbriviating' the layer
        if sizes > n_nodes:
            dots = TexMobject("\\vdots")
            dots.move_to(nodes)
            VGroup(*nodes[:len(nodes) // 2]).next_to(
                dots, UP, MED_SMALL_BUFF
            )
            VGroup(*nodes[len(nodes) // 2:]).next_to(
                dots, DOWN, MED_SMALL_BUFF
            )
            layer.dots = dots
            layer.add(dots)
            if self.brace_for_largesizess:
                brace = Brace(layer, LEFT)
                brace_label = brace.get_tex(str(size))
                layer.brace = brace
                layer.brace_label = brace_label
                layer.add(brace, brace_label)

        return layer

    def add_edges(self):
        self.edge_groups = VGroup()
        for l1, l2 in zip(self.layers[:-1], self.layers[1:]):
            edge_group = VGroup()
            for n1, n2 in it.product(l1.nodes, l2.nodes):

                edge = self.get_edge(n1, n2)
                edge_group.add(edge)
                n1.edges_out.add(edge)
                n2.edges_in.add(edge)
            self.edge_groups.add(edge_group)
        self.add_to_back(self.edge_groups)

    def get_edge(self, node1, node2):
        return Line(
            node1.get_center(),
            node2.get_center(),
            buff = self.node_radius,
            stroke_color = self.edge_color,
            stroke_width = self.edge_stroke_width,
        )

    def get_active_layer(self, layer_index, activation_vector):
        layer = self.layers[layer_index].deepcopy()
        self.activate_layer(layer, activation_vector)
        return layer

    def activate_layer(self, layer, activation_vector):
        n_nodes = len(layer.nodes)
        av = activation_vector
        def arr_to_num(arr):
            return (np.sum(arr > 0.1) / float(len(arr)))**(1./3)

        if len(av) > n_nodes:
            if self.average_shown_activation_of_large_layer:
                indices = np.arange(n_nodes)
                indices *= int(len(av)/n_nodes)
                indices = list(indices)
                indices.append(len(av))
                av = np.array([
                    arr_to_num(av[i1:i2])
                    for i1, i2 in zip(indices[:-1], indices[1:])
                ])
            else:
                av = np.append(
                    av[:n_nodes/2],
                    av[-n_nodes/2:],
                )
        for activation, node in zip(av, layer.nodes):
            node.set_fill(
                color = self.node_fill_color,
                opacity = activation
            )
        return layer

    def activate_layers(self, input_vector):
        activations = self.network.get_activation_of_all_layers(input_vector)
        for activation, layer in zip(activations, self.layers):
            self.activate_layer(layer, activation)

    def deactivate_layers(self):
        all_nodes = VGroup(*it.chain(*[
            layer.nodes
            for layer in self.layers
        ]))
        all_nodes.set_fill(opacity = 0)
        return self

    def get_edge_propogation_animations(self, index):
        edge_group_copy = self.edge_groups[index].copy()
        edge_group_copy.set_stroke(
            self.edge_propogation_color,
            width = 1.5*self.edge_stroke_width
        )
        return [ShowCreationThenDestruction(
            edge_group_copy,
            run_time = self.edge_propogation_time,
            lag_ratio = 0.5
        )]

    def add_output_labels(self):
        self.output_labels = VGroup()
        for n, node in enumerate(self.layers[-1].nodes):
            label = TexMobject(str(n))
            label.set_height(0.75*node.get_height())
            label.move_to(node)
            label.shift(node.get_width()*RIGHT)
            self.output_labels.add(label)
        self.add(self.output_labels)


class NetworkScene(Scene):
    CONFIG = {
    "layout" : {
        0 : {"A":"None"},
        1 : {"B":"A", "D":"A"},
        2 : {"C":"B", "E":"D", "F":"D"},
    },
        "network_mob_config" : {},
    }

    def construct(self):
        self.add_network()

        self.wait()
        self.play(
            DrawBorderThenFill(self.network_mob.layers),
            lag_ratio = 0.5,
            run_time = 2,
            rate_func=linear
        )

        self.play(ShowCreation(
            self.network_mob.edge_groups,
            lag_ratio = 0.5,
            run_time = 2,
            rate_func=linear,
        ))
        self.wait()

    def add_network(self):
        self.network = Network()
        self.network.import_network(self.layout)

        self.network_mob = NetworkMobject(
            self.network,
            **self.network_mob_config
        )
        #self.add(self.network_mob)

    def feed_forward(
                    self,
                    input_vector,
                    false_confidence = False,
                    added_anims = None
                    ):
        if added_anims is None:
            added_anims = []
        activations = self.network.get_activation_of_all_layers(
            input_vector
        )
        if false_confidence:
            i = np.argmax(activations[-1])
            activations[-1] *= 0
            activations[-1][i] = 1.0
        for i, activation in enumerate(activations):
            self.show_activation_of_layer(i, activation, added_anims)
            added_anims = []

    def show_activation_of_layer(self, layer_index, activation_vector, added_anims = None):
        if added_anims is None:
            added_anims = []
        layer = self.network_mob.layers[layer_index]
        active_layer = self.network_mob.get_active_layer(
            layer_index, activation_vector
        )
        anims = [Transform(layer, active_layer)]
        if layer_index > 0:
            anims += self.network_mob.get_edge_propogation_animations(
                layer_index-1
            )
        anims += added_anims
        self.play(*anims)

    def remove_random_edges(self, prop = 0.9):
        for edge_group in self.network_mob.edge_groups:
            for edge in list(edge_group):
                if np.random.random() < prop:
                    edge_group.remove(edge)

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -l  -s  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"NetworkScene"
    os.system(command_A + command_B)