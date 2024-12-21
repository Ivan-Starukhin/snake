class point2d:
    def __init__(self, i_x=0.0, i_y=0.0) -> None:
        self.x = i_x
        self.y = i_y

    def __add__(self, other):
        return point2d(self.x + other.x, self.y + other.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def rest(self, num):
        return point2d(self.x % num, self.y % num)
    
class point3d:
    def __init__(self, i_x=0.0, i_y=0.0, i_z=0.0) -> None:
        self.x = i_x
        self.y = i_y
        self.z = i_z

    def __add__(self, other):
        return point2d(self.x + other.x, self.y + other.y, self.z + other.z)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    def rest(self, num):
        return point2d(self.x % num, self.y % num, self.z & num)

class game_info:
    class snake_info:
        def __init__(self, i_origin, i_move_direction="down") -> None:
            self.location = [i_origin]
            self.head = i_origin
            self.tail = i_origin
            self.move_direction = i_move_direction

    def __init__(self, i_field_size) -> None:
        self.is_valid = True
        self.field_size = i_field_size
        self.snake = self.snake_info(i_origin=point2d(int(i_field_size/2), int(i_field_size/2)))
        self.food = []
        self.barriers = []
