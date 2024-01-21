# Tool Manager

"Tool Manager" is an application designed to streamline the work of programmers and operators, as well as to facilitate efficient management of milling tools in the production process.
## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Local Machine Setup](#local-machine-setup)
* [Docker Setup](#docker-setup)
* [Functionalities](#functionalities)
* [Screens](#screens)

## General Info
<details>
<summary>Click to expand</summary>

"Tool Manager" is a multifunctional project optimized for the work of programmers and operators. The main purpose of the application is to control, manage, and efficiently utilize tools in the production process.

The Tool Manager project is based on design patterns, which help maintain the application's health and facilitate the development of its functionalities. Application testing is carried out using the built-in Django module: TestCase. The use of the Factory Boy library ensures that test data is randomly generated, allowing a thorough check of the application's correctness. Code formatting rules are strictly adhered to with the help of the isort, PEP8 Black and pre-commit libraries.

The database is designed in Postgres, which simplifies complex operations related to data processing and storage.

Poetry has been added to the project for integration, serving as a robust tool for managing dependencies and packaging in Python. With Poetry, you can effortlessly declare the libraries your project relies on, and it takes care of installing or updating them seamlessly.

The user-friendly and intuitive Tool Manager user interface is created using the Bootstrap template. It enables convenient management of the machinery park, tool components (holders, tools), and the tools themselves.
</details>

## Technologies & Tools
<details>
<summary>Click to expand</summary>

The Tool Manager project is built with the following technologies & tools:
- Python 3.11
- Django 4.23
- Poetry 1.7.1
- PostgreSQL 15
- Docker / Docker-Compose
- HTML/CSS/Bootstrap

</details>

## Local Machine Setup
<details>
<summary>Click to expand</summary>

To run this application, follow these steps:

1.	Clone the repository:

```git clone https://github.com/wszemart/tool_manager```

2. Create virtual environment

```python -m venv venv```


3. Navigate to the repository directory:

```cd tool_manager```

4. Install all the required dependencies listed in the requirements.txt file. You can do this using the pip tool:

```pip install -r requirements.txt```

5. Run the application:

```python manage.py runserver```

After completing these steps, the application will be accessible at http://localhost:8000.

</details>

## Docker Setup
<details>
<summary>Click to expand</summary>

1. Install Docker
2. Download the repository
3. Go to directory with Dockerfile and docker-compose.yaml files.
4. On the command line, within this directory, build the image and start the container:

```docker-compose build```

5. If that's successful you can then start it up by:

```docker-compose up```

6. Open http://0.0.0.0:8000 in your browser.


</details>

## Functionalities
<details>
<summary>Click here to see general information about <b>Functionality</b>!</summary>

#### 1. User Account and Permission Management:

<ul>
The application allows for effective user account management and the assignment and management of permissions.

The application enables administrators, users with appropriate permissions, and users themselves to create new user accounts. When creating a user account, permissions from the 'Operator' group are assigned to the user. These permissions grant access to specific functions and tasks in the application. User group and permission changes are made by administrators and users with the necessary permissions.
</ul>

#### 2. Tool Component Management: Holder and Tool

<ul>
Logged-in users with the necessary permissions (belonging to the 'Programmer' group) can add, edit, and delete holders and tools. Users in the 'Operator' group can only view the data.
</ul>

#### 3. Tool Management:

<ul>
Logged-in users in the 'Programmer' group can create tools from the holder and tool components, assign them to machines, edit, and delete them. Users in the 'Operator' group have the ability to view data and edit three selected fields. Users from both groups can add comments to individual tools. This facilitates and accelerates the exchange of information about a specific tool and creates a usage history. Notifications are sent to users after each comment is added, ensuring that no information escapes them.
 </ul>

#### 4. Machine Park Management:

<ul>
Logged-in users in the 'Programmer' group can add, edit, and delete machines from the machine park. Each machine has a 'Description' field where users can include additional information. The page containing the details of a specific machine displays a table containing all tools assigned to it. The table allows data to be sorted by each column and data to be searched within the table. Data from the table can be printed to a PDF file or saved in CSV format.
</ul>

</details>

## Screens
<details>
<summary>Click to expand</summary>

![register](https://github.com/wszemart/tool_manager/assets/95930936/20927c3d-5798-4b2a-ace5-057ec7db2f2b)

![main](https://github.com/wszemart/tool_manager/assets/95930936/85318f5a-2228-4899-a9c9-d2119904c05c)

![machine_view](https://github.com/wszemart/tool_manager/assets/95930936/ebeb627e-2ae2-4cae-85d7-9ea1af75ddbd)

![tool_assembly view](https://github.com/wszemart/tool_manager/assets/95930936/f8c37564-9c1a-43a8-8c73-50b3b23266da)

![comment](https://github.com/wszemart/tool_manager/assets/95930936/ebdcf05b-b30d-487b-b95b-6f5cf53aec87)
</details>
