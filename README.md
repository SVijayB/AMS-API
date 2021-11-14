# ams-api

<p align="center">
        <img src="https://i.pinimg.com/originals/72/10/78/721078d6b03e349cea9e59f24b42420c.png" width=500>
    <br>AMS - Assignment Management System
</p>

## API Endpoints

| ID  | Endpoint               | Example                                            | Details                                         |
| --- | ---------------------- | -------------------------------------------------- | ----------------------------------------------- |
| 1   | [/]                    | https://ams-api.herokuapp.com/                     | Index.                                          |
| 1   | [/api/]                | https://ams-api.herokuapp.com/api/                 | API Base endpoint with documentation.           |
| 3   | [api/auth/login]       | https://ams-api.herokuapp.com/api/auth/login       | POST login creds, Validates details.            |
| 4   | [api/auth/signup]      | https://ams-api.herokuapp.com/api/auth/signup      | POST details, Validates and updates DB.         |
| 5   | [api/auth/prof-signup] | https://ams-api.herokuapp.com/api/auth/prof-signup | POST request: Upload CSV File to add professors |

## Installation

To install and run the bot on your local system, follow below mentioned steps:

-   Do a `git clone https://github.com/ARUNBALACHOCKALINGAM/AMS.git`.
-   Once you have the source code downloaded, create a virtual environment to safely download and install dependencies. To do so, use `python3 -m venv venv`, then `source venv/bin/activate` to enter the virtual environment.
-   Once done, you can install dependencies by using `pip install -r requirements.txt`.
-   Now, rename `.env.example` file present in the root of the project to `.env` and add your variables.

Running `main.py` using `python3 main.py` will start the API. It is by default hosted at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

If you are facing any issues with installation, feel free to reach out to us via Email.
