function PySpark_Sedona_Delta_Test {
    docker run --rm -it -v ${pwd}:/app test:latest $args
}
