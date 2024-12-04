class Grocery:
    def __init__(self):
        self.grocery_list = {}
    
    def add_grocery_item(self, item: str)-> dict:
        if item in self.grocery_list:
            self.grocery_list[item] += 1
            return self.grocery_list
        else:
            self.grocery_list[item] = 1
    
  
if __name__ == "__main__":
    grocery = Grocery()
    grocery.main()