from utility import utils


def main():
    file_contents = "data/contents_shrink.json"
    dir_root = "D:\\"

    # загрузка структуры манги с сайта и её сохранение в файле формата JSON.
    # url = "https://coloredmanga.com/manga/one-piece/"
    # manga_contents = utils.build_contents(url)
    # utils.save_contents(manga_contents, filename=file_contents)

    # загрузка структуры манги из файла.
    manga_contents = utils.build_contents(file_contents, from_file=True)
    # проверочное сохранение в этот же файл.
    # utils.save_contents(manga_contents, filename=file_contents)
    # скачивание манги
    utils.download_manga(manga_contents, dir_root, is_flatten=False)


if __name__ == '__main__':
    main()
