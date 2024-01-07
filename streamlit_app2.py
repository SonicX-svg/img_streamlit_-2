from tensorflow.keras.applications import EfficientNetB0
import streamlit as st
@st.cache(allow_output_mutation=True)
def load_model():
     model = EfficientNetB0(weights='imagenet')
     return model
     
def preprocess_image(img):
    x = image.img_to_array(img) #преобразование изображения в нампай массив
    x = np.expand_dmis(x, axis=0)
    x = preprocess_input(x) # преобразует значения пикселей изображения в значения от -1 до 1
    return x
    
def print_predictions(preds):
    classes = decode_predictions(preds, top=3)[0]
    for cl in classes:
        st.write(cl[1], cl[2])
        
        
        
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