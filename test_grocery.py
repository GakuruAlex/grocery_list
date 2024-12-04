import pytest
from grocery import Grocery

@pytest.mark.parametrize("item, dict",[
    ("apple", {"apple": 1}),
    ("apple", {"apple": 2}),
    ("ice cream", {"apple": 2, "ice cream": 1})
])

class TestAddGroceryitem:
    grocery = Grocery()
    
    def test_add_grocery_item(self, item, dict):
        assert self.grocery.add_grocery_item(item) == dict