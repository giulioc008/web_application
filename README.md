# web_application template

**Python template** for building a **Web Application**



## Modules

### Coverage

Tool for measuring code coverage of Python programs

* Version: 5.2
* Website: https://coverage.readthedocs.io/en/coverage-5.2/#
* Documentation: https://coverage.readthedocs.io/en/coverage-5.2/config.html
* Installing: `pip install --upgrade --no-cache-dir coverage`



### Flask

Lightweight WSGI web application framework

* Version: 1.1.2
* Website: https://flask.palletsprojects.com
* Documentation: https://flask.palletsprojects.com/en/1.1.x/api/
* Module name: **flask**
* Installing: `pip install --upgrade --no-cache-dir Flask`



### PyMySQL

Module used to connect to a MySQL Server

* Version: 0.9.3
* Website: https://pymysql.readthedocs.io/en/latest/
* Documentation: https://pymysql.readthedocs.io/en/latest/modules/index.html
* Module name: **pymysql**
* Requirements:
	- Python -- one of the following:
		+ [CPython](http://www.python.org/) : 2.7 and >= 3.5
		+ [PyPy](http://pypy.org/) : Latest version
	- MySQL Server -- one of the following:
		+ [MySQL](http://www.mysql.com/) >= 5.5
		+ [MariaDB](https://mariadb.org/) >= 5.5
* Installing: `pip install --upgrade --no-cache-dir PyMySQL`



### pytest

Framework that makes building simple and scalable tests easy

* Version: 5.4.3
* Website: https://docs.pytest.org/en/stable/contents.html
* Documentation:
	- https://docs.pytest.org/en/stable/getting-started.html#create-your-first-test
	- https://docs.pytest.org/en/stable/reference.html
* Module name: **pytest**
* Installing: `pip install --upgrade --no-cache-dir pytest`



### Requests

HTTP library for Python, built for human beings

* Version: 2.23.0
* Website: https://requests.readthedocs.io/en/master/
* Documentation: https://requests.readthedocs.io/en/master/user/advanced/
* Module name: **requests**
* Installing: `pip install --upgrade --no-cache-dir requests`



## How to install the dependencies

To install the dependencies, create a [Virtual Enviroment](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments) and use: `pip install -r requirements.txt`



## How to run the application

To run the application, use: `flask run --host=0.0.0.0`



## How to test the application

To test the application, use: `pytest; coverage run -m pytest`
