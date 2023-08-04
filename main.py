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


def criaDBAR(lines):
    i=0
    for line in lines:
        ind=line.find("DBAR")
        if ind==0:
            break
        i=i+1

    inicio=i
    for line in lines[inicio:]:
        ind=line.find("99999\n")
        if ind==0:
            break
        i=i+1
    fim=i+1

    DBARlines=lines[inicio:fim].copy()


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


    dfDBAR=pd.DataFrame(data=dDBAR)
    dfDBAR.to_csv("DBAR.csv",index=None)
    return dfDBAR

def criaDLIN(lines):
    i=0
    for line in lines:
        ind=line.find("DLIN")
        if ind==0:
            break
        i=i+1

    inicio=i
    for line in lines[inicio:]:
        ind=line.find("99999\n")
        if ind==0:
            break
        i=i+1
    fim=i+1

    DLINlines=lines[inicio:fim].copy()


    lstde=[]
    lstde_ligado=[]
    lstop=[]
    lstpara_ligado=[]
    lstpara=[]
    lstcircuito=[]
    lstestado=[]
    lstproprietario=[]
    lstresistencia=[]
    lstreatancia=[]
    lstsuceptancia=[]
    lsttap=[]
    lsttap_min=[]
    lsttap_max=[]
    lstdefasagem=[]
    lstbarracontrolad=[]
    lstcapacidadenominal=[]
    lstcapacidadeememergencia=[]
    lstnumerodetaps=[]
    lstcapacidadedeequipamento=[]






    for line in DLINlines[2:-1]:
        de=line[0:5] # caracteres 1-05 do DLIN
        de_ligado=line[5] # caractere 6 do DLIN
        op= line[7] # caractere 8
        para_ligado=line[9] # caractere 10
        para=line[10:15] # caractere 11-15
        circuito=line[15:17] # caractere 16-17
        estado=line[17] # caractere 18
        proprietario=line[18] # caractere 19
        resistencia=line[20:26] # caractere 21-26
        reatancia=line[26:32] #caractere 27-32
        suceptancia=line[32:38] # caractere 33-38
        tap=line[38:43] # caractere 39-43
        tap_min=line[43:48] # caractere 44-48
        tap_max=line[48:53] # caractee 49-53
        defasagem=line[53:58] # caractere 54-58
        barracontrolad=line[58:64] # caractere 59-64
        capacidadenominal=line[64:68] # caracere 65-68
        capacidadeememergencia=line[68:72] # caractere 69-72
        numerodetaps=line[72:74] # caractere 73-74 
        capacidadedeequipamento=line[74:78] # caractere 75-78

        lstde.append(de)
        lstde_ligado.append(de_ligado)
        lstop.append(op)
        lstpara_ligado.append(para_ligado)
        lstpara.append(para)
        lstcircuito.append(circuito)
        lstestado.append(estado)
        lstproprietario.append(proprietario)
        lstresistencia.append(resistencia)
        lstreatancia.append(reatancia)
        lstsuceptancia.append(suceptancia)
        lsttap.append(tap)
        lsttap_min.append(tap_min)
        lsttap_max.append(tap_max)
        lstdefasagem.append(defasagem)
        lstbarracontrolad.append(barracontrolad)
        lstcapacidadenominal.append(capacidadenominal)
        lstcapacidadeememergencia.append(capacidadeememergencia)
        lstnumerodetaps.append(numerodetaps)
        lstcapacidadedeequipamento.append(capacidadedeequipamento)

    dDLIN={"de":lstde,"ligado_de":lstde_ligado,"op":lstop,\
        "ligado_para":lstpara_ligado,"para":lstpara,"circuito":lstcircuito,"estado":lstestado,"prop":lstproprietario,\
            "r":lstresistencia,"x":lstreatancia,"bsh":lstsuceptancia,\
            "tap":lsttap,"tapmin":lsttap_min,"tapmax":lsttap_max,"defasagem":lstdefasagem,\
            "barracontrolada":lstbarracontrolad,"Capacidadenom":lstcapacidadenominal,"CapacidadeEmergencia":lstcapacidadeememergencia\
            ,"NumeroTaps":lstnumerodetaps,"CapacidadeEquipa":lstcapacidadedeequipamento}

    dfDLIN=pd.DataFrame(data=dDLIN)

    dfDLIN.to_csv("DLIN.csv",index=None)
    return dfDLIN

def criaDCSC(lines):
    i=0
    for line in lines:
        ind=line.find("DCSC")
        if ind==0:
            break
        i=i+1

    inicio=i
    for line in lines[inicio:]:
        ind=line.find("99999\n")
        if ind==0:
            break
        i=i+1
    fim=i+1

    DCSClines=lines[inicio:fim].copy()


    lstde=[]
    lstop=[]
    lstpara=[]
    lstcircuito=[]
    lstestado=[]
    lstpropietario=[]
    lstbypass=[]
    lstvalmin=[]
    lstvalmax=[]
    lstvalini=[]
    lstcontrole=[]
    lstvalesp=[]
    lstextremidademed=[]
    lstnumestagio=[]



    for line in DCSClines[2:-1]:
        de=line[0:5] # barra de 1-5
        op=line[6] # op 7
        para=line[9:14] # para 10-14
        circuito=line[14:16] # circuito 15-16
        estado=line[16] # estado 17
        propietario=line[17] # propietario 18
        bypass=line[18] #bypass 19
        valmin=line[25:31] # valor min 26-31
        valmax=line[31:37] # valor max 32-37 
        valini=line[37:43] # valor ini 38-43
        controle=line[43] # control 44
        valesp=line[45:51] # valor esp 46-51
        extremidademed=line[52:57] # extrem med 53-57
        numestagio=line[57:60] # N estagios 58-60


        lstde.append(de)
        lstop.append(op)
        lstpara.append(para)
        lstcircuito.append(circuito)
        lstestado.append(estado)
        lstpropietario.append(propietario)
        lstbypass.append(bypass)
        lstvalmin.append(valmin)
        lstvalmax.append(valmax)
        lstvalini.append(valini)
        lstcontrole.append(controle)
        lstvalesp.append(valesp)
        lstextremidademed.append(extremidademed)
        lstnumestagio.append(numestagio)



    dDCSC={"de":lstde,"op":lstop,"para":lstpara,\
        "circuito":lstcircuito,"estado":lstestado,"propietario":lstpropietario,"bypass":lstbypass,\
            "valmin":lstvalmin,"valmax":lstvalmax,"valini":lstvalini,\
            "modocontrol":lstcontrole,"valesp":lstvalesp,"extremidademed":lstextremidademed,"NumeEstag":lstnumestagio}

    dfDCSC=pd.DataFrame(data=dDCSC)
    dfDCSC.to_csv("DCSC.csv")
    return dfDCSC

def criaDCTR(lines):
    i=0
    for line in lines:
        ind=line.find("DCTR")
        if ind==0:
            break
        i=i+1

    inicio=i
    for line in lines[inicio:]:
        ind=line.find("99999\n")
        if ind==0:
            break
        i=i+1
    fim=i+1

    DCTRlines=lines[inicio:fim].copy()


    lstde=[]
    lstop=[]
    lstpara=[]
    lstcircuit=[]
    lstVmin=[]
    lstVmax=[]
    lsttipocontrole=[]
    lstmodocontrole=[]
    lstfasemin=[]
    lstfasemax=[]
    lsttipocontrole2=[]
    lstvalesp=[]
    lstextremmed=[]

    for line in DCTRlines[2:-1]:
        de=line[0:5] # barra de 1-5
        op=line[6] #operacao 07
        para=line[8:13] # barra para 09-13
        circuit=line[14:16] # circuito 15-16
        Vmin=line[17:21] # tensao minima 18-21
        Vmax=line[22:26] #tensao maxima 23-26
        tipocontrole=line[27] #tipo de controle 28
        modocontrole=line[29] # modo de controle 30
        fasemin=line[31:37] # fase minima 32-37
        fasemax=line[38:44] # fase maximna 39-44
        tipocontrole2=line[45] # tipo de controle 46
        valesp=line[47:53] # valor espec 48-53
        extremmed=line[54:59] # extremidade de med 55-59

        lstde.append(de)
        lstop.append(op)
        lstpara.append(para)
        lstcircuit.append(circuit)
        lstVmin.append(Vmin)
        lstVmax.append(Vmax)
        lsttipocontrole.append(tipocontrole)
        lstmodocontrole.append(modocontrole)
        lstfasemin.append(fasemin)
        lstfasemax.append(fasemax)
        lsttipocontrole2.append(tipocontrole2)
        lstvalesp.append(valesp)
        lstextremmed.append(extremmed)


    dCTR={"de":lstde, "op":lstop, "para":lstpara,"circuito":lstcircuit,\
        "Vmin":lstVmin,"Vmax":lstVmax,"tipo_de_controle":lsttipocontrole,\
        "modo_de_controle":lstmodocontrole,"fase_min":lstfasemin,\
        "fase_max":lstfasemax,"tipo_de_controle_2":lsttipocontrole2,\
        "val_espec":lstvalesp,"extremidade_medica":lstextremmed}


    dfCTR=pd.DataFrame(data=dCTR)


    dfCTR.to_csv("DCTR.csv", index=None)



#le arquivo
fname="arquivo.PWF"

with open(fname,'r') as f:
    lines=f.readlines()



dbar=criaDBAR(lines)
dlin=criaDLIN(lines)
dcsc=criaDCSC(lines)
dctr=criaDCTR(lines)



