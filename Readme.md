<h2>Backend Routes - Server (Django REST API)</h2>

<h2>Users</h2>
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
  <tr>
    <td>PUT</td><td>/users/:id/</td><td>update</td><td>Update user information</td>
  </tr>
  <tr>
    <td>DELETE</td><td>/users/:id/</td><td>destroy</td><td>Delete user</td>
  </tr>
</table>


<h2>Projects</h2>
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


<h2>Tasks</h2>
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


<h2>Task Log</h2>
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

<br>

<h3>ERD Diagram</h3>
<img src="updated2.png" alt="ERD Diagram" width="300">

<br><br>

<b>Backend Link:</b>  
<a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>
