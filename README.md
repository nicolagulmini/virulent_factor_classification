# virulent_factor_classification
Attempt to build a model that computes the probability of a protein to be a virulent factor.
Since this project takes inspiration from [PathoFact](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-020-00993-9), the feedforward artificial neural network model takes some protein features in input and it is trained in order to correctly classify if a protein is a virulent factor or not. In this terms, the task is a binary classification, so an entropy loss is used. 
The features are computed with [iFeature](https://github.com/Superzchen/iFeature) so the `utils.py` file contains a parser of the iFeature output files, to obtain the vectors to feed the model. They are:
- AAC: amino acids composition
- DPC: dipeptide composition
- CTDC: composition
- CTDT: transition
- CTDD: distribution
