# Simple Input - Output via Procedural Programming
# title = input('Title: ')
# author = input('Author: ')
# print(f'{title} by {author}')

# Step 2 - Moduralization
# def main():
#     title = get_book_title()
#     author = get_author_title()
#     print(f'{title} by {author}')

# def get_book_title():
#     title = input('Title: ')
#     return title
# def get_author_title():
#     author = input('Author: ')
#     return author

# if __name__ == '__main__':
#     main()

# Step 3.
# def main():
#     title, author = get_book_info()
#     print(f'{title} by {author}')

# def get_book_info():
#     title = input('Title: ')
#     author = input('Author: ')
#     return title, author # Toople

# if __name__ == '__main__':
#     main()

# Step 4.
# def main():
#     book = get_book_info()
#     print(f'{book[0]} by {book[1]}')

# def get_book_info():
#     title = input('Title: ')
#     author = input('Author: ')
#     return title, author

# if __name__ == '__main__':
#     main()

# Step 5 - Using List Mutability
# def main():
#     book = get_book_info()
#     book[0] = 'C'
#     print(f'{book[0]} by {book[1]}')

# def get_book_info():
#     title = input('Title: ')
#     author = input('Author: ')
#     return [title, author]

# if __name__ == '__main__':
#     main()

# Step 6 - Dictionaries
# def main():
#     book = get_book_info()
#     print(f'{book['title']}, {book['author']}')

# def get_book_info():
#     title = input('Title: ')
#     author = input('Author: ')
#     return {'title': title, "author" : author}

# if __name__ == '__main__':
#     main()

# 7 - Intro to OOP
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        