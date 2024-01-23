"""test_main.py"""

from steamlit.testing.v1 import AppTest

def test_increment_and_add():
   at = AppTest.from_file('streamlit_app2.py').run()
   at = at.file_uploader[0].set_value('cat108.jpg')
   at.button[0].click()    #симулируем нажатие кнопки распознавания
             #получаем результат работы модели
   assert 'cat' in response.status_code #сравниваем с действительный ответом

   
