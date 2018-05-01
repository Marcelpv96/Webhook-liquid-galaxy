"""
- Functions have to has the following template:

    def function_name(request):
        return "message which is said on google assistant"
"""


def function1(request):
    """
    Here code that will be executed
    """
    return "Triggered function number one"




"""
- This dictionary use the following schema:
    {"Intent name": function that trigger}

- In this case, intent name function_1 -> triggers function1().
"""
lg_functions = {"function_1": function1}
