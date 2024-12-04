class Grocery:
    def __init__(self):
        self.grocery_dict = {}
    
    def add_grocery_item(self, item: str)-> dict:
        """_Adds an item to the grocery dictionary_

        Args:
            item (str): _Item you need to shop_

        Returns:
            dict: _dictionary of item and count of the item_
        
        Example:
            Starting with empty dict
            >>> add_grocery_item("tomato")
                {"tomato":1}
            >>> add_grocery_item("tomato")
                {"tomato":2}
        """
        if item in self.grocery_dict:
            self.grocery_dict[item] += 1
        else:
            self.grocery_dict[item] = 1
        return self.grocery_dict
   
    def print_grocery_items(self)-> dict:
        """_Print grocery items begining with count then the item sorted in alphabetic order_
        
            Example:
                For the dict {"tomato":3, "apple":4}
                >>> print_grocery_list()
                    4 APPLE
                    3 TOMATO
        """
        for item, count in sorted(self.grocery_dict.items()):
            print(f"{count} {item.upper()}")

    def main(self):
        while True:
            try:
                grocery_item: str = input("")
                if grocery_item == "":
                    raise KeyError
            except EOFError:
                print("")
                self.print_grocery_items()
                break
            except KeyError:
                self.main()
            else:
                self.add_grocery_item(grocery_item)
  
if __name__ == "__main__":
    grocery = Grocery()
    grocery.main()