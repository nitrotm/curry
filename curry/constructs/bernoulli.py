from ..controlled import bernoulli as _bern

def bernoulli(p, q, rot='RX', definitions=None):
    '''
    Exploit an RX gate to create a simple bernoulli trial
    (bernoulli 0.5 0) # Create the 0.5 state on qubit 0
    '''
    if definitions is None:
        definitions = dict()
    p = float(p)
    return _bern(p, q, rot=rot)
