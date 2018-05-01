"""
- Functions have to has the following template:

    def function_name(request):
        return "message which will be said on google assistant"
"""


def function1(request):
    """
    Here insert code that will be executed
    """
    return "Triggered function number one"


"""
- This dictionary uses the following schema:
    {"Intent name ( intent name used in DialogFlow)": function that trigger}

- In this case, intent name function_1 -> triggers function1().
"""
lg_functions = {"function_1": function1}
