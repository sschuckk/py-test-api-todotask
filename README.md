<!-- Template idea get from: https://github.com/othneildrew/Best-README-Template -->

<!-- PROJECT LOGO -->
<div align="center">
  <h3 align="center">Py-Test REST API - Tasks</h3>
  <img src="images/REST-API.avif">
  <a href="https://github.com/sschuckk/py-test-api-todotask/issues">Report Bug</a>
  ·
  <a href="https://github.com/sschuckk/py-test-api-todotask/issues">Request Feature</a>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#test-plan">Test Plan</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#reports">Reports</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

The objective of this project is to develop an Integration Test suite for a REST API using Pytest 
and Requests libraries, with the goal of establishing a simple testing framework.

But why doing this with python? 
* Rich functionality
* Clear documentation
* It's FREE!
    * Rich functionality
    * Clear documentation
    * It's FREE



### Test Plan
```
1. Create a todo task: 
   - Create, read, verify
2. Update a todo task:
   - Create, update, read, verify
3. List created tasks:
   - Create, list, verify
4. Delete a specific task:
   - Create, delete, read, verify
```
Each test case is executed independently.

API Endpoint: https://todo.pixegami.io \
Documentation: https://todo.pixegami.io/docs

### Built With

[![Python][Python.com]][Python-url]
[![Python][Pytest.com]][Python-url]



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
To use the Script:
* Python: https://www.python.org/downloads/
* Pip: https://pip.pypa.io/en/stable/installation/
* Git: https://git-scm.com/downloads


### Installation

1. Clone the repo.
   ```sh
   git clone https://github.com/sschuckk/py-test-api-todotask
   ```
2. Install the packages according to the configuration file requirements.txt.
   ```sh
   pip install -r requirements.txt
   ```


<!-- USAGE EXAMPLES -->
## Usage

The project can be run by a terminal or directly in your IDE.

In your terminal go to the project folder and run:
1. For a simples execution:
   ```sh
   pytest -v
   ```
   [![Product presentation][product-exec1]]()

2. To show the logs on terminal:
   ```sh
   pytest -v --log-cli-level=INFO
   ```
   [![Product presentation][product-exec2]]()
   >_Logs options: DEBUG, INFO, WARN, ERROR, and Critical._

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LOGS AND REPORTS -->
## Reports (TODO):
You can find the execution logs inside the folder "py_test_api/logs." 
They are incremental and will be stored day by day.

[![Product presentation][product-exec3]]()


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project (`https://github.com/sschuckk/py-test-api-todotask/fork`)
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some new feature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the [MIT](https://opensource.org/license/mit/) License. It’s free, no legal restrictions, why not try it out?

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT 
## Contact

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-banner]: images/REST-API.avif
[product-exec1]: images/pytest_output_1.png
[product-exec2]: images/pytest_output_2.png
[product-exec3]: images/pytest_output_3.png
[Python.com]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/ 
[Pytest.com]: https://img.shields.io/badge/PYTEST-007ACC?style=for-the-badge&logo=pytest&logoColor=orange
[Pytest-url]: https://docs.pytest.org/