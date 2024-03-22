# This directory contains tasks thar aims at integrating web framework on the AirBnB Clone

## Resources:
- [A Minimal Application](https://flask.palletsprojects.com/en/2.3.x/quickstart/#url-building)
- [Template Designer Documentation](https://jinja.palletsprojects.com/en/2.9.x/templates/#synopsis)
- [What is Flask](https://palletsprojects.com/p/flask/)


## Learning objectiveS:
```
What is a Web Framework
How to build a web framework with Flask
How to define routes in Flask
What is a route
How to handle variables in a route
What is a template
How to create a HTML response in Flask by using a template
How to create a dynamic template (loops, conditions…)
How to display in HTML data from a MySQL database
```


```
 pip3 install Flask
```

0. Hello Flask!
Write a script that starts a Flask web application:

Your web application must be listening on ``0.0.0.0``, port ``5000``
- Routes:
-   ``/``: display “Hello HBNB!”
You must use the option ```strict_slashes=False``` in your route definition
```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```
guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$
```
