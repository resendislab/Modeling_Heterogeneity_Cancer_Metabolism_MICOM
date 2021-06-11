import pandas as pd
import networkx as nx
import nxviz
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

'''samples = {
 
 '27': 'com_0.1203_0.3573_0.5224',
 '28': 'com_0.0743_0.4116_0.5141',
 '29': 'com_0.1146_0.3683_0.5171',
 '30': 'com_0.1066_0.3876_0.5057',
 '31': 'com_0.113_0.4163_0.4708',
 '32': 'com_0.1104_0.4095_0.4801',
 '33': 'com_0.1197_0.3492_0.531',
 '34': 'com_0.1224_0.4243_0.4533',
 '35': 'com_0.1294_0.3577_0.5129',
 '36': 'com_0.1085_0.4273_0.4642',
 '37': 'com_0.0986_0.3896_0.5118',
 '38': 'com_0.1059_0.3785_0.5155',
 '39': 'com_0.0978_0.3768_0.5254',
 '40': 'com_0.1256_0.3674_0.507',
 '41': 'com_0.0798_0.4178_0.5024',
 '42': 'com_0.1213_0.3688_0.5099',
 '43': 'com_0.0994_0.4277_0.4729',
 '44': 'com_0.1218_0.4267_0.4515',
 '45': 'com_0.1292_0.424_0.4468',
 '46': 'com_0.0893_0.4163_0.4943',
 '47': 'com_0.1132_0.4124_0.4744',
 '48': 'com_0.1119_0.4015_0.4866',
 '49': 'com_0.0941_0.3962_0.5097',
 '50': 'com_0.1166_0.3752_0.5082',
 '51': 'com_0.0622_0.3633_0.5745',
 '52': 'com_0.0971_0.3993_0.5037',
 '53': 'com_0.1015_0.4162_0.4823',
 '54': 'com_0.1044_0.4019_0.4936',
 '55': 'com_0.1019_0.4137_0.4844',
 '56': 'com_0.0846_0.4125_0.5029',
 '57': 'com_0.0576_0.3659_0.5765',
 '58': 'com_0.0894_0.3928_0.5178',
 '59': 'com_0.0521_0.3721_0.5758',
 '60': 'com_0.0661_0.4274_0.5065',
 '61': 'com_0.0929_0.3934_0.5137',
 '62': 'com_0.0922_0.3936_0.5142',
 '63': 'com_0.5982_0.2657_0.1361',
 '64': 'com_0.5432_0.3125_0.1443',
 '65': 'com_0.5898_0.2342_0.176',
 '66': 'com_0.5544_0.2461_0.1994',
 '67': 'com_0.5442_0.2956_0.1602',
 '68': 'com_0.5891_0.303_0.1079',
 '69': 'com_0.5924_0.2647_0.1429',
 '70': 'com_0.5971_0.291_0.1119',
 '71': 'com_0.5465_0.2845_0.169',
 '72': 'com_0.5955_0.2621_0.1424',
 '73': 'com_0.5599_0.235_0.2051',
 '74': 'com_0.5736_0.2962_0.1302',
 '75': 'com_0.5839_0.2371_0.179',
 '76': 'com_0.5436_0.2487_0.2078',
 '77': 'com_0.595_0.2445_0.1605',
 '78': 'com_0.5575_0.3094_0.133',
 '79': 'com_0.558_0.2528_0.1892',
 '80': 'com_0.5422_0.2448_0.213',
 '81': 'com_0.6081_0.2704_0.1216',
 '82': 'com_0.5544_0.2559_0.1897',
 '83': 'com_0.5893_0.3071_0.1036',
 '84': 'com_0.55_0.2677_0.1822',
 '85': 'com_0.5545_0.2867_0.1588',
 '86': 'com_0.5499_0.2907_0.1594',
 '87': 'com_0.5984_0.28_0.1216',
 '88': 'com_0.5541_0.2415_0.2043',
 '89': 'com_0.5485_0.3009_0.1506',
 '90': 'com_0.5484_0.2718_0.1798',
 '91': 'com_0.557_0.2731_0.1699',
 '92': 'com_0.596_0.3096_0.0944',
 '93': 'com_0.5632_0.3067_0.1301',
 '94': 'com_0.5541_0.2465_0.1993',
 '95': 'com_0.5487_0.2559_0.1955',
 '96': 'com_0.5572_0.3037_0.1391','''
samples = {
 '126': 'com_0.0902_0.391_0.5188',
 '127': 'com_0.5739_0.2739_0.1522'}


metabolites = pd.read_csv("./data/metabolites.csv")[
    ["abbreviation", "fullName", "chargedFormula"]
]

#SCFAs = {"lactate": "EX_lac_", "O2": "O2t", "pyruvate": "EX_pyr_"}
#SCFAs = {"PDH": "PDHm",'PC':'PCm','FAOX':'FAOXC8060m','NADH':'NADH2_u10m','HMGC':'HMGCOAtm','ATPs':'ATPS4m','ATPt':'ATPtm'}
SCFAs = {"o2": "EX_o2",'chol':'EX_chol','gal':'EX_gal','ala':'EX_ala','pi':'EX_pi','glu':'EX_glu','lys':'EX_lys'}


def direction(els, rid):
    return els[els.reaction == rid].direction.unique()[0]


elast = []
for sa in samples:
    e = pd.read_csv("./data/elasticities/elasticities_" + sa + "_31.csv")
    e["id"] = sa
    elast.append(e)
elast = pd.concat(elast)
################################################################################################################
elast = elast[elast.direction == "reverse"]
elast["scfa"] = float("nan")


##################################################################################################3
#for i in elast.reaction:
#    if 'EX_' in i and '_m' in i:
#        print(i)


for name, pattern in SCFAs.items():
    elast.loc[elast.reaction.str.startswith(pattern), "scfa"] = name

production = (
    elast.groupby(["id", "effector", "scfa"]).elasticity.sum().reset_index()
)
production["type"] = production.effector.apply(
    lambda e: "diet" if e.startswith("EX_") else "abundance"
)
production["scfa"] = production.scfa + " " + production.id.map(samples)
production["abbreviation"] = production.effector.str.replace("(EX_)|(_m)", "")
production = pd.merge(production, metabolites, on="abbreviation", how="left")
production.loc[production.fullName.isna(), "fullName"] = production.loc[
    production.fullName.isna(), "abbreviation"
]


###################################################################################################
production = production[production.type == "abundance"]

#print(len(production))

cmap = sns.color_palette()[0:2]
cmap = dict(zip(production.type.unique(), cmap))
production.fullName = production.fullName.apply(
    lambda s: s if len(s) < 24 else s[:24] + "..."
)
ty = production[["fullName", "type"]].drop_duplicates()
ty = pd.Series(ty.type.values, index=ty.fullName)
typecols = ty.map(cmap).rename("type")
production = production.sort_values(by="id")
mat = production.pivot_table(
    index="scfa", columns="fullName", values="elasticity", fill_value=0
)
#print(mat)
g = sns.clustermap(
    mat,
    cmap="seismic",
    vmin= -10,#-production.elasticity.abs().max(), ###################################################################
    vmax= 10,#production.elasticity.abs().max(),#########################################################################
    figsize=(36, 12),
    col_colors=typecols,
    yticklabels=True,
    xticklabels=True,
    row_cluster=False,
    cbar_kws={"fraction": 1.0},
)
for label in cmap:
    g.ax_col_dendrogram.bar(0, 0, color=cmap[label], label=label, linewidth=0)
g.ax_col_dendrogram.legend(loc="best", ncol=3, frameon=False)
g.ax_heatmap.set_xlabel("")
g.ax_heatmap.set_ylabel("")
cold = g.ax_col_dendrogram.get_position()
g.ax_col_dendrogram.set_position(
    [cold.x0, cold.y0, cold.width, cold.height * 5]
)
g.ax_row_dendrogram.set_visible(False)
g.cax.set_position([0.25, 0.5, 0.01, 0.5])
g.savefig("./figures/elasticities_scan_31_medium.png", dpi=300)

but = production[production.scfa.str.startswith("lactate")].sort_values(
    by="elasticity", ascending=False
)
#print(but.head(20))