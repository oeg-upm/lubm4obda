<p align="center">
<img src="https://github.com/oeg-upm/lubm4obda/blob/main/logo.png" height="280" alt="morph">
</p>

**The LUBM4OBDA Benchmark** is an extension of the popular **[LUBM Benchmark](http://swat.cse.lehigh.edu/projects/lubm/)** to evaluate OBDA engines over relational databases:

- SQL dumps for **[MySQL](https://www.mysql.com/)** and **[PostgreSQL](https://www.postgresql.org/)**.
- Data generator for custom scaling factors.
- Original **[LUBM query set](http://swat.cse.lehigh.edu/projects/lubm/queries-sparql.txt)** (queries 1-14).
- Statement-level metadata query set for _standard reification_, _singleton property_ and _SPARQL-star_ (queries 15-18).
- **[R2RML](https://www.w3.org/TR/r2rml/)** and **[RML](https://rml.io/specs/rml/)** mappings.

## Data

There are two options to obtain the SQL dumps:

- Download the SQL dumps for scaling factors 1, 10, 100 and 1000 from **[Zenodo]()**.
- Use the **[Docker]()** container with the data generator to produce the data with **custom** scaling factors.

To use the docker container with the data generator just run the following command:

`docker`

Then follow the instructions prompted: provide scaling factor and select the DBMS (MySQL or PostgreSQL).

## Mappings

The **[mappings](https://github.com/oeg-upm/lubm4obda/tree/main/mappings)** directory of this GitHub repository contains all the R2RML and RML documents. The following mappings are available:

- **[R2RML](https://github.com/oeg-upm/lubm4obda/tree/main/mappings/r2rml)**:
  - [Basic](https://github.com/oeg-upm/lubm4obda/blob/main/mappings/r2rml/lubm4obda.r2rml.ttl), without statement-level metadata.
  - [Standard reification](https://github.com/oeg-upm/lubm4obda/blob/main/mappings/r2rml/lubm4obda-reification.r2rml.ttl).
  - [Singleton property](https://github.com/oeg-upm/lubm4obda/blob/main/mappings/r2rml/lubm4obda-singleton-property.r2rml.ttl).
  - [R2RML-star](https://github.com/oeg-upm/lubm4obda/blob/main/mappings/r2rml/lubm4obda-star.r2rml.ttl).

- **[RML](https://github.com/oeg-upm/lubm4obda/tree/main/mappings/rml)**:
  - [Basic](https://github.com/oeg-upm/lubm4obda/blob/main/mappings/rml/lubm4obda.rml.ttl), without statement-level metadata.
  - [Standard reification](https://github.com/oeg-upm/lubm4obda/blob/main/mappings/rml/lubm4obda-reification.rml.ttl).
  - [Singleton property](https://github.com/oeg-upm/lubm4obda/blob/main/mappings/rml/lubm4obda-singleton-property.rml.ttl).
  - [RML-star](https://github.com/oeg-upm/lubm4obda/blob/main/mappings/rml/lubm4obda-star.rml.ttl).

## Ontology

The ontology is available in the **[ontology](https://github.com/oeg-upm/lubm4obda/blob/main/ontology/univ-bench.owl)** directory of this GitHub repository.

## Queries

The queries are available in the **[queries](https://github.com/oeg-upm/lubm4obda/tree/main/queries)** directory of this GitHub repository. Keep in mind that **basic** mappings should be used for **queries 1-14**. There are three different versions of **queries 15-18**, one for each statement-level metadata approach (standard reification, singleton property or RDF-star), with each approach having its corresponding mapping.


Generate image:

`docker build -t lubm4obda .`

Run generator:

`docker run -itv "$(pwd)":/output lubm4obda`
