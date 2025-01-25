# Data Engineering Zoomcamp - Homework 01

## Question 1
Process:
- Start docker container with `docker run -it --entrypoint bash python:3.12.8`
- Run `pip --version`

Ans: `24.3.1`


## Question 2
Process:
 From the docker compose file we can see the database service name is "db" and the port for the database is 5432

Ans: `db:5433`


## Preparation of Postgresql and NY Taxi Data

#### Main Process:
Create a docker compose file with the Postgresql DB service, pgadmin4 service and the data ingestion service which uses the docker file to buid and execute the python script to ingest the data into the Postgresql DB.


#### Setup:

- To setup & test/run locally, create a .env file such as the following
```env
HOMEWORK_POSTGRES_USER = "hw_pg_user"
HOMEWORK_POSTGRES_PASS = "hw_pg_pass"


HOMEWORK_PGADMIN_EMAIL = "hw@pgadmin.com"
HOMEWORK_PGADMIN_PASS = "hw_pgadmin_pass"
```

- Run the following command
```bash
docker-compose up -d
```

- Access pgadmin4 at `http://localhost:18080` and login with the credentials in the .env file
## Question 3

### a.
```sql
SELECT 	COUNT(*)
FROM "ny-green-taxi-trips"
WHERE lpep_pickup_datetime >= DATE '2019-10-01'
AND lpep_dropoff_datetime < DATE '2019-11-01'
AND trip_distance <= 1;
```

### b.
```sql
SELECT 	COUNT(*)
FROM "ny-green-taxi-trips"
WHERE lpep_pickup_datetime >= DATE '2019-10-01'
AND lpep_dropoff_datetime < DATE '2019-11-01'
AND trip_distance > 1
AND trip_distance <= 3;
```

### c.
```sql
SELECT 	COUNT(*)
FROM "ny-green-taxi-trips"
WHERE lpep_pickup_datetime >= DATE '2019-10-01'
AND lpep_dropoff_datetime < DATE '2019-11-01'
AND trip_distance > 3
AND trip_distance <= 7;
```

### d.
```sql
SELECT 	COUNT(*)
FROM "ny-green-taxi-trips"
WHERE lpep_pickup_datetime >= DATE '2019-10-01'
AND lpep_dropoff_datetime < DATE '2019-11-01'
AND trip_distance > 7
AND trip_distance <= 10;
```

### e.
```sql
SELECT 	COUNT(*)
FROM "ny-green-taxi-trips"
WHERE lpep_pickup_datetime >= DATE '2019-10-01'
AND lpep_dropoff_datetime < DATE '2019-11-01'
AND trip_distance > 10;
```


Ans: `104,802; 198,924; 109,603; 27,678; 35,189`


## Question 4
```sql
SELECT 	lpep_pickup_datetime,
		MAX(trip_distance) as max_trip_distance
FROM "ny-green-taxi-trips"
GROUP BY lpep_pickup_datetime
ORDER BY max_trip_distance DESC
LIMIT 1;
```

Ans: `2019-10-31`


## Question 5
```sql
SELECT "Zone", SUM(total_amount)
FROM "ny-green-taxi-trips"
JOIN "ny-green-taxi-zones" ON "PULocationID" = "LocationID"
WHERE lpep_pickup_datetime <> DATE '2019-10-18'
GROUP BY "Zone"
ORDER BY SUM(total_amount) DESC;
```

Ans: `East Harlem North, East Harlem South, Morningside Heights`


## Question 6
```sql
SELECT "Zone", MAX(tip_amount)
FROM "ny-green-taxi-trips"
JOIN "ny-green-taxi-zones" ON "DOLocationID" = "LocationID"
WHERE lpep_pickup_datetime >= DATE '2019-10-01'
AND lpep_pickup_datetime <= DATE '2019-10-31'
GROUP BY "Zone"
ORDER BY MAX(tip_amount) DESC;
```

Ans: `JFK Airport`


## Question 7

Process: terraform apply applies the changes (terraform plan) automatically

Ans: `terraform init, terraform apply -auto-approve, terraform destroy`
