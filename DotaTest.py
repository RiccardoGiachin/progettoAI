import Perceptron as pc
import VotedPerceptron as vp
import numpy as np
import pandas as p
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
print ("DOTA TEST")

y=[]
X=[]
Y=[]

dt=p.read_csv("datasets/dota2Train.csv")
dt.columns = ['E', 'cluster ID', 'game mode', 'game type','Anti-Mage','Axe','bane','Bane','Bloodseeker','Crystal Maiden','Drow Ranger','Earthshaker','Juggernaut','Mirana','Shadow Fiend','Morphling','Phantom Lancer','Puck','Pudge','Razor'

,'Sand King'

,'Storm Spirit'

,'Sven'

,'Tiny'

,'Vengeful Spirit'

,'Windranger'

,'Zeus'

,'Kunkka'

,'Lina'

,'Lich'

,'Lion'

,'Shadow Shaman'

,'Slardar'

,'Tidehunter'

,'Witch Doctor'

,'Riki'

,'Enigma'

,'Tinker'

,'Sniper'

,'Necrophos'

,'Warlock'

,'Beastmaster'

,'Queen of Pain'

,'Venomancer'

,'Faceless Void'

,'Skeleton King'

,'Death Prophet'

,'Phantom Assassin'

, 'Pugna'

,'Templar Assassin'

,'Viper'

,'Luna'

,'Dragon Knight'

,'Dazzle'

,'Clockwerk'

,'Leshrac'

,'Natures Prophet'

,'Lifestealer'

,'Dark Seer'

,'Clinkz'

,'Omniknight'

,'Enchantress'

,'Huskar'

,'Night Stalker'

,'Broodmother'

,'Bounty Hunter'

,'Weaver'

,'Jakiro'

,'Batrider'

,'Chen'

,'Spectre'

,'Doom'

,'Ancient Apparition'

,'Ursa'

,'Spirit Breaker'

,'Gyrocopter'

,'Alchemist'

,'Invoker'

,'Silencer'

,'Outworld Devourer'

,'Brewmaster'

,'Shadow Demon'

,'Lone Druid'

,'Chaos Knight'

,'Meepo'

,'Treant Protector'

,'Ogre Magi'

,'Undying'

,'Rubick'

,'Disruptor'

,'Nyx Assassin'

,'Naga Siren'

,'Keeper of the Light'

,'Wisp'

,'Visage'

,'Slark'

,'Medusa'

,'Troll Warlord'

,'Centaur Warrunner'

,'Magnus'

,'Timbersaw'

,'Bristleback'

,'Tusk'

,'Skywrath Mage'

,'Abaddon'

,'Elder Titan'

,'Legion Commander'

,'Ember Spirit'

,'Earth Spirit'

,'Abyssal Underlord'

,'Terrorblade'

,'Phoenix'

,'Techies'

,'Oracle'

,'Winter Wyvern'

,'Arc Warden', 'giack' ]

dtest = p.read_csv('datasets/dota2Test.csv')
dtest.columns = ['E', 'cluster ID', 'game mode', 'game type','Anti-Mage','Axe','bane','Bane','Bloodseeker','Crystal Maiden','Drow Ranger','Earthshaker','Juggernaut','Mirana','Shadow Fiend','Morphling','Phantom Lancer','Puck','Pudge','Razor'

,'Sand King'

,'Storm Spirit'

,'Sven'

,'Tiny'

,'Vengeful Spirit'

,'Windranger'

,'Zeus'

,'Kunkka'

,'Lina'

,'Lich'

,'Lion'

,'Shadow Shaman'

,'Slardar'

,'Tidehunter'

,'Witch Doctor'

,'Riki'

,'Enigma'

,'Tinker'

,'Sniper'

,'Necrophos'

,'Warlock'

,'Beastmaster'

,'Queen of Pain'

,'Venomancer'

,'Faceless Void'

,'Skeleton King'

,'Death Prophet'

,'Phantom Assassin'

, 'Pugna'

,'Templar Assassin'

,'Viper'

,'Luna'

,'Dragon Knight'

,'Dazzle'

,'Clockwerk'

,'Leshrac'

,'Natures Prophet'

,'Lifestealer'

,'Dark Seer'

,'Clinkz'

,'Omniknight'

,'Enchantress'

,'Huskar'

,'Night Stalker'

,'Broodmother'

,'Bounty Hunter'

,'Weaver'

,'Jakiro'

,'Batrider'

,'Chen'

,'Spectre'

,'Doom'

,'Ancient Apparition'

,'Ursa'

,'Spirit Breaker'

,'Gyrocopter'

,'Alchemist'

,'Invoker'

,'Silencer'

,'Outworld Devourer'

,'Brewmaster'

,'Shadow Demon'

,'Lone Druid'

,'Chaos Knight'

,'Meepo'

,'Treant Protector'

,'Ogre Magi'

,'Undying'

,'Rubick'

,'Disruptor'

,'Nyx Assassin'

,'Naga Siren'

,'Keeper of the Light'

,'Wisp'

,'Visage'

,'Slark'

,'Medusa'

,'Troll Warlord'

,'Centaur Warrunner'

,'Magnus'

,'Timbersaw'

,'Bristleback'

,'Tusk'

,'Skywrath Mage'

,'Abaddon'

,'Elder Titan'

,'Legion Commander'

,'Ember Spirit'

,'Earth Spirit'

,'Abyssal Underlord'

,'Terrorblade'

,'Phoenix'

,'Techies'

,'Oracle'

,'Winter Wyvern'

,'Arc Warden', 'giack' ]

#print dtest.head()

y = dt[['Tusk']]
Y_train = [1 if y.Tusk == 1 else -1 for y in y.itertuples()]

ytest = dtest[['Tusk']]
Y_test = [1 if y.Tusk == 1 else -1 for y in ytest.itertuples()]
X=(dt.iloc[:, 0:116])

#X_train, X_test, Y_train, Y_test = train_test_split(X, Y,test_size=0.2 , random_state=0) we do not use this because we already have a dataset divided in test and train

X_train = np.insert(np.array(dt), 0,1, axis=1)
X_test = np.insert(np.array(dtest), 0, 1, axis=1)

oPer = pc.Perceptron(0.25,2)
oPer.training(X_train, Y_train)

predY = []
predY = [oPer.guess(z) for z in X_test]
for z in X_test:
    predY.append(oPer.guess(z))
    asc = 100*accuracy_score([z in Y_test] ,[z in predY] )
    plt.subplot(212)
    plt.xlabel('numero di dati in Xtest')
    plt.ylabel('accuratezza')
    plt.plot(x=z, y=asc)
plt.show()


"""#cm = confusion_matrix(Y_test, predY)
#np.set_printoptions(precision=3)

print("accuracy of a layer: %.2f%%" % (100*accuracy_score(Y_test,predY)))

print

print("confusion matrix, no normalization")
print cm
print
print

print ('normalized confusion matrix')
print cm.astype('float') / cm.sum(axis = 1)[:, np.newaxis]
print
print


print(classification_report(Y_test, predY))


print("VOTED PERCEPTRON")

o_vper = vp.VotedPerceptron(0.25, 50)


wei_voted, i_voted, length_array = o_vper.training(X_train, Y_train)


wei_Y_vper = [o_vper.guess(z) for z in X_test]

accu = 100*accuracy_score(Y_test, wei_Y_vper)
print("accuracy of a layer voted: %.2f%%" % (accu))

cmv = confusion_matrix(Y_test, wei_Y_vper)
np.set_printoptions(precision = 3)

print

print("confusion matrix voted not normalized")
print cmv
print
print


print("normalized confusion matrix")
print cmv.astype('float') / cmv.sum(axis=1)[:, np.newaxis]
print
print



print(classification_report(Y_test, wei_Y_vper))"""
