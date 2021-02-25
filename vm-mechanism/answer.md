# Answer
## Q1
### seed 1
ARG seed 1
ARG address space size 1k
ARG phys mem size 16k

Base-and-Bounds register information:

  Base   : 0x0000363c (decimal 13884)
  Limit  : 290

Virtual Address Trace
  VA  0: 0x0000030e (decimal:  782) --> PA or segmentation violation?
  VA  1: 0x00000105 (decimal:  261) --> PA or segmentation violation?
  VA  2: 0x000001fb (decimal:  507) --> PA or segmentation violation?
  VA  3: 0x000001cc (decimal:  460) --> PA or segmentation violation?
  VA  4: 0x0000029b (decimal:  667) --> PA or segmentation violation?

### Answer 1
those above limit are segmentation violations
0: 782 > 290, violation
1: 261 < 290, physical address = 13884 + 261
2: 507 > 290, violation
3: 460 > 290, violation
4: 667 > 290, violation

### seed 2
Base-and-Bounds register information:

Base   : 0x00003ca9 (decimal 15529)
Limit  : 500

Virtual Address Trace
VA  0: 0x00000039 (decimal:   57) --> PA or segmentation violation?
VA  1: 0x00000056 (decimal:   86) --> PA or segmentation violation?
VA  2: 0x00000357 (decimal:  855) --> PA or segmentation violation?
VA  3: 0x000002f1 (decimal:  753) --> PA or segmentation violation?
VA  4: 0x000002ad (decimal:  685) --> PA or segmentation violation?

### Answer 2
0: 57 < 500, physical address = 15529 + 57
1: 86 < 500, physical address = 15529 + 86
2: 855 > 500, violation
3: 753 > 500, violation
4: 685 > 500, violation

### seed 3
Base-and-Bounds register information:

Base   : 0x000022d4 (decimal 8916)
Limit  : 316

Virtual Address Trace
VA  0: 0x0000017a (decimal:  378) --> PA or segmentation violation?
VA  1: 0x0000026a (decimal:  618) --> PA or segmentation violation?
VA  2: 0x00000280 (decimal:  640) --> PA or segmentation violation?
VA  3: 0x00000043 (decimal:   67) --> PA or segmentation violation?
VA  4: 0x0000000d (decimal:   13) --> PA or segmentation violation?

### Answer 3
0: 378 > 316, violation
1: 618 > 316, violation
2: 640 > 316, violation
3: 67 < 316, physical address = 8916 + 67
4: 13 < 316, physical address = 8916 + 13

## Q2
###