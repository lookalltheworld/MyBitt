import unittest,HTMLReport
from test_case import create_wallet
from test_case import import_wallet
from test_case import send_money
from test_case import traction_money
suite=unittest.TestSuite()

#suite.addTest(unittest.TestLoader().loadTestsFromTestCase(create_wallet.creatWallet_class))
#suite.addTest(unittest.TestLoader().loadTestsFromTestCase(import_wallet.importWallet_class))
#suite.addTest(unittest.TestLoader().loadTestsFromTestCase(send_money.sendMoney_class))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(traction_money.tractionMoney_class))

HTMLReport.TestRunner(
    title='MyBitt项目自动化测试报告',
    description='MyBitt项目测试报告，本次测试覆盖主要流程'
).run(suite)
