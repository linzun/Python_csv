# -*- coding = utf-8 -*-
# @Time :  2023/3/12/0012 21:15
# @Author : HeyBro
# @File : cav_demo.py
# @Software : PyCharm


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
#import xlwt                                #进行excel操作
import csv
from astropy.convolution.kernels import Gaussian2DKernel
from astropy.convolution import convolve
#matplotlib.use('qt')

path1 = r"filder.flider"

list1 = pd.read_csv(path1,sep=',',dtype=float)
