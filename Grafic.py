import matplotlib.pyplot as plt
import numpy as np
import pandas as p
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import Perceptron as pc
import VotedPerceptron as vpc

def PokerPlotPer():
    y = []
    X = []
    Y = []
    print(" POKER HAND ")
    ph = p.read_csv('datasets/pokerhands.csv')
    ph.columns = ['type1', 'card1', 'type2', 'card2', 'type3', 'card3',
                  'type4', 'card4', 'type5', 'card5', 'typeofhand']
    y = ph[['card1']]
    Y = [1 if fy.card1 != 1 else -1 for fy in y.itertuples()]
    X = (ph.iloc[:, 0:10])

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)
    X_train = np.insert(np.array(X_train), 0, 1, axis=1)
    X_test = np.insert(np.array(X_test), 0, 1, axis=1)

    arrayPer = []
    cont = []
    arrayV=[]
    for i in range(0, 50, 5):
        o_per = pc.Perceptron(0.25, i)
        o_per.training(X_train, Y_train)
        o_vper = vpc.VotedPerceptron(0.25, i)
        o_vper.training(X_train, Y_train)
        wei_Y_per = [o_per.guess(z) for z in X_test]
        wei_Y_vper = [o_vper.guess(z) for z in X_test]
        acc = 100 * accuracy_score(Y_test, wei_Y_per)
        vacc = 100*accuracy_score(Y_test, wei_Y_vper)
        print acc
        print vacc
        arrayPer.append(acc)
        arrayV.append(vacc)
        cont.append(i)
    plt.title('Poker Test')
    plt.ylabel('accuracy')
    plt.xlabel('epochs')
    plt.plot(cont, arrayV, color='b')
    plt.plot(cont, arrayPer, color='r')
    plt.show()

def AirQualityplot():
    y = []
    X = []
    Y = []
    print(" AIR QUALITY")
    ph = p.read_csv('datasets/AirQualityUCI.csv')
    ph.columns = ['date', 'time', 'CO(GT)', 'PT08', 'NMHC', 'C6H6', 'PT08.S2', 'NOx', 'PT08.S3', 'NO2', 'PT08.S4',
                  'PT08.S5', 'T', 'RH', 'AH']
    y = ph[['T']]
    Y = [1 if fy.T == 0 else -1 for fy in y.itertuples()]
    X = (ph.iloc[:, 0:14])

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)
    X_train = np.insert(np.array(X_train), 0, 1, axis=1)
    X_test = np.insert(np.array(X_test), 0, 1, axis=1)
    arrayPer = []
    cont = []
    arrayV = []
    for i in range(0, 50,5):
        o_per = pc.Perceptron(0.25, i)
        o_per.training(X_train, Y_train)
        o_vper = vpc.VotedPerceptron(0.25, i)
        o_vper.training(X_train, Y_train)
        wei_Y_per = [o_per.guess(z) for z in X_test]
        wei_Y_vper = [o_vper.guess(z) for z in X_test]
        acc = 100 * accuracy_score(Y_test, wei_Y_per)
        vacc = 100 * accuracy_score(Y_test, wei_Y_vper)
        print acc
        print vacc
        arrayPer.append(acc)
        arrayV.append(vacc)
        cont.append(i)
    plt.title('Air Quality Test')
    plt.ylabel('accuracy')
    plt.xlabel('epochs')
    plt.plot(cont, arrayV, color='b')
    plt.plot(cont, arrayPer, color='r')
    plt.show()

def Dota2Plot():
    y = []
    X = []
    Y = []

    dt = p.read_csv("datasets/dota2Train.csv")
    dt.columns = ['E', 'cluster ID', 'game mode', 'game type', 'Anti-Mage', 'Axe', 'bane', 'Bane', 'Bloodseeker',
                  'Crystal Maiden', 'Drow Ranger', 'Earthshaker', 'Juggernaut', 'Mirana', 'Shadow Fiend', 'Morphling',
                  'Phantom Lancer', 'Puck', 'Pudge', 'Razor'

        , 'Sand King'

        , 'Storm Spirit'

        , 'Sven'

        , 'Tiny'

        , 'Vengeful Spirit'

        , 'Windranger'

        , 'Zeus'

        , 'Kunkka'

        , 'Lina'

        , 'Lich'

        , 'Lion'

        , 'Shadow Shaman'

        , 'Slardar'

        , 'Tidehunter'

        , 'Witch Doctor'

        , 'Riki'

        , 'Enigma'

        , 'Tinker'

        , 'Sniper'

        , 'Necrophos'

        , 'Warlock'

        , 'Beastmaster'

        , 'Queen of Pain'

        , 'Venomancer'

        , 'Faceless Void'

        , 'Skeleton King'

        , 'Death Prophet'

        , 'Phantom Assassin'

        , 'Pugna'

        , 'Templar Assassin'

        , 'Viper'

        , 'Luna'

        , 'Dragon Knight'

        , 'Dazzle'

        , 'Clockwerk'

        , 'Leshrac'

        , 'Natures Prophet'

        , 'Lifestealer'

        , 'Dark Seer'

        , 'Clinkz'

        , 'Omniknight'

        , 'Enchantress'

        , 'Huskar'

        , 'Night Stalker'

        , 'Broodmother'

        , 'Bounty Hunter'

        , 'Weaver'

        , 'Jakiro'

        , 'Batrider'

        , 'Chen'

        , 'Spectre'

        , 'Doom'

        , 'Ancient Apparition'

        , 'Ursa'

        , 'Spirit Breaker'

        , 'Gyrocopter'

        , 'Alchemist'

        , 'Invoker'

        , 'Silencer'

        , 'Outworld Devourer'

        , 'Brewmaster'

        , 'Shadow Demon'

        , 'Lone Druid'

        , 'Chaos Knight'

        , 'Meepo'

        , 'Treant Protector'

        , 'Ogre Magi'

        , 'Undying'

        , 'Rubick'

        , 'Disruptor'

        , 'Nyx Assassin'

        , 'Naga Siren'

        , 'Keeper of the Light'

        , 'Wisp'

        , 'Visage'

        , 'Slark'

        , 'Medusa'

        , 'Troll Warlord'

        , 'Centaur Warrunner'

        , 'Magnus'

        , 'Timbersaw'

        , 'Bristleback'

        , 'Tusk'

        , 'Skywrath Mage'

        , 'Abaddon'

        , 'Elder Titan'

        , 'Legion Commander'

        , 'Ember Spirit'

        , 'Earth Spirit'

        , 'Abyssal Underlord'

        , 'Terrorblade'

        , 'Phoenix'

        , 'Techies'

        , 'Oracle'

        , 'Winter Wyvern'

        , 'Arc Warden', 'giack']

    dtest = p.read_csv('datasets/dota2Test.csv')
    dtest.columns = ['E', 'cluster ID', 'game mode', 'game type', 'Anti-Mage', 'Axe', 'bane', 'Bane', 'Bloodseeker',
                     'Crystal Maiden', 'Drow Ranger', 'Earthshaker', 'Juggernaut', 'Mirana', 'Shadow Fiend',
                     'Morphling', 'Phantom Lancer', 'Puck', 'Pudge', 'Razor'

        , 'Sand King'

        , 'Storm Spirit'

        , 'Sven'

        , 'Tiny'

        , 'Vengeful Spirit'

        , 'Windranger'

        , 'Zeus'

        , 'Kunkka'

        , 'Lina'

        , 'Lich'

        , 'Lion'

        , 'Shadow Shaman'

        , 'Slardar'

        , 'Tidehunter'

        , 'Witch Doctor'

        , 'Riki'

        , 'Enigma'

        , 'Tinker'

        , 'Sniper'

        , 'Necrophos'

        , 'Warlock'

        , 'Beastmaster'

        , 'Queen of Pain'

        , 'Venomancer'

        , 'Faceless Void'

        , 'Skeleton King'

        , 'Death Prophet'

        , 'Phantom Assassin'

        , 'Pugna'

        , 'Templar Assassin'

        , 'Viper'

        , 'Luna'

        , 'Dragon Knight'

        , 'Dazzle'

        , 'Clockwerk'

        , 'Leshrac'

        , 'Natures Prophet'

        , 'Lifestealer'

        , 'Dark Seer'

        , 'Clinkz'

        , 'Omniknight'

        , 'Enchantress'

        , 'Huskar'

        , 'Night Stalker'

        , 'Broodmother'

        , 'Bounty Hunter'

        , 'Weaver'

        , 'Jakiro'

        , 'Batrider'

        , 'Chen'

        , 'Spectre'

        , 'Doom'

        , 'Ancient Apparition'

        , 'Ursa'

        , 'Spirit Breaker'

        , 'Gyrocopter'

        , 'Alchemist'

        , 'Invoker'

        , 'Silencer'

        , 'Outworld Devourer'

        , 'Brewmaster'

        , 'Shadow Demon'

        , 'Lone Druid'

        , 'Chaos Knight'

        , 'Meepo'

        , 'Treant Protector'

        , 'Ogre Magi'

        , 'Undying'

        , 'Rubick'

        , 'Disruptor'

        , 'Nyx Assassin'

        , 'Naga Siren'

        , 'Keeper of the Light'

        , 'Wisp'

        , 'Visage'

        , 'Slark'

        , 'Medusa'

        , 'Troll Warlord'

        , 'Centaur Warrunner'

        , 'Magnus'

        , 'Timbersaw'

        , 'Bristleback'

        , 'Tusk'

        , 'Skywrath Mage'

        , 'Abaddon'

        , 'Elder Titan'

        , 'Legion Commander'

        , 'Ember Spirit'

        , 'Earth Spirit'

        , 'Abyssal Underlord'

        , 'Terrorblade'

        , 'Phoenix'

        , 'Techies'

        , 'Oracle'

        , 'Winter Wyvern'

        , 'Arc Warden', 'giack']

    # print dtest.head()

    y = dt[['Tusk']]
    Y_train = [1 if y.Tusk == 1 else -1 for y in y.itertuples()]

    ytest = dtest[['Tusk']]
    Y_test = [1 if y.Tusk == 1 else -1 for y in ytest.itertuples()]
    X = (dt.iloc[:, 0:116])

    X_train = np.insert(np.array(dt), 0, 1, axis=1)
    X_test = np.insert(np.array(dtest), 0, 1, axis=1)
    arrayPer = []
    arrayV = []
    cont =[]
    for i in range(0, 50,5):
        o_per = pc.Perceptron(0.25, i)
        o_per.training(X_train, Y_train)
        o_vper = vpc.VotedPerceptron(0.25, i)
        o_vper.training(X_train, Y_train)
        wei_Y_per = [o_per.guess(z) for z in X_test]
        wei_Y_vper = [o_vper.guess(z) for z in X_test]
        acc = 100 * accuracy_score(Y_test, wei_Y_per)
        vacc = 100 * accuracy_score(Y_test, wei_Y_vper)
        print acc
        print vacc
        arrayPer.append(acc)
        arrayV.append(vacc)
        cont.append(i)
    plt.title('Dota Test')
    plt.ylabel('accuracy')
    plt.xlabel('epochs')
    plt.plot(cont, arrayV, color='b')
    plt.plot(cont, arrayPer, color='r')
    plt.show()


