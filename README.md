![Copia de logosxsss (3)](https://github.com/resendislab/Modeling_Heterogeneity_Cancer_Metabolism_MICOM/assets/45723112/4e369c2c-cab2-4e9f-a9b4-c2bfe2e4248a)


# Modeling Cancer Metabolism Heterogeneity with MICOM

Through the implementation of single cell sequencing technologies (scRNASeq) we were able to characterize the presence of 3 subpopulations in a Multicellular Tumor Spheroids of MCF-7 with invasive, proliferative and reservoir characteristics. [background](https://www.nature.com/articles/s41598-020-69026-7). 

The Community modeling was performed using the  [MICOM](https://journals.asm.org/doi/10.1128/mSystems.00606-19) tool.
### MICOM

#### What is it?
With the GEMs generated from the previos step, we can create a MICOM object. MICOM is a Python package for metabolic modeling of cellular communities. `micom` allows you to construct a community model from a list on input COBRA models and manages exchange fluxes between individuals and between individuals with the environment. It explicitly accounts for different abundances of individuals in the community and can thus incorporate data from sc-rRNA sequencing experiments. It allows optimization with a variety of algorithms modeling the trade-off between egoistic growth rate maximization and cooperative objective

MICOM docs: https://resendislab.github.io/micom/


## Optimizer
 To run CORDA you must install Gurobi Optimizer https://www.gurobi.com/documentation/9.1/quickstart_mac/software_installation_guid.html. You can obtain a free academic license. 

## Genome-Scale Metabolic Models (GEMs) Jupyter Notebooks

The firts step was to generate a GEM for each population.The Python 3.7.9 notebook used to generate reconstructions for each of the three previosly identified cell populations based on Recon2.2 and single-cell transcription data. The notebook can be found in the folder "CORDA".

### Transcriptome Data

The transcriptome data used for this project is located under the 'Transcriptome Data/imputated' directory. 

The "MCTS_norm_X.csv" files contain the gene expression levels of each of the three sub-populations previously identified to be part of MCF Multicellular Tumor Spheroids (https://www.nature.com/articles/s41598-020-69026-7). 

The "Dif_Exp_X.csv" files contain the differential expression analysis results. We use this data to understand better which genes are being expressed and, therefore, create more accurate metabolic models.

Additionally, the file named HugoV2.csv is used to map all of the metabolic genes in Recon2.2 (HUGO IDs = HGNC) to the genes on the expression matrices (gene symbols). E.g. HGNC:23647 -> ADGRE3.

### CORDA Generated GEMs 

The resulting individual metabolic reconstructions (SBML files) are located in 'SBMLs'. These reconstructions are used as inputs to create a MICOM object, which is the engine we use to simulate a colony (diffents sub-populations and their interactions) and optimize community growth. 

The SBML files are: 
 - cobraA.xml = ModelA.xml = Invasive cells
 - cobraB.xml = ModelB.xml = Reservoir cells
 - cobraC.xml = ModelC.xml = Proliferative cells



### How to run

1. The `MICOM` folder contains all the material needed to run the modeling, for practicality purposes the code is designed to be run in Google Colab.
2. The `Scripts` folder contains the notebooks to model the community, essentiality analysis, gradients and instructions to visualize the results.
3. `Input_files` contains the original xml files and the modified gradients.




# Atribution

Jorge Enrique Arellano\
Christian Padrón\
Aarón Vázquez\
Osbaldo Resendis
Juan José Oropeza\
[Human Systems Biology Lab](https://resendislab.github.io/)


