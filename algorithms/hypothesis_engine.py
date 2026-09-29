ROOTS=["dns","routing","load_balancer","firewall","server","application"]

def uniform_prior(): return {r:1/len(ROOTS) for r in ROOTS}

def update(prior, likelihoods, abnormal):
    weights={}
    for r,p in prior.items():
        like=likelihoods[r] if abnormal else 1-likelihoods[r]
        weights[r]=p*like
    z=sum(weights.values()) or 1.0
    return {r:v/z for r,v in weights.items()}
