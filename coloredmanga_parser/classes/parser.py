import lxml.html

from decorators import timer


class Parser:
    def __init__(self, data: str) -> None:
        """
        Класс, разбирающий данные формата html.
        """
        self.data = data

    @timer
    def parse_manga_page(self) -> tuple[str, dict[str:[dict[str:str]]]]:
        """
        Разбирает главную страницу манги и находит название манги, тома и главы для соответствующих томов.
        """
        parsed_data = {}

        tree = lxml.html.document_fromstring(self.data)

        title = tree.xpath("//head/title/text()")[0].split('|')[0].strip()

        for el in tree.xpath("//*[starts-with(@class, 'parent has-child')]"):
            vol_name = el.xpath(".//a/text()")[0].strip()
            chapters_names = el.xpath(".//*[@class='wp-manga-chapter  ']/a/text()")
            chapters_links = el.xpath(".//*[@class='wp-manga-chapter  ']/a//@href")

            parsed_data[vol_name] = parsed_data.setdefault(vol_name, {})

            for chapter_name, chapter_link in zip(chapters_names, chapters_links):
                d_chapter = {chapter_name.strip(): chapter_link}
                parsed_data[vol_name][chapter_name.strip()] = chapter_link

        return title, parsed_data

    @timer
    def parse_chapter_page(self) -> list[str]:
        """
        Разбирает html-страницу главы и находит ссылки на страницы манги (т.е. изображения).
        """
        parsed_data = []

        tree = lxml.html.document_fromstring(self.data)

        for el in tree.xpath("//*[@class='page-break ']"):
            parsed_data.append(el.xpath(".//img//@src")[0].strip())

        return parsed_data
