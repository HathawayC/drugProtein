# coding:utf-8

import pandas as pd
import matplotlib.pylab as plt
import pdb
# table = pd.read_csv('../data/dpi1.csv')
# distribute = pd.read_csv('../data/dpi1_离散or连续.csv')
# # distribute = distribute[distribute['len']==1]
# # print ("', '").join(distribute['featrueName'])


# # ******************************************************************************************************
# # ************************************ 下面是检查值是不是唯一的 ********************************************
# # ******************************************************************************************************
# # for i in range(len(distribute['featrueName'])):
# #     arr = table[distribute['featrueName'][i]]
# #     print distribute['featrueName'][i]
# #     temp = str(float(distribute['values'][i].split('[')[1].split(']')[0]))
# #     print "temp:",temp
# #     for val in arr:
# #         if str(val) != temp:
# #             print val


# # ******************************************************************************************************
# # ************************************ 下面是离散值的分布 *************************************************
# # ******************************************************************************************************
# # distribute = distribute[(distribute['len']>1) & (distribute['len']<20)]
# # head = distribute['featrueName']

# # for h in head:
# #     print h
# #     t = sorted(table[h].values)
# #     x = range(len(t))
# #     plt.scatter(x,t,c='k')
# #     plt.title('distribution of '+ h)
# #     plt.show();


# # ******************************************************************************************************
# # ************************************ 下面是连续值的分布 *************************************************
# # ******************************************************************************************************
# distribute = distribute[distribute['len'] > 20]
# head = distribute['featrueName']
# print ("', '").join(head)

# # for h in head:
# #     print h
# #     t = sorted(table[h].values)
# #     x = range(len(t))
# #     plt.scatter(x,t,c='k')
# #     plt.title('distribution of '+ h)
# #     plt.show();


table = pd.read_csv('../data/drug_protein*encode_id.csv')
for h in ['protein_DPComp_WG', 'protein_DPComp_WQ', 'protein_MoreauBrotoAuto_FreeEnergy11', 'protein_Triad_173', 'protein_PAAC_23', 'protein_PAAC_1']:
    # for h in table.columns[500:]:
    print h
    t = sorted(table[h].values)
    # pdb.set_trace()
    x = range(len(t))
    plt.scatter(x, t, c='k')
    plt.annotate('-1 means missing', xy=(0, -1), xytext=(1000, -1))
    # plt.title('Distribution of ' + h)
    plt.title('Distribution of ' + h.split('_')
              [0] + ' ' + '_'.join(h.split('_')[1:]))
    plt.xlabel('value')
    plt.ylabel('order of entiry')
    # table[h].plot(kind='kde', label='asdf',
    #               title='Distribution of %s' % h.replace('_', ' '))
    plt.show()
