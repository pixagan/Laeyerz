from laeyerz.flow.Flow import Flow
from laeyerz.flow.Node import Node
from laeyerz.flow.Edge import Edge
from laeyerz.flow.Model import Model


simple_flow = Flow()

def model0(app_state):
    input0 = app_state.get_params(["input0"])

    print("Model 0 :", input0)

    output = {"output0":0}

    return output


simple_flow.add_node("Model 0", model0)


def model1(app_state):
    input1 = app_state.get_params(["input1"])

    print("Model 1 :", input1)

    output = {"output1":1}

    return output

simple_flow.add_node("Model 1", model1)


def model2(app_state):
    input2 = app_state.get_params(["input2"])

    print("Model 2 :", input2)

    output = {"output2":2}

    return output

simple_flow.add_node("Model 2", model2)



simple_flow.add_edge("START", "Model 0")
simple_flow.add_edge("Model 0", "Model 1")
simple_flow.add_edge("Model 1", "Model 2")
simple_flow.add_edge("Model 2", "END")

simple_flow.finalize()

input_data = {
    "input0": "Hello, world!"
}
output = simple_flow.evaluate(input_data)






# simple_flow.add_edge("START", node_0.id)


# simple_flow.finalize()

# input_data = {
#     "input0": "Hello, world!"
# }

# output = simple_flow.evaluate(input_data)


# simple_flow.add_nodes([node_0, node_1, node_2])
# simple_flow.add_edges([edge_1, edge_2])
# simple_flow.start = node_0.id



# simple_flow.finalize()

# input_data = {}

# output = simple_flow.evaluate(input_data)











