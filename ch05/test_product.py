from product import Product


class TestProduct:
    def test_transform_name_for_sku(self):
        small_black_shoes = Product("shoes", "S", "black")
        expected_value = "SHOES"
        actual_value = small_black_shoes.transform_name_for_sku()
        assert expected_value == actual_value

    def test_transform_color_for_sku(self):
        small_black_shoes = Product("shoes", "S", "black")
        expected_value = "BLACK"
        actual_value = small_black_shoes.transform_color_for_sku()
        assert expected_value == actual_value

    def test_generate_sku(self):
        small_black_shoes = Product("shoes", "S", "black")
        expected_value = "SHOES-S-BLACK"
        actual_value = small_black_shoes.generate_sku()
        assert expected_value == actual_value
