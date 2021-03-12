# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 16:18:54 2021

@author: gaeta
"""
import Tree

class Alphabet:
    
    def __init__(self,liste):
        self.liste = liste
        
    def ajouterChar(self,char):
        #ajoute un charactère à l'alphabet
        boole=False
        for i in range(len(self.liste)):
            if self.liste[i][1]==char:
                self.liste[i][0] = self.liste[i][0]+1
                boole=True
        if not boole:
            self.liste.append([1,char])
        return self.liste
    
    def ajouterLigne(self, ligne):
        #ajoute l'ensemble des charactères d'une ligne à l'alphabet
        for char in ligne:
            self.liste = self.ajouterChar(char)
        return self.liste
    
    def ajouterTexte(self,texte):
        #ajoute l'ensemble des charactères de l'ensemble des lignes d'un texte
        for ligne in texte:
            self.liste=self.ajouterLigne(ligne)
        return self.liste
    
    def trierAlphabet(self):
        #trie l'alphabet du plus petit nombre d'occurences au plus grand
        self.liste.sort()
        return self.liste
    
    def alphabetToTree(self):
        #transforme chacune des lettres de l'alphabet en feuille
        for i in range(len(self.liste)):
            self.liste[i]=Tree.Tree(self.liste[i][0],self.liste[i][1])
        return self.liste