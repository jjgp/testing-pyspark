from .utils import ReusedSQLTestCase

class DataFrameTests(ReusedSQLTestCase):

    def test_simple_join(self):
        self.assertEqual(self.spark.range(1, 1).count(), 0)
    
