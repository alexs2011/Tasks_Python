from classes.c_utils.downloader import Downloader


class Page:
    def __init__(self, page_url: str, n_page: str) -> None:
        """
        Класс, хранящий url-адрес страницы и её номер в главе.
        """
        self.number = n_page
        self.url = page_url

    def __repr__(self):
        """
        Строковое представление класса в формате JSON.
        """
        return f'' \
               f'\n\t\t\t{{\n"url": "{self.url}",\n' \
               f'\t\t\t"number": "{self.number}"\n}}'

    def download(self, path: str, page_number: str) -> None:
        """
        Загружает страницу манги и сохраняет её с необходимым расширением.
        """
        # Определяем расширение файла.
        extension = self.url.split(".")[-1]
        path = f"{path}{page_number}.{extension}"
        downloader = Downloader(self.url)
        downloader.download_img(path)
