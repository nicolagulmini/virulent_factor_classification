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

![loss](https://user-images.githubusercontent.com/62892813/137992562-e35bb45f-6034-46dd-81b0-0bac7c66d86c.png)
![accuracy](https://user-images.githubusercontent.com/62892813/137992567-fded0e28-05b0-4589-9205-8dffe7aee316.png)

the accuracy on the test set is 76%. The accuracy on [this](https://drive.google.com/drive/folders/11_t9oVYcTjX9yVkNvk9qHWqSxbFCvXAA?usp=sharing) negative test set is 84%. The accuracy on a positive test set is coming soon.
