with open("inputs/day_03.txt", "r") as text_file:
    lines = text_file.readlines()
    data = [line.strip() for line in lines]

# ======== Part 1 ========
gamma_rate_bits = []
epsilon_rate_bits = []
for col in zip(*data):
    number_bits = sum(int(bit) for bit in col if bit == "1")
    threshold = len(col) // 2
    if number_bits > threshold:
        gamma_rate_bits.append("1")
        epsilon_rate_bits.append("0")
    else:
        gamma_rate_bits.append("0")
        epsilon_rate_bits.append("1")
gamma_rate_bin = int("".join(gamma_rate_bits), 2)
epsilon_rate_bin = int("".join(epsilon_rate_bits), 2)
print(f"gamma_rate_bin: {gamma_rate_bin}, epsilon_rate_bin: {epsilon_rate_bin}")
print(f"product: {gamma_rate_bin * epsilon_rate_bin}")

