import utils


def main():
    filename = "..\\coloredmanga_parser\\data\\contents.json"

    # загрузка структуры манги с сайта и её сохранение в файле формата JSON.
    # url = "https://coloredmanga.com/manga/one-piece/"
    # manga_contents = utils.build_contents(url)
    # utils.save_contents(manga_contents, filename=filename)

    # загрузка структуры манги из файла.
    manga_contents = utils.build_contents(filename, from_file=True)
    # проверочное сохранение в этот же файл.
    # utils.save_contents(manga_contents, filename=filename)


if __name__ == '__main__':
    main()
