import unittest
from Testing_functions.module_for_ya.class_YaUpLoader import YaUploader
import os
from dotenv import load_dotenv, find_dotenv
from parameterized import parameterized

class TestRequest(unittest.TestCase):
    @parameterized.expand(
        [
            (201, 201),
            (404, 404),
            (401, 401),
            (409, 409)
        ]
    )

    def test_creating_a_folder(self, error_code, result):
        load_dotenv(find_dotenv())
        NEW_PATH = 'new_folder'
        new_folder = YaUploader(os.getenv('YA_TOKEN'))
        result_fun = new_folder.creating_a_folder(NEW_PATH)

        self.assertEqual(result_fun, result)

if __name__ == '__main__':
    unittest.main()
