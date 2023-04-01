# StestaApi
<p align="center">
  <img src="https://cdn.discordapp.com/attachments/714130033957929012/734709351574667294/Untitled-2.png">
</p>


This project is an API implementation of [Stesta](https://github.com/Elathius/stesta), a free, opensource task management and progress tracking app built on django. It provides a RESTful interface for accessing and manipulating the data stored in the original project.

#
## Setup

To set up the project, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Adiziel/StestaApi.git
   ```

2. Navigate to the project directory:

   ```bash
   cd StestaApi
   ```

3. Create a virtual environment::

   ```bash
   python -m venv .venv
   ```

4. Activate virtual environment:

   ```bash
   source .venv/bin/activate
   ```

5. Install project dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

6. Setup .env file in root directory of project:

   ```bash
   touch .env
   ```
7. Paste this with values replacing placeholders (Create Postgres Database before this):

    ```bash
    SECRET_KEY=django-insecure-r4h_c=%57(w)u@)2v495ot4a0aen+%%f^5^op$+rj-y5#n0u-u
    DATABASE_USER=YOUR_DATABASE_USER
    DATABASE_NAME=YOUR_DATABASE_NAME
    DATABASE_PASSWORD=YOUR_DATABASE_PASSWORD
    DATABASE_HOST=127.0.0.1
    ```

8. Make migrations and migrate 

    ```bash
      python3 manage.py makemigrations
      python3 manage.py migrate
    ```

9. Fire up!

    ```bash
      python3 manage.py runserver
    ```

#
## Usage
For detailed documentation lookup this file -> [Usage.md][def]

[def]: ./USAGE.md

#