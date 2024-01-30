# QUESTION: What would be a good way to separate this interface?

from abc import ABCMeta, abstractmethod
class IPerceptionSystem(metaclass=ABCMeta):

    @abstractmethod
    def connect(self):
        raise NotImplementedError()

    @abstractmethod
    def capture(self):
        raise NotImplementedError()
    
    @abstractmethod
    def disconnect(self):
        raise NotImplementedError()
    
    @abstractmethod
    def segment_img(self):
        raise NotImplementedError()
    
    @abstractmethod
    def predict_shape(self):
        raise NotImplementedError()
    
    @abstractmethod
    def predict_material(self):
        raise NotImplementedError()
    
    @abstractmethod
    def generate_pick_points(self):
        raise NotImplementedError()
    

### Notes ### (There is no right answer and the way it should be separated really depends on requirements)
    # DeviceInterface
        # connect
        # disconnect
    
    # Camera Interface
        # capture
    
    # PerceptionSystemInterface
        # generate pick points
        # segment_img
    
    # PredictProperties
        # predict_shape
        # predict_material


