from pyspark.sql import Row

from .utils import ReusedSQLTestCase


class DataFrameTests(ReusedSQLTestCase):
    def test_simple_join(self):
        df1 = self.spark.createDataFrame([("a", "b")], ["a", "b"])
        df2 = self.spark.createDataFrame([("b", "c")], ["b", "c"])

        df = df1.join(df2, "b").collect()
        expected = [Row(b="b", a="a", c="c")]
        self.assertEqual(df, expected)

    def test_namedtuple_to_dataframe(self):
        """
        TODO: create a pattern of converting named tuple to dataframe
        """
        pass
