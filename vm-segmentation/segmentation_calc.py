virtual_address = 4200
seg_mask = 0x3000  # 0b11,0000,0000,0000
seg_shift = 12
segment = (virtual_address & seg_mask) >> seg_shift

offset_mask = 0xFFF
offset = virtual_address & offset_mask
