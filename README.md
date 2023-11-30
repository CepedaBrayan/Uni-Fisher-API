# UNI FISHER API

## Overview

Application to scrape university cut scores via API REST.

### Architecture

This project is developed using [FastAPI](https://fastapi.tiangolo.com/) and Docker by far.
The choice of tools and technologies for this project is driven by specific requirements. FastAPI is chosen for its efficiency in creating REST APIs quickly, its performance, and its ease of use. Docker is chosen for its ease of use and its ability to create a portable environment for the project.

## Getting Started

Follow these steps to set up and run the project:

1. Clone the repository.
2. Open Docker Desktop (compatible with macOS and Windows) or Docker Engine (compatible with Linux) and ensure that it is running.
3. Open a terminal into .docker folder and run the following commands:

```bash
docker-compose build
docker-compose up
```

4. Open a browser and navigate to http://localhost:8080/docs to access the API documentation and play with the API.


# Testing

Testing is done using [pytest](https://docs.pytest.org/en/stable/). The test files are located in the `test` folder.


## Running Tests

To run the tests, follow these steps:

1. Up the application:

    ```bash
    docker-compose up
    ```
1. Open a terminal into the .docker folder and create a bash session:

    ```bash
    docker-compose exec app bash
    ```

2. Run pytest:

    ```bash
    pytest
    ```

## Support

If you have any questions or issues, feel free to reach out to me via email at [riveracepedabrayan@gmail.com](mailto:riveracepedabrayan@gmail.com). If you'd like to contribute, please open a pull request. Any sponsorship is greatly appreciated.



