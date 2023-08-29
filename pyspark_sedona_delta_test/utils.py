from sedona.spark import SedonaContext


def create_spark_session() -> SedonaContext:
    """Creates PySpark Session.

    Returns:
        SparkSession: New PySpark Session.
    """
    spark = (
        SedonaContext.builder()
        .appName('PySpark_Sedona_Delta_Docker_App')
        .master('local')
        .config(
            'spark.sql.extensions', 'io.delta.sql.DeltaSparkSessionExtension'
        )
        .config(
            'spark.sql.catalog.spark_catalog',
            'org.apache.spark.sql.delta.catalog.DeltaCatalog',
        )
    ).getOrCreate()

    return SedonaContext.create(spark)
