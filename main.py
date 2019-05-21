import cv2

import keras
import numpy as np
import pandas as pd
import tensorflow as tf

class Facial_Detection(keras.models.Model):
    def __init__(self):
        super().__init__()
        self.region_prop_network = None
        self.facial_classification_network = None
        self.region_extraction_network = None

    def call(self, frame):
        region_proposals = self.region_prop_network(frame)
        regions = self.region_extraction_network(region_proposals)
        for index, region in enumerate(regions):
            if self.facial_classification_network.predict(region, batch_size=1)[0]:
                regions.pop(index)
        return regions


# class Region_Propositional_Network
                


        