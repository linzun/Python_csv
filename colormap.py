# -*- coding = utf-8 -*-
# @Time :  2023/4/10/0010 19:24
# @Author : HeyBro
# @File : colormap.py
# @Software : PyCharm
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
def Get_cmap():
    cm_data = np.array([
        [0,0,0],
        [0,0,0.0322580645161290],
        [0,0,0.0645161290322581],
        [0,0,0.0967741935483871],
        [0,0,0.129032258064516],
        [0,0,0.161290322580645],
        [0,0,0.193548387096774],
        [0,0,0.225806451612903],
        [0,0,0.258064516129032],
        [0,0,0.290322580645161],
        [0,0,0.322580645161290],
        [0,0,0.354838709677419],
        [0,0,0.387096774193548],
        [0,0,0.419354838709677],
        [0,0,0.451612903225806],
        [0,0,0.483870967741936],
        [0,0,0.516129032258065],
        [0,0,0.548387096774194],
        [0,0,0.580645161290323],
        [0,0,0.612903225806452],
        [0,0,0.645161290322581],
        [0,0,0.677419354838710],
        [0,0,0.709677419354839],
        [0,0,0.741935483870968],
        [0,0,0.774193548387097],
        [0,0,0.806451612903226],
        [0,0,0.838709677419355],
        [0,0,0.870967741935484],
        [0,0,0.903225806451613],
        [0,0,0.935483870967742],
        [0,0,0.967741935483871],
        [0,0,1],
        [0,0.0156250000000000,1],
        [0,0.0312500000000000,1],
        [0,0.0468750000000000,1],
        [0,0.0625000000000000,1],
        [0,0.0781250000000000,1],
        [0,0.0937500000000000,1],
        [0,0.109375000000000,1],
        [0,0.125000000000000,1],
        [0,0.140625000000000,1],
        [0,0.156250000000000,1],
        [0,0.171875000000000,1],
        [0,0.187500000000000,1],
        [0,0.203125000000000,1],
        [0,0.218750000000000,1],
        [0,0.234375000000000,1],
        [0,0.250000000000000,1],
        [0,0.265625000000000,1],
        [0,0.281250000000000,1],
        [0,0.296875000000000,1],
        [0,0.312500000000000,1],
        [0,0.328125000000000,1],
        [0,0.343750000000000,1],
        [0,0.359375000000000,1],
        [0,0.375000000000000,1],
        [0,0.390625000000000,1],
        [0,0.406250000000000,1],
        [0,0.421875000000000,1],
        [0,0.437500000000000,1],
        [0,0.453125000000000,1],
        [0,0.468750000000000,1],
        [0,0.484375000000000,1],
        [0,0.500000000000000,1],
        [0,0.515625000000000,1],
        [0,0.531250000000000,1],
        [0,0.546875000000000,1],
        [0,0.562500000000000,1],
        [0,0.578125000000000,1],
        [0,0.593750000000000,1],
        [0,0.609375000000000,1],
        [0,0.625000000000000,1],
        [0,0.640625000000000,1],
        [0,0.656250000000000,1],
        [0,0.671875000000000,1],
        [0,0.687500000000000,1],
        [0,0.703125000000000,1],
        [0,0.718750000000000,1],
        [0,0.734375000000000,1],
        [0,0.750000000000000,1],
        [0,0.765625000000000,1],
        [0,0.781250000000000,1],
        [0,0.796875000000000,1],
        [0,0.812500000000000,1],
        [0,0.828125000000000,1],
        [0,0.843750000000000,1],
        [0,0.859375000000000,1],
        [0,0.875000000000000,1],
        [0,0.890625000000000,1],
        [0,0.906250000000000,1],
        [0,0.921875000000000,1],
        [0,0.937500000000000,1],
        [0,0.953125000000000,1],
        [0,0.968750000000000,1],
        [0,0.984375000000000,1],
        [0,1,1],
        [0.0156250000000000,1,0.984375000000000],
        [0.0312500000000000,1,0.968750000000000],
        [0.0468750000000000,1,0.953125000000000],
        [0.0625000000000000,1,0.937500000000000],
        [0.0781250000000000,1,0.921875000000000],
        [0.0937500000000000,1,0.906250000000000],
        [0.109375000000000,1,0.890625000000000],
        [0.125000000000000,1,0.875000000000000],
        [0.140625000000000,1,0.859375000000000],
        [0.156250000000000,1,0.843750000000000],
        [0.171875000000000,1,0.828125000000000],
        [0.187500000000000,1,0.812500000000000],
        [0.203125000000000,1,0.796875000000000],
        [0.218750000000000,1,0.781250000000000],
        [0.234375000000000,1,0.765625000000000],
        [0.250000000000000,1,0.750000000000000],
        [0.265625000000000,1,0.734375000000000],
        [0.281250000000000,1,0.718750000000000],
        [0.296875000000000,1,0.703125000000000],
        [0.312500000000000,1,0.687500000000000],
        [0.328125000000000,1,0.671875000000000],
        [0.343750000000000,1,0.656250000000000],
        [0.359375000000000,1,0.640625000000000],
        [0.375000000000000,1,0.625000000000000],
        [0.390625000000000,1,0.609375000000000],
        [0.406250000000000,1,0.593750000000000],
        [0.421875000000000,1,0.578125000000000],
        [0.437500000000000,1,0.562500000000000],
        [0.453125000000000,1,0.546875000000000],
        [0.468750000000000,1,0.531250000000000],
        [0.484375000000000,1,0.515625000000000],
        [0.500000000000000,1,0.500000000000000],
        [0.515625000000000,1,0.484375000000000],
        [0.531250000000000,1,0.468750000000000],
        [0.546875000000000,1,0.453125000000000],
        [0.562500000000000,1,0.437500000000000],
        [0.578125000000000,1,0.421875000000000],
        [0.593750000000000,1,0.406250000000000],
        [0.609375000000000,1,0.390625000000000],
        [0.625000000000000,1,0.375000000000000],
        [0.640625000000000,1,0.359375000000000],
        [0.656250000000000,1,0.343750000000000],
        [0.671875000000000,1,0.328125000000000],
        [0.687500000000000,1,0.312500000000000],
        [0.703125000000000,1,0.296875000000000],
        [0.718750000000000,1,0.281250000000000],
        [0.734375000000000,1,0.265625000000000],
        [0.750000000000000,1,0.250000000000000],
        [0.765625000000000,1,0.234375000000000],
        [0.781250000000000,1,0.218750000000000],
        [0.796875000000000,1,0.203125000000000],
        [0.812500000000000,1,0.187500000000000],
        [0.828125000000000,1,0.171875000000000],
        [0.843750000000000,1,0.156250000000000],
        [0.859375000000000,1,0.140625000000000],
        [0.875000000000000,1,0.125000000000000],
        [0.890625000000000,1,0.109375000000000],
        [0.906250000000000,1,0.0937500000000000],
        [0.921875000000000,1,0.0781250000000000],
        [0.937500000000000,1,0.0625000000000000],
        [0.953125000000000,1,0.0468750000000000],
        [0.968750000000000,1,0.0312500000000000],
        [0.984375000000000,1,0.0156250000000000],
        [1,1,0],
        [1,0.984375000000000,0],
        [1,0.968750000000000,0],
        [1,0.953125000000000,0],
        [1,0.937500000000000,0],
        [1,0.921875000000000,0],
        [1,0.906250000000000,0],
        [1,0.890625000000000,0],
        [1,0.875000000000000,0],
        [1,0.859375000000000,0],
        [1,0.843750000000000,0],
        [1,0.828125000000000,0],
        [1,0.812500000000000,0],
        [1,0.796875000000000,0],
        [1,0.781250000000000,0],
        [1,0.765625000000000,0],
        [1,0.750000000000000,0],
        [1,0.734375000000000,0],
        [1,0.718750000000000,0],
        [1,0.703125000000000,0],
        [1,0.687500000000000,0],
        [1,0.671875000000000,0],
        [1,0.656250000000000,0],
        [1,0.640625000000000,0],
        [1,0.625000000000000,0],
        [1,0.609375000000000,0],
        [1,0.593750000000000,0],
        [1,0.578125000000000,0],
        [1,0.562500000000000,0],
        [1,0.546875000000000,0],
        [1,0.531250000000000,0],
        [1,0.515625000000000,0],
        [1,0.500000000000000,0],
        [1,0.484375000000000,0],
        [1,0.468750000000000,0],
        [1,0.453125000000000,0],
        [1,0.437500000000000,0],
        [1,0.421875000000000,0],
        [1,0.406250000000000,0],
        [1,0.390625000000000,0],
        [1,0.375000000000000,0],
        [1,0.359375000000000,0],
        [1,0.343750000000000,0],
        [1,0.328125000000000,0],
        [1,0.312500000000000,0],
        [1,0.296875000000000,0],
        [1,0.281250000000000,0],
        [1,0.265625000000000,0],
        [1,0.250000000000000,0],
        [1,0.234375000000000,0],
        [1,0.218750000000000,0],
        [1,0.203125000000000,0],
        [1,0.187500000000000,0],
        [1,0.171875000000000,0],
        [1,0.156250000000000,0],
        [1,0.140625000000000,0],
        [1,0.125000000000000,0],
        [1,0.109375000000000,0],
        [1,0.0937500000000000,0],
        [1,0.0781250000000000,0],
        [1,0.0625000000000000,0],
        [1,0.0468750000000000,0],
        [1,0.0312500000000000,0],
        [1,0.0156250000000000,0],
        [1,0,0],
        [0.984375000000000,0,0],
        [0.968750000000000,0,0],
        [0.953125000000000,0,0],
        [0.937500000000000,0,0],
        [0.921875000000000,0,0],
        [0.906250000000000,0,0],
        [0.890625000000000,0,0],
        [0.875000000000000,0,0],
        [0.859375000000000,0,0],
        [0.843750000000000,0,0],
        [0.828125000000000,0,0],
        [0.812500000000000,0,0],
        [0.796875000000000,0,0],
        [0.781250000000000,0,0],
        [0.765625000000000,0,0],
        [0.750000000000000,0,0],
        [0.734375000000000,0,0],
        [0.718750000000000,0,0],
        [0.703125000000000,0,0],
        [0.687500000000000,0,0],
        [0.671875000000000,0,0],
        [0.656250000000000,0,0],
        [0.640625000000000,0,0],
        [0.625000000000000,0,0],
        [0.609375000000000,0,0],
        [0.593750000000000,0,0],
        [0.578125000000000,0,0],
        [0.562500000000000,0,0],
        [0.546875000000000,0,0],
        [0.531250000000000,0,0],
        [0.515625000000000,0,0],
        [0.500000000000000,0,0]
    ])
    Jet_black= LinearSegmentedColormap.from_list('jet', cm_data)
    # Jet_black = LinearSegmentedColormap.from_list('moreland', cm_data)
    return Jet_black