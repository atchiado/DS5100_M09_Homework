import unittest
from m09_homework.booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        mybooklover = BookLover(name = 'Cilian Murphy', email = 'cmurphy@gmail.org', fav_genre = 'Romance')
        mybooklover.add_book('East of Eden', 4)
        self.assertIn('East of Eden', mybooklover.book_list['book_name'].values)

    def test_2_add_book(self):
        mybooklover = BookLover(name = 'Cilian Murphy', email = 'cmurphy@gmail.org', fav_genre = 'Romance')
        mybooklover.add_book('East of Eden', 4)
        mybooklover.add_book('East of Eden', 4)
        expected = 1
        self.assertEqual(len(mybooklover.book_list), expected)
    
    def test_3_has_read(self):
        mybooklover = BookLover(name = 'Cilian Murphy', email = 'cmurphy@gmail.org', fav_genre = 'Romance')
        mybooklover.add_book('American Prometheus', 2)
        result = mybooklover.has_read('American Prometheus')
        expected = True
        self.assertEqual(result, expected)

    def test_4_has_read(self):
        mybooklover = BookLover(name = 'Cilian Murphy', email = 'cmurphy@gmail.org', fav_genre = 'Romance')
        mybooklover.add_book('American Prometheus', 2)
        result = mybooklover.has_read('The Corrections')
        expected = False
        self.assertEqual(result, expected)

    def test_5_num_books_read(self):
        mybooklover = BookLover(name = 'Cilian Murphy', email = 'cmurphy@gmail.org', fav_genre = 'Romance')
        mybooklover.add_book('American Prometheus', 2)
        mybooklover.add_book('The Corrections', 5)
        mybooklover.add_book('East of Eden', 3)
        expected = 3
        self.assertEqual(mybooklover.num_books_read(), expected)
    
    def test_6_fav_books(self):
        mybooklover = BookLover(name = 'Cilian Murphy', email = 'cmurphy@gmail.org', fav_genre = 'Romance')
        mybooklover.add_book('American Prometheus', 2)
        mybooklover.add_book('The Corrections', 5)
        mybooklover.add_book('East of Eden', 3)
        mybooklover.add_book('Les Miserables', 4)
        myfavbooks = mybooklover.fav_books()
        expected = 3
        self.assertGreater(myfavbooks['book_rating'].min(), expected)

if __name__ == '__main__':
    unittest.main(verbosity=3)