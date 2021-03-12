# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 08:26:15 2021

@author: gaetan
"""
import Alphabet
import Tree  
import ListeCodage

import os
print('veuillez déposer votre fichier texte à compresser dans le dossier contenant le code')
print("veuillez vérifier que les fichiers '<titre>_comp.bin' et '<titre>_freq.txt' n'existent pas")
print('quel est le titre de votre fichier ?')
titre = input()
fichier = open(titre + '.txt','r')
lignes = fichier.readlines()

#création des deux fichiers à produire
fichierCompresse = open(titre + '_comp.bin','x')
alphabet = open(titre + '_freq.txt', 'x')

#détermination de l'alphabet et des fréquences
alpha = Alphabet.Alphabet([])
alpha.liste = alpha.ajouterTexte(lignes)
alpha.liste = alpha.trierAlphabet()

#détermination du nombre total de charactères du texte
totalCharacteres = 0
for i in range(len(alpha.liste)):
    totalCharacteres+=alpha.liste[i][0]
    
#remplissage du fichier des fréquences
alphabet.write(str(len(alpha.liste))+'\n')
for i in alpha.liste:
    alphabet.write(i[1] + ' ' + str(i[0]) + '\n')

#réalisation de l'arbre de huffman
listeArbre = alpha.alphabetToTree()
arbre = Tree.Tree(0,'coucou')
arbre = arbre.huffman(listeArbre)

#codage du texte
code = arbre.codage('')
code = ListeCodage.ListeCodage(code)
texte = code.codageTexte(lignes)

#récupération du nombre de bits
bits=len(texte)

#écriture du fichier compressé
while len(texte)>8:
    fichierCompresse.write(texte[0:8]+'\n')
    texte = texte[8:len(texte)]
fichierCompresse.write(texte)

#fermeture des fichiers texte
alphabet.close()
fichier.close()
fichierCompresse.close()

#affichage du taux de compression
sizeCompresse = os.path.getsize(titre + '_comp.bin')
sizeAlphabet = os.path.getsize(titre + '_freq.txt')
sizeFichier = os.path.getsize(titre + '.txt')
taux = 1 - (sizeCompresse + sizeAlphabet) / sizeFichier
print('le taux de compression est :', taux)

#affichage du nombre moyen de bits de codage
print(bits/totalCharacteres)