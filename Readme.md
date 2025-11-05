<h1>💻 Backend Repository Overview</h1>

<h2>🔹 Backend Repository (Current)</h2>
<p><strong>Description:</strong> This repository contains the Django REST API backend for the project. It manages Projects, Tasks, and Task Logs with full CRUD operations and role-based authentication using JWT.</p>

<h3>🧩 Main Features</h3>
<ul>
  <li>User authentication and registration (JWT-based)</li>

  <li>Full CRUD for Projects, Tasks.</li>
  <li>Task assignment and tracking</li>
  <li>Associate tasks to projects and logs to tasks</li>
  <li>API endpoints ready for integration with frontend SPA</li>
</ul>

<h2>⚙️ Installation / Setup</h2>
<ol>
<li>Enter the Right Folder: <code>cd Capstone-backend</code></li>
  <li>Clone the repository: <code>git clone<a> https://github.com/fatimahbali/Capstone-backend.git</a></code></li>
  <li>Create a virtual environment: <code>pipenv shell </code></li>
  <li>Activate the environment: <code>source venv/bin/activate</code> (Linux/macOS) or <code>venv\Scripts\activate</code> (Windows)</li>
  <li>Activate the environment: <code>source venv/bin/activate</code> (Linux/macOS) or <code>venv\Scripts\activate</code> (Windows)</li>
  <li>  Open the psql terminal by running : <code>psql</code></li>
  <li> Create Database : <code>CREATE DATABASE project_name;</code></li>
  <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
  <li>Run Migrations: 
  <code>python3 manage.py makemigrations</code>
  <code>python3 manage.py migrate</code></li>
  <li>Start server: <code>python3 manage.py runserver</code></li>
</ol>

<h2>🔹 Backend Setup</h2>

<h3>💡 Core Technologies</h3>
<ul>
  <li><b>Framework:</b> Django (Python)</li>
  <li><b>Language:</b> Python 3.10+</li>
  <li><b>Database:</b> PostgreSQL</li>
  <li><b>Scripting:</b> JavaScript (for utilities or frontend integration)</li>
</ul>

<h2>🔹 Tech Stack</h2>

<h3>💡 Core Technologies</h3>
<ul>
  <li><b>Framework:</b> Django</li>
  <li><b>Language:</b> Python 3.10+</li>
  <li><b>Database:</b> PostgreSQL</li>
  <li><b>Scripting:</b> JavaScript (for frontend or utility scripts)</li>
</ul>

<h3>🧑‍💻 Development Tools</h3>
<ul>
  <li>Virtual Environment: venv (for dependency isolation)</li>
  <li>Package Manager: pip (Python)</li>
  <li>JavaScript Tools: npm / Node.js</li>
  <li>Database Tools: psql (PostgreSQL CLI)</li>
</ul>

<h3>🏗️ Architecture</h3>
<ul>
  <li>📁 Project Structure: Apps organized by feature (users, projects, tasks)</li>
  <li>🌐 API Layer: Django REST Framework (if used) or centralized views</li>
  <li>🧭 Routing: URLs handled via Django <code>urls.py</code></li>
  <li>🪝 State Management: Handled server-side with Django models and forms, or client-side with JS</li>
</ul>




<h2>⚙️ Backend Routes - Server (Django REST API)</h2>

<h2>👥Users</h2>
<table border="1">
  <tr>
    <th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th>
  </tr>
  <tr>
  <tr>
    <td>GET</td><td>/users/:id/</td><td>show</td><td>Show user details</td>
  </tr>
    <td>POST</td><td>/users/signup/</td><td>create</td><td>Register a new user</td>
  </tr>
  <tr>
    <td>POST</td><td>/users/login/</td><td>login</td><td>Login user</td>
  </tr>
  <tr>
    <td>POST</td><td>/users/logout/</td><td>delete</td><td>Logout user</td>
  </tr>

</table>


<h2>🗂Projects</h2>
<table border="1">
  <tr>
    <th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th>
  </tr>
  <tr>
    <td>GET</td><td>/projects/</td><td>index</td><td>List all projects for logged-in user</td>
  </tr>
  <tr>
    <td>POST</td><td>/projects/</td><td>create</td><td>Create a new project</td>
  </tr>
  <tr>
    <td>GET</td><td>/projects/:id/</td><td>show</td><td>Show project details</td>
  </tr>
  <tr>
    <td>PUT/PATCH</td><td>/projects/:id/</td><td>update</td><td>Update project</td>
  </tr>
  <tr>
    <td>DELETE</td><td>/projects/:id/</td><td>destroy</td><td>Delete project</td>
  </tr>
</table>


<h2>🧩Tasks</h2>
<table border="1">
  <tr>
    <th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th>
  </tr>
  <tr>
    <td>GET</td><td>/projects/:project_id/tasks/</td><td>index</td><td>List all tasks in a specific project</td>
  </tr>
  <tr>
    <td>POST</td><td>/projects/:project_id/tasks/</td><td>create</td><td>Create a new task for a project</td>
  </tr>
  <tr>
    <td>GET</td><td>/tasks/:id/</td><td>show</td><td>Show task details</td>
  </tr>
  <tr>
    <td>PUT/PATCH</td><td>/tasks/:id/</td><td>update</td><td>Update task details</td>
  </tr>
  <tr>
    <td>DELETE</td><td>/tasks/:id/</td><td>destroy</td><td>Delete task</td>
  </tr>
</table>


<h2>🕒Task Log</h2>
<table border="1">
  <tr>
    <th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th>
  </tr>
  <tr>
    <td>GET</td><td>/tasks/:task_id/logs/</td><td>index</td><td>Show all logs for a task</td>
  </tr>
  <tr>
    <td>POST</td><td>/tasks/:task_id/logs/</td><td>create</td><td>Create a new log for a task</td>
  </tr>
  <tr>
    <td>GET</td><td>/tasklogs/:id/</td><td>show</td><td>Show a specific log entry</td>
  </tr>
</table>
<h3>🧩 Associate Task to Project</h3>
<table border="1">
  <tr>
    <th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th>
  </tr>
  <tr>
    <td>POST</td><td>/projects/:project_id/tasks/</td><td>create</td><td>Create a new task associated with a specific project</td>
  </tr>
  <tr>
    <td>GET</td><td>/projects/:project_id/tasks/</td><td>index</td><td>List all tasks under a specific project</td>
  </tr>
</table>

<h3>🕒 Associate Task to Task Log</h3>
<table border="1">
  <tr>
    <th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th>
  </tr>
  <tr>
    <td>POST</td><td>/tasks/:task_id/logs/</td><td>create</td><td>Create a new log entry associated with a specific task</td>
  </tr>
  <tr>
    <td>GET</td><td>/tasks/:task_id/logs/</td><td>index</td><td>List all log entries for a specific task</td>
  </tr>
</table>


<br>

<h2>🧩 IceBox Features (Future Enhancements)</h2>
<ul>
  <li>📊 Dashboard with project and task analytics</li>
  <li>🔔 Real-time notifications for updates and new tasks</li>
  <li>📱 Mobile-friendly interface and potential mobile app</li>
  <li>🔍 Advanced filtering and search (by status, due date, assignee)</li>
 <li>👥 Add an Employee model for staff management</li>
<li>👥 Expand user role system to include Admin and Employee accounts</li>
</ul>


<h3>ERD Diagram</h3>
<img src="lastupdated2.png" alt="ERD Diagram" width="300">

<br><br>
<b>Frontend Link:</b>
<pre><code>git clone https://github.com/fatimahbali/Capstone-frontend.git
cd Capstone-frontend
</code>

<a href="http://localhost:5173">Link to frontend: http://localhost:5173/</a></pre>
<b>Backend Link:</b> 

<pre><code>git clone https://github.com/fatimahbali/Capstone-backend.git
cd Capstone-backend</code> 

<a href="http://127.0.0.1:8000/">Link to Backend : http://127.0.0.1:8000/</a>
