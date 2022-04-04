import random
import keras
import keras
from keras.layers import Input
from keras.models import Model
from keras.applications.resnet import preprocess_input, decode_predictions
import os
from PIL import Image
import numpy as np
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSessions
