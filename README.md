# incubator
REST API that serves data from [National Vulnerability Database](https://nvd.nist.gov/)

## Prerequisites
System dependencies:
- [Docker](https://docker.com)
- [Docker Compose](https://docs.docker.com/compose/)

## Gettings started
To run this app locally, run the following:
```bash
docker-compose up
```
This will build up all the services that are listed in docker-compose.yml file.
<br>

If you are running this project for the first time, tables in the database are not defined. To solve this, open new terminal window and type the following:
```bash
docker exec -it incubator_api python create_db.py
```
This will create all tables and columns in the databse and grant the user permissions needed. Use this command whenever you make a new chane to databse models in `app/models.py` or you just want to flush the database


## Made with
- [Docker](https://docker.com/) - containerzation and virtualization
- [Flask](https://www.palletsprojects.com/p/flask/) - micro web framework 
- [Postgres](https://postgres.com/) - open source relational database system
