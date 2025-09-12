class ChaiUtils:

    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

raw = " water ,  milk, ginger  , honey  "

obj = ChaiUtils()
print(obj.clean_ingredients(raw))

# Static method doesn't require anyobject creation
cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)
