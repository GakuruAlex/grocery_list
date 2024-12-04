class Grocery:
    def __init__(self):
        self.grocery_list = {}
    
    def add_grocery_item(self, item: str)-> dict:
        if item in self.grocery_list:
            self.grocery_list[item] += 1
            return self.grocery_list
        else:
            self.grocery_list[item] = 1
   

    def main(self):
        while True:
            try:
                grocery_item: str = input("")
            except EOFError:
                print(self.print_grocery_items())
                break
            else:
                self.add_grocery_item(grocery_item)
  
if __name__ == "__main__":
    grocery = Grocery()
    grocery.main()