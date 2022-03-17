import rdflib

g = rdflib.Graph()
g.parse('Universities-1.nt')

q = """
    SELECT DISTINCT ?p
    WHERE {
        ?s a <http://www.lehigh.edu/~zhp2/2004/0401/univ-bench.owl#university> .
        ?s ?p ?o .
    }
"""

for row in g.query(q):
    print(str(row))

"""
(rdflib.term.URIRef('http://www.lehigh.edu/~zhp2/2004/0401/univ-bench.owl#university'),)
(rdflib.term.URIRef('http://www.lehigh.edu/~zhp2/2004/0401/univ-bench.owl#department'),)
(rdflib.term.URIRef('http://www.lehigh.edu/~zhp2/2004/0401/univ-bench.owl#fullProfessor'),)
(rdflib.term.URIRef('http://www.lehigh.edu/~zhp2/2004/0401/univ-bench.owl#associateProfessor
(rdflib.term.URIRef('http://www.lehigh.edu/~zhp2/2004/0401/univ-bench.owl#assistantProfessor
(rdflib.term.URIRef('http://www.lehigh.edu/~zhp2/2004/0401/univ-bench.owl#lecturer'),)
(rdflib.term.URIRef('http://www.lehigh.edu/~zhp2/2004/0401/univ-bench.owl#undergraduateStudent
(rdflib.term.URIRef('http://www.lehigh.edu/~zhp2/2004/0401/univ-bench.owl#graduateStudent
(rdflib.term.URIRef('http://www.lehigh.edu/~zhp2/2004/0401/univ-bench.owl#researchGroup
(rdflib.term.URIRef('http://www.lehigh.edu/~zhp2/2004/0401/univ-bench.owl#publication
(rdflib.term.URIRef('http://www.lehigh.edu/~zhp2/2004/0401/univ-bench.owl#undergraduateCourse
(rdflib.term.URIRef('http://www.lehigh.edu/~zhp2/2004/0401/univ-bench.owl#graduateCourse
(rdflib.term.URIRef('http://www.lehigh.edu/~zhp2/2004/0401/univ-bench.owl#teachingAssistant'),)
(rdflib.term.URIRef('http://www.lehigh.edu/~zhp2/2004/0401/univ-bench.owl#researchAssistant'),)********


"""
