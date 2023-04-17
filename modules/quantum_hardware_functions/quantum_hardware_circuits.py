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
  qc.append(qfa_2,[qr[6],qr[7],qr[8],qr[9]])
  return qc
