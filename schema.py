import typing
import strawberry


books_list = []
def get_books():
    return [i for i in books_list]


@strawberry.type
class Book:
    title: str
    author: str

@strawberry.type
class Query:
    books: typing.List[Book]


@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)



@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:
        print(f'Adding {title} by {author}')
        books_list.append(Book(title=title, author=author))
        return Book(title=title, author=author)