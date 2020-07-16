import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
#
# print('generating heatmap')
train = pd.read_csv('./data/train_V2.csv')
# print(train['weaponsAcquired'].value_counts())
# f,ax = plt.subplots(figsize=(15, 15))
# sns.heatmap(train.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax, cmap="Blues")
# plt.savefig('figures/heatmap_2.jpeg')
# print('generated heatmap')

# print('generating kill')
# plt.figure(figsize=(15,8))
# sns.jointplot(x="winPlacePerc", y="killPlace", data=train)
# plt.title("Kill Place vs Win Percentage", loc='center')
# plt.savefig('figures/killPlace.jpeg')
#
print('generating walk')
f,ax1 = plt.subplots(figsize=(15, 5))
sns.jointplot(x="winPlacePerc", y="walkDistance",   data=train, height=10, ratio=3, color="r")
plt.savefig('figures/walk_to_win.jpeg')
#
print('generating travel')
f,ax1 = plt.subplots(figsize=(15, 5))
train['travel'] = train['walkDistance']+train['rideDistance']+train['swimDistance']
sns.jointplot(x="winPlacePerc", y="travel",  data=train, height=10, ratio=3, color="g")
plt.savefig('figures/travel_to_win.jpeg')
#
# print('generating Boosts')
# f,ax = plt.subplots(figsize=(15, 5))
# train['boosts'] = train[train['boosts'] < 11]
# print("deleted extras")
# sns.pointplot(x='boosts',y='winPlacePerc',data=train,color='c',alpha=1)
# print("plotted")
# plt.title('Boosts vs Win Percentage',fontsize = 20,color='blue')
# plt.xlabel('Number of Boost Items Used',fontsize = 15,color='c')
# plt.ylabel('Win Percentage', color='c')
# plt.savefig('figures/BoostvWin.jpeg')
#
# print('generating vehicle destroys')
# f,ax = plt.subplots(figsize=(15, 5))
# sns.pointplot(x='vehicleDestroys',y='winPlacePerc',data=train,color='r',alpha=1)
# plt.title('Vehicles Destroyed vs Win Percentage',fontsize = 20,color='r')
# plt.xlabel('Number of Vehicles Destroyed',fontsize = 15,color='r')
# plt.ylabel('Win Percentage', color='r')
# plt.savefig('figures/Vehicle_Dest_vs_wins.jpeg')
#
# print('generating weapons')
# train['weaponsAcquired'] = train[train['weaponsAcquired'] < train['weaponsAcquired'].quantile(0.99)]
# print("deleted extras")
# train['weapons_acquired'] = pd.cut(train['weaponsAcquired'], [-1, 0, 2, 5, 10, 20, 50, 100, train['weaponsAcquired'].max()], labels=['0 weapons','1-2 weapons', '3-5 weapons', '6-10 weapons', '11-20 weapons', '21-50 weapons', '51-100 weapons', '100+ weapons'])
# plt.figure(figsize=(15,8))
# sns.boxplot(x="weapons_acquired", y="winPlacePerc", data=train)
# plt.title('Weapons Acquired vs Win Percentage',fontsize = 20,color='blue')
# plt.savefig('figures/weaponsvswinplaceperc.jpeg')

# travel = train[['walkDistance', 'rideDistance', 'swimDistance', 'totalDistance', 'winPlacePerc']].copy()
# f,ax = plt.subplots(figsize=(15, 15))
# sns.heatmap(travel.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
# plt.savefig('figures/travel_heatmap.jpeg')
