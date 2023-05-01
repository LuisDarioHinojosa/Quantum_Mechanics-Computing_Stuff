# Quantum Gates Utils (Currently Not Implemented)
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import math

# midpoint qubit comparison circuit 
def mqcc():
  mqcc_qr = QuantumRegister(4)
  mqcc_qc = QuantumCircuit(mqcc_qr)

  # loss than / greater than
  mqcc_qc.cx(mqcc_qr[0],mqcc_qr[2])
  mqcc_qc.crx(-math.pi/2,mqcc_qr[2],mqcc_qr[3])
  mqcc_qc.cx(mqcc_qr[1],mqcc_qr[2])
  mqcc_qc.csx(mqcc_qr[1],mqcc_qr[3])
  mqcc_qc.csx(mqcc_qr[2],mqcc_qr[3])
  mqcc_qc.cx(mqcc_qr[3],mqcc_qr[2])

  # equal
  mqcc_qc.x(mqcc_qr[0])
  mqcc_qc.cx(mqcc_qr[0],mqcc_qr[1])
  return mqcc_qc

# quantum bit string circuit
def qbsc():
  qcr = QuantumRegister(3)
  qbsc = QuantumCircuit(qcr)
  qbsc.csx(qcr[1],qcr[2])
  qbsc.cx(qcr[0],qcr[1])
  qbsc.crx(-math.pi/2,qcr[0],qcr[2])
  qbsc.csx(qcr[1],qcr[2])
  qbsc.cx(qcr[0],qcr[1])
  return qbsc

# quantum half adder
def qha():
  qha_qr = QuantumRegister(3)
  qha_template = QuantumCircuit(qha_qr)
  qha_template.ccx(qha_qr[0],qha_qr[1],qha_qr[2])
  qha_template.cnot(qha_qr[0],qha_qr[1])
  return qha_template

# quantum full adder
def qfa():
  qfa_qr = QuantumRegister(4)
  qfa_template = QuantumCircuit(qfa_qr)
  qfa_template.csx(qfa_qr[1],qfa_qr[3])
  qfa_template.cx(qfa_qr[0],qfa_qr[1])
  qfa_template.csx(qfa_qr[2],qfa_qr[3])
  qfa_template.csx(qfa_qr[0],qfa_qr[3])
  qfa_template.cx(qfa_qr[1],qfa_qr[2])
  qfa_template.crx(-math.pi / 2,qfa_qr[2],qfa_qr[3])
  return qfa_template

# quantum full substractor
def qfs():
  qfs_qr = QuantumRegister(4)
  qfs_template = QuantumCircuit(qfs_qr)
  qfs_template.crx(-math.pi / 2,qfs_qr[2],qfs_qr[3]) # vgate dagger
  qfs_template.cx(qfs_qr[1],qfs_qr[2])
  qfs_template.csx(qfs_qr[1],qfs_qr[3]) #vgate
  qfs_template.cx(qfs_qr[0],qfs_qr[2])
  qfs_template.csx(qfs_qr[0],qfs_qr[3])
  qfs_template.csx(qfs_qr[2],qfs_qr[3])
  return qfs_template

# quantum half substractor
def qhs():
  qhs_qr = QuantumRegister(3)
  qhs_template = QuantumCircuit(qhs_qr)
  qhs_template.crx(-math.pi / 2,qhs_qr[1],qhs_qr[2])
  qhs_template.cx(qhs_qr[0],qhs_qr[1])
  qhs_template.csx(qhs_qr[0],qhs_qr[2])
  qhs_template.csx(qhs_qr[1],qhs_qr[2])
  return qhs_template

# quantum multiplexed
def qmux():
  qmux_q = QuantumRegister(6)
  q_mux_template = QuantumCircuit(qmux_q)
  q_mux_template.cswap(qmux_q[1],qmux_q[2],qmux_q[3])
  q_mux_template.cswap(qmux_q[1],qmux_q[4],qmux_q[5])
  q_mux_template.cswap(qmux_q[0],qmux_q[3],qmux_q[5])
  return q_mux_template

# quantum demultiplexer
def qdemux():
  qdemux_q = QuantumRegister(6)
  q_demux_template = QuantumCircuit(qdemux_q)
  q_demux_template.cswap(qdemux_q[1],qdemux_q[2],qdemux_q[3])
  q_demux_template.cswap(qdemux_q[0],qdemux_q[2],qdemux_q[4])
  q_demux_template.cswap(qdemux_q[0],qdemux_q[3],qdemux_q[5])
  return q_demux_template

# quantum_multiplier 2 to 1
def q_mult_2_1():
  qr = QuantumRegister(10)
  qc = QuantumCircuit(qr)
  # add the tofoli gates to copy the x bits to the full adder's input'
  qc.ccx(qr[0],qr[1],qr[3])
  qc.ccx(qr[0],qr[2],qr[7])
  # instance two quantum full adders
  qfa_1 = qfa()
  qfa_2 = qfa()
  qc.append(qfa_1,[qr[3],qr[4],qr[5],qr[6]])
  qc.append(qfa_2,[qr[7],qr[8],qr[6],qr[9]])
  return qc

def q_mult_2_2():
  qr = QuantumRegister(14)
  qc = QuantumCircuit(qr)

  # copy qubits into the adders' inputs 
  qc.ccx(qr[0],qr[2],qr[4])
  qc.ccx(qr[0],qr[3],qr[8])
  qc.ccx(qr[1],qr[2],qr[9])
  qc.ccx(qr[1],qr[3],qr[11])

  # instance quantum full adders
  qfa_1 = qfa()
  qfa_2 = qfa()
  qfa_3 = qfa()

  # add the full adders
  qc.append(qfa_1,[qr[4],qr[5],qr[6],qr[7]])
  qc.append(qfa_2,[qr[8],qr[9],qr[7],qr[10]])
  qc.append(qfa_3,[qr[11],qr[12],qr[10],qr[13]])

  return qc

"""
In order for the encoder and decoder to work, some qubits must be set to |1> at the begginning of the circuit.
Therefore, the 'initialize_quantum_state' option will set the corresponding qubits to |1> if set to 'True'.
You may or may not need it depeding on the experiment. This is why the option was added.
"""

# quantum encoder bcd 
def quantum_bdc_encoder_4_2(initialize_quantum_state = False):
  # instance quantum circuit
  qr = QuantumRegister(6)
  qc = QuantumCircuit(qr)
  # apply not gates
  qc.x(qr[0])
  qc.x(qr[1])
  qc.x(qr[2])

  if initialize_quantum_state:
    # these are because we must send |1> to the 4 and 5th qubits
    qc.x(qr[4])
    qc.x(qr[5])
  
  # apply toffoli gates
  qc.ccx(qr[0],qr[1],qr[4])
  qc.ccx(qr[0],qr[2],qr[5])
  return qc

# quantum decoder bcd 
def quantum_bdc_decoder_4_2(initialize_quantum_state = False):
  # instance quantum circuit
  qr = QuantumRegister(4)
  qc = QuantumCircuit(qr)
  if initialize_quantum_state:
    # this gate must receibe |1> on for the circuit to work
    qc.x(qr[3])
  # build the quantum circuit
  qc.cx(qr[0],qr[3])
  qc.ccx(qr[1],qr[3],qr[2])
  qc.cx(qr[2],qr[1])
  qc.swap(qr[0],qr[1])
  qc.cx(qr[2],qr[3])
  qc.cx(qr[0],qr[1])

  return qc


"""
This two functions provide the functionality required to simulate a quantum shifter and rotator (classical computing bit operations).
One is for performing the operations to the left, and the other one is of performing the operations to the right.
The main difference between the quantum shifter and the quantion rotator is that one losses the information and the other one shifts 
the last bit to the oposite side of the sequence.
You may change the function's functionality depending on the qubits you measure:

|        | rotator     | shifter   |
|--------|-------------|-----------|
| qubits | [1,2,3,4,5] | [1,2,3,4] |

Like with the quantum encoder and decoder, you need a qubit in the exited state |1> for the circuit to work.
You may set up the initialize_quantum_state parameter to True for it to be initialized, but it depends on the problem context.
"""

def right_shifter_rotator(initialize_quantum_state = False):
  QUBIT_NUM = 6
  qr = QuantumRegister(QUBIT_NUM)
  qc = QuantumCircuit(qr)
  # initialized ket 0 to |1>
  if initialize_quantum_state:
    qc.x(qr[0])
  # implement quantum circuit
  qc.cswap(qr[0],qr[1],qr[2])
  qc.cswap(qr[0],qr[2],qr[3])
  qc.cswap(qr[0],qr[3],qr[4])
  qc.cswap(qr[0],qr[4],qr[5])
  return qc

def left_shifter_rotator(initialize_quantum_state = False):
  QUBIT_NUM = 6
  qr = QuantumRegister(QUBIT_NUM)
  qc = QuantumCircuit(qr)
  # initialized ket 0 to |1>
  if initialize_quantum_state:
    qc.x(qr[0])
  # implement quantum circuit
  qc.cswap(qr[0],qr[4],qr[5])
  qc.cswap(qr[0],qr[3],qr[4])
  qc.cswap(qr[0],qr[2],qr[3])
  qc.cswap(qr[0],qr[1],qr[2])
  return qc
