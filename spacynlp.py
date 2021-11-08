# import spacy
# import neuralcoref

# nlp = spacy.load("en_core_web_sm")
# neuralcoref.add_to_pipe(nlp)
# doc1 = nlp('My sister has a dog. She loves him.')
# print("=======",doc1._.coref_clusters)
# print("=======",doc1._.has_coref)

# doc2 = nlp('Angela lives in Boston. She is quite happy in that city.')
# for ent in doc2.ents:
#     print("=======",ent._.coref_cluster)
# print("=======",doc2._.coref_clusters)
# print("=======",doc2._.has_coref)


import spacy
import neuralcoref
nlp = spacy.load("en_core_web_sm")
neuralcoref.add_to_pipe(nlp)

doc = nlp(u'My sister has a dog. She loves him')

print("=======",doc._.coref_clusters)
print("=======",doc._.coref_clusters[1].mentions)
print("===him====",doc._.coref_clusters[1].mentions[-1])
print("===a dog====",doc._.coref_clusters[1].mentions[-1]._.coref_cluster.main)

token = doc[-1]
print("===true====",token._.in_coref)
print("=======",token._.coref_clusters)

span = doc[-1:]
print("=======",span._.is_coref)
print("=======",span._.coref_cluster.main)
print("=======",span._.coref_cluster.main._.coref_cluster)


