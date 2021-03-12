# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 16:18:55 2021

@author: gaeta
"""
import Codage

class Tree:
    
    def __init__(self, valeur, charactere, fg=None, fd=None):
        self.valeur=valeur
        self.charactere=charactere
        self.fg=fg
        self.fd=fd
        
    def recherchePosition(self, liste):
        #cherche la position de la feuille dans la liste des feuilles pour que la liste des feuilles reste triée
        compteur=0
        while compteur<len(liste) and liste[compteur].valeur<=self.valeur:
            compteur+=1
        return compteur
        
    def replacement(self,liste):
        #place la feuille dans la liste pour que la liste reste triée
        liste.append(self)
        indice = self.recherchePosition(liste)
        frigo=self
        for i in range(indice,len(liste)):
            frigo,liste[i]=liste[i],frigo
        return liste
    
    def huffman(self,liste):
        #crée l'arbre de huffman 
        element1 = liste.pop(0)
        element2 = liste.pop(0)
        nouvelArbre = Tree( element1.valeur + element2.valeur, 'Node', element1, element2)
        if liste==[]:
            return nouvelArbre
        liste = nouvelArbre.replacement(liste)
        return self.huffman(liste)
        
    
    def codage(self,code):
        #donne sous forme de liste les codes de chaque lettre
        if self.charactere!='Node':
                return [Codage.Codage(self.charactere,code)]
        return self.fg.codage(code+'0') + self.fd.codage(code+'1')
    