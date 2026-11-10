"""Lists, dictionaries, a loop, and a returned value."""
def total_pages(books):
    pages = 0
    for book in books:
        pages += book["pages"]
    return pages

if __name__ == "__main__":
    books = [{"title": "A", "pages": 12}, {"title": "B", "pages": 8}]
    print(total_pages(books))
