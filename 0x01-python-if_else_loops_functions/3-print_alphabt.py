#!/usr/bin/python3
print("".join(["{:c}".format(i) for i in range(ord('\
a'), ord('z')+1) if i not in [ord('q'), ord('e')]]), end="")
