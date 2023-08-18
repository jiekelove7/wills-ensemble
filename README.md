Implementing a Dynamic Voting Ensemble for rumour detection

Can find PHEME dataset online, the others are already in the repo.
Need to install the glove twitter pre-trained embeddings from https://nlp.stanford.edu/projects/glove/

Requires python 3.7, create rest of environment with req.txt file
Create a directory named "spacy-twitter", then use the command `python -m spacy init vectors en glove\glove.twitter.27B.200d.txt spacy-twitter` to allow spacy to use the dataset.