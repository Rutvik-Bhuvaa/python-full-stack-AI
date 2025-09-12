class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dic(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)
        
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]


print(ChaiUtils.is_valid_size("Medium"))


order_one = ChaiOrder.from_dic({"tea_type": "Ginger", "sweetness": "No", "size": "Small"})

order_two = ChaiOrder.from_string("Lemon-Yes-Large")

order_three = ChaiOrder("Oolong", "No", "Medium")

print(order_one.__dict__)
print(order_two.__dict__)
print(order_three.__dict__)