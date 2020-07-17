# fidelio
REST API that serves data from [National Vulnerability Database](https://nvd.nist.gov/)

## Prerequisites
System dependencies:
- [Docker](https://docker.com)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3.6.9 +](https://python.org)

## Getting started
To run this app locally, run the following:
```bash
docker-compose up
```
This will build up all the services that are listed in [docker-compose.yml](./docker-compose.yml) file.
<br>

If you are running this project for the first time, tables in the database are not defined and empty. To solve this, open new terminal window and type the following commands:
```bash
python3 download_cve.py
```
```bash
python3 download_cpe.py
```
*These two commands will download all the data from NVD in zip files*
<br>
<br>
```bash
docker exec -it fidelio_api python manip_db.py create-tables
```
*This will create all the tables defined in [models.py](./app/models.py)*
<br>
<br>
```bash
docker exec -it fidelio_api python manip_db.py fill-db-cve
```
*This will extract all the CVE data from zip files and fill the database with them*
<br>
<br>
```bash
docker exec -it fidelio_api python manip_db.py fill-db-cpe
```
*This will extract all the CPE, vendor and product data from zip files and fill the database with them*
<br>
<br>
```bash
docker exec -it fidelio_api python manip_db.py build-rel
```
*This will create relationships between CVE and CPE models*
<br>
<br>
**NOTE**: Last command is very resource intensive, execution can last up to 24 hours


## API usage
API uses [Swagger](https://swagger.io) to display documentation, you can find it [here](http://46.101.210.113/api/docs).


## Code Style
Linter flake8 was used during the writing of the project. Main guideline is to not overcomplicate things and to not cross line length which is set to 100.

## Made with
- [Docker](https://docker.com/) - containerzation and virtualization
- [Flask](https://www.palletsprojects.com/p/flask/) - micro web framework 
- [Postgres](https://postgres.com/) - open source relational database system
