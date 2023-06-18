from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_bloch_multivector
from qiskit import transpile,execute

"""
Miscelaneus functions to perform general task in making quantum computing experiments
"""


# function to plot the quantum state in terms of the block sphere (useful for visualizing superposition outputs)
def plot_block_sphere(exp,backend):
  plot_bloch_multivector(execute(exp,backend).result().get_statevector())

# simulate the quantum circuit in a built in backend a certain number of times
def ideal_qc_simulation(exp,backend,num_measurements = 1024):
  qc_compiled = transpile(exp,backend)
  job = backend.run(qc_compiled,shots = num_measurements)
  result = job.result()
  return result.get_counts()

# convert a decimal number to binary and generate the quantum state based on the binary representation
def stateGenerator(state):
    state = state[::-1]
    current = int(state, 2)
    newState = [0 for i in range(0, 2**(len(state)))]
    newState[current] = 1
    return newState

# initialized a quantum circuit by changind the target qubits to |1>. Set hadamard to True if you need that qubit to have a superposition state. 
def initialize_quantum_circuit(qc,target_qubits,hadamard = False):
  for q in target_qubits:
    if hadamard:
      qc.h(q)
    else:
      qc.x(q)

# filter a certain number of measured qubits from a binary string (useful if you measured all the qubits of the quantum circuit)
def get_target_measurement(output,target_qubits):
  filtered_output = list()
  for q in target_qubits:
    filtered_output.append(output[q])
  return ''.join(filtered_output)

# change the output from little endian (qiskit default) to big endian and viceversa
def reverse_output(output):
  rev = [output[q] for q in reversed(range(len(output)))]
  return ''.join(rev)

# make quantum measurements based on a list of target qubits. Ser irregular to True if the number of target qubits is different from the length of the quantum register.
def make_meaurement(qc,qr,cr,output_qubits,irregular = False):
  if not irregular:
    for q in output_qubits:
      qc.measure(qr[q],cr[q])
  else:
    for c,q in enumerate(output_qubits):
      qc.measure(qr[q],qc[c])
