from math import pi
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from experiment_utils import *
import random
import qiskit_textbook.tools as qt
import os
import sys


# added to be able to use the experiment_utils script.  
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

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

def superdense_coding(s):
  """
  Superdense coding is a quantum communication algorithm in which to classical bits are sent using a single qubit.
  The qubit is suposed to be shared between an emisor and a receiber. It consist on one system per party, and 
  shares an entangled state.
  Inputs: String represented the two bit classical sequence.
  Output: The superdence coding quantum circuit corresponding to the input sequence.
  """
  # initialize the quantum circuit
  cr = ClassicalRegister(2)
  qr = QuantumRegister(2)
  qc = QuantumCircuit(qr,cr)
  
  # get the entangled state 
  qc.h(0)
  qc.cx(0,1)
  qc.barrier()
  
  # get the bell state corresponding to the input sequence
  if(s[0] == '1'):
    qc.x(0)
  if (s[1] == '1'):
    qc.z(0)
  qc.barrier()
  
  # remove the entangled state
  qc.cx(0,1)
  qc.h(0)
  qc.barrier()

  # measure the quantum circuit
  for i in range(2):
    qc.measure(i,i)
  
  return qc


def simon_circuit(s):
  """
  Inputs: Secret sequence s
  Problem statement:
  F(x) = F(y) if y = x + s
  """
  # get the length of the sequence
  n = len(s)
  # instance two qubits for each bit in the sequence
  qc = QuantumCircuit(2*n, 2*n)
  # apply superpositiion
  qc.h(range(n))
  qc.barrier()
  # apply the unknown oracle function
  qc.append(qt.simon_oracle(s),qc.qubits)
  qc.barrier()
  # measure
  qc.measure(range(n, 2*n), range(n, 2*n))
  qc.barrier()
  # another superposition
  qc.h(range(n))
  # measurement
  qc.measure(range(n), range(n))
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


# quantum phase estimation
def quantum_phase_estimation(n,angle):
  qc = QuantumCircuit(n,n-1)
  # initialize the quantum circuit
  # apply the haddamard gates
  initialize_quantum_circuit(qc,list(range(0,n-1)),hadamard=True)
  # apply the x gate to transition the last qubit into |1>
  initialize_quantum_circuit(qc,[n-1],hadamard=False)
  angle = pi * angle

  qc.barrier()

  # controlled phase gates
  for i in range(0,n-1):
    for j in range(2 ** i):
      qc.cp(angle,i,n-1)
  qc.barrier()

  # implement inverse quantum fourier transform
  for i in range(0,n//2):
    qc.swap(i,n-i-1)
  for i in range(n):
    for j in range(i):
      qc.cp(-pi/float(2**(i-j)),i,j)
    qc.h(i)
  
  qc.barrier()

  # measure
  qc.measure(range(0,n-1),range(0,n-1))

  return qc


# Grover Algorithm Functions
def cccZ():
  """
  Triple Control Z Rotation:
  It is a gate that only present a rotations in the last qubit if the first three qubits are in the exited state
  """
  qc = QuantumCircuit(4)
  qc.cp(pi/4, 0, 3)
  qc.cx(0, 1)
  qc.cp(-pi/4, 1, 3)
  qc.cx(0, 1)
  qc.cp(pi/4, 1, 3)
  qc.cx(1, 2)
  qc.cp(-pi/4, 2, 3)
  qc.cx(0, 2)
  qc.cp(pi/4, 2, 3)
  qc.cx(1, 2)
  qc.cp(-pi/4, 2, 3)
  qc.cx(0, 2)
  qc.cp(pi/4, 2, 3)
  gate = qc.to_gate(label=' cccZ')
  return gate


def grover_difussion_operator():
  """
  Inversion along the mean
  """
  qc = QuantumCircuit(4)
  qc.h(range(4))
  qc.x(range(4))
  qc.append(cccZ(), [0, 1, 2, 3])
  qc.x(range(4))
  qc.h(range(4))
  gate = qc.to_gate(label=" Diffusion")
  return gate


def grover_oracle(n):
  """
  Takes the 4 bit string and returns the gate that comprehends
  - Grover Oracle
  - INVERSION
  """
  qc = QuantumCircuit(4)
  if (n[3] != str(1)):
    qc.x(0)
  if (n[2] != str(1)):
    qc.x(1)
  if (n[1] != str(1)):
    qc.x(2)
  if (n[0] != str(1)):
    qc.x(3)
  qc.append(cccZ(), [0, 1, 2, 3])
  if (n[3] != str(1)):
    qc.x(0)
  if (n[2] != str(1)):
    qc.x(1)
  if (n[1] != str(1)):
    qc.x(2)
  if (n[0] != str(1)):
    qc.x(3)
  gate = qc.to_gate(label=' Grover Oracle')
  return gate

def grover_iteration(inp):
  """
  Receives a quantum circuit as input, creates the corresponding grover algorithm, 
  appends the input to the circuit, and returns it converted into a gate. 
  """
  qc = QuantumCircuit(4)
  qc.append(grover_oracle(inp), [0, 1, 2, 3])
  qc.append(grover_difussion_operator(), [0, 1, 2, 3])
  gate = qc.to_gate(label = ' Grover Iterate')
  return gate
