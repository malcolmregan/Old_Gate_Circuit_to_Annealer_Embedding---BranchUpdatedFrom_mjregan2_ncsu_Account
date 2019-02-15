################################################################################
## SWAP - control: q0_0 target: q1_0 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q1_0' not in globals():
    q1_0=0

qubit_biases = {'q0_0' : 1, 'q1_0' : 1, 'outq0_0' : 1, 'outq1_0' : 1, 'a' : 6, 'b' : 6}
binding_weights = {('c', 'outq0_0') : 2,('c','outq1_0') : 2, ('c', 'a') : -4, ('c', 'b') : -4, ('q0_0', 'outq0_0') : -2, ('q0_0', 'a') : 2, ('q0_0', 'b') : -2, ('q1_0', 'outq1_0') : -2, ('q1_0', 'a') : -2, ('q1_0', 'b') : 2, ('outq0_0', 'a') : -4, ('outq1_0', 'b') : -4}
bqm = dimod.BinaryQuadraticModel(qubit_biases, binding_weights, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['c']==1 and sample['q0_0']==q0_0 and sample['q1_0']==q1_0 and int(energy)==0:
        q0_0=sample['outq0_0']
        q1_0=sample['outq1_0']
        tgt1_before = sample['q0_0']
        tgt2_before = sample['q1_0']
        break

print('#' * 80)
print("SWAP operation on q0_0 (control), q1_0 (target):")
print("    in:  q0_0={0}, q1_0={1}".format(tgt1_before, tgt2_before))
print("    out: q0_0={0}, q1_0={1}".format(q0_0, q1_0))
print('#' * 80)
print()
################################################################################
## SWAP - control: q0_0 target: q1_0 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q1_0' not in globals():
    q1_0=0

qubit_biases = {'q0_0' : 1, 'q1_0' : 1, 'outq0_0' : 1, 'outq1_0' : 1, 'a' : 6, 'b' : 6}
binding_weights = {('c', 'outq0_0') : 2,('c','outq1_0') : 2, ('c', 'a') : -4, ('c', 'b') : -4, ('q0_0', 'outq0_0') : -2, ('q0_0', 'a') : 2, ('q0_0', 'b') : -2, ('q1_0', 'outq1_0') : -2, ('q1_0', 'a') : -2, ('q1_0', 'b') : 2, ('outq0_0', 'a') : -4, ('outq1_0', 'b') : -4}
bqm = dimod.BinaryQuadraticModel(qubit_biases, binding_weights, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['c']==1 and sample['q0_0']==q0_0 and sample['q1_0']==q1_0 and int(energy)==0:
        q0_0=sample['outq0_0']
        q1_0=sample['outq1_0']
        tgt1_before = sample['q0_0']
        tgt2_before = sample['q1_0']
        break

print('#' * 80)
print("SWAP operation on q0_0 (control), q1_0 (target):")
print("    in:  q0_0={0}, q1_0={1}".format(tgt1_before, tgt2_before))
print("    out: q0_0={0}, q1_0={1}".format(q0_0, q1_0))
print('#' * 80)
print()
################################################################################
## SWAP - control: q0_0 target: q1_0 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q1_0' not in globals():
    q1_0=0

qubit_biases = {'q0_0' : 1, 'q1_0' : 1, 'outq0_0' : 1, 'outq1_0' : 1, 'a' : 6, 'b' : 6}
binding_weights = {('c', 'outq0_0') : 2,('c','outq1_0') : 2, ('c', 'a') : -4, ('c', 'b') : -4, ('q0_0', 'outq0_0') : -2, ('q0_0', 'a') : 2, ('q0_0', 'b') : -2, ('q1_0', 'outq1_0') : -2, ('q1_0', 'a') : -2, ('q1_0', 'b') : 2, ('outq0_0', 'a') : -4, ('outq1_0', 'b') : -4}
bqm = dimod.BinaryQuadraticModel(qubit_biases, binding_weights, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['c']==1 and sample['q0_0']==q0_0 and sample['q1_0']==q1_0 and int(energy)==0:
        q0_0=sample['outq0_0']
        q1_0=sample['outq1_0']
        tgt1_before = sample['q0_0']
        tgt2_before = sample['q1_0']
        break

print('#' * 80)
print("SWAP operation on q0_0 (control), q1_0 (target):")
print("    in:  q0_0={0}, q1_0={1}".format(tgt1_before, tgt2_before))
print("    out: q0_0={0}, q1_0={1}".format(q0_0, q1_0))
print('#' * 80)
print()
################################################################################
## SWAP - control: q0_0 target: q1_0 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q1_0' not in globals():
    q1_0=0

qubit_biases = {'q0_0' : 1, 'q1_0' : 1, 'outq0_0' : 1, 'outq1_0' : 1, 'a' : 6, 'b' : 6}
binding_weights = {('c', 'outq0_0') : 2,('c','outq1_0') : 2, ('c', 'a') : -4, ('c', 'b') : -4, ('q0_0', 'outq0_0') : -2, ('q0_0', 'a') : 2, ('q0_0', 'b') : -2, ('q1_0', 'outq1_0') : -2, ('q1_0', 'a') : -2, ('q1_0', 'b') : 2, ('outq0_0', 'a') : -4, ('outq1_0', 'b') : -4}
bqm = dimod.BinaryQuadraticModel(qubit_biases, binding_weights, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['c']==1 and sample['q0_0']==q0_0 and sample['q1_0']==q1_0 and int(energy)==0:
        q0_0=sample['outq0_0']
        q1_0=sample['outq1_0']
        tgt1_before = sample['q0_0']
        tgt2_before = sample['q1_0']
        break

print('#' * 80)
print("SWAP operation on q0_0 (control), q1_0 (target):")
print("    in:  q0_0={0}, q1_0={1}".format(tgt1_before, tgt2_before))
print("    out: q0_0={0}, q1_0={1}".format(q0_0, q1_0))
print('#' * 80)
print()
################################################################################
## SWAP - control: q0_0 target: q1_0 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q1_0' not in globals():
    q1_0=0

qubit_biases = {'q0_0' : 1, 'q1_0' : 1, 'outq0_0' : 1, 'outq1_0' : 1, 'a' : 6, 'b' : 6}
binding_weights = {('c', 'outq0_0') : 2,('c','outq1_0') : 2, ('c', 'a') : -4, ('c', 'b') : -4, ('q0_0', 'outq0_0') : -2, ('q0_0', 'a') : 2, ('q0_0', 'b') : -2, ('q1_0', 'outq1_0') : -2, ('q1_0', 'a') : -2, ('q1_0', 'b') : 2, ('outq0_0', 'a') : -4, ('outq1_0', 'b') : -4}
bqm = dimod.BinaryQuadraticModel(qubit_biases, binding_weights, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['c']==1 and sample['q0_0']==q0_0 and sample['q1_0']==q1_0 and int(energy)==0:
        q0_0=sample['outq0_0']
        q1_0=sample['outq1_0']
        tgt1_before = sample['q0_0']
        tgt2_before = sample['q1_0']
        break

print('#' * 80)
print("SWAP operation on q0_0 (control), q1_0 (target):")
print("    in:  q0_0={0}, q1_0={1}".format(tgt1_before, tgt2_before))
print("    out: q0_0={0}, q1_0={1}".format(q0_0, q1_0))
print('#' * 80)
print()
################################################################################
## SWAP - control: q0_0 target: q1_0 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q1_0' not in globals():
    q1_0=0

qubit_biases = {'q0_0' : 1, 'q1_0' : 1, 'outq0_0' : 1, 'outq1_0' : 1, 'a' : 6, 'b' : 6}
binding_weights = {('c', 'outq0_0') : 2,('c','outq1_0') : 2, ('c', 'a') : -4, ('c', 'b') : -4, ('q0_0', 'outq0_0') : -2, ('q0_0', 'a') : 2, ('q0_0', 'b') : -2, ('q1_0', 'outq1_0') : -2, ('q1_0', 'a') : -2, ('q1_0', 'b') : 2, ('outq0_0', 'a') : -4, ('outq1_0', 'b') : -4}
bqm = dimod.BinaryQuadraticModel(qubit_biases, binding_weights, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['c']==1 and sample['q0_0']==q0_0 and sample['q1_0']==q1_0 and int(energy)==0:
        q0_0=sample['outq0_0']
        q1_0=sample['outq1_0']
        tgt1_before = sample['q0_0']
        tgt2_before = sample['q1_0']
        break

print('#' * 80)
print("SWAP operation on q0_0 (control), q1_0 (target):")
print("    in:  q0_0={0}, q1_0={1}".format(tgt1_before, tgt2_before))
print("    out: q0_0={0}, q1_0={1}".format(q0_0, q1_0))
print('#' * 80)
print()
################################################################################
## SWAP - control: q0_0 target: q1_0 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q1_0' not in globals():
    q1_0=0

qubit_biases = {'q0_0' : 1, 'q1_0' : 1, 'outq0_0' : 1, 'outq1_0' : 1, 'a' : 6, 'b' : 6}
binding_weights = {('c', 'outq0_0') : 2,('c','outq1_0') : 2, ('c', 'a') : -4, ('c', 'b') : -4, ('q0_0', 'outq0_0') : -2, ('q0_0', 'a') : 2, ('q0_0', 'b') : -2, ('q1_0', 'outq1_0') : -2, ('q1_0', 'a') : -2, ('q1_0', 'b') : 2, ('outq0_0', 'a') : -4, ('outq1_0', 'b') : -4}
bqm = dimod.BinaryQuadraticModel(qubit_biases, binding_weights, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['c']==1 and sample['q0_0']==q0_0 and sample['q1_0']==q1_0 and int(energy)==0:
        q0_0=sample['outq0_0']
        q1_0=sample['outq1_0']
        tgt1_before = sample['q0_0']
        tgt2_before = sample['q1_0']
        break

print('#' * 80)
print("SWAP operation on q0_0 (control), q1_0 (target):")
print("    in:  q0_0={0}, q1_0={1}".format(tgt1_before, tgt2_before))
print("    out: q0_0={0}, q1_0={1}".format(q0_0, q1_0))
print('#' * 80)
print()
################################################################################
## SWAP - control: q0_0 target: q1_0 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q1_0' not in globals():
    q1_0=0

qubit_biases = {'q0_0' : 1, 'q1_0' : 1, 'outq0_0' : 1, 'outq1_0' : 1, 'a' : 6, 'b' : 6}
binding_weights = {('c', 'outq0_0') : 2,('c','outq1_0') : 2, ('c', 'a') : -4, ('c', 'b') : -4, ('q0_0', 'outq0_0') : -2, ('q0_0', 'a') : 2, ('q0_0', 'b') : -2, ('q1_0', 'outq1_0') : -2, ('q1_0', 'a') : -2, ('q1_0', 'b') : 2, ('outq0_0', 'a') : -4, ('outq1_0', 'b') : -4}
bqm = dimod.BinaryQuadraticModel(qubit_biases, binding_weights, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['c']==1 and sample['q0_0']==q0_0 and sample['q1_0']==q1_0 and int(energy)==0:
        q0_0=sample['outq0_0']
        q1_0=sample['outq1_0']
        tgt1_before = sample['q0_0']
        tgt2_before = sample['q1_0']
        break

print('#' * 80)
print("SWAP operation on q0_0 (control), q1_0 (target):")
print("    in:  q0_0={0}, q1_0={1}".format(tgt1_before, tgt2_before))
print("    out: q0_0={0}, q1_0={1}".format(q0_0, q1_0))
print('#' * 80)
print()
################################################################################
## SWAP - control: q0_0 target: q1_0 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q1_0' not in globals():
    q1_0=0

qubit_biases = {'q0_0' : 1, 'q1_0' : 1, 'outq0_0' : 1, 'outq1_0' : 1, 'a' : 6, 'b' : 6}
binding_weights = {('c', 'outq0_0') : 2,('c','outq1_0') : 2, ('c', 'a') : -4, ('c', 'b') : -4, ('q0_0', 'outq0_0') : -2, ('q0_0', 'a') : 2, ('q0_0', 'b') : -2, ('q1_0', 'outq1_0') : -2, ('q1_0', 'a') : -2, ('q1_0', 'b') : 2, ('outq0_0', 'a') : -4, ('outq1_0', 'b') : -4}
bqm = dimod.BinaryQuadraticModel(qubit_biases, binding_weights, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['c']==1 and sample['q0_0']==q0_0 and sample['q1_0']==q1_0 and int(energy)==0:
        q0_0=sample['outq0_0']
        q1_0=sample['outq1_0']
        tgt1_before = sample['q0_0']
        tgt2_before = sample['q1_0']
        break

print('#' * 80)
print("SWAP operation on q0_0 (control), q1_0 (target):")
print("    in:  q0_0={0}, q1_0={1}".format(tgt1_before, tgt2_before))
print("    out: q0_0={0}, q1_0={1}".format(q0_0, q1_0))
print('#' * 80)
print()
################################################################################
## SWAP - control: q0_0 target: q1_0 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q1_0' not in globals():
    q1_0=0

qubit_biases = {'q0_0' : 1, 'q1_0' : 1, 'outq0_0' : 1, 'outq1_0' : 1, 'a' : 6, 'b' : 6}
binding_weights = {('c', 'outq0_0') : 2,('c','outq1_0') : 2, ('c', 'a') : -4, ('c', 'b') : -4, ('q0_0', 'outq0_0') : -2, ('q0_0', 'a') : 2, ('q0_0', 'b') : -2, ('q1_0', 'outq1_0') : -2, ('q1_0', 'a') : -2, ('q1_0', 'b') : 2, ('outq0_0', 'a') : -4, ('outq1_0', 'b') : -4}
bqm = dimod.BinaryQuadraticModel(qubit_biases, binding_weights, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['c']==1 and sample['q0_0']==q0_0 and sample['q1_0']==q1_0 and int(energy)==0:
        q0_0=sample['outq0_0']
        q1_0=sample['outq1_0']
        tgt1_before = sample['q0_0']
        tgt2_before = sample['q1_0']
        break

print('#' * 80)
print("SWAP operation on q0_0 (control), q1_0 (target):")
print("    in:  q0_0={0}, q1_0={1}".format(tgt1_before, tgt2_before))
print("    out: q0_0={0}, q1_0={1}".format(q0_0, q1_0))
print('#' * 80)
print()
