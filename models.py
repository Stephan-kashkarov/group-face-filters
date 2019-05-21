import cv2

import keras
import numpy as np
import pandas as pd
import tensorflow as tf

def region_extraction(frame, regions):
    pass


class Region_Propositional_Network(keras.models.Model):
    def __init__(self):
        super().__init__()
        
    def call(self, frame):
        pass

            
class Facial_Classification_Network(keras.models.Model):
    def __init__(self):
        super().__init__()

    def call(self, face):
        pass


class Facial_Detection_Network(keras.models.Model):
    def __init__(self):
        super().__init__()
        self.region_prop_network = Region_Propositional_Network()
        self.facial_classification_network = Facial_Classification_Network()

    def call(self, frame):
        region_proposals = self.region_prop_network.predict(frame)
        for index, region in region_extraction(frame, region_proposals):
            if self.facial_classification_network.predict(region, batch_size=1)[0]:
                regions.pop(index)
        return regions



        