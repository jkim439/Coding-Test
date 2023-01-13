# AND
print("AND\t", bin(0b101 & 0b111))

# OR
print("OR\t", bin(0b101 | 0b111))

# XOR
print("XOR\t", bin(0b101 ^ 0b111))

# NOT
print("NOT\t", bin(~0b101))

# SHIFT
print("SFT\t", bin(0b101 << 2))

# ADD
print("ADD\t", bin(0b101 | (1 << 1)))

# DEL
print("DEL\t", bin(0b101 & ~(1 << 0)))

# PRINT
print("PRT\t", bin(0b101 & (1 << 2)))

# TOGGLE
print("TOG\t", bin(0b101 ^ (1 << 1)))
