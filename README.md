<p align="center">
<img src="https://github.com/oeg-upm/lubm4obda/blob/main/logo.png" height="280" alt="morph">
</p>

Generate image:

`docker build -t lubm4obda .`

Run generator:

`docker run -itv "$(pwd)":/output lubm4obda`

## Data

The benchmark generates data compatible with **[MySQL](https://www.mysql.com/)** ans **[PostgreSQL](https://www.postgresql.org/)**. There are two options to obtain the data:

- Download the data dumps available in the **[data](https://github.com/oeg-upm/lubm4obda/tree/main/data)** directory (scale factors 1, 10 and 100) or **[Zenodo]()** (scale factors 1, 10, 100 and 1000).
- Use the **[Docker]()** container with the data generator to produce the data with custom scaling factors.

To use the docker container with the data generator run the following:

## Ontology

The ontology is available in the **[ontology]** directory of this GitHub repository.

## Queries

## Mappings
