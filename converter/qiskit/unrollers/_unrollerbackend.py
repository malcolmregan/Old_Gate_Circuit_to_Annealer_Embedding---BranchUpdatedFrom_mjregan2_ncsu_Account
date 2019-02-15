

from ._backenderror import BackendError


class UnrollerBackend(object):
    pass


    def __init__(self, basis=None):
        pass


    def set_basis(self, basis):
        pass


    def version(self, version):
        pass


    def new_qreg(self, qreg):
        pass


    def new_creg(self, creg):
        pass


    def define_gate(self, name, gatedata):
        pass


    def u(self, arg, qubit, nested_scope=None):
        pass


    def cx(self, qubit0, qubit1):
        pass


    def measure(self, qubit, bit):
        pass


    def barrier(self, qubitlists):
        pass


    def reset(self, qubit):
        pass


    def set_condition(self, creg, cval):
        pass


    def drop_condition(self):
        pass

    def start_gate(self, name, args, qubits, nested_scope=None, extra_fields=None):
        pass



    def end_gate(self, name, args, qubits, nested_scope=None):
        pass


    def get_output(self):
        pass
