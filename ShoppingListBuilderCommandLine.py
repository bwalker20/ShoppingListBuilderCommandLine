import Recipe

class App:
    def __init__(self):
        #create initial variables
        self.recipe = Recipe.Recipe()
        self.shopping_list = dict()
        
    def mainloop(self):
        #create main running loop
        var = 'A'
        while var != 'E':
            print("Please decide what you would like to do")
            print("1. Enter A to add a new recipe")
            print("2. Enter S to select from recipes")
            print("3. Enter P to print your current shopping list")
            print("4. Enter E to exit")
            var = input()
            if var == 'A':
                self.recipe.add_new()
            elif var == 'S':
                self.recipe.select(self.shopping_list)
            elif var == 'P':
                self.print_list()
            elif var == 'E':
                continue
            else:
                print("Please enter a valid command")

    def print_list(self):
        for i in self.shopping_list:
            print(str(self.shopping_list[i]) + " : " + i)

app = App()
app.mainloop()