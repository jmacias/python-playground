"""
Data Classes
 * What are they
 * how to define it
 * When to use it
"""

# %%

from dataclasses import dataclass, field
# Good defaults for immutable value objects :)


@dataclass(frozen=True, eq=True)
class MyVals:
    name: str
    value: int
    mylist: list = field(default_factory=list)

    def __post_init__(self):  # Good place for validations
        if self.name is "Test":
            raise ValueError


MyVals("name", 2, [1, 1])


# %% Error
MyVals("Test", 2)
