def p_norm(v,p):
	d = float(p)
	s = sum([i**p for i in v])
	return s**(1/d)
