import argparse

# very slow
class LZ4Decompressor:
    def __init__(self, data: bytes):
        self.d = data
        self.i = 0
        self.dict = [-1] * 65536
        self.oi = 0
    def out(self, byte):
        self.dict[self.oi] = byte
        self.oi = (self.oi + 1) & 0xffff
    def read_seq(self):
        token = self.d[self.i]
        self.i += 1
        lit_len = token >> 4
        output = []
        copy_len = (token & 0xf) + 4
        if lit_len == 15:
            while self.d[self.i] == 255:
                lit_len += 255
                self.i += 1
            lit_len += self.d[self.i]
            self.i += 1
        # output literal
        for i in range(lit_len):
            ch = self.d[self.i]
            output.append(ch)
            self.out(ch)
            self.i += 1
        if self.i == len(self.d):
            return bytes(output)
        offset = int.from_bytes(self.d[self.i:self.i+2], byteorder='little')
        self.i += 2
        if copy_len == 19:
            while self.d[self.i] == 255:
                copy_len += 255
                self.i += 1
            copy_len += self.d[self.i]
            self.i += 1
        # copy dictionary
        for i in range(copy_len):
            prev_pos = (self.oi - offset) & 0xffff
            out = self.dict[prev_pos]
            output.append(out)
            self.out(out)
        try:
            return bytes(output)
        except:
            print(output)
            raise
    def read(self):
        out = []
        while self.i < len(self.d):
            s=self.read_seq()
            out.append(s)
        return b''.join(out)

# from K4os.Compression.LZ4 pickler format
# repo is https://github.com/MiloszKrajewski/K4os.Compression.LZ4
def read_k4os_lz4_pickler(dat: bytes) -> bytes:
    header = dat[0]
    if header == 0:
        # uncompressed
        return dat[1:]
    
    if header == 0x40:
        size_diff = dat[1]
        pos = 2
    elif header == 0x80:
        size_diff = int.from_bytes(dat[1:3], byteorder='little')
        pos = 3
    elif header == 0xc0:
        size_diff = int.from_bytes(dat[1:5], byteorder='little')
        pos = 5
    else:
        raise TypeError('Unknown K4os.Compresssion.LZ4 header byte {}'.format(header))

    compressed_size = len(dat) - pos
    decompressor = LZ4Decompressor(dat[pos:])
    out_dat = decompressor.read()
    if len(out_dat) != compressed_size + size_diff:
        print(f'Size differs! expected: {compressed_size+size_diff} actual {len(out_dat)}')
    return out_dat

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('infile')
arg_parser.add_argument('outfile')
arg_parser.add_argument('--meta', action='store_true')
args = arg_parser.parse_args()
infile = args.infile

with open(infile, 'rb') as fin:
    dat = fin.read()
    meta_len = int.from_bytes(dat[0:4], byteorder='little')
    meta = read_k4os_lz4_pickler(dat[4:4+meta_len])
    if args.meta:
        with open(args.outfile, 'wb') as fout:
            fout.write(meta)
            exit()
    else:
        print(meta)

    main_dat = read_k4os_lz4_pickler(dat[4+meta_len:])
    with open(args.outfile, 'wb') as fout:
        fout.write(main_dat)
