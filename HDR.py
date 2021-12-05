from EnviromentalDataHDR import *

city = input('Please select a location Carson(c),Fort Yates(f), or Linton(l)')
c = 1
while c == True:
    if city == ('c'):
        data_carson = input('Please select a graph from this list: \n Bare Soil(BS)  \n Temp Dew Point(DP) \n Penman PET(PENPET) \n Turf Soil Temp(TSP) \n Wind Chill(WC) \n Wind Speed(WS) \n Average Temp(AT) \n Max Wind Speed(MWS) \n Max Temp(MaxT) \n Min Temp(MinT) \n Total Penman PET(TPP) \n Total Solar Radiation(TSR)\n Quit(q) \n')
        if data_carson == 'BS':
            CarsonBS()
        elif data_carson == 'DP':
            CarsonDP()
        elif data_carson == 'PENPET':
            CarsonPENPET()
        elif data_carson == 'TSP':
            CarsonTSP()
        elif data_carson == 'WC':
            CarsonWC()
        elif data_carson =='WS':
            CarsonWS()
        elif data_carson =='AT':
            carsonAT()
        elif data_carson == 'MWS':
            carsonMWS()
        elif data_carson =='MaxT':
            carsonMaxT()
        elif data_carson =='MinT':
            carsonMinT()
        elif data_carson == 'TPP':
            carsonTPP()
        elif data_carson == 'TSR':
            carsonTSR()
        else:
            data_carson == 'q'
            c = 0
    elif city == ('f'):
        data_fortyates = input('Please select a graph from this list: \n Bare Soil(BS)  \n Temp Dew Point(DP) \n Penman PET(PENPET) \n Turf Soil Temp(TSP) \n Wind Chill(WC) \n Wind Speed(WS) \n Average Temp(AT) \n Max Wind Speed(MWS) \n Max Temp(MaxT) \n Min Temp(MinT) \n Total Penman PET(TPP) \n Total Solar Radiation(TSR)\n Quit(q) \n')
        if data_fortyates == 'BS':
            FortYatesBS()
        elif data_fortyates == 'DP':
            FortYatesDP()
        elif data_fortyates == 'PENPET':
            FortYatesPENPET()
        elif data_fortyates == 'TSP':
            FortYatesTSP()
        elif data_fortyates == 'WC':
            FortYatesWS()
        elif data_fortyates =='WS':
            FortYatesWS()
        elif data_fortyates =='AT':
            FortYatesAT()
        elif data_fortyates == 'MWS':
            FortYatesMWS()
        elif data_fortyates =='MaxT':
            FortYatesMaxT()
        elif data_fortyates =='MinT':
            FortYatesMinT()
        elif data_fortyates == 'TPP':
            FortYatesTPP()
        elif data_fortyates == 'TSR':
            FortYatesTSR()
        else:
            data_carson == 'q'
            c = 0
    elif city == 'l':
        data_linton = input('Please select a graph from this list: \n Bare Soil(BS)  \n Temp Dew Point(DP) \n Penman PET(PENPET) \n Turf Soil Temp(TSP) \n Wind Chill(WC) \n Wind Speed(WS) \n Average Temp(AT) \n Max Wind Speed(MWS) \n Max Temp(MaxT) \n Min Temp(MinT) \n Total Penman PET(TPP) \n Total Solar Radiation(TSR)\n Quit(q) \n')
        if data_linton == 'BS':
            lintonBS()
        elif data_linton == 'DP':
            lintonDP()
        elif data_linton == 'PENPET':
            lintonPENPET()
        elif data_linton == 'TSP':
            lintonTSP()
        elif data_linton == 'WC':
            lintonWC()
        elif data_linton =='WS':
            lintonWS()
        elif data_linton =='AT':
            lintonAT()
        elif data_linton == 'MWS':
            lintonMWS()
        elif data_linton =='MaxT':
            lintonMaxT()
        elif data_linton =='MinT':
            lintonMinT()
        elif data_linton == 'TPP':
            lintonTPP()
        elif data_linton == 'TSR':
            lintonTSR()
        else:
            data_linton == 'q'
            c = 0
    
            
    
