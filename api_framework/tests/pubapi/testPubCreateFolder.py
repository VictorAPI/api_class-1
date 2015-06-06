from pubapiutils import Calls
from pubapiutils import Config
from pubapiutils import Utils
import httplib


class TestClass:
    def __init__(self):
        self.no_json = 'NoJSON'
        self.calls = Calls()
        self.config = Config()
        self.utils = Utils()

    def test_create_5_folders_positive(self):
        l = []
        for i in range(5):
            folder_name = self.utils.random_name()
            resp = self.calls.create_folder(folder_name)
            assert resp.status_code == httplib.CREATED
            assert resp.json == self.no_json
            l.append(folder_name)
        for item in l:
            resp = self.calls.delete_folder(folder_path=self.config.testpath + item)
            assert resp.status_code == httplib.OK