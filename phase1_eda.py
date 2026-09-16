import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# RUL = Entire life of the engine (The last cycle) - Current cycle


INDEX_COLS = ["unit", "cycle"]
SETTING_COLS = ["op_setting1","op_setting2","op_setting3"]
SENSOR_COLS = [f"sensor_{i}" for i in range(1,22)] # 6th -26th columns (n=21)
ALL_COLS = INDEX_COLS + SETTING_COLS + SENSOR_COLS
