import copy ##Cópia profunda vs Cópia Superficial
import math

##Inputs
gama = 1
v = 2
u = 2
ro = 1
length = 1

##Mesh
lineVolums = 30
inicialValue = 0
deltax = length / (lineVolums - 1)

##Border Variables
northBorder = 1
westBorder = 1
eastBorder = 0
southBorder = 0

##Data Viariables
counter = 0

#Data Loop
resid = 0.00001
decimalPrecision = 2

def createMesh(lineVolums, inicialValue): 
  line = []
  mesh = []
  for i in range(lineVolums + 2):
    line.append(inicialValue)
  for j in range(lineVolums + 2):
    mesh.append(line.copy())
  return mesh

def insertNone(mesh):

  mesh[0][0] = None
  mesh[0][len(mesh) - 1] = None
  mesh[len(mesh) - 1][0] = None
  mesh[len(mesh) - 1][len(mesh) - 1] = None
  return mesh

def calculatet1(mesh):
  global counter
  l = len(mesh)
  
  mesh0 = copy.deepcopy(mesh)
  mesh = copy.deepcopy(mesh)
  
  for i in range(1, l - 1):
    ##northern border
    mesh[0][i] = (- mesh0[1][i]) + (2 * northBorder)
    ##western border
    mesh[i][0] = - mesh0[i][1] + 2 * westBorder
    ##southern border
    mesh[l - 1][i] = - mesh0[l - 2][i] + 2 * southBorder
    ##eastern border
    mesh[i][l - 1] = - mesh0[i][l - 2] + 2 * eastBorder
    
  #centralVolums
  for i in range(1, l - 1):
    for j in range(1, l - 1):
    
      ## Aw * OW
      W = ((ro * u * deltax/2) + gama) * mesh0[i][j-1]
      ## Ae * OE
      E = ((-ro * u * deltax/2) + gama) * mesh0[i][j + 1]
      ## An * ON
      N = ((-ro * v * deltax/2) + gama) * mesh0[i - 1][j]
      ## As * OS
      S = ((ro * v * deltax/2) + gama) * mesh0[i + 1][j]
            
      mesh[i][j] = (W + E + N + S) / (4 * gama)

  if(counter < 500):
    ##residue(mesh0, mesh, resid)
    if(counter == 499):
      centralLine = math.floor(len(mesh)/2)
      print(mesh[centralLine])
    counter += 1
    calculatet1(mesh)

  # else:
  #   print('O número de iterações foi de {counter}'.format(counter = counter))
  #   print(mesh[4])

def residue(matrix1, matrix2, resid):
  response = False

  if (len(matrix1) != len(matrix2)):
    
    print('As matrizes não tem o mesmo tamanho')
    return response
  else:
    for i in range(1, len(matrix1) -1):
      for j in range(1, len(matrix1) - 1):

        if(abs(matrix1[i][j] - matrix2[i][j]) > resid):
          response = True
          return response

  return response

def main():
  mesh = createMesh(lineVolums, inicialValue)
  meshWithNone = insertNone(mesh)
  calculatet1(meshWithNone)

main()