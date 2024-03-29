import streamlit as st
import tensorflow as tf
import io
from PIL import Image
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.applications.efficientnet import decode_predictions
import numpy as np

@st.cache(allow_output_mutation=True)
def load_model():
     model = EfficientNetB0(weights='imagenet')
     return model
     
def preprocess_image(img):
    x = image.img_to_array(img) #преобразование изображения в нампай массив
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x) # преобразует значения пикселей изображения в значения от -1 до 1
    return x
    
def print_predictions(preds):
    classes = decode_predictions(preds, top=3)[0]
    for cl in classes:
        st.write(cl[1], cl[2])
def load_image():
    """Создание формы для загрузки изображения"""
    # Форма для загрузки изображения средствами Streamlit
    uploaded_file = st.file_uploader(
        label='Выберите изображение для распознавания')
    if uploaded_file is not None:
        # Получение загруженного изображения
        image_data = uploaded_file.getvalue()
        # Показ загруженного изображения на Web-странице средствами Streamlit
        st.image(image_data)
        # Возврат изображения в формате PIL
        return Image.open(io.BytesIO(image_data))
    else:
        return None        
        
        
# Загружаем предварительно обученную модель
model = load_model()
# Выводим заголовок страницы
st.title('Классификация изображений')
# Выводим форму загрузки изображения и получаем изображение
img = load_image()
# Показывам кнопку для запуска распознавания изображения
result = st.button('Распознать изображение')
# Если кнопка нажата, то запускаем распознавание изображения
if result:
    # Предварительная обработка изображения
    x = preprocess_image(img)
    # Распознавание изображения
    preds = model.predict(x)
    # Выводим заголовок результатов распознавания жирным шрифтом
    # используя форматирование Markdown
    st.write('**Результаты распознавания:**')
    # Выводим результаты распознавания
    print_predictions(preds)
