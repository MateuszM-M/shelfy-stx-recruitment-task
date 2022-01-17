import requests

# from .forms import SearchApiForm


def search_api():
    queries = {'q': 'Hobbit',
               'title':'',
               'author':'',
               'isbn':''}
    url = 'https://www.googleapis.com/books/v1/volumes'
    get_books = requests.get(
        f"{url}?q={queries['q']}")
        # +intitle:{queries['title']}+inauthor:{queries['author']}+isbn:{queries['isbn']}"
        # )

    return get_books.json()

def def_value():
    return 'empty'


def render_to_table():
    books = search_api()
    books = books['items']
    import_books = []
    if books:
        for book in books:
            volume = book['volumeInfo']
            try:
                book_dict = {'title': volume['title'],
                              'authors': volume['authors'],
                              'published_date': volume['publishedDate'],
                              'page_count': volume['pageCount']}
                import_books.append(book_dict)
            except KeyError as e:
                print(e)
                continue
    
    breakpoint()
    print(import_books)
    
render_to_table()    
    