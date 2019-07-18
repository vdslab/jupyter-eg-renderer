import json
import networkx
import ipywidgets as widgets
from traitlets import Unicode
from networkx.readwrite import json_graph

@widgets.register
class EgRenderer(widgets.DOMWidget):
    """An example widget."""
    _view_name = Unicode('HelloView').tag(sync=True)
    _model_name = Unicode('HelloModel').tag(sync=True)
    _view_module = Unicode('jupyter-eg-renderer').tag(sync=True)
    _model_module = Unicode('jupyter-eg-renderer').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)
    data = Unicode('{"nodes": [], "links": []}').tag(sync=True)
    # layout_method = Unicode('hierarchy').tag(sync=True)

    # Data Loading
 
    # Node Geometry
    default_node_width=Unicode('10').tag(sync=True)
    default_node_height=Unicode('10').tag(sync=True)

    # Node Representation
    default_node_fill_color = Unicode('white').tag(sync=True)
    default_node_fill_opacity = Unicode('1').tag(sync=True)
    default_node_stroke_color = Unicode('white').tag(sync=True)
    default_node_label = Unicode('').tag(sync=True)
    

    def render(self, graph):
        data = json_graph.node_link_data(graph)
        self.data = json.dumps(data)

