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


# ======== Part 2 ========
print("\n\n")
oxygen_candidates = list(data)
counter = 0
while len(oxygen_candidates) > 1:
    number_bits = sum(int(bit) for col in oxygen_candidates for bit in col[counter] if bit == "1")
    threshold = (len(oxygen_candidates) + 1) // 2
    oxygen_reference = "1" if number_bits >= threshold else "0"
    oxygen_candidates = [candidate for candidate in oxygen_candidates if candidate[counter] == oxygen_reference]
    counter += 1

co2_candidates = list(data)
counter = 0
while len(co2_candidates) > 1:
    number_bits = sum(int(bit) for col in co2_candidates for bit in col[counter] if bit == "1")
    threshold = (len(co2_candidates) + 1) // 2
    co2_reference = "0" if number_bits >= threshold else "1"
    co2_candidates = [candidate for candidate in co2_candidates if candidate[counter] == co2_reference]
    counter += 1


oxygen_rate_bin = int("".join(oxygen_candidates[0]), 2)
co2_rate_bin = int("".join(co2_candidates[0]), 2)
print(f"oxygen_rate_bin: {oxygen_rate_bin}, co2_rate_bin: {co2_rate_bin}")
print(f"product: {oxygen_rate_bin * co2_rate_bin}")
