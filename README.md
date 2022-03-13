# virulent_factor_classification
Model that computes the probability of a protein to be a virulent factor.
Since this project takes inspiration from [PathoFact](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-020-00993-9), the feedforward artificial neural network model takes some protein features as input and it is trained in order to correctly classify if a protein is a virulent factor or not. In this terms, the task is a binary classification, so an entropy loss is used. 
The features are computed with [iFeature](https://github.com/Superzchen/iFeature) so a parser of the iFeature output files, to obtain the vectors to feed the model, is used. They are:
- AAC: amino acids composition
- DPC: dipeptide composition
- CTDC: composition
- CTDT: transition
- CTDD: distribution

([here](https://github.com/Superzchen/iFeature/blob/master/iFeatureManual.pdf) if you want more information about what they are and how to compute them).

# Dataset

The positive samples (proteins which are virulence factors) are taken from [VFDB](http://www.mgc.ac.cn/VFs/main.htm), while the negative samples are taken from [UniProtKB](https://www.uniprot.org/help/uniprotkb) searching 
```
taxonomy:"Bacteria [2]" NOT virulent NOT virulence NOT pathogen NOT pathogenic NOT lethal NOT adhesin NOT toxin NOT invasin NOT antiphagocytic NOT hemolysin NOT endotoxin NOT exotoxin NOT infect NOT subtilisin NOT infective NOT enterotoxin NOT hydrolase NOT lipopolysaccharide NOT lipase NOT immunoevasion NOT immunomodulation NOT aldolase NOT phospholipase NOT biofilm NOT pilus NOT multidrug NOT flagellar NOT flagella NOT motility NOT infection NOT adherence NOT lipoprotein AND reviewed:yes
```
and then manually removing the proteins according to
```
excluding antibiotics
excluding heparinase 
excluding spore
```
Redundant sequences above a similarity treshold of the 60% were removed from both datsets using the [CD-hit](http://weizhong-lab.ucsd.edu/cdhit-web-server/cgi-bin/index.cgi?cmd=cd-hit) web interface. ~3100 non-reduntant sequences for each dataset were thus considered for the further steps.

Then, the two datasets are concatenated, shuffled, and a train-validation-test split is performed taking 50% of the proteins for training, 25% for the validation and 25 for testing.

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

Here the performance in terms of accuracy on training and validation sets:

![acc](https://user-images.githubusercontent.com/62892813/158029536-0f10cd8d-7238-4eb9-8401-7340ed2c6248.png)

the accuracy on the test set is 79.6%.

Every passage herein described can be found in [this notebook](./example.ipynb)
