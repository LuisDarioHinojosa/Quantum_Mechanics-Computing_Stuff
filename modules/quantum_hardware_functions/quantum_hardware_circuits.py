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
  return mqcc_qc.to_gate(label="MQCC_gate")

# quantum bit string circuit
def qbsc():
  qcr = QuantumRegister(3)
  qbsc = QuantumCircuit(qcr)
  qbsc.csx(qcr[1],qcr[2])
  qbsc.cx(qcr[0],qcr[1])
  qbsc.crx(-math.pi/2,qcr[0],qcr[2])
  qbsc.csx(qcr[1],qcr[2])
  qbsc.cx(qcr[0],qcr[1])
  return qbsc.to_gate(label = "QBSC_gate")

# quantum half adder
def qha():
  qha_qr = QuantumRegister(3)
  qha_template = QuantumCircuit(qha_qr)
  qha_template.ccx(qha_qr[0],qha_qr[1],qha_qr[2])
  qha_template.cnot(qha_qr[0],qha_qr[1])
  return qha_template.to_gate(label = "QHA_gate")

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
  return qfa_template.to_gate(label = "QHA_gate")

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
  return qfs_template.to_gate(label = "QFS_gate")

# quantum half substractor
def qhs():
  qhs_qr = QuantumRegister(3)
  qhs_template = QuantumCircuit(qhs_qr)
  qhs_template.crx(-math.pi / 2,qhs_qr[1],qhs_qr[2])
  qhs_template.cx(qhs_qr[0],qhs_qr[1])
  qhs_template.csx(qhs_qr[0],qhs_qr[2])
  qhs_template.csx(qhs_qr[1],qhs_qr[2])
  return qhs_template.to_gate(label = "QHS_gate")

# quantum multiplexed
def qmux():
  qmux_q = QuantumRegister(6)
  q_mux_template = QuantumCircuit(qmux_q)
  q_mux_template.cswap(qmux_q[1],qmux_q[2],qmux_q[3])
  q_mux_template.cswap(qmux_q[1],qmux_q[4],qmux_q[5])
  q_mux_template.cswap(qmux_q[0],qmux_q[3],qmux_q[5])
  return q_mux_template.to_gate(label = "QMUX_gate")

# quantum demultiplexer
def qdemux():
  qdemux_q = QuantumRegister(6)
  q_demux_template = QuantumCircuit(qmux_q)
  q_demux_template.cswap(qmux_q[1],qmux_q[2],qmux_q[3])
  q_demux_template.cswap(qmux_q[0],qmux_q[2],qmux_q[4])
  q_demux_template.cswap(qmux_q[0],qmux_q[3],qmux_q[5])
  return q_demux_template.to_gate(label = "QDEMUX_gate")

  
