from math import log

#Function to calculate LMTD(Logarithmic Mean Temperature Difference) for Parallel Flow
def LMTD_Parallel(hot_inlet_temp,hot_outlet_temp,cold_inlet_temp,cold_outlet_temp):
    temp_diff_1 = abs(hot_inlet_temp - cold_inlet_temp)
    temp_diff_2 = abs(hot_outlet_temp - cold_outlet_temp)
    LMTD_Parallel = ((temp_diff_1 - temp_diff_2) / log(temp_diff_1 / temp_diff_2))
    return LMTD_Parallel

#Function to calculate LMTD(Logarithmic Mean Temperature Difference) for Counter Flow
def LMTD_Counter(hot_inlet_temp,hot_outlet_temp,cold_inlet_temp,cold_outlet_temp):
    temp_diff_1 = abs(hot_inlet_temp - cold_outlet_temp)
    temp_diff_2 = abs(hot_outlet_temp - cold_inlet_temp)
    LMTD_Counter = ((temp_diff_1 - temp_diff_2) / log(temp_diff_1 / temp_diff_2))
    return LMTD_Counter

print("#METHODS\n1)LMTD Method\n  (returns LMTD value for Parallel or Counter flow in °C)\n\n#Type of Heat Exchanger.\n1)Parallel Flow\n2)Counter Flow\n\nEnter option number.\n(1)LMTD Method(Parallel Flow)\n(2)LMTD Method(Counter Flow)\n")
option = int(input())

#Input parameters for LMTD(Logarithmic Mean Temperature Difference) Method
if option >= 1 and option <= 2:
    hot_inlet_temp = float(input("Enter the inlet temperature of the hot fluid (°C): "))
    hot_outlet_temp = float(input("Enter the outlet temperature of the hot fluid (°C): "))
    cold_inlet_temp = float(input("Enter the inlet temperature of the cold fluid (°C): "))
    cold_outlet_temp = float(input("Enter the outlet temperature of the cold fluid (°C): "))
    
    if option == 1:
        LMTD_Parallel = LMTD_Parallel(hot_inlet_temp,hot_outlet_temp,cold_inlet_temp,cold_outlet_temp)
        print("\nLMTD value for parallel flow: %.3f °C"%(LMTD_Parallel))
    elif option == 2:
        LMTD_Counter = LMTD_Counter(hot_inlet_temp,hot_outlet_temp,cold_inlet_temp,cold_outlet_temp)
        print("\nLMTD value for counter flow: %.3f °C"%(LMTD_Counter))
else:
    print("Enter correct option number!")

    
