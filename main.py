from pathlib import Path

from pyspark_sedona_delta_test.test_application import TestApplication
from pyspark_sedona_delta_test.utils import create_spark_session

if __name__ == '__main__':
    spark = create_spark_session()

    test_application = TestApplication(spark=spark)

    test_application.big_data_to_delta(
        path=Path('/app/data/input/big_data.csv'),
        delta_path=Path('/app/data/output/big_data.delta'),
    )

    test_application.geo_data_to_delta(
        path=Path('/app/data/input/polygons.geojson'),
        delta_path=Path('/app/data/output/polygons.delta'),
    )
