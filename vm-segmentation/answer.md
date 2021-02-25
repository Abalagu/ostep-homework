# Answers
## Q1
### P1
`segmentation.py -a 128 -p 512 -b 0 -l 20 -B 512 -L 20 -s 0`

ARG seed 0
ARG address space size 128
ARG phys mem size 512

Segment register information:

Segment 0 base  (grows positive) : 0x00000000 (decimal 0)
Segment 0 limit                  : 20

Segment 1 base  (grows negative) : 0x00000200 (decimal 512)
Segment 1 limit                  : 20

Virtual Address Trace
VA  0: 0x0000006c (decimal:  108) --> PA or segmentation violation?
VA  1: 0x00000061 (decimal:   97) --> PA or segmentation violation?
VA  2: 0x00000035 (decimal:   53) --> PA or segmentation violation?
VA  3: 0x00000021 (decimal:   33) --> PA or segmentation violation?
VA  4: 0x00000041 (decimal:   65) --> PA or segmentation violation?

### A1
VA 0:
As the address space is of size 128, it is represented by 7 bits, 2**7 = 128.

First convert hex address to binary address to check the highest bit.

va = 108 = 0x6c = 0b1101100, the highest bit is 1, therefore it belongs to segment 1, the space grows backward.

The offset is 108 - 128 = -20, it grows negatively 20 addresses.

Applying the offset to the physical base address 512, actual physical address is 492.


VA 1:
va 1 = 97 = 0b1100001, the highest bit is 1, belonging to segment 1, the stack.

the offset is 97 - 128 = -31

as it exceeds the stack size of 20, it causes segmentation fault.

VA 2:

va2 = 53 = 0b0110101, the offset is 53, exceeding limit of 20, thus segmentation fault. 

## Thoughts

