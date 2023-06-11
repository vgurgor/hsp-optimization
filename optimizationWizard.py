import os
import sys
import SchoolScheduling

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
            print("--  1  --  HST Uygulamasından alınan txt ile optimizasyon yap                                                         --")
            print("------------------------------------------------------------------------------------------------------------------------")

        if(mission==''):
            mission = input('Yapılacak işlem kodunu girin: ')

        if(mission=='1'): 
            params = self.getDataFromTxt('')
            school = SchoolScheduling(params['days'], params['periods'], params['courses'], params['teachers'], params['classrooms'])
            school.optimize()

            # Sonuçları yazdırma
            school.print_results()

    def getDataFromTxt (self, txtFile=''):
        if(txtFile==''):
            txt = self.chooseTxt()
            with open("{}".format(txt)) as f:
                content = f.readlines()
            content = [x.strip() for x in content]
            if(len(content)==0):
                print("txt dosyasi bos")
                self.getDataFromTxt('')
            else:
                global_degerler = {}
                exec(content, global_degerler)

                return global_degerler
        else:
            with open("{}".format(txtFile)) as f:
                content = f.readlines()
            content = [x.strip() for x in content]
            if(len(content)==0):
                print("txt dosyasi bos")
                self.getDataFromTxt('')
            else:
                global_degerler = {}
                exec(content, global_degerler)

                return global_degerler
               
    def chooseTxt(self, isReturn=False):
        if(isReturn == False):
            folder = "input/"
            allFiles = os.listdir("{}".format(folder))
            txtFiles = filter(lambda x: x[-4:] == '.txt', allFiles)
            txtArray = []
            print("TXT DOSYALARI")
            s=0
            for i in txtFiles:
                txtArray.append("{}{}".format(folder,i))
                print("{} | {}".format(s,i))
                s = s+1

        txtCode = input('TXT kodu girin: ')

        try:
            return txtArray[int(txtCode)]
        except:
            print("Hatali txt kodu")
            self.chooseTxt(True)

OptimizationWizard();