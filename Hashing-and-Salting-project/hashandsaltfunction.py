#hash
def sha256(hashsalt):
    #hashfunction
    import hashsalt
    hashsalt = hashie + random.randint(0,255)
    hashsalt = hashie.encode('utf-8') 
    m = hashlib.sha256(hashie)
    return m.hexdigest()
