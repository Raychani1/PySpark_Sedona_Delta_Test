# PySpark-Sedona-Delta Test Project

This little project was created to give an example use-case for the Docker Image created in this [Project](https://github.com/Raychani1/PySpark_Sedona_Delta_Docker).

### **Built With**
[![Python 3.10][Python]][Python-url]
[![Docker][Docker]][Docker-url]

## **Getting Started**

#### **Prerequisites**

* **Docker** - To use this environment an installed copy of Docker is required. For this purpose [**Docker**][Docker-url] or [**Docker Desktop**](https://www.docker.com/products/docker-desktop/) is recommended. The following product can be downloaded from their website or installed through a package manager.

### Docker Container
To get a Dockerized version of the app up and running follow these simple steps.

1. Clone the repo and navigate to the Project folder
   ```sh
   git clone https://github.com/Raychani1/PySpark_Sedona_Delta_Test
   ```

2. Build the Docker Image
   ```sh
   docker build -t pyspark_sedona_delta_test .
   ```

3. Create alternative way for more convenient execution

   On Linux:
   ```sh
   alias PySpark_Sedona_Delta_Test="docker run --rm -it -v $(pwd):/app pyspark_sedona_delta_test:latest"
   ```

   On Windows:

   Load the function from the PowerShell Script using the dot notation
      ```sh
      . .\pyspark_sedona_delta_test.ps1
      ```

6. Run your project through the environment
   ```sh
   PySpark_Sedona_Delta_Test python main.py
   ```
</br>

## **License**

Distributed under the **MIT License**. See [LICENSE](https://github.com/Raychani1/PySpark_Sedona_Delta_Test/blob/main/LICENSE) for more information.

<!-- Variables -->

[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/

[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
