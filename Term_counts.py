import pandas as pd

plaintext = pd.DataFrame()

# Filter the articles for relevance by checking given keywords in articles

filtered = plaintext.filter(lambda x: x if any(["SQL", "RDF", "XML", "NoSQL", "Machine Learning", "Hadoop",
                                                "Internet of Things", "Data Science", "Blockchain"])
                                           in x is True else None)


# word counts

tags = ["SQL", "RDF", "XML", "NoSQL", "Machine Learning", "Hadoop",
                                                "Internet of Things", "Data Science", "Blockchain"]



# plot




# 2)

# sort df and search for words -> output df containg year paper keyword



# tags = input from link