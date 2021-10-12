from Bio import SeqIO
import numpy as np
import random

def from_files_to_vectors(fasta_path, positive=True):
    if positive:
        proteins = list(SeqIO.parse(fasta_path+'positive_virulent.fasta', "fasta"))
    else:
        proteins = list(SeqIO.parse(fasta_path+'negative_virulent.fasta', "fasta"))
    extension = ".out"
    files = ["aac", "dpc", "ctdc", "ctdt", "ctdd"]
    datasets = [[] for el in files]
    for i in range(len(files)):
        with open(fasta_path+files[i]+extension) as f:
            lines = f.readlines()[1:]
            check_prot = 0
            for line in lines:
                information = line.split('\t')
                if not information[0] == proteins[check_prot].id:
                    print("Error in protein order! Return")
                    return datasets
                datasets[i].append(np.array([float(el) for el in information[1:]]))
                check_prot += 1
        datasets[i] = np.array(datasets[i])
    return datasets

def from_vectors_to_train_and_test_with_labels(positive_datasets, negative_datasets):
    if not (len(positive_datasets) == 5 and len(negative_datasets) == 5):
        print("Error in datasets!")
        return
    # train - test positive and negative split
    train = set(random.sample(range(len(positive_datasets[0])), int(len(positive_datasets[0])*0.75)))
    test = set(random.sample(range(len(negative_datasets[0])), int(len(negative_datasets[0])*0.75)))
    train_positive_datasets = []
    train_negative_datasets = []
    test_positive_datasets = []
    test_negative_datasets = []
    for ds in positive_datasets:
        train_positive_datasets.append(np.array([x for i,x in enumerate(ds) if not i in train]))
        test_positive_datasets.append(np.array([x for i,x in enumerate(ds) if i in train]))
    for ds in negative_datasets:
        train_negative_datasets.append(np.array([x for i,x in enumerate(ds) if not i in test]))
        test_negative_datasets.append(np.array([x for i,x in enumerate(ds) if i in test]))
    
    # merge positive and negative datasets and permute them (adding the labels)
    positive_train_labels = [1. for _ in range(len(train_positive_datasets[0]))]
    positive_test_labels = [1. for _ in range(len(test_positive_datasets[0]))]
    negative_train_labels = [0. for _ in range(len(train_negative_datasets[0]))]
    negative_test_labels = [0. for _ in range(len(test_negative_datasets[0]))]
    
    x_train = [train_positive_datasets[_] + train_negative_datasets[_] for _ in range(len(train_positive_datasets))]
    y_train = positive_train_labels + negative_train_labels
    # se x_train mi da errore è perche non è formato da liste ma da vettori, allora nelle righe intorno alla 40 rimuovi np.array e mettilo alla fine
    x_test = [test_positive_datasets[_] + test_negative_datasets[_] for _ in range(len(test_positive_datasets))]
    y_test = positive_test_labels + negative_test_labels
    
    shuffler = np.random.permutation(len(x_train[0])) # same permutation on x and y
    x_train = [ds[shuffler] for ds in x_train]
    y_train = y_train[shuffler]
    # no validation for now
    shuffler = np.random.permutation(len(x_test[0])) 
    x_test = [ds[shuffler] for ds in x_test]
    y_test = y_test[shuffler]
    
    return x_train, y_train, x_test, y_test

positive_datasets = from_files_to_vectors('./training/positive/')
negative_datasets = from_files_to_vectors('./training/negative/', positive=False)

x_train, y_train, x_test, y_test = from_vectors_to_train_and_test_with_labels(positive_datasets, negative_datasets)


