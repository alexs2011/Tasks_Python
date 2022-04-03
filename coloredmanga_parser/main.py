from utility import utils


def main():
    # файл со структурой манги, куда будет произведено сохранение структуры, и впоследствии из которого может быть
    # осуществлена её загрузка.
    file_contents = "data/contents_full.json"
    # Корневая директория, в которой будет создана папка с названием манги и загружены её тома, главы и страницы.
    dir_root = "D:\\"

    # Ссылка на главную страницу манги.
    url = "https://coloredmanga.com/manga/one-piece/"

    # Загрузка структуры манги с сайта.
    # manga_contents = utils.build_contents(url)

    # Сохранение загруженной структуры в файле формата JSON.
    # utils.save_contents(manga_contents, filename=file_contents)

    # Загрузка структуры манги из файла.
    manga_contents = utils.build_contents(file_contents, from_file=True)

    # Проверочное сохранение в этот же файл.
    # utils.save_contents(manga_contents, filename=file_contents)

    # Скачивание манги.
    utils.download_manga(manga_contents, dir_root, start_vol=78, end_vol=79, is_flatten=True)


if __name__ == '__main__':
    main()
