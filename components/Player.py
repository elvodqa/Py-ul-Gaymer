
from components.Component import Component


class Player(object):
    def __init__(self, *args):
        super(Player, self).__init__(*args)
        self.components = []

    def attach_component(self, component: Component):
        self.components.insert(component)

    def remove_component(self, component: Component):
        for v in self.components:
            if v == component:
                self.components.remove(v)


        