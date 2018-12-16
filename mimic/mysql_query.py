#-*- encoding:utf-8 -*-
__author__ = ''
import pymysql

#程序说明：分别根据情况设置相应的是共有的基因还是共有的GO 还是公有的pathway



db = pymysql.connect("10.194.181.128","root","lyh123","dictionary")
cursor = db.cursor()
cursor.execute("select version()")
result = cursor.fetchall()


cursor.execute("select * from dis_coor")
dis_con_sig = cursor.fetchall()
t = 0
h = 0
discon = {}
f = open("D:\\dis_go_list.txt","w")


def fetch_con_gene(ICD9CM_1, ICD9CM_2):
    sql = "select  d.geneSymbol\
            from DisGeNET_all_gene_disease_pmid_associations as d, cui_to_icd as ci\
              where ci.ICD9CM = \"{icd}\" and ci.CUI = d.diseaseId".format(icd=ICD9CM_1)
    cursor.execute(sql)
    ICD9CM_1_genes = list(cursor.fetchall())
    sql = "select  d.geneSymbol\
            from DisGeNET_all_gene_disease_pmid_associations as d, cui_to_icd as ci\
              where  ci.ICD9CM = \"{icd}\" and ci.CUI = d.diseaseId".format(icd=ICD9CM_2)
    cursor.execute(sql)
    ICD9CM_2_genes = list(cursor.fetchall())
    con_gene = set(ICD9CM_1_genes) & set(ICD9CM_2_genes)
    return con_gene

def fetch_con_pathway(ICD9CM_1, ICD9CM_2):
    sql = "select  rp.pathway_id\
            from DisGeNET_all_gene_disease_pmid_associations as d, cui_to_icd as ci, reactome_pathway_gene as rp\
              where ci.ICD9CM = \"{icd}\" and ci.CUI = d.diseaseId and d.geneSymbol = rp.gene_symble".format(icd=ICD9CM_1)
    cursor.execute(sql)
    ICD9CM_1_genes = list(cursor.fetchall())
    sql = "select  rp.pathway_id\
            from DisGeNET_all_gene_disease_pmid_associations as d, cui_to_icd as ci, reactome_pathway_gene as rp\
              where ci.ICD9CM = \"{icd}\" and ci.CUI = d.diseaseId and d.geneSymbol = rp.gene_symble".format(icd=ICD9CM_2)
    cursor.execute(sql)
    ICD9CM_2_genes = list(cursor.fetchall())
    con_pathway = set(ICD9CM_1_genes) & set(ICD9CM_2_genes)
    return con_pathway

def fetch_con_go(ICD9CM_1, ICD9CM_2):
    sql = "select  gs.go_id\
            from DisGeNET_all_gene_disease_pmid_associations as d, cui_to_icd as ci, goid_gene_symb_id as gs\
              where  ci.ICD9CM = \"{icd}\" and ci.CUI = d.diseaseId  and d.geneSymbol = gs.hgnc_symbol".format(icd=ICD9CM_1)
    cursor.execute(sql)
    ICD9CM_1_genes = list(cursor.fetchall())
    sql = "select  gs.go_id\
            from DisGeNET_all_gene_disease_pmid_associations as d, cui_to_icd as ci, goid_gene_symb_id as gs\
              where  ci.ICD9CM = \"{icd}\" and ci.CUI = d.diseaseId  and d.geneSymbol = gs.hgnc_symbol".format(icd=ICD9CM_2)
    cursor.execute(sql)
    ICD9CM_2_genes = list(cursor.fetchall())
    con_go = set(ICD9CM_1_genes) & set(ICD9CM_2_genes)
    return con_go

try:
    for row in dis_con_sig:
        ICD9CM_1 = row[0]
        ICD9CM_2 = row[1]
        print(t)
        t = t + 1
        #con_gene = fetch_con_gene(ICD9CM_1=ICD9CM_1, ICD9CM_2=ICD9CM_2)
        #con_gene = fetch_con_pathway(ICD9CM_1=ICD9CM_1, ICD9CM_2=ICD9CM_2)
        con_gene = fetch_con_go(ICD9CM_1=ICD9CM_1, ICD9CM_2=ICD9CM_2)
        if len(con_gene):
            print("find {i}".format(i=h))
            h = h + 1
            con_gene = list(con_gene)
            con_gene = [gene[0] for gene in con_gene]
            c_m = ",".join(con_gene)
            discon[h] = [ICD9CM_1,ICD9CM_2,c_m]
        else:
            pass
    print("totle pair{sig},have common gene pair{hav}".format(sig=t,hav=h))

    for h,content in discon.items():
        f.write(str(content[0]))
        f.write("@@")
        f.write(str(content[1]))
        f.write("@@")
        f.write(str(content[2]))
        f.write("\n")
except:
    print("data base connect error!")
finally:
    db.close
    f.close()

