import math

import utility.utils as utils
from utility.decorators import console_log
from classes.volume import Volume
from classes.c_utils.downloader import Downloader
from classes.c_utils.parser import Parser


class Manga:
    def __init__(self, link: str, from_file: bool) -> None:
        """
        Класс, хранящий название манги и список томов, получаемые на основе ссылки.
        При вызове принимает ссылку (на главную страницу либо на файл JSON) и флаг того, считываются ли данные из файла.
        """
        self.link = link
        self.from_file = from_file

        self.name = None
        self.volumes: list[Volume] = []

        self.__build_volumes()

    def __repr__(self):
        """
        Строковое представление класса в формате JSON.
        """
        return '' \
               f'{{\n"url": "{self.link}",\n' \
               f'"name": "{self.name}",\n' \
               f'"volumes": {self.volumes}\n}}'

    def __len__(self) -> int:
        """
        Возвращает количество томов в манге.
        """
        return len(self.volumes)

    @console_log(info='обработана главная страница')
    def __get_vols_from_url(self) -> dict[str, dict[str, str]]:
        """
        На основе url-адреса скачивает главную страницу манги и при помощи Parser определяет название и
        тома, а так же url-адреса глав, соответствующих томам.
        """
        downloader = Downloader(self.link)
        manga_html = downloader.download_html()

        parser = Parser(manga_html)
        self.name, manga_vols = parser.parse_manga_page()

        return manga_vols

    # @console_log(info='обработана главная страница')
    def __get_vols_from_file(self) -> list[dict]:
        """
        На основе файла JSON заполняет поля класса Manga. Возвращает список томов для дальнейшей обработки.
        """
        downloader = Downloader(self.link)
        manga_json = downloader.download_local_file()

        self.link = manga_json['url']
        self.name = manga_json['name']

        return manga_json['volumes']

    def __build_vols_from_utl(self, manga_vols: dict[str, dict[str, str]]) -> None:
        """
        Заполняет список томов для данных, полученных из удалённого источника.
        """
        # обработка только 2-х томов в целях отладки.
        manga_vols = {k: manga_vols[k] for k in list(manga_vols)[:2]}

        for vol_name, chapters in manga_vols.items():
            # Главы в томах располагаются в обратном порядке, например,
            # от Chapter_8 к Chapter_1, поэтому переворачиваем.
            sorted_chapters = dict(sorted(chapters.items(), key=lambda x: int(x[0].split()[1])))
            self.volumes.append(Volume(vol_name, sorted_chapters))

    def __build_vols_from_file(self, manga_vols: list[dict]) -> None:
        """
        Заполняет список томов для данных, полученных из файла.
        """
        for vol in manga_vols:
            self.volumes.append(Volume(vol['vol_name'], vol['chapters'], from_file=True))

    def __build_volumes(self) -> None:
        """
        Формирует данные, учитывая, откуда они поступают: из файла или удалённого ресурса.
        """
        if self.from_file:
            manga_vols = self.__get_vols_from_file()
            self.__build_vols_from_file(manga_vols)
        else:
            manga_vols = self.__get_vols_from_url()
            self.__build_vols_from_utl(manga_vols)

    def __validate_downloading_params(self, start_vol: int, end_vol: int) -> None:
        """
        Проверяет правильность параметров ограничения начального и конечного томов для сохранения.
        """
        if start_vol != 0 or end_vol != 0:
            if len(self.volumes) == 1 and self.volumes[0].name == "No Volumes":
                raise ValueError(
                    "У данной манги нет томов, только список глав. Параметры start_vol и end_vol недоступны."
                )
        if start_vol < 0 or end_vol < 0:
            raise ValueError("Номер тома не может быть меньше 0.")
        if start_vol != 0 and end_vol != 0:
            if start_vol >= end_vol:
                raise ValueError("Номер начального тома больше или равен номеру конечного.")

    def download(self, dir_root: str, is_flatten: bool, start_vol: int, end_vol: int) -> None:
        """
        Загружает тома манги с учетом опциональных ограничений start_vol и end_vol, и сохраняет их.
        """
        self.__validate_downloading_params(start_vol, end_vol)

        path = f"{dir_root}{self.name}\\"
        permitted_path = utils.create_dir(path)

        if end_vol == 0:
            end_vol = math.inf

        for vol in self.volumes:
            # У некоторых манг на сайте нет томов, только главы. Обрабатываем такой случай.
            if not (len(self.volumes) == 1 and self.volumes[0].name == "No Volumes"):
                vol_num = int(vol.name.split()[1])
            else:
                vol_num = 1
            if start_vol <= vol_num < end_vol:
                vol.download(permitted_path, is_flatten)
