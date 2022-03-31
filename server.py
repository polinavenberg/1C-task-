import socket
from game import words
from random import randint
import threading


def one_game(words_list, client_socket):
    word = words_list[randint(0, len(words_list))]
    hidden_word = '*' * len(word)
    hidden_list = list(hidden_word)
    word_list = list(word)
    used_letters = []
    tries = len(word) * 2
    count_help = 0

    text_about_tries = 'У Вас есть ' + str(tries) + ' попыток.\n'

    text_every_step = 'Введите одну русскую букву или все слово сразу' + (
                ' или напишите "подсказка"' if count_help < 1 else '') + '\n'

    client_socket.send((hidden_word + '\n' + text_about_tries + text_every_step).encode('utf-8'))

    for i in range(tries):
        letter = client_socket.recv(1024).decode('utf-8').lower()

        if letter == 'подсказка' and count_help < 1:
            count_help += 1
            client_socket.send('Какую букву вы хотите открыть?'.encode('utf-8'))
            ind = int(client_socket.recv(1024).decode('utf-8'))
            text_about_help = ''

            while 0 < ind < len(hidden_word) and hidden_word[ind] != '*':
                client_socket.send('Эта буква уже открыта, введите другую позицию'.encode('utf-8'))
                ind = int(client_socket.recv(1024).decode('utf-8'))

            if 0 < ind < len(hidden_word):
                let = word_list[ind - 1]
                count = 0
                for j in range(len(word)):
                    if word_list[j] == let:
                        hidden_list[j] = let
                        count += 1
                hidden_word = ''.join(hidden_list)
                text_about_help += 'Вы открыли ' + str(count) + ' ' + ('букву\n' if count == 1 else 'буквы\n')
                hidden_list[ind - 1] = let
                used_letters.append(let)
                text_about_help += 'Вам больше нельзя использовать подсказки\n'
                text_about_help += hidden_word + '\n'
            else:
                text_about_help += 'Зачем ломать игру? В слове нет буквы с таким номером\n'
                text_about_help += hidden_word + '\n'

            text_every_step = 'Введите одну русскую букву или все слово сразу' + (
                ' или напишите "подсказка"' if count_help < 1 else '') + '\n'

            text_to_send = text_every_step + 'Вы уже вводили эти буквы: ' + ' '.join(
                used_letters) + '\n' + 'У вас осталось ' + str(
                tries - i - 1) + ' попыток\n'

            client_socket.send((text_about_help + text_to_send).encode('utf-8'))

        else:
            if letter == 'подсказка' and count_help == 1:
                client_socket.send(('Вы уже использовали подсказку, введите что-нибудь другое\n').encode('utf-8'))
                letter = client_socket.recv(1024).decode('utf-8').lower()

            if len(letter) == len(word):
                if letter == word:
                    client_socket.send(('Ура, вы угадали слово\n' + 'Напишите "да", если хотите продолжить играть, иначе "нет"').encode('utf-8'))
                    answer = client_socket.recv(1024).decode('utf-8').lower()
                    if answer != "да":
                        client_socket.send('End'.encode('utf-8'))
                        return 0
                    return 1
                else:
                    text_every_step = 'Введите одну русскую букву или все слово сразу' + (
                        ' или напишите "подсказка"' if count_help < 1 else '') + '\n'
                    text_to_send = text_every_step + 'Вы уже вводили эти буквы: ' + ' '.join(
                        used_letters) + '\n' + 'У вас осталось ' + str(
                        tries - i - 1) + ' попыток\n'

                    client_socket.send(('Неправильное слово или неверный ввод\n' + hidden_word + '\n' + text_to_send).encode('utf-8'))

            else:
                while (not (len(letter) == 1 and ord(letter) >= (ord('а')) and ord(
                        letter) <= (ord('я')))) or letter in used_letters:
                    if letter in used_letters:
                        client_socket.send(('Эта буква уже была введена, введите другую букву\n').encode('utf-8'))
                    else:
                        client_socket.send(('Неверный ввод, попробуйте еще раз\n').encode('utf-8'))
                    letter = client_socket.recv(1024).decode('utf-8').lower()

                used_letters.append(letter)

                if letter not in word_list:
                    text_every_step = 'Введите одну русскую букву или все слово сразу' + (
                        ' или напишите "подсказка"' if count_help < 1 else '') + '\n'
                    text_to_send = text_every_step + 'Вы уже вводили эти буквы: ' + ' '.join(
                        used_letters) + '\n' + 'У вас осталось ' + str(
                        tries - i - 1) + ' попыток\n'

                    client_socket.send(('Такой буквы в слове нет\n' + hidden_word + '\n' + text_to_send).encode('utf-8'))
                else:
                    count = 0
                    for j in range(len(word)):
                        if word_list[j] == letter:
                            hidden_list[j] = letter
                            count += 1

                    hidden_word = ''.join(hidden_list)
                    if '*' not in hidden_word:
                        client_socket.send(('Поздравляю, вы угадали слово!\n' + 'Напишите "да", если хотите продолжить играть, иначе "нет".').encode('utf-8'))
                        answer = client_socket.recv(1024).decode('utf-8').lower()
                        if answer != "да":
                            client_socket.send('End'.encode('utf-8'))
                            return 0
                        return 1
                    else:
                        text_every_step = 'Введите одну русскую букву или все слово сразу' + (
                            ' или напишите "подсказка"' if count_help < 1 else '') + '\n'

                        text_to_send = text_every_step + 'Вы уже вводили эти буквы: ' + ' '.join(
                            used_letters) + '\n' + 'У вас осталось ' + str(
                            tries - i - 1) + ' попыток\n'

                        client_socket.send(('вы угадали ' + str(count) + ' ' + ('букву\n' if count == 1 else 'буквы\n') + hidden_word + '\n' + text_to_send).encode('utf-8'))
        if '*' in hidden_word and i == tries - 1:
            client_socket.send(('К сожалению, вы проиграли\n' + 'Это было слово ' + word + '\n' + 'Напишите "да", если хотите продолжить играть, иначе "нет".').encode('utf-8'))

            answer = client_socket.recv(1024).decode('utf-8').lower()
            if answer == 'нет':
                client_socket.send('End'.encode('utf-8'))
                return 0
            return 1
    return 0


def game(client_socket):
    rule = 'Игра "Поле Чудес". Вам загадано слово. \n' \
           'Вы можете ввести латинскую букву или все слово сразу. е = ё. ' \
           'Также за всю игру вы можете получить 1 подсказку. Удачи!\n'

    client_socket.send(rule.encode('utf-8'))

    while True:
        flag = one_game(words, client_socket)
        if flag == 0:
            client_socket.close()
            break



def main():
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    serv_socket.bind(('127.0.0.1', 53210))
    serv_socket.listen(100)

    while True:
        client_socket, client_address = serv_socket.accept()
        print('Connected by', client_address)
        thread = threading.Thread(target=game, args=(client_socket,))
        thread.start()


if __name__ == '__main__':
    main()
