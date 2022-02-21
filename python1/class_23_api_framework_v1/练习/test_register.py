import json
import unittest

import ddt

from common.excel_handler import ExcelHandler
from common.logger_handler import logger
from config.setting import config
from common import yaml_handler
from common import request_handler
from common import db_handler


yaml_data = yaml_handler.yaml_read(config.yaml_config_path)


@ddt.ddt
class Test_Register(unittest.TestCase):
    excel = ExcelHandler(config.data_path)
    data = excel.read("register")

    def setUp(self) -> None:
        self.req  = request_handler.RequestHandler()
        self.db = db_handler.DBHandler(host=yaml_data["database"]["host"],port=yaml_data["database"]["port"],
                                       user=yaml_data["database"]["user"],password=yaml_data["database"]["password"],
                                       database=yaml_data["database"]["database"],
                                       charset="utf8")
    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()
    @ddt.data(*data)
    def test_register(self,testdata):
        res = self.req.visit(config.host+testdata["url"],
                             testdata["method"],
                             headers=json.loads(testdata["headers"]),
                             json=json.loads(testdata["json"]))

        try:
            self.assertEqual(res["status"],json.loads(testdata["excepted"])["code"])
            self.excel.write(config.data_path,
                             "register",
                             testdata['case_id'] + 1,
                             9,
                             '测试失败'
                             )
        except AssertionError as e:
            logger.error(f"断言失败:{e}")
            raise e