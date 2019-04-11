import sys
import unittest
import TC_AppointmentViewerScroll, TC_PasswordForget


class Test_Suite(unittest.TestCase):

    def test_main(self):
        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TC_PasswordForget.ESU_ATS),
            unittest.defaultTestLoader.loadTestsFromTestCase(TC_AppointmentViewerScroll.ESU_ATS),

        ])
        runner = unittest.TextTestRunner()
        runner.run(self.suite)

import unittest
if __name__ == "__main__":
    unittest.main()