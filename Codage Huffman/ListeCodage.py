# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 16:18:56 2021

@author: gaeta
"""
class ListeCodage:
    
    def __init__(self,liste):
        self.liste=liste
        
    def rechercheCodage(self, charactere):
        for i in range(len(self.liste)):
            if self.liste[i].charactere==charactere:
                return self.liste[i].code
            
    def codageCharactere(self, charactere):
        #code un charactère
        return self.rechercheCodage(charactere)
    
    def codageLigne(self, ligne):
        #code l'ensemble des charactères d'une ligne
        code=''
        for char in ligne:
            code+= self.codageCharactere(char)
        return code
    
    def codageTexte(self, texte):
        #code l'ensemble des lignes d'un texte
        code=''
        for ligne in texte:
            code+= self.codageLigne(ligne)
        return code