##Inputs
gama = 1
v = 2
u = 2
ro = 1
length = 1

##Mesh
lineVolums = 3
inicialValue = 0.5
deltax = length / (lineVolums - 1)
deltay = deltax

##Border Variables
northBorder = 1
westBorder = 1
eastBorder = 0
southBorder = 0

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
  l = len(mesh)
  
  for i in range(1, l - 1):
    ##northern border
    mesh[0][i] = - mesh[1][i] + 2 * northBorder
    ##western border
    mesh[i][0] = - mesh[i][1] + 2 * westBorder
    ##southern border
    mesh[l - 1][i] = - mesh[l - 2][i] + 2 * southBorder
    ##eastern border
    mesh[i][l - 1] = - mesh[i][l - 2] + 2 * eastBorder
    ##centralVolums
    for j in range(1, l - 1):
      mesh[i][j] = (ro * ) * mesh[i - i]

def main():
  mesh = createMesh(lineVolums, inicialValue)
  meshWithNone = insertNone(mesh)
  print(meshWithNone)
  print(calculatet1(meshWithNone))


main()