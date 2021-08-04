import inspect
from collections import OrderedDict


def filter_public_attributes(dict_instance):
    public_attributes = dict()
    for attr_name, attr_value in dict_instance.items():
        # to remove private and protected
        # functions
        # To remove other methods that
        # doesnot start with a underscore
        if (
            not attr_name.startswith("_")
            and not inspect.ismethod(attr_value)
            and not inspect.isclass(attr_value)
        ):
            public_attributes[attr_name] = attr_value

    return public_attributes


class MetaConstants(type):
    class Meta:
        hidden_constants = []

    def __init__(self, *args, **kwargs):

        self._names = tuple()
        self._values = tuple()
        self._n = 0
        self._constants = OrderedDict(
            filter_public_attributes(super().__dict__)
        )

        for attr_name, attr_value in self._constants.items():
            self._names += (attr_name,)
            self._values += (attr_value,)

    def __str__(self):
        return str(tuple(self))

    @property
    def __dict__(self):
        return dict(self._constants)

    def __iter__(self):
        self._n = 0
        return self

    def __next__(self):
        if self._n < len(self._names):
            attr_name = self._names[self._n]
            self._n += 1
            if attr_name not in self.Meta.hidden_constants:
                return getattr(self, attr_name)
            return self.__next__()

        raise StopIteration


class Constants(metaclass=MetaConstants):
    """
    Structure to allow access to constant values through dot
    notation in a comfortable fashion.

    Example:
    >>> class Numbers(Constants):
            class Meta:
                hidden_constants = ["INFINITE"]

            ONE = 1
            TWO = 2
            THREE = 3
            INFINITE = "inf"
    >>> list(Numbers)
    [1, 2, 3]
    >>> Numbers.__dict__
    {"ONE": 1, "TWO": 2, "THREE": 3, "INFINITE": "inf"}
    >>> Numbers.ONE
    1
    >>> 1 in Numbers
    True
    >>> Numbers.INFINITE
    'inf'
    >>> 'inf' in Numbers
    False

    """
