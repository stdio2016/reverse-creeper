import struct
import array
class CNBTReader:
    def __init__(self, dat: bytes):
        self.d = dat
        self.i = 0
    def readByte(self):
        dat = self.d[self.i]
        self.i += 1
        return dat
    def readNBytes(self, n):
        dat = self.d[self.i:self.i+n]
        self.i += n
        return dat
    def readSByte(self):
        b = self.readByte()
        return b if b < 128 else b - 256
    def readInt16(self):
        return int.from_bytes(self.readNBytes(2), 'little', signed=True)
    def readUInt16(self):
        return int.from_bytes(self.readNBytes(2), 'little', signed=False)
    def readInt32(self):
        return int.from_bytes(self.readNBytes(4), 'little', signed=True)
    def readUInt32(self):
        return int.from_bytes(self.readNBytes(4), 'little', signed=False)
    def readInt64(self):
        return int.from_bytes(self.readNBytes(8), 'little', signed=True)
    def readUInt64(self):
        return int.from_bytes(self.readNBytes(8), 'little', signed=False)
    def readFloat32(self):
        return struct.unpack('f', self.readNBytes(4))[0]
    def readFloat64(self):
        return struct.unpack('d', self.readNBytes(8))[0]
    def readStr(self):
        size = self.readInt16()
        #print(size)
        return self.readNBytes(size).decode('utf8')
    def readVector2(self):
        return struct.unpack('ff', self.readNBytes(8))
    def readVector3(self):
        return struct.unpack('fff', self.readNBytes(12))
    def readVector4(self):
        return struct.unpack('ffff', self.readNBytes(16))
    def readByteArray(self):
        size = self.readInt32()
        return self.readNBytes(size)
    def readIntArray(self):
        size = self.readInt32()
        return array.array('i', self.readNBytes(size * 4))
    def readVector2Array(self):
        size = self.readInt32()
        return [struct.unpack('ff', self.readNBytes(8)) for _ in range(size)]
    def readVector3Array(self):
        size = self.readInt32()
        return [struct.unpack('fff', self.readNBytes(12)) for _ in range(size)]
    def readVector4Array(self):
        size = self.readInt32()
        return [struct.unpack('ffff', self.readNBytes(16)) for _ in range(size)]
    def readFloatArray(self):
        size = self.readInt32()
        return array.array('f', self.readNBytes(size * 4))
    def readList(self):
        tag = self.readByte()
        size = self.readInt32()
        obj = []
        for i in range(size):
            value = self.readTag(tag)
            obj.append(value)
        return obj
    def readStringArray(self):
        size = self.readInt32()
        obj = []
        for i in range(size):
            value = self.readStr()
            obj.append(value)
        return obj
    def readCompound(self):
        obj = {}
        tag = self.readByte()
        while tag != 0:
            name = self.readStr()
            #print(tag, name)
            value = self.readTag(tag)
            obj[name] = value
            if self.i >= len(self.d):
                break
            tag = self.readByte()
        return obj
    def readTag(self, tag):
        if tag == 1:
            return ('int', self.readInt32())
        if tag == 2:
            return ('float', self.readFloat32())
        if tag == 3:
            return self.readStr()
        if tag == 4:
            return self.readList()
        if tag == 5:
            return ('short', self.readInt16())
        if tag == 6:
            return self.readFloat64()
        if tag == 7:
            return self.readByteArray()
        if tag == 8:
            return ('byte', self.readByte())
        if tag == 9:
            return ('long', self.readInt64())
        if tag == 10:
            return self.readCompound()
        if tag == 11:
            return self.readIntArray()
        if tag == 224: # unknown, maybe Vector4i?
            return struct.unpack('<iiii', self.readNBytes(16))
        if tag == 225: # unknown, maybe Vector2i?
            return struct.unpack('<ii', self.readNBytes(8))
        if tag == 226: # unknown, maybe Vector3i?
            return struct.unpack('<iii', self.readNBytes(12))
        if tag == 227:
            return [x != 0 for x in self.readByteArray()]
        if tag == 229:
            return self.readVector4()
        if tag == 230:
            return self.readByte() == 1
        if tag == 231:
            return self.readStringArray()
        if tag == 232:
            return self.readVector2Array()
        if tag == 233:
            return self.readVector3Array()
        if tag == 234:
            return self.readVector2()
        if tag == 235:
            return self.readVector3()
        if tag == 236:
            return ('quaternion', *self.readVector4())
        if tag == 243:
            return self.readFloatArray()
        if tag == 249:
            return ('uint', self.readUInt32())
        if tag == 250:
            return ('ushort', self.readUInt16())
        if tag == 251:
            return ('sbyte', self.readSByte())
        raise TypeError(f'unknown tag {tag}')