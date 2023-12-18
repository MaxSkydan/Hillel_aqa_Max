	https://github.com/antohaUa/hillel_aqa_301123
	antoha.ua@gmail.com

#Create a virtual environment
	python -m venv venv  - для создания виртуального окружения
#Activate virtual environment
	venv/Scripts/activate - для активации виртуального окружения
	deactivate - для деактивации виртуального окружения
#For debug on cmd ipython
	В виртуальных окружениях, созданных под Windows, в подкаталоге Scripts лежит activate.bat,
	который и служит "аналогом linux команды source".
	C:\Users\Максим\PycharmProjects\Hillel_aqa_Max\venv\Scripts\activate.bat
	ipython
	dir(str) - для просмотра всех возможных методов
	help(str.count) - для просмотра что делает метод
#How install and use linter
	pip install wemake-python-styleguide
	добавь файл setup.cfg в папку корневую проекта
	файл setup.cfg должен иметь в себе эту информацию  -
	[flake8]
	ignore=WPS,DAR
	min-name-length=3
	venv/scripts/flake8.exe c:/users/Максим/pycharmprojects/hillel_aqa_max/newtest.py - для запуска проверки
	(смотри что бы запуск происходил с папки в которой есть нужная тебе venv и проверь абсолютный путь)
	либо запускай с любой директории, но нужно точно указывать абсолютный путь
	(C:/Users/Максим/PycharmProjects/Hillel_aqa_Max/venv/Scripts/flake8.exe /
	c:/users/Максим/pycharmprojects/hillel_aqa_max/hillel_aqa_max/first_program.py)