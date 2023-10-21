## To run the Bitly-URL-Shortener, you need to follow the following steps:

Make sure you have Python installed on your computer. If not, you can download and install Python from the official Python website (https://www.python.org).

Ensure you have pip (Python Package Installer) installed. Usually, pip comes installed with Python. You can check if pip is already installed by running the following command in the terminal or command prompt:

```pip --version```

Clone the Bitly-URL-Shortener repository to your computer by running the following command in the terminal or command prompt:

```git clone https://github.com/0x6281/Bitly-URL-Shortener.git```

Navigate to the newly created project directory:

```cd Bitly-URL-Shortener```

Install the required dependencies by running the following command:

```pip install -r requirements.txt```

Open the ```short.py``` file and find the section that says ```"YOUR_ACCESS_TOKEN"```. Replace ```"YOUR_ACCESS_TOKEN"``` with your Bitly access token. This token is required to access the Bitly API and shorten URLs.

After replacing the Bitly access token, you can run the short.py script by executing the following command:

```python short.py```

>Make sure you have followed all the above steps correctly and provided a valid Bitly access token to run the Bitly-URL-Shortener
