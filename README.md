# ranking_portal_demo
Demo repository for company ranking portal written in Django.

## How To Run Locally?

### Install Docker
- Go to the page https://docs.docker.com/get-docker/.
- Do the necessary steps according to your OS and install Docker Engine (Alternatively, you can also install Docker Desktop).

### Clone the project
- Clone the project to your computer. Open it with your favourite IDE (VS Code is suggested since this project runs 2 Docker containers at the same time. For low resource computers, VS Code is lightweight and Docker will already use lots of resources.)

### Create a .env file
- Copy the contents of .env.example file into a .env file.
- Provide necessary data inside the .env file.

### Run the test containers using docker-compose
- Run the command below to run both backend and DB test containers and create a network for their communication (See docker-compose.yml file for details).
```
docker-compose up -d
```
Note: The given command do not rebuilds the Docker images. It just reruns the docker-compose.yml file. If any changes have been made in Dockerfile (image description), one must delete the current images/volumes etc. and run the command again or run the command below.
```
docker-compose up --build
```

### Navigate to http://localhost:8000/companies
- Once the development server is running, you can access the application by navigating to [http://localhost:8000/companies](http://localhost:8000/companies) in your web browser.

### Additional details
- The command below shows the running Docker containers. Getting the running container's ID is essential for entering inside the container.
```
docker ps
```
- The command below opens a terminal inside the specified Docker container. The whole container ID can be provided or the first 3 characters of the container ID is enough for the command to run.
```
docker exec -it <container_id> bash
```
- The difference between Linux and Windows end line characters (CRLF and LF) can break down the containers and result with errors. The error below is previously occured because of that problem. You can tell Git to not autocorrect CRLF with the command below the error message.
```
Problem wait.sh was not found. Error in CRLF.
```
```
git config --global core.autocrlf false
```
and if you are developing on Windows and your Docker container is a Linux environment, there may be an issue with line endings (CRLF vs. LF). Scripts created on Windows might have the wrong line endings for Unix environments. Thus, use dos2unix to convert the file format.
```
dos2unix wait.sh
```
- Django migrations can sometimes be problematic. Changing lots of columns/tables and creating migrations will cause problems (Django checks the updated columns/tables and wants to make the changes according to SQL rules). If stucked, one can delete the migrations folder, drop the tables and go to django_migrations table and drop the previous migrations' rows. The last one is essential since Django thinks it did the migration if a row exists for that migration in that table (This is not the best way to deal with migration problems. This README will be updated after determining suitable migration pipelines for both development and production).
- You can install your favourite HTTP client (Postman is suggested but Postman desktop app is heavy) and DB client (Datagrip is suggested) for testing purposes.


```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass;
python -m venv .venv; .\.venv\Scripts\Activate.ps1;
python -m ensurepip --upgrade; pip install -r requirements.txt;
python -m pip install --upgrade pip
```
- Bypass ExecutePolicy for Powershell scripts.
- Create an activate virtual Python environment.
- Install and update requirements.
- For debugging, run Python: Django RemoteDB
