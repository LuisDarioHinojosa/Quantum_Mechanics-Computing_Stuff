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
