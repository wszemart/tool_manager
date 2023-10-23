# Tool Manager

"Tool Manager" is an application designed to streamline the work of programmers and operators, as well as to facilitate efficient management of milling tools in the production process.
## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Functionality](#functionality)

## General Info
<details>
<summary>Click to expand</summary>

"Tool Manager" is a multifunctional project optimized for the work of programmers and operators. The main purpose of the application is to control, manage, and efficiently utilize tools in the production process.

The Tool Manager project is based on design patterns, which help maintain the application's health and facilitate the development of its functionalities. Application testing is carried out using the built-in Django module: TestCase. The use of the Factory Boy library ensures that test data is randomly generated, allowing a thorough check of the application's correctness. Code formatting rules are strictly adhered to with the help of the isort and PEP8 Black libraries.

The database is designed in PostgreSQL, which simplifies complex operations related to data processing and storage.

The user-friendly and intuitive Tool Manager user interface is created using the Bootstrap template. It enables convenient management of the machinery park, tool components (holders, tools), and the tools themselves.
</details>

## Technologies
<details>
<summary>Click to expand</summary>

The Tool Manager project is built with the following technologies:
- Python
- Django
- PostgreSQL
- Docker
- Docker-compose
- HTML
- CSS


</details>

## Setup
<details>
<summary>Click to expand</summary>

To run this application, follow these steps:

1.	Clone the repository:
    
git clone https://github.com/wszemart/tool_manager

2. Navigate to the repository directory:

cd tool_manager

3.	Install all the required dependencies listed in the requirements.txt file. You can do this using the pip tool:

pip install -r requirements.txt

4.	Run the application:

python manage.py runserver

After completing these steps, the application will be accessible at http://localhost:8000.

</details>

## Functionality
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

