#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hochi
#
# Created:     05/09/2021
# Copyright:   (c) hochi 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##import time
####print(time.time())
##
##
##def calcProd():
##    #Calculate the product of the first 100.000 number
##    product=1
##    for i in range(1,100000):
##        product=product*i
##    return product
##
##
##startTime=time.time()
##prod=calcProd()
##endTime=time.time()
##print("The result is %s digits long" % (len(str(prod))))
##print('Took %s seconds to calculate.' % (endTime - startTime))

##########################################################################



##
##import time
##
##
##print(time.ctime())   # tiempo
##
##thisMoment=time.time()
##
##print(time.ctime(thisMoment))  # tiempo
#########################################################################
#####################THE TIME SLEEP


##import time
##for i in range(23):
##    print("Tik")
##    time.sleep(1)
##    print("Tak")
##    time.sleep(1)


#######################################################################
########################################REDONDEAR DECIMALES
##import time
##now =time.time()
##print(now)
##print(round(now,4))#redondea decimales.
##print(round(now,2))#redondea decimales.
##print(round(now))#elimina por completo las decimales
#########################################################################
##
##import time
##
###Dysplay the program instructions
##print("""Press Enter to begin,Afterward press Enter to "click" the stopwatch\
## press CTR C to quit.""")
##input()  # press Enter to begin
##print("Started")
##startTime=time.time() # get the first lap time
##lastTime=startTime
##lapNum=1
### Start tracking the lap times.
##try:
##    while True:
##
##        input
##        lapTime=round(time.time()-lastTime,2)
##        totalTime=round(time.time()-startTime,2)
##        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
##        lapNum+= 1
##        lastTime = time.time() # reset the last lap time
##except KeyboardInterrupt:
### Handle the Ctrl-C exception to keep its error message from displaying.
##    print('\nDone.')











############################################################

##########################DESFRAGMENTAR EL TIEMPO  Y SEPARARLO
##import datetime
##
##datetime.datetime.now()
##
##
##dt = datetime.datetime(2019, 10, 21, 16, 29, 0)
##dt.year, dt.month, dt.day
##dt.hour,dt.minute,dt.second
##
##print(dt.year,dt.hour)

################################################

################CONVERTIR DE UnIX TIME A NORMaL TIME
#datetime.datetime.fromtimestamp()  ######3

##import datetime, time
##datetime.datetime.fromtimestamp(1000000)
##datetime.datetime.fromtimestamp(time.time())


###################################################
###################COMPARACION ENTRE FECHAS
##import datetime
##
##
##halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
##newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
##oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
##
##print(halloween2019 == oct31_2019)
##print(halloween2019 > newyears2020)
##print(newyears2020 > halloween2019)
##print(newyears2020 != oct31_2019)


###########
###########################Delta time ~duration de
##import datetime
##delta=datetime.timedelta(days=11,hours=10,minutes=9,seconds=8)
##delta.days,delta.seconds,delta.microseconds
##delta.total_seconds()
##print(str(delta))


#######################################################
###################FECHA Y FECHA dentro de 1000 dias.
##import datetime
##dt=datetime.datetime.now()
##print(dt)
##thousandDays=datetime.timedelta(days=1000)
##
##print(dt + thousandDays)


###


import datetime

oct21st=datetime.datetime(2019,10,21,16,29,0)
aboutThirtyYears=datetime.timedelta(days=365*30)
print(oct21st)