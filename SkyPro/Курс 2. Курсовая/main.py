"""
https://skyengpublic.notion.site/2-3849668e2da3404ab2fb5976ab0d7338

url: https://jsonkeeper.com/b/RI5V
test_ValueError_url = "https://jsonkeeper.com/b/6JQ9"
"""
import utils

if __name__ == '__main__':
    url = "https://jsonkeeper.com/b/RI5V"
    word = utils.load_random_word(url)

    user_name = input("Введите имя игрока: ")
    player = utils.generate_player(user_name)

    print(f"\nПривет, {player.name}!")
    print(f"Составьте {len(word)} слов из слова {word.word.upper()}")
    print("Слова должны быть не короче 3 букв")
    print("Поехали, ваше первое слово?")

    while len(word) != len(player):
        user_input = input("\nВаше слово: ").lower()

        if user_input in utils.FINISH_GAME:
            break

        if word.is_subword_valid(user_input):
            if not player.is_subword_used(user_input):
                print("Верно")
                player.add(user_input)
            else:
                print("Вы уже использовали это слово")
        else:
            print("Неверно")

    if user_input in utils.FINISH_GAME:
        print("\nИгра завершена!")
    else:
        print("\nСлова закончились, игра завершена!")
    print(f"Вы угадали слов: {len(player)}")
