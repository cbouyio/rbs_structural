# RNA binding proteins project

#### Work done in the context of the "Projet long" of M1BI

### Prenom, Nom

## Intro - Motivation

Reviews on RBPs and the computation methods developed for their identification and (on section Data)

## Material - Data & Methods

### Tools - software:

1. https://www.w3schools.com/python/pandas/default.asp
2. https://realpython.com/python-for-data-analysis/
3. 


### Data:
1. Presentation: https://www.genome.gov/sites/default/files/Multimedia/Slides/ENCODE2016-ResearchAppsUsers/vanNostrand_eCLIP.pdf
2. Paper e-CLIP: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7410833/
3. Paper for nucleac acid binding: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7831508/
4. Data e-CLIP ENCODE: https://www.encodeproject.org/encore-matrix/?type=Experiment&status=released&internal_tags=ENCORE
5. Data RPF: http://sysbio.gzzoc.com/rpfdb/index.html
6. 

### Model Papers:
1. Predicting the translation efficiency of messenger RNA in mammalian cells https://www.biorxiv.org/content/10.1101/2024.08.11.607362v1
2. Translation efficiency covariation across cell types is a conserved organizing principle of mammalian transcriptomes https://www.biorxiv.org/content/10.1101/2024.08.11.607360v1
3. 

## Remarks
1. Costas - Find the document and data and results from the previous M2 stage (Sepher).


## After meeting on 30/10/2024

Techincal part
1. Add an additional column "No_feat" to show the total number of features for each RBP.
-> done 
2. Create a motif_info list and put only the features that have a "motif" or a "binding" type.
-> done (not in the final file)
3. Generate three new columns in the output file one "Binding_site" one "Motifs" and one "Domains" and you put all the BS IDs and all the Motif IDs and Domain IDs semicolon separed.
-> done (the column have the ID only once if it's repeated, for binding_id I took the evidenceCode)
4. At the end out data file will have the following columns "rbp_name","uniprotID","No_Features","motifs"(motif IDs semicolon separated),"binding_Sites"(BS IDs semicolon separated)
-> and domains (IDs semicolon separated) ? 
