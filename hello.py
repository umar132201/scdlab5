class Rectangle(Shape):
    def _init_(self, length, width):
        super()._init_("Rectangle")
        self.__length = length
        self.__width = width