class Page:
    def __init__(self, page_url: str, n_page: int) -> None:
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
