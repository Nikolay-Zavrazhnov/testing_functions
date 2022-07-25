
import unittest
from Testing_functions.task_1 import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, \
    remove_doc_from_shelf, add_new_shelf, append_doc_to_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf, \
    show_document_info
from unittest.mock import patch
from parameterized import parameterized

#ДЗ задача №1
class TestFunctions_1(unittest.TestCase):

    @parameterized.expand(
        [
            ({"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
             ("passport", "2207 876234", "Василий Гупкин")),
            ({"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
             ("invoice", "11-2", "Геннадий Покемонов")),
            ({"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
             ("insurance", "10006", "Аристарх Павлов"))
        ]
    )

    def test_show_document_info(self, document, result):
        """Метод тестирует функцию - show_document_info"""
        result_fun = show_document_info(document)
        self.assertEqual(result, result_fun)


    def test_check_document_existance_true(self):
        """Метод тестирует функцию - check_document_existance -True"""
        result = check_document_existance('11-2')
        etalon = True
        self.assertEqual(result, etalon)

    def test_check_document_existance_false(self):
        """Метод тестирует функцию - check_document_existance-False"""
        result = check_document_existance('11-22')
        etalon = False
        self.assertEqual(result, etalon)

    @patch('Testing_functions.main.input', return_value='10006')
    def test_get_doc_owner_name(self, input):
        '''Метод тестрирует функцию - get_doc_owner_name'''
        etalon = 'Аристарх Павлов'
        self.assertEqual(get_doc_owner_name(), etalon)

    def test_get_all_doc_owners_names(self):
        """Метод тестрирует функцию - get_all_doc_owners_names"""

        result = get_all_doc_owners_names()
        etalon = {'Василий Гупкин', 'Аристарх Павлов', 'Геннадий Покемонов'}
        self.assertEqual(result, etalon)

    def test_remove_doc_from_shelf(self, doc_number='11-2'):
        """метод тестирует функцию remove_doc_from_shelf(doc_number)"""

        result = remove_doc_from_shelf(doc_number)
        etalon = '11-2'
        self.assertEqual(result, etalon)

    @patch('Testing_functions.main.input', return_value='2')
    def test_add_new_shelf_false(self, return_value):
        """Метод тестирует функцию - check_document_existance"""

        etalon = '2', False
        result = add_new_shelf()
        self.assertEqual(result, etalon)

    @patch('Testing_functions.main.input', return_value='5')
    def test_add_new_shelf_true(self, return_value):
        """Метод тестирует функцию - add_new_shelf_true"""

        etalon = '5', True
        result = add_new_shelf()
        self.assertEqual(result, etalon)

    def test_append_doc_to_shelf(self, doc_number='11-3', shelf_number='2'):
        """Метод тестирует функцию - append_doc_to_shelf"""

        result = append_doc_to_shelf(doc_number, shelf_number)
        etalon = ['10006', '11-3']
        self.assertEqual(result, etalon)

    @patch('Testing_functions.main.input', return_value='11-2')
    def test_get_doc_shelf(self, user_doc_number):
        """Метод тестирует функцию - get_doc_shelf"""
        etalon = '1'
        result = get_doc_shelf()
        self.assertEqual(result, etalon)

    def test_move_doc_to_shelf(self, doc='11-2', shelf='3'):
        etalon = '11-2', '3'
        result = move_doc_to_shelf(doc, shelf)
        self.assertEqual(result, etalon)


# выделил в отдельный класс т.к. при запуске вызов функции delete_doc() удаляет элемент,
# по которому ведут проверки другие тесты

class TestFunctions_2(unittest.TestCase):
    @patch('Testing_functions.main.input', return_value='11-2')
    def test_delete_doc(self, return_value):
        """Метод тестирует функцию - delete_doc"""

        etalon = '11-2', True
        result = delete_doc()
        self.assertEqual(result, etalon)
if __name__ == '__main__':
    unittest.main()
