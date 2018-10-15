class Architecture:
    # Constants:
    MAX_MEMORY = 4096
    PROGRAM_COUNTER_START = 0x200

    def __init__(self):

        # The CHIP-8 had 4k (4096 bytes) of memory
        self.memory = bytearray(self.MAX_MEMORY)

        # The CHIP-8 had a series of registers as follows:
        # 
        #   1 x 16-bit index register        (I)
        #   1 x 16-bit program counter       (PC)
        #   1 x 16-bit stack pointer         (SP)
        #   1 x 8-bit delay timer            (DT)
        #   1 x 8-bit sound timer            (ST)
        # 
        #   16 x 8-bit general registers     (V0 - VF)

        self.GeneralRegisters = {
            0x0: 0,
            0x1: 0,
            0x2: 0,
            0x3: 0,
            0x4: 0,
            0x5: 0,
            0x6: 0,
            0x7: 0,
            0x8: 0,
            0x9: 0,
            0xA: 0,
            0xB: 0,
            0xC: 0,
            0xD: 0,
            0xE: 0,
            0xF: 0,
        }

        self.CpuRegisters = {
            'I' : 0,
            'SP': 0,
            'PC': 0,
            'RPL': bytearray(16)
        }

        self.Timers = {
            'DT': 0,
            'ST': 0,
        }

    def LOAD_ROMFILE(self, filename, offset=PROGRAM_COUNTER_START):
        """
        Load the ROM indicated by the filename into memory.
        """
        ROM = open(filename, 'rb').read()
        for i, value in enumerate(ROM):
            print("Index: {}, value: {}".format(offset+i, hex(value)))
            self.memory[offset + i] = value


if __name__ == '__main__':
    CPU = Architecture()
    CPU.LOAD_ROMFILE("C:\\Users\\shiva\\Downloads\\BRIX")
