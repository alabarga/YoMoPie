import YoMoPie
import time

yomo = YoMoPie.YoMoPie()  ##create a new YoMoPie Object

##yomo.set_lines(1)  ##set number of lines to 1. Following commands will do the same


yomo.write_8bit(0x0B, 0x10)  ##MMODE 0x10
yomo.write_8bit(0x0D, 0x24)  ##WATMODE 0x24
yomo.write_8bit(0x0E, 0x24)  ##VAMODE 0x24
yomo.write_16bit(0x13, [0x00, 0xC8])   ##LINCYC
yomo.write_16bit(0x0F, [0x04, 0x00])   ##IRQEN


pe=1

Cf = 0.000014
CfV = 0.000047159
CfI = 0.000010807

watt = 58.3
    
'''
        Wh/LSB constant = (W * Accumulation time(s)/3600)/(LAENERGY/4)
        
        with
        
        Accumulation time(s) = LINCYC[15:0] * Line Period/(2*#of phase selected)
        
        and
        
        Line Period(s) = Period Register * 2.4 * 10^-6
        
        
        Simulated load with 100mVpp @ 50Hz on the input of the AMC1100 and the output of the CST1020:
        calculated Load: 61,778Vpp and 1,92App
        Ueff = 61,778/sqrt(2) = 43,68V
        Ieff = 1,92/sqrt(2) = 1,375A
        -> load = 59,30W/h
        
        -> Cf = 0.000014
        
        -> Cf(VRMS) = 0.000047159
        -> Cf(IRMS) = 0.000010807
'''

while True:
##    print("--------------------------")
##    period = yomo.get_period()[1] * 0.0000024
##    print("Line Period = %f s" %(period))
##    linecycles = yomo.read_16bit(0x13)
##    print("Linecycles = %f" %(linecycles))
##    atime = linecycles*period/2
##    print("Accumulation time = %f s" %(atime))
##    laenergy = yomo.get_laenergy()
##    print("LAENERGY = %d" %(laenergy[1]))
##    cf = watt*(atime/3600)/((1+laenergy[1])/4)
##    print("Wh/LSB const = %f" %(cf))
##    print("--------------------------")
##  
  
    yomo.do_n_measurements(1000,5,"calibration_99_4_2018.log")
  
##yomo.do_n_measurements(1000,1,"test_150mv.log")
   
##    print("VRMS = %f V" %(yomo.get_vrms()[1]*CfV))
##    print("IRMS = %f A" %(yomo.get_irms()[1]*CfI))
##    print("Aenergy = %d" %yomo.read_24bit(0x01))
##    raen=yomo.read_24bit(0x02)
##    print("RAenergy = %d" %raen)
##    print("LAenergy = %d" %yomo.read_24bit(0x03))
##    print("VAenergy = %d" %yomo.read_24bit(0x04))
##    print("RVAenergy = %d" %yomo.read_24bit(0x05))
##    print("LVAenergy = %d" %yomo.read_24bit(0x06))
##    print("%f Watt/h" %(raen*Cf*3600/pe))
    ##time.sleep(pe)
    ##print(yomo.read_16bit(0x25))
    ##print(yomo.read_24bit(0x02))
    ##print(yomo.read_24bit(0x03))
    ##print(yomo.read_24bit(0x05))
        
yomo.close()   