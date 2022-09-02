from pathlib import Path
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import NearestNeighbors, KNeighborsClassifier
import matplotlib.pylab as plt
import seaborn as sns 
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import os

class modeloPacientes():
    def __init__(self):
        self.traductor = []
        self.scaler = StandardScaler() #para Feature scaling
        self.knn = KNeighborsClassifier(n_neighbors=9)
    
    #funcion donde se creara la data
    def entrenar(self):
        cwd = os.getcwd()
        pacientes =  pd.read_csv(f'{cwd}/dataFinal.csv', sep=';', header=None)
        pacientesOriginales =  pd.read_csv(f'{cwd}/dataFinal.csv', sep=';', header=None)
        pacientes.columns = ['SEXO','ORIENTACION SEXUAL','IDENTIDAD GENERO','EDAD AÑOS','APORTA','AUTOIDENTIDAD PACIENTE','TIPO DE BONO PACIENTE','GP 1','PREVENCION','MORBILIDAD','CONDICION DE DIAGNOSTICO','CODIGO CIE 10']
        pacientesOriginales.columns = ['SEXO','ORIENTACION SEXUAL','IDENTIDAD GENERO','EDAD AÑOS','APORTA','AUTOIDENTIDAD PACIENTE','TIPO DE BONO PACIENTE','GP 1','PREVENCION','MORBILIDAD','CONDICION DE DIAGNOSTICO','CODIGO CIE 10']
        pacientes = pacientes.iloc[1:,:]
        pacientesOriginales = pacientesOriginales.iloc[1:]
        
        # poner todos en minusculas
        for x in range(len(pacientes.columns)):    
            for i in range(len(pacientes.iloc[:,0])):
                pacientes.iloc[i,x] = pacientes.iloc[i,x].lower() 
                pacientesOriginales.iloc[i,x] = pacientesOriginales.iloc[i,x].lower() 
                
        #codificacion de la data
        label_encoder = [] 
        for columna, valor in enumerate(pacientes.iloc[0,:]):    
            if valor.isdigit() and int(valor) != 0: # para la columna 9 y 10 uqe tienen un 0 como primer valor
                pacientes.iloc[:,columna] = pacientes.iloc[:,columna].astype(int) # cambio de tipo de dato para edad y casteo
                for t in range(len(pacientes.iloc[:,columna])):
                    pacientes.iloc[t,columna] = int(pacientes.iloc[t,columna])
            else:
                label_encoder.append(preprocessing.LabelEncoder()) #creacion de instancia de label enconder
                pacientes.iloc[:,columna] = label_encoder[-1].fit_transform(pacientes.iloc[:,columna]) # se codifica toda la columna
                pacientes.iloc[:,columna].astype(int)
                
        #creacion de diccionario 
        dic = {}   
        for columna in range(len(pacientes.columns)):
            for x in range(len(pacientes.iloc[:,columna].unique())):
                dic[pacientes.iloc[:,columna].unique()[x]] = pacientesOriginales.iloc[:,columna].unique()[x] 
            self.traductor.append(dic)
            dic = {}       
            
        #desarrollo del modelo
        X = pacientes.drop(['CODIGO CIE 10'], axis=1)
        y = pacientes['CODIGO CIE 10']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
        # Feature scaling
        cols = X_train.columns
        X_train = self.scaler.fit_transform(X_train)
        X_test = self.scaler.transform(X_test)
        X_train = pd.DataFrame(X_train, columns=[cols])
        X_test = pd.DataFrame(X_test, columns=[cols])
        #creacion de modelo KNN
        self.knn.fit(X_train, y_train)

    def predecir(self, nuevaObservacion):
        #transforma a minusculas
        for x in range(len(nuevaObservacion)):
            nuevaObservacion[x] = nuevaObservacion[x].lower()
        #aplicar transformaciones
        for x in range(11):
            for i in self.traductor[x]:
                if(x != 3):
                    if self.traductor[x][i] == nuevaObservacion[x]:
                        nuevaObservacion[x] = int(i)
                else:
                    nuevaObservacion[x]  = int(nuevaObservacion[x])
                    
        #escalado de los datos
        nuevaDatafeature = pd.DataFrame([{'SEXO':nuevaObservacion[0],
                                          'ORIENTACION SEXUAL':nuevaObservacion[1],
                                          'IDENTIDAD GENERO':nuevaObservacion[2],
                                          'EDAD AÑOS':nuevaObservacion[3],
                                          'APORTA':nuevaObservacion[4],
                                          'AUTOIDENTIDAD PACIENTE':nuevaObservacion[5],
                                          'TIPO DE BONO PACIENTE':nuevaObservacion[6],
                                          'GP 1':nuevaObservacion[7],
                                          'PREVENCION':nuevaObservacion[8],
                                          'MORBILIDAD':nuevaObservacion[9],
                                          'CONDICION DE DIAGNOSTICO':nuevaObservacion[10]}])
        nuevaDatafeature = pd.DataFrame(self.scaler.transform(nuevaDatafeature),columns = ['SEXO','ORIENTACION SEXUAL','IDENTIDAD GENERO','EDAD AÑOS','APORTA','AUTOIDENTIDAD PACIENTE','TIPO DE BONO PACIENTE','GP 1','PREVENCION','MORBILIDAD','CONDICION DE DIAGNOSTICO'])
        return self.traductor[11][self.knn.predict(nuevaDatafeature)[0]]
