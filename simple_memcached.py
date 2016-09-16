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