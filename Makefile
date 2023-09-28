install: #Устанавливаем Poetry
	poetry install
brain-games: #Запускаем игру
	poetry run brain-games
build: #Собираем пакет
	poetry build
publish: #Публикуем пакет в PyPI, не добавляем в каталог
	poetry publish --dry-run
package-install: #Устанавливаем пакет из ОС
	python3 -m pip install --user dist/*.whl
