from abc import ABC, abstractmethod

class BaseInfer(ABC):
    @abstractmethod
    def _load_weights(self):
        ...
    
    @abstractmethod
    def __call__(self):
        ...

    @staticmethod
    def force_input(input):
        if type(input) == str:
            import imghdr
            if imghdr.what(input) is not None:
                import cv2
                input = cv2.imread(input)
        return input    