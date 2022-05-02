class Product:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color

    def transform_name_for_sku(self):
        return self.name.upper()

    def transform_color_for_sku(self):
        return self.color.upper()

    def generate_sku(self):
        """
        この製品のSKU (Stock Keeping Unit: 最小管理単位)を生成する
        """
        name = self.transform_name_for_sku()
        color = self.transform_color_for_sku()
        return f"{name}-{self.size}-{color}"
