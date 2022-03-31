# Игра "Поле Чудес"

Игра, в которой нужно угадать слово по буквам. Используется coding utf-8.


## Описание

В начале игры загадывается одно слово на русском языке. Выводится в виде "*****". Количество "*" равно количеству букв в слове.

Далее игроку дается количество попыток, в два раза большее длины слова. Каждый шаг подробно описывается комментариями в консоли.

В игре можно воспользоваться подсказкой, но всего 1 раз. Также можно не только угадывать слово по буквам, но и ввести все слово сразу.

Взаимодействие игры и игрока происходит с помощью двух программ “сервер” и “клиент”, которые написаны при помощи *socket*

В программе реализована возможность, чтобы в игру могли играть несколько игроков одновременно, что реализуется при помощи *threading*.

## Как запустить

Для запуска нужно скачать файлы из репозитория. Файлы *game.py* и *server.py* должны лежать в одной папке и запустить в PyCharm файл *client.py* или в консоли с помощью команды:
```
python client.py
```
В консоли должен быть coding: utf-8
