from math import pi
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from experiment_utils import *
import random
import qiskit_textbook.tools as qt

"""
Functions related to quantum algorithms
"""

"""
This functions where retrieved from qiskit documentation
"""

def qft_rotations(circuit, n):
    """Performs qft on the first n qubits in circuit (without swaps)"""
    if n == 0:
        return circuit
    n -= 1
    circuit.h(n)
    for qubit in range(n):
        circuit.cp(pi/2**(n-qubit), qubit, n)
    # At the end of our function, we call the same function again on
    # the next qubits (we reduced n by one earlier in the function)
    qft_rotations(circuit, n)
def swap_registers(circuit, n):
    for qubit in range(n//2):
        circuit.swap(qubit, n-qubit-1)
    return circuit

def qft(circuit, n):
    """QFT on the first n qubits in circuit"""
    qft_rotations(circuit, n)
    swap_registers(circuit, n)
    return circuit

"""
This functions are of my own authoring.
"""
def simon_circuit(s):
   n = len(s)
   # intialize a two bits for each bit in the secret sequence
   qc = QuantumCircuit(2*n,2*n)
   # apply haddamard to get superposition
   qc.h(range(n))
   qc.barrier()
   qc += qt.simon_oracle(s)
   qc.barrier()
   # measure the lower circuits (|0>)
   qc.measure(range(2*n),range(2*n))
   qc.barrier()
   # apply another hadamard gate
   qc.h(range(n))
   qc.measure(range(n),range(n))
   return qc
   



def deutch_jozsa(qc,initialize_jozsa = True):
  """
  The function receibes a quantum circuit as parameter and implements the deutch josza algorithm.
  ***THE CIRCUIT MUST ME EMPTY***
  qc: quantum circuit instance
  initialize_jozsa: If set to true, the function assumes the qubits have not been initialized yet.
  """
  assert len(qc.qubits) == 2,"The quantum circuit must have only two qubits."
  num_qubits = len(qc.qubits)
  if initialize_jozsa:
    # initialize the quantum circuit
    initialize_quantum_circuit(qc,target_qubits = [1],hadamard=False)
    qc.barrier()
  # apply the initial hadamard gates
  for i in range(num_qubits):
    qc.h(i)
  qc.barrier()
  # fetch a random oracle 
  oracle = random.randint(0,num_qubits+1)
  # instance a circuit to hold the oracle gate
  oracle_gate = QuantumCircuit(num_qubits)
  # create the corresponding function depending on whether the fase kickback is odd or even
  if(oracle == 0): # f_0(x) = 0 
    pass 
  elif(oracle == 1): # f(x) = x
    oracle_gate.cx(0,1)
  elif(oracle == 2): # f(x) = 1
    oracle_gate.cx(0,1)
    oracle_gate.x(0)
    oracle_gate.cx(0,1)
  else: # f(x) = x + 1
    oracle_gate.x(0)
    oracle_gate.cx(0,1)

  # transform the circuit into a quantum gate  
  gate = oracle_gate.to_gate(label = "Oracle")
  qc.append(gate,[0,1])
  qc.barrier()

  # apply the initial hadamard gates
  for i in range(num_qubits):
    qc.h(i)
  qc.barrier()
  # make a quantum measurement
  for i in range(num_qubits):
    qc.measure(i,i)
  return qc
