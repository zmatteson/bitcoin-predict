from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.models import load_model
from btc.models import Price


def index(request):
    return HttpResponse(Price.objects.all().order_by('?')[:10])