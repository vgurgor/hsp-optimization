import os
import sys
import json
from SchoolScheduling import SchoolScheduling

class OptimizationWizard:
    def __init__(self):
        try:
            os.mkdir("output")
        except:
            a=1
        try:
            os.mkdir("input")
        except:
            a=1
        sys.setrecursionlimit(852963741)
        print("------------------------------------------------------------------------------------------------------------------------")
        print("--                                      HST Gurobi Optimizasyon Aracı                                                 --")
        print("------------------------------------------------------------------------------------------------------------------------")
            
        self.getMission()

    def getMission(self, mission='', isReturn=False):
        if(isReturn==False):
            print("")
            print("------------------------------------------------------------------------------------------------------------------------")
            print("-- KOD --                                       İŞLEM                                                                 --")
            print("------------------------------------------------------------------------------------------------------------------------")
            print("--  1  --  HST Uygulamasından alınan json ile optimizasyon yap                                                        --")
            print("------------------------------------------------------------------------------------------------------------------------")

        if(mission==''):
            mission = input('Yapılacak işlem kodunu girin: ')

        if(mission=='1'): 
            params = self.getDataFromJson('')
            
            school = SchoolScheduling(params['days'], params['periods'], params['courses'], params['teachers'], params['classrooms'])
            school.optimization()
            school.print_results()
            

    def getDataFromJson (self, jsonFile=''):
        if(jsonFile==''):
            jsonfile = self.chooseJson()
            with open(jsonfile) as f:
                content = json.load(f)
            return content
               
    def chooseJson(self, isReturn=False):
        if(isReturn == False):
            folder = "input/"
            allFiles = os.listdir("{}".format(folder))
            jsonFiles = filter(lambda x: x[-5:] == '.json', allFiles)
            jsonArray = []
            print("JSON DOSYALARI")
            s=0
            for i in jsonFiles:
                jsonArray.append("{}{}".format(folder,i))
                print("{} | {}".format(s,i))
                s = s+1

        jsonCode = input('JSON kodu girin: ')

        try:
            return jsonArray[int(jsonCode)]
        except:
            print("Hatali json kodu")
            self.chooseJson(True)

OptimizationWizard()