CACHE = {};

def set(key, value):
	try:
		CACHE[key]= value
		return True
	except:
		return None

def get(key):
	try: return CACHE[key];
	except: return None;

def delete(key):
	try:
		return CACHE[key]
	except:
		return None

def flush():
	CACHE.clear();

def gets(key):
	v = CACHE.get(key)
	if v:
		return v, hash(repr(v))

def cas(key, value, cas_unique):
	r = gets(key)
	if r:
		val, unique = r
		if unique == cas_unique:
			return set(key, value)
		else:
			return False 