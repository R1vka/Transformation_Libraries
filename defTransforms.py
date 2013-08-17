pivot = PVector()

def setup():
	size(200,200)
	global pos, pivot, r, square, square2

	pos = PVector(20,30)
	square = [PVector(-10,-10), PVector(10,-10), PVector(10,10), PVector(-10, 10)]
	square2 = scale(square, 2)
	pivot = PVector(width/2, height/2)
	r = 0




def draw():
	background(150)
	global pos, r, square2

	r+=1

	p = rotation(pos, r, pivot)
	square2 = scale(square2, 1.01)

	square3 = scale(square, sin(frameCount*.01)*20)


	fill(255)

	rectMode(CENTER)
	rect(p.x,p.y, 20,20)

	noFill()

	beginShape()
	for i,j in enumerate(square):
		vertex(j.x,j.y)
	endShape(CLOSE)

	beginShape()
	for i,j in enumerate(square2):
		vertex(j.x,j.y)
	endShape(CLOSE)

	beginShape()
	for i,j in enumerate(square3):
		vertex(j.x,j.y)
	endShape(CLOSE)



##inserting a PVector or list of PVectors; returning rotated PVector or list of PVectors
def rotation(vERTICES, tHETA_degrees, pIVOT = PVector(0,0)):
	#if single PVector, place in list to allow enumeration
	if not(type(vERTICES) == type([])):
		l = False
		vERTICES = [vERTICES]
	else:
		l = True


	rVerts = []
	th = radians(tHETA_degrees)
	p = pIVOT

	for i,j in enumerate(vERTICES):
		rX = j.x * cos(th) - j.y * sin(th)
		rY = j.x * sin(th) + j.y * cos(th)
		v = PVector(rX, rY)
		v = translate(v, p)
		rVerts.append(v)

	if l:
		return rVerts
	else:
		return rVerts[0]

def scale(vERTICES, dELTA, pIVOT = PVector(0,0)):
	if not(type(vERTICES) == type([])):
		l = False
		vERTICES = [vERTICES]
	else:
		l = True


	sVerts = []
	de = dELTA
	p = pIVOT

	for i,j in enumerate(vERTICES):
		X = j.x - p.x
		Y = j.y - p.y
		sX = X * de
		sY = Y * de
		v = PVector(sX,sY)
		v = translate(v, p)
		sVerts.append(v)

	if l:
		return sVerts
	else:
		return sVerts[0]

def translate(vERTICES, pIVOT = PVector(0,0)):
	if not(type(vERTICES) == type([])):
		l = False
		vERTICES = [vERTICES]
	else:
		l = True


	tVerts = []
	p = pIVOT

	for i,j in enumerate(vERTICES):
		tX = (j.x + p.x)
		tY = (j.y + p.y)
		v = PVector(tX,tY)
		tVerts.append(v)
	
	if l:
		return tVerts
	else:
		return tVerts[0]


def centroid():
	
	return PVector(0,0)
