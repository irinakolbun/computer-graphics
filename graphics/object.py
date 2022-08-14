from abc import ABC, abstractmethod


class Object(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def ray_intersect(self, ray):
        pass
