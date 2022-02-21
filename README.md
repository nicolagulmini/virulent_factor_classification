# virulent_factor_classification
Attempt to build a model that computes the probability of a protein to be a virulent factor.
Since this project takes inspiration from [PathoFact](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-020-00993-9), the feedforward artificial neural network model takes some protein features in input and it is trained in order to correctly classify if a protein is a virulent factor or not. In this terms, the task is a binary classification, so an entropy loss is used. 
The features are computed with [iFeature](https://github.com/Superzchen/iFeature) so the `utils.py` file contains a parser of the iFeature output files, to obtain the vectors to feed the model. They are:
- AAC: amino acids composition
- DPC: dipeptide composition
- CTDC: composition
- CTDT: transition
- CTDD: distribution

([here](https://github.com/Superzchen/iFeature/blob/master/iFeatureManual.pdf) if you want more information about what they are and how to compute them).

## brief feature computation tutorial (colab, uploading an `input.fasta` file with your proteins)
```
!rm -r iFeature
!git clone https://github.com/Superzchen/iFeature
!python iFeature/iFeature.py --file ./input.fasta --type AAC --out aac.out    # amino acids composition
!python iFeature/iFeature.py --file ./input.fasta --type DPC --out dpc.out    # dipeptide composition
!python iFeature/iFeature.py --file ./input.fasta --type CTDC --out ctdc.out  # composition
!python iFeature/iFeature.py --file ./input.fasta --type CTDT --out ctdt.out  # transition
!python iFeature/iFeature.py --file ./input.fasta --type CTDD --out ctdd.out  # distribution
```

# Performance

The model is trained on the same datasets of PathoFact for 20 epochs. Here the performance in terms of loss and accuracy on training and validation sets:

![loss](https://user-images.githubusercontent.com/62892813/154985962-61661e0c-6ea3-4445-b568-ecc3c59024d6.png)
![acc](https://user-images.githubusercontent.com/62892813/154985964-5d1d3f54-8374-4f26-ab1e-3f7300c9770d.png)

the accuracy on the test set is 76%. The accuracy on [this](https://drive.google.com/drive/folders/11_t9oVYcTjX9yVkNvk9qHWqSxbFCvXAA?usp=sharing) negative test set is 84%. The accuracy on [this](https://drive.google.com/drive/folders/1yKBrBPAbS7NsB2PQ3c9tA6dO4d2ovkeK?usp=sharing) positive test set is 64%. 
