import pytest
from main import BooksCollector

class TestBooksCollector:
    
    # 1)Негативная проверка на метод add_new_book

    def test_add_new_book_same_book_not_added_twice(self, collection):
        
        collection.add_new_book('Гордость и предубеждение и зомби')
        collection.add_new_book('Гордость и предубеждение и зомби')

        # проверяем, что у нас осталась только одна книга
        assert len(collection.get_books_genre()) == 1
        assert 'Гордость и предубеждение и зомби' in collection.get_books_genre()

    # 2) Позитивная проверка на метод add_new_book
    @pytest.mark.parametrize('valid_len_book',  
        ['A' * 2,
         'A' * 40,
        'A' * 20])
    
    def test_add_new_book_add_book_with_valid_len(self, collection, valid_len_book):
        collection.add_new_book(valid_len_book)    
        assert valid_len_book in collection.get_books_genre() 
        
    # 3) Негативная проверка на метод add_new_book
    @pytest.mark.parametrize('invalid_len_book', ['', 'A' * 41, 'A' * 90])
    
    def test_add_new_book_with_invalid_len(self, collection, invalid_len_book):
        collection.add_new_book(invalid_len_book)
        assert invalid_len_book not in collection.get_books_genre()
         
    # 4) Позитивная проверка на метод set_book_genre
          
    def test_set_book_genre_correct_genre_successful(self, collection):
        collection.add_new_book('Пуаро')
        collection.set_book_genre('Пуаро', 'Детективы')
        assert collection.get_book_genre('Пуаро') == 'Детективы'
        
    # 5) Позитивная проверка на метод get_book_genre
    
    def test_get_book_genre_correct_genre_by_book_title(self, collection):
        collection.books_genre = {'Недоросль': 'Комедии'} 
        assert collection.get_book_genre('Недоросль') == 'Комедии'
        
    # 6) Позитивная проверка на метод get_books_with_correct_genre
    
    def test_get_books_with_specific_genre_get_book_with_correct_genre(self, collection):
        collection.books_genre = {
            'Гарри Поттер': 'Фантастика',
            'Властелин колец': 'Фантастика',
            'Недоросль': 'Комедии',
            'Горе от ума':'Комедии'
        }
        assert collection.get_books_with_specific_genre('Комедии') == ['Недоросль', 'Горе от ума']
        
    # 7) Позитивная проверка на метод get_books_for_chilren
    
    def test_get_books_for_children_successful(self, collection):
        collection.books_genre = {
            'Джуманджи': 'Фантастика',
            'Ну, погоди': 'Мультфильмы',
            'Война миров': 'Ужасы'
        }                            
        assert collection.get_books_for_children() == ['Джуманджи', 'Ну, погоди']
        
    # 8) Негативная проверка на метод get_books_for_children
    
    def test_get_books_for_children_when_book_has_no_genre(self, collection):
        collection.add_new_book('Звездные войны')
        assert collection.get_books_for_children() == []
    
    # 9) Позитивная проверка на метод add_book_in_favorites
    
    def test_add_book_in_favorites_added_successful(self, collection):
        collection.add_new_book('Властелин колец')
        collection.add_book_in_favorites('Властелин колец')
        assert collection.get_list_of_favorites_books() == ['Властелин колец']
        
    # 10) Негативная проверка на метод add_book_in_favorites
    
    def test_add_book_in_favorites_not_in_library(self, collection):
        collection.add_book_in_favorites('Несуществующая книга')
        assert collection.get_list_of_favorites_books() == []

    # 11) Негативная проверка на метод add_book_in_favorites
    
    def test_add_book_in_favorites_not_added_twice(self, collection):
        collection.add_new_book('Властелин колец')
        collection.add_book_in_favorites('Властелин колец')
        collection.add_book_in_favorites('Властелин колец')
        assert collection.get_list_of_favorites_books() == ['Властелин колец']

    # 12) Позитивная проверка на метод delete_book_from_favorites
    
    def test_delete_book_from_favorites_successful_deleted(self, collection):
        collection.add_new_book('Буратино')
        collection.add_book_in_favorites('Буратино')
        collection.delete_book_from_favorites('Буратино')
        assert collection.get_list_of_favorites_books() == []
        
    # 13) Позитивная проверка на метод get_list_of_favorites_books
    
    def test_get_list_of_favorites_books_successful(self, collection):
        collection.favorites = ['Гарри Поттер', 'Властелин колец', 'Буратино']
        assert collection.get_list_of_favorites_books() == ['Гарри Поттер', 'Властелин колец', 'Буратино']