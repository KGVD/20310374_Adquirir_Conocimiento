# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 19:02:11 2023

@author: LoboM
"""

import json
from difflib import get_close_matches

def Cargar_Basededatos(file_path: str)->dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
        return data
        
def Guardar_Basededatos(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
        
def Buscar(user_question: str, question: list[str])-> str or None:
    matches: list=get_close_matches(user_question, question, n=1, cutoff=0.6)
    return matches[0] if matches else None 

def Respuesta(question: str, knowledge_base: dict)-> str or None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
        
def Robot():
    knowledge_base: dict= Cargar_Basededatos('knowledge_base.json')
    
    while True:
        user_input: str= input('Tu:')
        
        if user_input.lower()=='quit':
            break

        best_match: str or None=Buscar(user_input, [q["question"] for q in knowledge_base["questions"]]) 
        
        if best_match:
            answer:str=Respuesta(best_match, knowledge_base)
            print(f'Bot: {answer}')   
        else:
            print('Bot: No conosco la respuesta, ¿Podrias enseñarme?')
            new_answer: str= input('Escribe la respuesta a la pregunta o escribe "S" para saltar: ')
            
            if new_answer.lower()!='S':
                knowledge_base["questiones"].append({"question":user_input, "answer": new_answer})
                Guardar_Basededatos('knowledge_base.json', knowledge_base)
                print('Bot: Gracias, mi conocimiento se expande')
                
                
if __name__ == '__main__':
    print('Bienvenido, oprime "R" para salir')
    Robot()        
        
        
            