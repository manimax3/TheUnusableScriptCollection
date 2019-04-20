#!/bin/bash
echo "Kexecint new kernel"
sudo kexec -l /boot/vmlinuz --initrd=/boot/initrd --reuse-cmdline
sudo systemctl kexec
