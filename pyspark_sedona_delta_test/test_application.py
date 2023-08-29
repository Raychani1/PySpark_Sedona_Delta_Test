from pathlib import Path

import geopandas as gpd
from pyspark.sql import functions as F
from pyspark.sql.dataframe import DataFrame
from sedona.spark import SedonaContext


class TestApplication:

    """Represents the test application which showcases functionality of the
    Docker Environment.
    """

    def __init__(self, spark: SedonaContext) -> None:
        """Initializes the Test Application Class.

        Args:
            spark (SedonaContext): Spark Session.
        """
        self._spark = spark

    def __csv_to_spark(self, path: Path) -> DataFrame:
        """Loads CSV file to Spark DataFrame.

        This method tests the proper functionality of PySpark.

        Args:
            path (Path): Input CSV File path.

        Returns:
            DataFrame: Loaded DataFrame.
        """
        return (
            self._spark.read.format('csv')
            .option('delimiter', ';')
            .option('header', 'true')
            .option('encoding', 'ISO-8859-1')
            .load(path.as_posix())
        )

    def _load_geo_data_to_spark_df(self, path: Path) -> DataFrame:
        """Loads GeoJSON file to Spark DataFrame.

        This method tests the proper functionality of PySpark combined with
            Sedona.

        Args:
            path (Path): Input GeoJSON File path.

        Returns:
            DataFrame: Loaded DataFrame.
        """
        data = gpd.read_file(path.as_posix())
        data['geometry'] = data['geometry'].to_wkt()

        return self._spark.createDataFrame(data).withColumn(
            'geometry', F.expr('ST_GeomFromText(geometry)')
        )

    def big_data_to_delta(self, path: Path, delta_path: Path) -> None:
        """Loads data from CSV and saves to Delta Table.

        This method tests the proper functionality of PySpark combined with
            Delta Lake.

        Args:
            path (Path): Input CSV File path.
            delta_path (Path): Output Delta Table path.
        """
        # Load data to check PySpark functionality
        data_sdf = self.__csv_to_spark(path=path)

        # Select subset of columns so show() result is readable
        data_sdf.select(
            [
                'id',
                'data_inversa',
                'dia_semana',
                'horario',
                'uf',
                'br',
                'km',
                'municipio',
                'causa_acidente',
            ]
        ).show()

        # Write data to check Delta functionality
        data_sdf.write.format('delta').mode('overwrite').save(
            delta_path.as_posix()
        )

    def geo_data_to_delta(self, path: Path, delta_path: Path) -> None:
        """Loads data from GeoJSON and saves to Delta Table.

        This method tests the proper functionality of PySpark combined with
           Sedona and Delta Lake.

        Args:
            path (Path): Input GeoJSON File path.
            delta_path (Path): Output Delta Table path.
        """
        # Load data to check PySpark and Sedona functionality
        data_sdf = self._load_geo_data_to_spark_df(path=path)

        # Apply Sedona Function for testing purposes
        data_sdf.createOrReplaceTempView('data')
        data_sdf = self._spark.sql(
            'SELECT *, ST_AREA(data.geometry) AS area FROM data'
        )

        data_sdf.show()

        # Write data to check Delta functionality
        data_sdf.write.format('delta').mode('overwrite').save(
            delta_path.as_posix()
        )
