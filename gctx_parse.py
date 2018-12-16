

#package install

import pandas as pd
from cmapPy.pandasGEXpress import parse

inst_info = pd.read_csv("D:\\project\\expression\\GSE92743_Broad_GTEx_inst_info.txt", sep="\t")
#sig_info.columns
#vorinostat_ids = sig_info["sig_id"][sig_info["pert_iname"] == "vorinostat"]
print("number of samples treated with vorinostat:")
#len(vorinostat_ids)
from cmapPy.pandasGEXpress import parse
gene_info = parse("D:\\project\\expression\\GSE92743_Broad_GTEx_gene_info.txt", meta_only=True)

vorinostat_only_gctoo = parse("D:\\project\\expression\\no_meta_GTEx_L1000_level_3_q2norm_n3176x12320.gctx")
vorinostat_only_gctoo = parse("D:\\project\\GSE70138_Broad_LINCS_Level3_INF_mlr12k_n345976x12328.gctx")
vorinostat_only_gctoo.data_df.shape #yup!
dir(vorinostat_only_gctoo.data_df)
type(vorinostat_only_gctoo.data_df)
data = vorinostat_only_gctoo.data_df
data.to_csv("D:\\project\\b.csv")
