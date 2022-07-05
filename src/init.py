import math
import pyodide

GOLDEN_RATIO = (1.0 + math.sqrt(5)) / 2
GOLDEN_ANGLE = 2.0 * math.pi * (1.0 - 1.0 / GOLDEN_RATIO)

def normalize(val: float, min: float, max: float) -> float:
	return (val - min) / (max - min)

def lerp (val: float, start: float, end: float) -> float:
	return (1 - val) * start + val * end

def phyllotaxis(c: float, r: float) -> dict:
	for i in range(c):
		phi = math.sqrt(i / c)
		theta = i * GOLDEN_ANGLE
		x = math.cos(theta) * phi * r
		y = math.sin(theta) * phi * r
		yield {
			'x': x,
			'y': y,
			'i': i,
			'r': lerp(normalize(i, 1, c), 1, 5),
			'c': '#073642' if i % 2 else '#b58900' 
		}

plot_size = 600
node_count = 800

svgns = 'http://www.w3.org/2000/svg'
svg = document.getElementById('plot')
svg.setAttribute('width', plot_size)
svg.setAttribute('height', plot_size)

for d in phyllotaxis(node_count, 200):
	node = document.createElementNS(svgns, 'circle')
	node.setAttribute('cx', d['x'] + plot_size / 2)
	node.setAttribute('cy', d['y'] + plot_size / 2)
	node.setAttribute('r', d['r'])
	node.setAttribute('fill', d['c'] )
	svg.appendChild(node)