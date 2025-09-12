def chai_flavour(flavour="masala"):
    """Return the flavour of chai""" # this is doc string or function documentation string
    return flavour

print(chai_flavour.__doc__)
print(chai_flavour.__name__)


def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa

    :param chai: Number of chai cups (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    : return: (total amount, thank you message)
    """

    total = chai*10 + samosa*15
    return total, "Thank you for visiting chaicode.com"

print(generate_bill.__doc__)