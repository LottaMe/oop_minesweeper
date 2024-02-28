class InputHandler:
    def get_valid_input(self, max:int):
        i = input("Enter input between 0 and " + str(max) + ":  ")
        while not self.__is_valid_input(i=i, max=max):
            i = input("try again")
        return i
    
    def __is_valid_input(self, i:str, max: int):
        if not i.isdigit() or int(i)>= max:
            return False
        return True