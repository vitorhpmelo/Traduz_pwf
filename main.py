#%%

import numpy as np
import pandas as pd


#DBAR Dados de barras
#DLIN Dados de linhas
#DCSC Leitura dos dados de CSC (de para)
#DCNV conversor CA-CC
#DELO Dados de ELO
#DTPF o controle de tensão por variação automática de tap (CTAP).
#DCTR dados complementares de transformadores (de para)
#DCER Leitura dos dados de compensador estático de reativos.


fname="arquivo.PWF"

with open(fname,'r') as f:
    lines=f.readlines()

# %% encontra DBAR
i=0
for line in lines:
    ind=line.find("DBAR")
    if ind==0:
        break
    i=i+1
# %%
inicio=i
for line in lines[inicio:]:
    ind=line.find("99999\n")
    if ind==0:
        break
    i=i+1
fim=i+1
# %%

DBARlines=lines[inicio:fim].copy()


# %% Encontra DLIN
i=0
for line in lines:
    ind=line.find("DLIN")
    if ind==0:
        break
    i=i+1
# %%
inicio=i
for line in lines[inicio:]:
    ind=line.find("99999\n")
    if ind==0:
        break
    i=i+1
fim=i+1

DLINlines=lines[inicio:fim].copy()



#%% Bloco de leitura do DBAR

lstnum=[]
lstop=[]
lstestado=[]
lsttipo=[]
lstDGBT=[]
lstnome=[]
lstDGLT=[]
lstV=[]
lstteta=[]
lstGeracaoativa=[]
lstGeracaoreativa=[]
lstGeracaReaMin=[]
lstGeracaReaMax=[]
lstBarraContro=[]
lstCargaAtiva=[]
lstCargaReativa=[]
lstCapacitor=[]
lstArea=[]
lstVf=[]
lstM=[]
for line in DBARlines[2:-1]:
    num=line[0:5]
    operacao=line[5]
    estado=line[6]
    tipo=line[7]
    DGBT=line[8:10]
    nome=line[10:22]
    DGLT=line[22:24]
    V=line[24:28]
    teta=line[28:32]
    Geracaoativa=line[32:37]
    Geracaoreativa=line[37:42]
    GeracaReaMin=line[42:47]
    GeracaReaMax=line[47:52]
    BarraContro=line[52:58]
    CargaAtiva=line[58:63]
    CargaReativa=line[63:68]
    Capacitor=line[68:73]
    Area=line[73:76]
    Vf=line[76:80]
    M=line[80:81]
    
    lstnum.append(num)
    lstop.append(operacao)
    lstestado.append(estado)
    lsttipo.append(tipo)
    lstDGBT.append(DGBT)
    lstnome.append(nome)
    lstDGLT.append(DGLT)
    lstV.append(V)
    lstteta.append(teta)
    lstGeracaoativa.append(Geracaoativa)
    lstGeracaoreativa.append(Geracaoreativa)
    lstGeracaReaMin.append(GeracaReaMin)
    lstGeracaReaMax.append(GeracaReaMax)
    lstBarraContro.append(BarraContro)
    lstCargaAtiva.append(CargaAtiva)
    lstCargaReativa.append(CargaReativa)
    lstCapacitor.append(Capacitor)
    lstArea.append(Area)
    lstVf.append(Vf)
    lstM.append(M)



dDBAR={"num":lstnum,"op":lstop,"estado":lstestado,"tipo":lsttipo,\
      "DGBT":lstDGBT,"nome":lstnome,"DGLT":lstDGLT,"V":lstV,"teta":lstteta,\
        "GeracaoAtiva":lstGeracaoativa,"GeracaoReativa":lstGeracaoreativa,"GeracaoReativaMin":lstGeracaReaMin,\
        "GeracaoReativaMax":lstGeracaReaMax,"BarraContro":lstBarraContro,"CargaAtiva":lstCargaAtiva,\
        "CargaReativa":lstCargaReativa,"Capacitor/reator":lstCapacitor,"Area":lstArea,"Vf":lstVf,"M":lstM}
# %%

dfDBAR=pd.DataFrame(data=dDBAR)
dfDBAR.to_csv("DBAR.csv",index=None)
# %%

