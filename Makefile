install: #Устанавливаем Poetry
	poetry install
brain-games: #Приветствие
	poetry run brain-games
build: #Собираем пакет
	poetry build
publish: #Публикуем пакет в PyPI, не добавляем в каталог
	poetry publish --dry-run
package-install: #Устанавливаем пакет из ОС
	python3 -m pip install --user dist/*.whl
lint: #Запускаем проверку линтером
	poetry run flake8 brain_games
brain-even: #Игра чёт-нечёт
	poetry run brain-even
brain-calc: #Игра калькулятор
	poetry run brain-calc
brain-gcd: #Игра НОД
	poetry run brain-gcd
brain-progression: #Игра арифметическая прогрессия
	poetry run brain-arithm-progress
brain-prime: #Игра "простое число или нет"
	poetry run brain-prime
