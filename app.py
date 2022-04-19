import tensorflow as tf
import os, sys
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import pandas as pd
model_loaded = keras.models.load_model(r"C:\Users\Oksana\models\VKR")
col=['Cоотношение матрица-наполнитель %','Плотность, кг/м3 %', 'модуль упругости, ГПа %','Количество отвердителя, м.% %','Содержание эпоксидных групп,%_2 %','Температура вспышки, С_2 %','Поверхностная плотность, г/м2 %','Модуль упругости при растяжении,ГПа %','Потребление смолы, г/м2 %','Угол нашивки, град %','Шаг нашивки %','Плотность нашивки %']
diap=['(0.88.....8.5)','(2300......3882)', '(4......2391)', '(50......291)','(20......48)', '(260......636)','(3.....1791)','(86.....144)','(90.....590)','(0...173)','(1.....21)','(39....138)']
input_val = pd.DataFrame()
j = []
i = 0
print("Модель прогноза- Прочность при растяжении, Мпа %")
while i < len(col):
    line = f" {col[i]}{diap[i]}: "
    while True:
        try:
            param_val = input(line)
            param_value=float(param_val)
        except:
            print("ОШИБКА введите числовое значение")
            continue
        break
    j.append(param_value)
    i += 1
df= pd.DataFrame([j],columns =col)
test_predictions = model_loaded.predict(df).flatten()
print(" Прогнозное значение прочность при растяжении:",str(test_predictions)[1:-1])

