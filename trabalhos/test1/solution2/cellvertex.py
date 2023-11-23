import sys
sys.setrecursionlimit(2000)

##initializing variables

h = 100 ## W/m²
Tf = 50 ## °C
numberPoints = 5
d = 0.2 ## m 
k = 237 ## W/m°C
Ac = 1
Deltax = d/(numberPoints - 1)
Aconv = Deltax ## m²
Tinf = 20 ## °C
resudue = 0.001

##Visualization variables
counter = 0
decimalPlaces = 4


##Volumes on the left - coefficients
Ap_l = ((3 * k * Ac) / Deltax) + h * Aconv
Ae_l = k * Ac / Deltax
B_l = (((2 * k * Ac) / Deltax) * Tf) + (h * Aconv * Tinf)


##Volumes on the center - coefficients
Ap_c = ((2 * k * Ac) / Deltax) + h * Aconv
Ae_c = k * Ac / Deltax
Aw_c = k * Ac / Deltax
B_c = h * Aconv * Tinf

##Volume on the right - coefficients
Ap_r = ((k * Ac) / Deltax) + h * Aconv
Aw_r = k * Ac / Deltax
B_r = h * Aconv * Tinf

def setList(numberPoints, Tf, Tinf):
  firstList = []
  firstList.append(Tf)
  for i in range(1,numberPoints):
    firstList.append(Tinf)
  print(firstList)
  return firstList

def nextStep(t0):

  length = len(t0)

  t1 = t0.copy()
  t1[0] = t0[0]

  for i in range(1, length - 1):
    t1[i] = (Ae_c * t0[i + 1] + (Aw_c * t0[i - 1]) + B_c) / Ap_c

  t1[length - 1] = (Aw_r * t0[length - 2] + B_r) / Ap_r

  if(residue(t0, t1, resudue)):

    global counter
    counter += 1

    print(setdecimalPlaces(t1, decimalPlaces))
    nextStep(t1)

  else:
    print(counter)

def main():
  t0 = setList(numberPoints, Tf, Tinf)
  nextStep(t0)

def residue(list1, list2, residue):

  res = False

  if (len(list1) != len(list2)):
    print('Os vetores não tem o mesmo comprimento')
    return res
  else:
    for i in range(len(list1)):

      if(abs(list1[i] - list2[i]) > residue):
        res = True
        return res
      
  return res

def setdecimalPlaces(list, decimalPlaces):

  newList = list.copy()
  for i in range(len(list)):
    newList[i] = round(list[i], decimalPlaces)
  return newList

main()