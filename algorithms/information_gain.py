import math

def entropy(probs):
    return -sum(p * math.log2(p) for p in probs if p > 0)

def expected_information_gain(prior, likelihoods):
    """likelihoods[root] = P(tool returns abnormal | root). Binary observation model."""
    roots=list(prior)
    h0=entropy([prior[r] for r in roots])
    p_abn=sum(prior[r]*likelihoods[r] for r in roots)
    expected_h=0.0
    for abnormal, p_obs in [(True,p_abn),(False,1-p_abn)]:
        if p_obs <= 0: continue
        post=[]
        for r in roots:
            like=likelihoods[r] if abnormal else 1-likelihoods[r]
            post.append(prior[r]*like/p_obs)
        expected_h += p_obs*entropy(post)
    return max(0.0,h0-expected_h)
