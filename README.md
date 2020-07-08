# web_application template

**Python template** for building a **Web Application**



## Modules

### FastAPI

Web framework for building APIs with Python 3.6+ based on standard Python type hints


* Version: 0.54.1
* Website: https://fastapi.tiangolo.com/
* Documentation: https://fastapi.tiangolo.com/tutorial/
* Module name: **fastapi**
* Requirements: **uvicorn**
* Installing: `pip install --upgrade --no-cache-dir fastapi; pip install --upgrade --no-cache-dir uvicorn`



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

To run the application, use: `uvicorn app:app --reload`


## Check the application

Your application run at http://localhost:8000/ and have two type of documentation:

* Interactive Docs: it is provided by [Swagger UI](https://github.com/swagger-api/swagger-ui) at http://localhost:8000/docs
* Alternative Docs: it is provided by [ReDoc](https://github.com/Rebilly/ReDoc) at http://localhost:8000/redoc
