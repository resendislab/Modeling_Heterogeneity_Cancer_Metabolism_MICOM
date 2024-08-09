![Copia de logosxsss (3)](https://github.com/resendislab/Modeling_Heterogeneity_Cancer_Metabolism_MICOM/assets/45723112/4e369c2c-cab2-4e9f-a9b4-c2bfe2e4248a)


# Modeling Cancer Metabolism Heterogeneity with MICOM

Through the implementation of single cell sequencing technologies (scRNASeq) we were able to characterize the presence of 3 subpopulations in a Multicellular Tumor Spheroids of MCF-7 with invasive, proliferative and reservoir characteristics. [background](https://www.nature.com/articles/s41598-020-69026-7). 

The Community modeling was performed using the  [MICOM](https://journals.asm.org/doi/10.1128/mSystems.00606-19) tool.





## Optimizer
 To run CORDA you must install Gurobi Optimizer https://www.gurobi.com/documentation/9.1/quickstart_mac/software_installation_guid.html. You can obtain a free academic license. 

## Imputation

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
 - cobraA.xml
 - cobraB.xml
 - cobraC.xml

##### Under review
The python notebooks used to run micom can be found in directory micom. The file "analysis-w-micom" is where single reaction deletion is tested. The file "micom_syn_data" is where the 256 communities with different abundancies are generated and PCA is perfomred to unveil the most variable and least variable reactions of each population/community. The folder "models" inside "micom" contains all .pickle community models. The file "exchanges_2" generates media-related figures of the communities. Finally the "micom_analysis" makes a qualitative analysis of a single micom reconstruction. 


### MICOM

#### What is it?
With the GEMs generated from the previos step, we can create a MICOM object. MICOM is a Python package for metabolic modeling of cellular communities. `micom` allows you to construct a community model from a list on input COBRA models and manages exchange fluxes between individuals and between individuals with the environment. It explicitly accounts for different abundances of individuals in the community and can thus incorporate data from sc-rRNA sequencing experiments. It allows optimization with a variety of algorithms modeling the trade-off between egoistic growth rate maximization and cooperative objective

MICOM docs: https://resendislab.github.io/micom/

#### Data
Under the `data` directory, you will find different files needed to run python scripts (`scripts_figures`) to produce figures like the ones of the micom paper (https://github.com/micom-dev/paper). For more detail on how to produce each file or what they do please visit the github of `micom-dev/paper`. You should also be able to find information on the scripts.

The `models` folder contains many PICKLE files. Each of these files have a built micom model with different abundances that can be loaded into your notebooks/script and run/optimized/analyze. Models that start with `community_scan` have different abundances with each individual abudance equally distributed between 0 to 1 (e.g. abundanceA = 0.26, abundanceB = 0.2, abundanceC = 0.54). **However, the sum of the three abundances must equal 1**.  

#### Notebooks

- The `heatmap_medium.ipynb` produces a correlation matrix of all the metabolites present in the media. This figure shows the optimized community growth when two metabolites are removed from the media.  

- The `analysis-w-micom.ipynb` iterates over significant reactions (obtained from a PCA analysis in micom_syn_data.ipynb) in the model and zeros (turns off) their flux. This way we can observe their effect in the model.

- The `micom_fundamentals.ipynb` makes a qualitative exploration of the reaction, fluxes and FBA results of a single micom model. It is a good basic guide to learn to explore micom's data.

- The `exchanges_2.ipynb` generates some of the files under `data` directory and produces the media figures of the micom paper. 

- The `micom_syn_data.ipynb` generates 256 equally-distributed-abudances models and produces quantitative and more statistically significant data. Using PCA, it determines the most (robust/elastic) and least (preserved) variable reactions across the models. We hypothesize that the preserved reactions are highly important and that the robust reactions allows the community to adjust to the environment.


# Atribution

Santiago Mille\
Jorge Arellano\
Christian Padrón\
Aarón Vázquez\
Osbaldo Resendis\
[Human Systems Biology Lab](https://resendislab.github.io/)



## How to run the various notebooks

1. Run the `CORDA` notebook to generate 3 SBML files.
2. Run `micom_fundamental` to explore the data and get familiar with it.
3. Run `micom_syn_data` to obtain the data needed for the coming notebooks.
4. Run `exchanges_2` to obtain a heatmap of exchange fluxes and further files needed to run the figures' producing scripts.
5. Run `analysis-w-micom` to learn which reactions lower the overall mass production.
6. Run `heatmap_medium` produces a correlation matrix of all the metabolites present in the media.
7. Run the python scripts under `scripts_figures`


