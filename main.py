import habr
KEYWORDS = ['дизайн', 'фото', 'web', 'Python']


if __name__ == '__main__':
    item = habr.Habr()
    print('Поиск по всей доступной preview-информации:')

    item.preview_info(KEYWORDS)
    print('\n')
    print('Поиск целиком по всей статье:')

    item.article_text(KEYWORDS)





















# if __name__ == '__main__':
#     print()


