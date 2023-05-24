# Lingua_Franca

A simple translator using :

![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white) 
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Google](https://img.shields.io/badge/google-4285F4?style=for-the-badge&logo=google&logoColor=white)

This project uses a simple Flask/Python script to get an item, send it to the Google Translate API in order to translate it, and get the translation back to display it for the user.

The translated word or phrase is shown on the HTML page, which uses simple JavaScript for the layout.

Translation is available in two modes: language to language or auto-detect to language. For the auto-detect part, we use the langdetect library.

# How it works:

We use an AJAX script that auto-refreshes the web page to get the translation, eliminating the need to refresh it manually. In the Python script, we use the GET/POST method with two distinct routes. The first route is used to connect to the web page, and the second (/translate) is used to retrieve the translation from the API and display it to the user.

The reason we've chosen Flask and Python for this project is primarily because Flask is a lightweight and small Python framework that works well for small projects like this one. Additionally, it allows us to build the app using only a single Python file.

The main challenge was the implementation of the API in order to obtain the translation. We encountered multiple errors when trying to connect to the API. Fortunately, these errors were resolved by changing the path of both the HTML and Python files.

# Installing and Running the Project:

To use and run this project, you simply need to download all the files from the repository. Once the download is complete, extract the files and follow these steps:

1. Install the required packages/libraries by running the following commands in your terminal:

Install the `requests` library:
   
      pip install requests

Install the langdetect library:

      pip install langdetect

Install the flask library:

      pip install flask

2. After installing the packages, run the Python file.

3. In the terminal, an IP address should appear. You can either click on it directly or copy/paste the IP address into a browser to access the online translator.

Once all the step above completed you can write and translate a word or sentance in the langages available to you. If you don't know the origin langage you can use the auto-detect function. 
