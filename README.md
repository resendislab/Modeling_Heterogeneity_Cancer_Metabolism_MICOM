# Modeling Cancer Metabolism Heterogeneity with MICOM

> You can download the modified version of micom that works with Recon2.2 from https://github.com/SantiagoMille/micom
> Once you have downloaded the modified micom, install it as a python package in your conda/pyenv enviroment. 
> Run ```pip install -e .``` in the code's directory. 

## Data and Code


### Genome-Scale Metabolic Models (GEMs) Jupyter Notebooks

The Python 3.7.9 notebooks used to generate reconstructions for each of the three previosly identified cell populations based on Recon2.2 and transcription, data can be found in the directory 'CORDA'. The first iteration of reconstruction notebooks do not use Differential Expression data. On the other hand, the newest versions do use it and are labeled with **"Dif_Exp"**. Each of this notebooks have comments that explain what is being done on each step of the process.

### MICOM

To generate a 

MICOM docs: https://resendislab.github.io/micom/

### Transcriptome Data

The transcriptome data used for this project is located under the 'Transcriptome Data' directory. 

The "ScaledData_kmeans_Class_uMAP_X.csv" files contain the gene expression levels of each of the three sub-populations previously identified to be part of MCF Multicellular Tumor Spheroids (https://www.nature.com/articles/s41598-020-69026-7). 

The "Dif_Exp_X.csv" files contain the differential expression analysis results. We use this data to get a better idea of which genes are being expressed and therefore create more accurate metabolic models.

Additionally, the file named HugoV2.csv is used to map all of the metabolic genes in Recon2.2 (HUGO IDs = HGNC) to the genes on the expression matrices (gene symbols). E.g. HGNC:23647 -> ADGRE3

### CORDA Generated GEMs 

The resulting individual metabolic reconstructions (SBML files) are located in 'SBMLs'. These reconstructions are used as inputs to create a MICOM object, which is the engine we use to simulate a colony (diffents sub-populations and their interactions) and optimize community growth. 

Newest SBML files are: 
 - cobraA_Mar16_div50_NormalObj
 - cobraB_Mar16_div50_NormalObj
 - cobraC_Mar16_div50_NormalObj

The python notebooks used to run micom can be found in directory micom. The file "analysis-w-micom" is where single reaction deletion is tested. The file "micom_syn_data" is where the 256 communities with different abundancies are generated and PCA is perfomred to unveil the most variable and least variable reactions of each population/community. The folder "models" inside "micom" contains all .pickle community models. The file "exchanges_2" generates media-related figures of the communities. Finally the "micom_analysis" makes a qualitative analysis of a single micom reconstruction. 