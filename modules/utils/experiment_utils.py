from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_bloch_multivector
from qiskit import transpile,execute


def plot_block_sphere(exp,backend):
  plot_bloch_multivector(execute(exp,backend).result().get_statevector())

def ideal_qc_simulation(exp,backend,num_measurements = 1024):
  qc_compiled = transpile(exp,backend)
  job = backend.run(qc_compiled,shots = num_measurements)
  result = job.result()
  return result.get_counts()

def stateGenerator(state):
    state = state[::-1]
    current = int(state, 2)
    newState = [0 for i in range(0, 2**(len(state)))]
    newState[current] = 1
    return newState

def initialize_quantum_circuit(qc,target_qubits,hadamard = False):
  for q in target_qubits:
    if hadamard:
      qc.h(q)
    else:
      qc.x(q)

def get_target_measurement(output,target_qubits):
  filtered_output = list()
  for q in target_qubits:
    filtered_output.append(output[q])
  return ''.join(filtered_output)

def reverse_output(output):
  rev = [output[q] for q in reversed(range(len(output)))]
  return ''.join(rev)

def make_meaurement(qc,qr,cr,output_qubits):
  for q in output_qubits:
    qc.measure(qr[q],cr[q])
