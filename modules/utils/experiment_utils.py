from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_bloch_multivector
from qiskit import transpile,execute

def ideal_qc_simulation(exp,backend,num_measurements = 1024):
  qc_compiled = transpile(exp,backend)
  job = backend.run(qc_compiled,shots = num_measurements)
  result = job.result()
  return result.get_counts()

def state_generator(state):
    state = state[::-1]
    current = int(state, 2)
    newState = [0 for i in range(0, 2**(len(state)))]
    newState[current] = 1
    return newState

def get_measure(quantumC, n,backend):
    measures = []
    for i in range(0, n):
        outcome = execute(quantumC, backend).result()
        hist = outcome.get_counts()
        for i in hist.keys():
            measures.append(i)
    return measures