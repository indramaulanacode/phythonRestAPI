"""
Comprehensive Python Class with All Special Methods
"""


class SpecialMethods:
    """A class demonstrating all Python special (magic) methods."""
    
    # ============================================
    # Object Creation and Initialization
    # ============================================
    
    def __new__(cls, *args, **kwargs):
        """Create a new instance of the class."""
        print(f"__new__ called for {cls}")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, value=0, name="Object"):
        """Initialize the instance."""
        print(f"__init__ called")
        self.value = value
        self.name = name
        self.data = []
    
    def __del__(self):
        """Destructor called when instance is about to be destroyed."""
        print(f"__del__ called for {self.name}")
    
    # ============================================
    # String Representation
    # ============================================
    
    def __repr__(self):
        """Official string representation for debugging."""
        return f"SpecialMethods(value={self.value}, name='{self.name}')"
    
    def __str__(self):
        """Informal string representation for end users."""
        return f"{self.name}: {self.value}"
    
    def __bytes__(self):
        """Convert to bytes."""
        return str(self).encode('utf-8')
    
    def __format__(self, format_spec):
        """Custom format specification."""
        if format_spec == 'v':
            return f"Value: {self.value}"
        elif format_spec == 'n':
            return f"Name: {self.name}"
        return str(self)
    
    # ============================================
    # Comparison Operators
    # ============================================
    
    def __lt__(self, other):
        """Less than: <"""
        return self.value < other.value
    
    def __le__(self, other):
        """Less than or equal: <="""
        return self.value <= other.value
    
    def __eq__(self, other):
        """Equal: =="""
        if isinstance(other, SpecialMethods):
            return self.value == other.value
        return False
    
    def __ne__(self, other):
        """Not equal: !="""
        return not self.__eq__(other)
    
    def __gt__(self, other):
        """Greater than: >"""
        return self.value > other.value
    
    def __ge__(self, other):
        """Greater than or equal: >="""
        return self.value >= other.value
    
    def __hash__(self):
        """Make instance hashable (for use in sets/dicts)."""
        return hash((self.value, self.name))
    
    def __bool__(self):
        """Truth value testing."""
        return self.value != 0
    
    # ============================================
    # Arithmetic Operators
    # ============================================
    
    def __add__(self, other):
        """Addition: +"""
        if isinstance(other, SpecialMethods):
            return SpecialMethods(self.value + other.value)
        return SpecialMethods(self.value + other)
    
    def __sub__(self, other):
        """Subtraction: -"""
        if isinstance(other, SpecialMethods):
            return SpecialMethods(self.value - other.value)
        return SpecialMethods(self.value - other)
    
    def __mul__(self, other):
        """Multiplication: *"""
        if isinstance(other, SpecialMethods):
            return SpecialMethods(self.value * other.value)
        return SpecialMethods(self.value * other)
    
    def __truediv__(self, other):
        """True division: /"""
        if isinstance(other, SpecialMethods):
            return SpecialMethods(self.value / other.value)
        return SpecialMethods(self.value / other)
    
    def __floordiv__(self, other):
        """Floor division: //"""
        if isinstance(other, SpecialMethods):
            return SpecialMethods(self.value // other.value)
        return SpecialMethods(self.value // other)
    
    def __mod__(self, other):
        """Modulo: %"""
        if isinstance(other, SpecialMethods):
            return SpecialMethods(self.value % other.value)
        return SpecialMethods(self.value % other)
    
    def __divmod__(self, other):
        """Divmod function."""
        if isinstance(other, SpecialMethods):
            return divmod(self.value, other.value)
        return divmod(self.value, other)
    
    def __pow__(self, other, modulo=None):
        """Power: **"""
        if isinstance(other, SpecialMethods):
            result = self.value ** other.value
        else:
            result = self.value ** other
        if modulo:
            result %= modulo
        return SpecialMethods(result)
    
    # ============================================
    # Reflected (Right) Arithmetic Operators
    # ============================================
    
    def __radd__(self, other):
        """Reflected addition."""
        return SpecialMethods(other + self.value)
    
    def __rsub__(self, other):
        """Reflected subtraction."""
        return SpecialMethods(other - self.value)
    
    def __rmul__(self, other):
        """Reflected multiplication."""
        return SpecialMethods(other * self.value)
    
    def __rtruediv__(self, other):
        """Reflected true division."""
        return SpecialMethods(other / self.value)
    
    def __rfloordiv__(self, other):
        """Reflected floor division."""
        return SpecialMethods(other // self.value)
    
    def __rmod__(self, other):
        """Reflected modulo."""
        return SpecialMethods(other % self.value)
    
    def __rpow__(self, other):
        """Reflected power."""
        return SpecialMethods(other ** self.value)
    
    # ============================================
    # Augmented Assignment
    # ============================================
    
    def __iadd__(self, other):
        """In-place addition: +="""
        if isinstance(other, SpecialMethods):
            self.value += other.value
        else:
            self.value += other
        return self
    
    def __isub__(self, other):
        """In-place subtraction: -="""
        if isinstance(other, SpecialMethods):
            self.value -= other.value
        else:
            self.value -= other
        return self
    
    def __imul__(self, other):
        """In-place multiplication: *="""
        if isinstance(other, SpecialMethods):
            self.value *= other.value
        else:
            self.value *= other
        return self
    
    def __itruediv__(self, other):
        """In-place true division: /="""
        if isinstance(other, SpecialMethods):
            self.value /= other.value
        else:
            self.value /= other
        return self
    
    def __ifloordiv__(self, other):
        """In-place floor division: //="""
        if isinstance(other, SpecialMethods):
            self.value //= other.value
        else:
            self.value //= other
        return self
    
    def __imod__(self, other):
        """In-place modulo: %="""
        if isinstance(other, SpecialMethods):
            self.value %= other.value
        else:
            self.value %= other
        return self
    
    def __ipow__(self, other):
        """In-place power: **="""
        if isinstance(other, SpecialMethods):
            self.value **= other.value
        else:
            self.value **= other
        return self
    
    # ============================================
    # Unary Operators
    # ============================================
    
    def __neg__(self):
        """Unary negative: -obj"""
        return SpecialMethods(-self.value)
    
    def __pos__(self):
        """Unary positive: +obj"""
        return SpecialMethods(+self.value)
    
    def __abs__(self):
        """Absolute value: abs(obj)"""
        return SpecialMethods(abs(self.value))
    
    def __invert__(self):
        """Bitwise inversion: ~obj"""
        return SpecialMethods(~int(self.value))
    
    # ============================================
    # Type Conversion
    # ============================================
    
    def __complex__(self):
        """Convert to complex."""
        return complex(self.value)
    
    def __int__(self):
        """Convert to int."""
        return int(self.value)
    
    def __float__(self):
        """Convert to float."""
        return float(self.value)
    
    def __round__(self, n=0):
        """Round to n digits."""
        return round(self.value, n)
    
    def __trunc__(self):
        """Truncate to integral."""
        import math
        return math.trunc(self.value)
    
    def __floor__(self):
        """Floor value."""
        import math
        return math.floor(self.value)
    
    def __ceil__(self):
        """Ceiling value."""
        import math
        return math.ceil(self.value)
    
    def __index__(self):
        """Convert to index (for slicing)."""
        return int(self.value)
    
    # ============================================
    # Bitwise Operators
    # ============================================
    
    def __and__(self, other):
        """Bitwise AND: &"""
        if isinstance(other, SpecialMethods):
            return SpecialMethods(int(self.value) & int(other.value))
        return SpecialMethods(int(self.value) & int(other))
    
    def __or__(self, other):
        """Bitwise OR: |"""
        if isinstance(other, SpecialMethods):
            return SpecialMethods(int(self.value) | int(other.value))
        return SpecialMethods(int(self.value) | int(other))
    
    def __xor__(self, other):
        """Bitwise XOR: ^"""
        if isinstance(other, SpecialMethods):
            return SpecialMethods(int(self.value) ^ int(other.value))
        return SpecialMethods(int(self.value) ^ int(other))
    
    def __lshift__(self, other):
        """Left shift: <<"""
        if isinstance(other, SpecialMethods):
            return SpecialMethods(int(self.value) << int(other.value))
        return SpecialMethods(int(self.value) << int(other))
    
    def __rshift__(self, other):
        """Right shift: >>"""
        if isinstance(other, SpecialMethods):
            return SpecialMethods(int(self.value) >> int(other.value))
        return SpecialMethods(int(self.value) >> int(other))
    
    # Reflected bitwise operators
    def __rand__(self, other):
        """Reflected AND."""
        return SpecialMethods(int(other) & int(self.value))
    
    def __ror__(self, other):
        """Reflected OR."""
        return SpecialMethods(int(other) | int(self.value))
    
    def __rxor__(self, other):
        """Reflected XOR."""
        return SpecialMethods(int(other) ^ int(self.value))
    
    def __rlshift__(self, other):
        """Reflected left shift."""
        return SpecialMethods(int(other) << int(self.value))
    
    def __rrshift__(self, other):
        """Reflected right shift."""
        return SpecialMethods(int(other) >> int(self.value))
    
    # In-place bitwise operators
    def __iand__(self, other):
        """In-place AND: &="""
        if isinstance(other, SpecialMethods):
            self.value = int(self.value) & int(other.value)
        else:
            self.value = int(self.value) & int(other)
        return self
    
    def __ior__(self, other):
        """In-place OR: |="""
        if isinstance(other, SpecialMethods):
            self.value = int(self.value) | int(other.value)
        else:
            self.value = int(self.value) | int(other)
        return self
    
    def __ixor__(self, other):
        """In-place XOR: ^="""
        if isinstance(other, SpecialMethods):
            self.value = int(self.value) ^ int(other.value)
        else:
            self.value = int(self.value) ^ int(other)
        return self
    
    def __ilshift__(self, other):
        """In-place left shift: <<="""
        if isinstance(other, SpecialMethods):
            self.value = int(self.value) << int(other.value)
        else:
            self.value = int(self.value) << int(other)
        return self
    
    def __irshift__(self, other):
        """In-place right shift: >>="""
        if isinstance(other, SpecialMethods):
            self.value = int(self.value) >> int(other.value)
        else:
            self.value = int(self.value) >> int(other)
        return self
    
    # ============================================
    # Container/Sequence Methods
    # ============================================
    
    def __len__(self):
        """Return length: len(obj)"""
        return len(self.data)
    
    def __getitem__(self, key):
        """Get item: obj[key]"""
        return self.data[key]
    
    def __setitem__(self, key, value):
        """Set item: obj[key] = value"""
        self.data[key] = value
    
    def __delitem__(self, key):
        """Delete item: del obj[key]"""
        del self.data[key]
    
    def __iter__(self):
        """Return iterator: for x in obj"""
        return iter(self.data)
    
    def __reversed__(self):
        """Reversed iterator: reversed(obj)"""
        return reversed(self.data)
    
    def __contains__(self, item):
        """Membership test: item in obj"""
        return item in self.data
    
    # ============================================
    # Attribute Access
    # ============================================
    
    def __getattr__(self, name):
        """Get attribute that doesn't exist."""
        return f"Attribute '{name}' not found"
    
    def __setattr__(self, name, value):
        """Set attribute: obj.name = value"""
        super().__setattr__(name, value)
    
    def __delattr__(self, name):
        """Delete attribute: del obj.name"""
        super().__delattr__(name)
    
    def __getattribute__(self, name):
        """Get any attribute (called unconditionally)."""
        return super().__getattribute__(name)
    
    def __dir__(self):
        """Directory of attributes: dir(obj)"""
        return super().__dir__()
    
    # ============================================
    # Callable Objects
    # ============================================
    
    def __call__(self, *args, **kwargs):
        """Make instance callable: obj()"""
        print(f"Called {self.name} with args={args}, kwargs={kwargs}")
        return self.value
    
    # ============================================
    # Context Managers
    # ============================================
    
    def __enter__(self):
        """Enter context: with obj as x"""
        print(f"Entering context for {self.name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context."""
        print(f"Exiting context for {self.name}")
        if exc_type is not None:
            print(f"Exception: {exc_type}, {exc_val}")
        return False  # Don't suppress exceptions
    
    # ============================================
    # Async Context Managers (Python 3.5+)
    # ============================================
    
    async def __aenter__(self):
        """Async enter context: async with obj"""
        print(f"Async entering context for {self.name}")
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async exit context."""
        print(f"Async exiting context for {self.name}")
        return False
    
    # ============================================
    # Async Iteration (Python 3.5+)
    # ============================================
    
    def __aiter__(self):
        """Async iterator: async for x in obj"""
        return self
    
    async def __anext__(self):
        """Async next item."""
        if len(self.data) == 0:
            raise StopAsyncIteration
        return self.data.pop(0)
    
    # ============================================
    # Descriptor Protocol
    # ============================================
    
    def __get__(self, instance, owner):
        """Descriptor get."""
        print(f"__get__ called")
        return self
    
    def __set__(self, instance, value):
        """Descriptor set."""
        print(f"__set__ called with {value}")
        self.value = value
    
    def __delete__(self, instance):
        """Descriptor delete."""
        print(f"__delete__ called")
    
    def __set_name__(self, owner, name):
        """Set descriptor name (Python 3.6+)."""
        print(f"__set_name__ called: owner={owner}, name={name}")
    
    # ============================================
    # Pickling/Copying
    # ============================================
    
    def __getstate__(self):
        """Get state for pickling."""
        return {'value': self.value, 'name': self.name, 'data': self.data}
    
    def __setstate__(self, state):
        """Set state from unpickling."""
        self.value = state['value']
        self.name = state['name']
        self.data = state['data']
    
    def __reduce__(self):
        """Reduce for pickling."""
        return (self.__class__, (self.value, self.name))
    
    def __reduce_ex__(self, protocol):
        """Extended reduce for pickling."""
        return self.__reduce__()
    
    def __copy__(self):
        """Shallow copy: copy.copy(obj)"""
        return SpecialMethods(self.value, self.name)
    
    def __deepcopy__(self, memo):
        """Deep copy: copy.deepcopy(obj)"""
        import copy
        return SpecialMethods(copy.deepcopy(self.value, memo), 
                            copy.deepcopy(self.name, memo))
    
    # ============================================
    # Other Special Methods
    # ============================================
    
    def __sizeof__(self):
        """Return size in memory."""
        import sys
        return sys.getsizeof(self.value) + sys.getsizeof(self.name)
    
    def __instancecheck__(self, instance):
        """Custom isinstance() behavior."""
        return isinstance(instance, SpecialMethods)
    
    def __subclasscheck__(self, subclass):
        """Custom issubclass() behavior."""
        return issubclass(subclass, SpecialMethods)
    
    # ============================================
    # Class Methods
    # ============================================
    
    def __init_subclass__(cls, **kwargs):
        """Called when class is subclassed."""
        super().__init_subclass__(**kwargs)
        print(f"Subclass {cls.__name__} created")
    
    def __class_getitem__(cls, item):
        """Support for generic types: Class[Type]"""
        return f"{cls.__name__}[{item}]"


# ============================================
# Example Usage
# ============================================

if __name__ == "__main__":
    print("=" * 50)
    print("Creating objects")
    print("=" * 50)
    obj1 = SpecialMethods(10, "Object1")
    obj2 = SpecialMethods(5, "Object2")
    
    print("\n" + "=" * 50)
    print("String representations")
    print("=" * 50)
    print(f"str(obj1): {str(obj1)}")
    print(f"repr(obj1): {repr(obj1)}")
    print(f"format(obj1, 'v'): {format(obj1, 'v')}")
    
    print("\n" + "=" * 50)
    print("Comparisons")
    print("=" * 50)
    print(f"obj1 > obj2: {obj1 > obj2}")
    print(f"obj1 == obj2: {obj1 == obj2}")
    print(f"bool(obj1): {bool(obj1)}")
    
    print("\n" + "=" * 50)
    print("Arithmetic")
    print("=" * 50)
    obj3 = obj1 + obj2
    print(f"obj1 + obj2 = {obj3}")
    print(f"obj1 * 2 = {obj1 * 2}")
    
    print("\n" + "=" * 50)
    print("Container operations")
    print("=" * 50)
    obj1.data = [1, 2, 3, 4, 5]
    print(f"len(obj1): {len(obj1)}")
    print(f"obj1[0]: {obj1[0]}")
    print(f"2 in obj1: {2 in obj1}")
    
    print("\n" + "=" * 50)
    print("Callable")
    print("=" * 50)
    result = obj1("test", key="value")
    
    print("\n" + "=" * 50)
    print("Context manager")
    print("=" * 50)
    with obj1 as o:
        print(f"Inside context: {o}")
    
    print("\n" + "=" * 50)
    print("Type conversions")
    print("=" * 50)
    print(f"int(obj1): {int(obj1)}")
    print(f"float(obj1): {float(obj1)}")
    print(f"abs(SpecialMethods(-5)): {abs(SpecialMethods(-5))}")
