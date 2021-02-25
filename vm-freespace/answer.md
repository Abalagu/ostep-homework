## Q1
```text
seed 0
size 100
baseAddr 1000
headerSize 0
alignment -1
policy BEST
listOrder ADDRSORT
coalesce False
numOps 10
range 10
percentAlloc 50
allocList 
compute False

ptr[0] = Alloc(3) returned ?
List? 

Free(ptr[0])
returned ?
List? 

ptr[1] = Alloc(5) returned ?
List? 

Free(ptr[1])
returned ?
List? 

ptr[2] = Alloc(8) returned ?
List? 

Free(ptr[2])
returned ?
List? 

ptr[3] = Alloc(8) returned ?
List? 

Free(ptr[3])
returned ?
List? 

ptr[4] = Alloc(2) returned ?
List? 

ptr[5] = Alloc(7) returned ?
List? 
```

## A1
be careful that the free memory list does not coalesce.  when freed, it remains as a small block as is.

given base addr 1000, and size 100, the memory range would be `[1000,1100)`.  
1. alloc(3), return addr = 1000, free list `[1003,1100)`
2. free, return None, free list `[1000,3], [1003, 97]`
3. alloc(5), return addr 1000, free list `[1000, 3], [1008, 92]`
4. free(), `[1000, 3], [1003, 5], [1008, 92]`
5. alloc(8), `[1000, 3], [1003, 5], [1016, 84]`
6. free(), `[1000, 3], [1003, 5], [1008, 8], [1016, 84]`
7. alloc(8), `[1000, 3], [1003, 5], [1016, 84]`
8. free(), `[1000, 3], [1003, 5], [1008, 8], [1016, 84]`
9. alloc(2), free list `[1002, 1], [1003, 5], [1008, 8], [1016, 84]` 
10. alloc(7), free list `[1002, 1], [1003, 5], [10015, 1], [1016, 84]`

## Q4
free list orderings
### first fit
the sorting affects how first fit picks free space.  if based on free space, then it generally results in more small fragmented blocks; if based on address, then it results in more fragmented blocks at the beginning, as search begins at the head.  

### worst fit
if using size sort, then the largest free block can be picked instantly if it fits, or it fails; 

### best fit
if using size sort, then search from the beginning of the free array, then return the first that matches.  

## Q5
without using coalescing, allocation to large blocks will fail eventually, as all blocks are fragmented.  Also it leads to longer search time, a fail cannot be confirmed until searching through the whole long list.





