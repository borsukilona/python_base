'''из этого файла будет браться вся инфа, когда мы будем ипортировать куда-либо наш пакет
тут будет прописано, какие модули мы будем брать (или какие функции каких модулей и т.д.)'''

#from . import html, java, php, python
#from .php import *
#from .doc import * #имортираем пакет (и все его модули), который находится внутри нашего пакета

# from .python import get_python - обращаемся к текущему каталогу к модулю, и не надо прописывать директорию
# from courses.python import get_python - конкретная функция из модуля (не очень правильно, будет красное, но сработает)
#from stepik.module_package.courses.python import get_python так будет правильно если учитывать абсолютный путь
# import courses.python - весь модуль
# from .python import * - внутри пакета так можно делать, таким образом импорируем все модули пакета (ибо количество модулей внутри пакета может меняться)

NAME = 'package courses'

