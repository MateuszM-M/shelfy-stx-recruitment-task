import requests


def search_api(queries):
    clean_queries = {}
    for k, v in queries.items():           
        if v != '':
            clean_queries[k] = v
    queries = clean_queries
    url = 'https://www.googleapis.com/books/v1/volumes?'
    
    if 'q' in queries:
        url += f"q={queries['q']}"
    if 'title' in queries:
        url += f"+intitle:{queries['title']}"
    if 'author' in queries:
        url += f"+inauthor:{queries['author']}"
    if 'isbn' in queries:
        url += f"+isbn:{queries['isbn']}"
    
    
    get_books = requests.get(url)
    
    return get_books.json()


def render_to_table(books):

    books = books['items']
    import_books = []
    
    
    if books:
        for book in books:
            volume = book['volumeInfo']
            if 'title' in volume:
                title = {'title': volume['title']}
            else:
                title = {'title': None}    
                
            if 'authors' in volume:
                authors = {'authors': (', ').join(volume['authors'])}
            else:
                authors = {'authors': None}    
                
            if 'publishedDate' in volume:
                published_date = {'published_date': volume['publishedDate']}
            else:
                published_date = {'published_date': None}
                
            if volume['industryIdentifiers']:
                isbn = {'isbn': volume['industryIdentifiers'][0]['identifier']}
            else:
                isbn = {'isbn': None}
                
            if 'pageCount' in volume:
                page_count = {'page_count': volume['pageCount']}
            else:
                page_count = {'page_count': None}
            
            if 'imageLinks' in volume:
                if 'thumbnail' in volume['imageLinks']:
                    image_link = {'image_link': volume['imageLinks']['thumbnail']}
                else:
                    image_link = {'image_link': None}
            else:
                image_link = {'image_link': None}
            
            if 'language' in volume:
                language = {'language': volume['language']}
            else:
                language = {'language': None}
            
                
                
            import_book = [title|authors|published_date|isbn|page_count|image_link|language]
            
            import_books.append(import_book)
    return import_books
    