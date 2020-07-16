import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})


print("reading")
train = pd.read_csv('./data/train_V2.csv')
print("read")

# data = train.copy()
# print("copied")
# data = data[data['boosts'] < 11]

# print("changed")
# f,ax1 = plt.subplots(figsize=(15, 5))
# sns.pointplot(x='boosts',y='winPlacePerc',data=data,color='blue',alpha=0.8)
# print("plotted")
# plt.xlabel('Number of Boost Items Used',fontsize = 15,color='blue')
# plt.ylabel('Win Percentage',fontsize = 15,color='blue')
# plt.title('Boosts vs Win Percentage',fontsize = 20,color='blue')
# plt.savefig('figures/BoostvWin_2.jpeg')
#
# print('generating vehicle destroys')
# f,ax = plt.subplots(figsize=(15, 5))
# sns.pointplot(x='vehicleDestroys',y='winPlacePerc',data=train,color='r',alpha=1)
# plt.title('Vehicles Destroyed vs Win Percentage',fontsize = 20,color='r')
# plt.xlabel('Number of Vehicles Destroyed',fontsize = 15,color='r')
# plt.ylabel('Win Percentage', color='r')
# plt.savefig('figures/Vehicle_Dest_vs_wins_V2.jpeg')

print('generating weapons')
print(train['weaponsAcquired'].dtypes)
train['weaponsAcquired'] = train[train['weaponsAcquired'] < train['weaponsAcquired'].quantile(0.99)]
print("deleted extras")
print(train['weaponsAcquired'].value_counts())
train['weapons_acquired'] = pd.cut(train['weaponsAcquired'], [-1, 0, 2, 5, 10, 20, 50, 100, train['weaponsAcquired'].max()], labels=['0 weapons','1-2 weapons', '3-5 weapons', '6-10 weapons', '11-20 weapons', '21-50 weapons', '51-100 weapons', '100+ weapons'])
plt.figure(figsize=(15,8))
sns.boxplot(x="weapons_acquired", y="winPlacePerc", data=train)
plt.title('Weapons Acquired vs Win Percentage',fontsize = 20,color='blue')
plt.savefig('figures/weaponsvswinplaceperc_V2.jpeg')
