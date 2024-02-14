<h3 align="center">
  REST API example application
</h3>

<p align="center">Create tags for application.</p>

<p align="center">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/matheralvs/nlw-expert-python?color=%237844e9">

  <a href="https://www.linkedin.com/in/matheralvs/" target="_blank" rel="noopener noreferrer">
    <img alt="Made by" src="https://img.shields.io/badge/made%20by-matheus-7844e9">
  </a>
  
  <a href="https://github.com/matheralvs/nlw-expert-python/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/matheralvs/nlw-expert-python?color=%237844e9">
  </a>

  <a href="https://github.com/matheralvs/nlw-expert-python/issues">
    <img alt="Repository issues" src="https://img.shields.io/github/issues/matheralvs/nlw-expert-python?color=%237844e9">
  </a>
</p>

<p align="center">
  <a href="#-about-the-project">About the project</a> •
  <a href="#-technologies">Technologies</a> •
  <a href="#-getting-started">Getting started</a> •
  <a href="#-how-to-contribute">How to contribute</a>
</p>

## ✅ About the project
This is an api designed in Python (using Flask) for creating tags. The api was built during NLW Expert, an event hosted by Rocketseat for those who want to learn new things and enter the technology market. In addition to building the API, architectural patterns, error handling, etc. were shown to make the application scalable and robust.

## 💻 Technologies
Technologies that I used to develop this api

- [Python](https://www.python.org/)
- [Venv](https://docs.python.org/pt-br/3/library/venv.html)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Python Barcode](https://python-barcode.readthedocs.io/en/stable/)

## 🚀 Getting started

**Clone the project and access the folder**

```bash
$ git clone https://github.com/matheralvs/nlw-expert-python.git && cd nlw-expert-python
```

**Follow the steps below**

```bash
# Enter the virtual environment (.env)
$ .venv/Scripts/activate 

# To finish, run
$ py run.py

# Well done, project is started!
```

## Create a Tag

### Request

`POST /create_tag/`

    curl -i -H 'Accept: application/json' -d 'product_code=123' http://localhost:3000/create_tag

### Response

    HTTP/1.1 201 Created
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Location: /create_tag
    Content-Length: 36

    {
      data: {
        "type": "Tag Image",
        "count": 1,
        "path": "{path from image}.png"
      }
    }
