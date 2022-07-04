<p align="center">
<img src="https://github.com/oeg-upm/lubm4obda/blob/main/logo.png" height="280" alt="morph">
</p>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6583207.svg)](https://doi.org/10.5281/zenodo.6583207)

**The LUBM4OBDA Benchmark** is an extension of the popular **[LUBM Benchmark](http://swat.cse.lehigh.edu/projects/lubm/)** to evaluate Ontology-Based Data Access (OBDA) engines over relational databases. In addition, LUBM4OBDA considers meta knowledge (also called reification or statement-level metadata) benchmarking. The main characteristics of LUBM4OBDA are:

- SQL data dumps for **[MySQL](https://www.mysql.com/)** and **[PostgreSQL](https://www.postgresql.org/)**.
- Data generator for custom scaling factors.
- Original **[LUBM query set](http://swat.cse.lehigh.edu/projects/lubm/queries-sparql.txt)** (queries 1-14).
- Meta knowledge query set for [_standard reification_](https://www.w3.org/TR/rdf-primer/#reification), [_singleton property_](https://dl.acm.org/doi/pdf/10.1145/2566486.2567973) and [_SPARQL-star_](https://w3c.github.io/rdf-star/cg-spec/2021-12-17.html#sparql-star) (queries 15-18).
- **[R2RML](https://www.w3.org/TR/r2rml/)** and **[RML](https://rml.io/specs/rml/)** mappings.

## Data

There are two options to obtain the SQL data dumps:

- Download the SQL data dumps for scaling factors 1, 10, 100 and 1000 from **[Zenodo](https://doi.org/10.5281/zenodo.6583207)**.
- Use the **[Docker](https://hub.docker.com/r/oegdataintegration/lubm4obda)** container with the data generator to produce the data with **custom** scaling factors.

To use the docker container with the data generator just run the following command from the terminal:

`docker run -itv "$(pwd)":/output oegdataintegration/lubm4obda`

Then follow the instructions prompted: provide the scaling factor and select the RDBMS (MySQL or PostgreSQL).

## Mappings

The **[mappings](https://github.com/oeg-upm/lubm4obda/tree/main/mappings)** directory of this GitHub repository contains all the R2RML and RML documents. The following mappings are provided:

- **[R2RML](https://github.com/oeg-upm/lubm4obda/tree/main/mappings/r2rml)**:
  - [Original](https://github.com/oeg-upm/lubm4obda/blob/main/mappings/r2rml/lubm4obda.r2rml.ttl), without meta knowledge.
  - [Standard reification](https://github.com/oeg-upm/lubm4obda/blob/main/mappings/r2rml/lubm4obda-reification.r2rml.ttl).
  - [Singleton property](https://github.com/oeg-upm/lubm4obda/blob/main/mappings/r2rml/lubm4obda-singleton-property.r2rml.ttl).
  - [R2RML-star](https://github.com/oeg-upm/lubm4obda/blob/main/mappings/r2rml/lubm4obda-star.r2rml.ttl).

- **[RML](https://github.com/oeg-upm/lubm4obda/tree/main/mappings/rml)**:
  - [Original](https://github.com/oeg-upm/lubm4obda/blob/main/mappings/rml/lubm4obda.rml.ttl), without meta knowledge.
  - [Standard reification](https://github.com/oeg-upm/lubm4obda/blob/main/mappings/rml/lubm4obda-reification.rml.ttl).
  - [Singleton property](https://github.com/oeg-upm/lubm4obda/blob/main/mappings/rml/lubm4obda-singleton-property.rml.ttl).
  - [RML-star](https://github.com/oeg-upm/lubm4obda/blob/main/mappings/rml/lubm4obda-star.rml.ttl).

## Ontology

The **Univ-Bench ontology** is available in the **[ontology](https://github.com/oeg-upm/lubm4obda/blob/main/ontology/univ-bench.owl)** directory of this GitHub repository.

## Queries

The queries are available in the **[queries](https://github.com/oeg-upm/lubm4obda/tree/main/queries)** directory of this GitHub repository. Keep in mind that **original** mappings should be used for **queries 1-14**. There are three different versions of **queries 15-18**, one for each meta knowledge approach (standard reification, singleton property or RDF-star), with each approach having its corresponding mapping.
