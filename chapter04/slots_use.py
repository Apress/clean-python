class WithSlots:
    """Using __slots__ magic here."""
    __slots__ = "foo"


class WithoutSlots:
    """Not using __slots__ here."""
    pass


with_slots = WithSlots()
without_slots = WithoutSlots()


with_slots.foo = "Foo"
without_slots.foo = "Foo"


"""
>> %timeit with_slots.foo
44.5 ns
>> %timeit without_slots.foo
54.5 ns
"""
