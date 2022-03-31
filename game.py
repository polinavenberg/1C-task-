# -*- coding: utf-8 -*-
from random import randint

words = ['подпись', 'вырез', 'гранит', 'кругозор', 'блузка', 'фараон',
         'клапан', 'еж', 'вымя', 'турист', 'колготки', 'питание',
         'сверток', 'дочерь', 'шампунь', 'броня', 'зайчатина', 'гимназист',
         'стелька', 'подделка', 'виза', 'затычка', 'решение', 'алкоголь',
         'шуруп', 'воровка', 'колодец', 'кабан', 'команда', 'бордель',
         'ловушка', 'буква', 'опера', 'сектор', 'математика', 'пароварка',
         'невезение', 'глубина', 'штука', 'справочник', 'вождь', 'хобот',
         'ширинка', 'усталость', 'служитель', 'жар', 'спальная', 'видео',
         'рот', 'просьба', 'фишка', 'рукопись', 'ракетчик', 'каблук', 'шрифт',
         'палец', 'ножка', 'халва', 'черника', 'незнайка', 'компания',
         'работница', 'мышь', 'исследование', 'кружка', 'мороженое', 'сиденье',
         'пулемет', 'печь', 'солист', 'свекла', 'стая', 'зелье', 'дума',
         'посылка', 'коготь', 'семафор', 'брат', 'различие', 'плоскостопие',
         'двигатель', 'сфера', 'тюльпан', 'затвор', 'внедорожник', 'самурай',
         'стан', 'алгоритм', 'параграф', 'глаз', 'медалист', 'пульт',
         'поводок', 'подлежащее', 'ор', 'бунт', 'удочка', 'лес', 'диспетчер',
         'монитор', 'вдова', 'пиратство', 'астролог', 'сосед', 'изобретатель',
         'чума', 'танец', 'затишье', 'пластелин', 'йог', 'маска', 'блоха',
         'судьба', 'сияние', 'рукавица', 'филе', 'заплыв', 'семга',
         'гиппопотам', 'мастер', 'походка', 'ландыш', 'яблоня', 'кляча',
         'лиса', 'свертываемость', 'раствор', 'соты', 'солод', 'спорт',
         'шифер', 'прощение', 'стопка', 'побег', 'простота', 'запах', 'беседа',
         'варенье', 'пароль', 'актер', 'вырубка', 'гвоздь', 'шкаф',
         'скальпель', 'гонг', 'профессор', 'казан', 'скорбь', 'извоз',
         'добавка', 'тропа', 'шеф', 'космонавт', 'грифель', 'лауреат', 'ромб',
         'борец', 'звон', 'канистра', 'олимпиада', 'оплата', 'спирт', 'баян',
         'перекресток', 'влажность', 'лотерея', 'насморк', 'оправдание',
         'мушкетер', 'мороз', 'утюг', 'санитария', 'опрятность']


def one_game(words_list):
    word = words_list[randint(0, len(words_list))]
    hidden_word = '*' * len(word)
    hidden_list = list(hidden_word)
    word_list = list(word)
    used_letters = []
    tries = len(word) * 2
    text_about_tries = '\nу вас есть ' + str(tries) + ' попыток'
    print(hidden_word + text_about_tries)
    count_help = 0

    for i in range(tries):
        print('введите одну русскую букву или все слово сразу' + (
            ' или напишите "подсказка"' if count_help < 1 else ''))
        if i > 0 and len(used_letters) > 0:
            print('вы уже вводили эти буквы: ' + ' '.join(used_letters))
        if i > 0:
            print('у вас осталось ' + str(tries - i) + ' попыток')

        letter = input().lower()
        if letter == 'подсказка' and count_help < 1:
            count_help += 1
            print('какую букву вы хотите открыть?')
            ind = int(input())
            if 0 < ind < len(hidden_word):
                let = word_list[ind - 1]
                count = 0
                for j in range(len(word)):
                    if word_list[j] == let:
                        hidden_list[j] = let
                        count += 1
                hidden_word = ''.join(hidden_list)
                print('вы открыли ' + str(count) + ' ' + ('букву' if count == 1 else 'буквы'))
                hidden_list[ind - 1] = let
                used_letters.append(let)
                print('вам больше нельзя использовать подсказки')
            else:
                print('зачем ломать игру? в слове нет буквы с таким номером')
        else:
            if letter == 'подсказка' and count_help == 1:
                print('вы уже использовали подсказку, введите что-нибудь другое')
                letter = input().lower()
            if len(letter) == len(word):
                if letter == word:
                    print('ура, вы угадали слово!')
                    hidden_word = letter
                    print(hidden_word)
                    break
                else:
                    print('неправильное слово или неверный ввод')
            else:
                while not (len(letter) == 1 and ord(letter) >= (ord('а')) and ord(
                        letter) <= (ord('я'))):
                    print('неверный ввод, попробуйте еще раз')
                    letter = input().lower()
                while letter in used_letters:
                    print('эта буква уже была введена, введите другую букву')
                    letter = input()
                used_letters.append(letter)

                if letter not in word_list:
                    print('такой буквы в слове нет')
                else:
                    count = 0
                    for j in range(len(word)):
                        if word_list[j] == letter:
                            hidden_list[j] = letter
                            count += 1

                    hidden_word = ''.join(hidden_list)
                    print('вы угадали ' + str(count) + ' ' + ('букву' if count == 1 else 'буквы'))

        if '*' not in hidden_word:
            print('поздравляю, вы угадали слово!')
            print(hidden_word)
            break

        print(hidden_word)
        print()

    if '*' in hidden_word:
        print('к сожалению, вы проиграли')
        print('это было слово ' + word)


if __name__ == '__main__':
    rule = 'Игра "Поле Чудес". Вам загадано слово. \n' \
           'Вы можете ввести латинскую букву или все слово сразу. е = ё. ' \
           'Также за всю игру вы можете получить 1 подсказку. Удачи!'
    print(rule)

    while True:
        one_game(words)
        print('если желаете продолжить, напишите "да", иначе "нет"')
        ans = input()
        if ans != 'да':
            break