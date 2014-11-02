from __future__ import print_function

from metakernel import MetaKernel


class EchoKernel(MetaKernel):
    implementation = 'Echo'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    banner = "Echo kernel - as useful as a parrot"

    def get_usage(self):
        return "This is the echo kernel."

    def do_execute_direct(self, code):
        return code.rstrip()

    def repr(self, data):
        return repr(data)

if __name__ == '__main__':
    from IPython.kernel.zmq.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=EchoKernel)