# -*- coding: utf-8 -*-
"""expressao_facial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FbNUvsCh21zkm2svJ4cznoLR4wcOcbFS

**Algoritmo de InteligĂȘncia Artificial**
"""

import cv2
import numpy as np
import pandas as pd
from google.colab.patches import cv2_imshow
import zipfile

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x

import tensorflow
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
tensorflow.__version__

from google.colab import drive
drive.mount('/content/gdrive')

path = "/content/gdrive/My Drive/Material.zip"
zip_object = zipfile.ZipFile(file = path, mode = "r")
zip_object.extractall('./')
zip_object.close

imagem = cv2.imread('Material/testes/teste04.jpg')
cv2_imshow(imagem)

imagem.shape

cascade_faces = "Material/haarcascade_frontalface_default.xml"
caminho_modelo = "Material/modelo_01_expressoes.h5"
face_detection = cv2.CascadeClassifier(cascade_faces)
classificador_emocoes = load_model(caminho_modelo, compile = False)
expressoes = ["Raiva", "Nojo", "Medo", "Feliz", "Triste", "Surpreso", "Neutro"]

faces = face_detection.detectMultiScale(imagem, scaleFactor = 1.2,
                                        minNeighbors = 5, minSize = (20,20))

faces

len(faces)

faces.shape

cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2_imshow(cinza)

cinza.shape

original = imagem.copy()

for (x, y, w, h) in faces: 
  roi = cinza[y:y + h, x:x + w]

  roi = cv2.resize(roi, (48, 48))

  cv2_imshow(roi)
  
  roi = roi.astype("float") / 255
  roi = img_to_array(roi)
  roi = np.expand_dims(roi, axis = 0)
 
  preds = classificador_emocoes.predict(roi)[0]
  print(preds)

  emotion_probability = np.max(preds)
  print(emotion_probability)

  print(preds.argmax())
  label = expressoes[preds.argmax()]

  cv2.putText(original, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.65,
            (0, 255, 0), 2, cv2.LINE_AA)
  cv2.rectangle(original, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2_imshow(original)

"""# Nova seĂ§ĂŁo"""