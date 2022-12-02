def read_input(path: str) -> list[list[int]]:
    raw_data = []
    with open(path, "r") as f:
        elf_inventory = []
        for line in f.readlines():
            line = line.strip()
            if line:
                elf_inventory.append(int(line))
            else:
                raw_data.append(elf_inventory)
                elf_inventory = []
    raw_data.append(elf_inventory)
    return raw_data
