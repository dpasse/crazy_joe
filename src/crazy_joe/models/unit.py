class Unit(object):
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f'{class_name}(name="{self.name}")'
