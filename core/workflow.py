from typing import Callable


class WorkflowNode:

    def __init__(
        self,
        name: str,
        handler: Callable
    ):

        self.name = name

        self.handler = handler


class WorkflowEdge:

    def __init__(
        self,
        source: str,
        target: str,
        condition=None
    ):

        self.source = source

        self.target = target

        self.condition = condition


class WorkflowGraph:

    def __init__(self):

        self.nodes = {}

        self.edges = []

        self.start_node = None

    def add_node(
        self,
        node: WorkflowNode
    ):

        self.nodes[node.name] = node

    def add_edge(
        self,
        edge: WorkflowEdge
    ):

        self.edges.append(edge)

    def set_start(
        self,
        node_name: str
    ):

        self.start_node = node_name

    async def run(
        self,
        state
    ):

        current = self.start_node

        while current:

            node = self.nodes[current]

            print(
                f"Running node: {current}"
            )

            state = await node.handler(
                state
            )

            next_node = None

            for edge in self.edges:

                if edge.source != current:
                    continue

                if (
                    edge.condition is None
                    or edge.condition(state)
                ):

                    next_node = edge.target
                    break

            current = next_node

        return state