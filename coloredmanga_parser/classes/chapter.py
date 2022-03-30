from classes.downloader import Downloader
from classes.parser import Parser
from classes.page import Page


class Chapter:
    def __init__(self, name: str, chapter_url: str, raw_pages: list[dict] = None, from_file: bool = False) -> None:
        """
        Класс, хранящий название главы и список url-адресов её страниц.
        """
        self.name = name
        self.url = chapter_url
        self.pages = []
        self.raw_pages = raw_pages
        self.from_file = from_file

        self.__build_pages()

    def __repr__(self):
        """
        Строковое представление класса в формате JSON.
        """
        return '' \
               f'\n\t\t{{\n"name": "{self.name}",\n' \
               f'\t\t"url": "{self.url}",\n' \
               f'\t\t"pages": {self.pages}\n}}'

    def __len__(self) -> int:
        """
        Возвращает количество страниц в главе.
        """
        return len(self.pages)

    def __get_pages_from_url(self) -> list[str]:
        """
        На основе url-адреса скачивает html-страницу главы и при помощи Parser определяет url-адреса страниц,
        т.е. изображений, в главе.
        """
        downloader = Downloader(self.url)
        downloader.download_html()
        chapter_html = downloader.data

        parser = Parser(chapter_html)
        return parser.parse_chapter_page()

    def __build_pages_from_url(self, chapter_pages: list[str]) -> None:
        """`
        Формирует список страниц для данных, полученных из удалённого источника.
        """
        for i, page in enumerate(chapter_pages, 1):
            self.pages.append(Page(page, i))

    def __build_pages_from_file(self) -> None:
        """`
        Формирует список страниц для данных, полученных из файла.
        """
        for page in self.raw_pages:
            self.pages.append(Page(page['url'], page['number']))

    def __build_pages(self) -> None:
        """
        Формирует список страниц данной главы с учётом того, откуда поступают данные.
        """
        if self.from_file:
            self.__build_pages_from_file()
        else:
            chapter_pages = self.__get_pages_from_url()
            self.__build_pages_from_url(chapter_pages)

        print(f"\t\tОбработана глава: {self.name}")
