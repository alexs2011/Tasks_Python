from classes.c_utils.downloader import Downloader


class Page:
    def __init__(self, page_url: str) -> None:
        """
        Класс, хранящий url-адрес страницы.
        """
        self.url = page_url

    def __repr__(self):
        """
        Строковое представление класса в формате JSON.
        """
        return f'' \
               f'\n\t\t\t\n"{self.url}"\n'

    def download(self, path: str, page_number: str) -> None:
        """
        Загружает страницу манги и сохраняет её с необходимым расширением.
        """
        # Определяем расширение файла.
        extension = self.url.split(".")[-1]
        path = f"{path}{page_number}.{extension}"
        downloader = Downloader(self.url)
        # downloader.download_img(path)
        print(path)
