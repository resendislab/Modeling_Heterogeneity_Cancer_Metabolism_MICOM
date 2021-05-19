#Modeling Cancer Metabolism Heterogeneity with MICOM

> You can download the modified version of micom that works with Recon2.2 from https://github.com/SantiagoMille/micom

## Data and code

The Python 3.7.9 notebooks used to generate each of the three reconstructions from the Recon2.2 model and transcription data can be found in the directory 'CORDA'. Newer ones are labedl with "Dif_Exp".

Transcription data is located in the 'Transcriptome Data' directory.

The resulting SBML files containing the reconstructions are located in 'SBMLs'. Current ones used for micom are: 
 - cobraA_Mar16_div50_NormalObj
 - cobraB_Mar16_div50_NormalObj
 - cobraC_Mar12_div50_NormalObj

The python notebooks used to run micom can be found in directory micom. The file "analysis-w-micom" is where single reaction deletion is tested. The file "micom_syn_data" is where the 256 communities with different abundancies are generated and PCA is perfomred to unveil the most variable and least variable reactions of each population/community. The folder "models" inside "micom" contains all .pickle community models. The file "exchanges_2" generates media-related figures of the communities. Finally the "micom_analysis" makes a qualitative analysis of a single micom reconstruction. 