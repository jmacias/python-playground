"""
* repr
* str
* format

Built in functions
"""

# %%


class Position:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        # Include all the data!
        # Format as python code, like a constructor code
        # so rather than hardcoded class name,  use
        return f"{type(self).__name__} (x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"Cords @ (x={self.x} , y={self.y})"

    def __format__(self, format_spec: str) -> str:
        # Follow format spec
        f = format_spec or ".2f"
        f_x = format(self.x, f)
        f_y = format(self.y, f)

        return f"Cords @ (x={f_x} , y={f_y})"


"""
everything inherit from Object

  `dir` function
"""

dir(Position(1, 1))

"""
We can override the dunder __str__, __repr__ or __format__
key to the built in method respectively
"""
p = Position(0, 0)
print(str(p))
print(repr(p))
print(format(p))
"""
Jupyter Server: local

BEFORE...
class Position:...
<__main__.Position object at 0x1029cefd0>

AFTER custom __repr__
"""

# str fn any OBJ to str,... __str__ delegates to __repr__
# repr is for devs.. str is for everyone...

# format delegates to str, but accept format spec
print(format(Position(1.123213123125124125124, 2.12424124125345643)))

help('FORMATTING')
