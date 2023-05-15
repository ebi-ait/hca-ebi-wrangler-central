---
layout: default
title: cypher query snippets
parent: Useful scripts
grand_parent: Tools
---

# cypher query snippets to help inspect metadata visually

You can use [Neo4j Cypher](https://neo4j.com/developer/cypher/resources/) queries in a web browser window together with the [HCA Ingest Service Graph Validation Suite](https://github.com/ebi-ait/ingest-graph-validator) to generate diagrams of experimental design or inspect HCA metadata.

- [Neo4j Cypher Refcard](https://neo4j.com/docs/cypher-refcard/current/) <https://neo4j.com/docs/cypher-refcard/current/>

## Pre-requisites and installation

You need to have the
* [HCA Ingest Service Graph Validation Suite](https://github.com/ebi-ait/ingest-graph-validator) installed,
* docker engine,
* a web browser.

## Usage

* Start `docker` (if not already running), then start the `ingest-graph-validator` back-end:

```
ingest-graph-validator init
```

* Load (`hydrate`) an HCA metadata spreadsheet or a submission from Ingest. For details, see:

```
ingest-graph-validator hydrate --help
```

* Go to <http://localhost:7474> in a browser to open the neo4j front-end.

* **IMPORTANT** For optimal visual experience in the [Neo4j Browser](https://neo4j.com/developer/neo4j-browser/), turn autocomplete off by going to the bottom of the settings menu and unticking `Connect result nodes`.

Copy and paste the `cypher` snippets below one-by-one into the Neo4j Browser command line.
Please, note that snippets 5. and 6. may crash your browser with some rich datasets with a large number of nodes or relationships. If that happens, just refresh the browser window, re-connect to the neo4j server and use snippets 1-5, or make a custom query for that dataset.
You can download the results as a CSV from the Table, Text, and Code views or download the graph as an SVG or PNG from the Graph view by clicking the download icon in the upper right corner of the user interface. For further help, see the [Neo4j Browser User Interface Guide.](https://neo4j.com/developer/neo4j-browser/)


1 Check if the desired project has been loaded:

```cypher
// Check project short name.
// Returns textual result.
MATCH (n:project)
RETURN n.`project_core.project_short_name` AS `project short name`
```

2  Make a sub-graph that displays protocol links

```cypher
// Inspect protocol links visually
MATCH protocols=()-[:DUMMY_EXPERIMENTAL_DESIGN]->(:process)-[:PROTOCOLS]->(:protocol)
RETURN protocols
```

3 Inspect the biomaterials:

```cypher
// From donor_organism to biomaterials (down 2 levels). 
MATCH p=(:donor_organism)-[:DUMMY_EXPERIMENTAL_DESIGN]->(:process)-[:DUMMY_EXPERIMENTAL_DESIGN]->(:biomaterial)-[:DUMMY_EXPERIMENTAL_DESIGN]->(:process)-[:DUMMY_EXPERIMENTAL_DESIGN]->(:biomaterial)
RETURN p
```

4 The following snippet is to visualise part of the experimental design in the metadata.It is useful for datasets with too many nodes and relationships to visualise at once.

```cypher
// Partial experimental design.
MATCH expdesign=(:biomaterial)-[:DUMMY_EXPERIMENTAL_DESIGN]->(:process)-[:DUMMY_EXPERIMENTAL_DESIGN]->(:biomaterial)-[:DUMMY_EXPERIMENTAL_DESIGN]->(:process)-[:DUMMY_EXPERIMENTAL_DESIGN]->(:sequence_file)
RETURN expdesign
```

5 Experimental design graph

```cypher
// Experimental design
// related to biomaterials.
// IMPORTANT: For optimal visual experience in the neo4j browser,
//    turn autocomplete off by going to the
//    bottom of the settings menu and unticking
//    'Connect result nodes'.
MATCH expdesign=(:donor_organism)-[:DUMMY_EXPERIMENTAL_DESIGN]->(:process)-[:DUMMY_EXPERIMENTAL_DESIGN]->(:biomaterial)-[:DUMMY_EXPERIMENTAL_DESIGN *2..8]-()
RETURN expdesign
```

6 Experimental design of project
```cypher
// Project experimental design
// without protocols.
// IMPORTANT: For optimal visual experience in the neo4j browser,
//    turn autocomplete off by going to the
//    bottom of the settings menu and unticking
//    'Connect result nodes'.
MATCH p=(:project)<-[:PROJECTS]-(:donor_organism)-[:DUMMY_EXPERIMENTAL_DESIGN]->(:process)-[:DUMMY_EXPERIMENTAL_DESIGN]->(:biomaterial)-[:DUMMY_EXPERIMENTAL_DESIGN *]-()
RETURN p
```
