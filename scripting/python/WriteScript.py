import os
import sys
import struct

class Opcode:
    name = "Unknown";
    opcodeIndex = 0;
    argByteCount = 0;
    
    def __init__(self, name, index, argByteCount):
        self.name = name;
        self.opcodeIndex = index;
        self.argByteCount = argByteCount;

class ScriptOp:
    opcodeDesc = None;
    argBytes = None;
    
    def __init__(self, desc, argBytes):
        self.opcodeDesc = desc;
        self.argBytes = argBytes;

udgOpcodes = list();

scriptData = list();
strArray = list();
nametags = list();

def initOpcodeList():
    udgOpcodes.append(Opcode("SetTextCount", 0, 2));
    udgOpcodes.append(Opcode("Text", 1, 2));
    
    udgOpcodes.append(Opcode("SkipByte_0x02", 2, 1));
    udgOpcodes.append(Opcode("SkipByte_0x03", 3, 1));
    
    udgOpcodes.append(Opcode("Continue_0x04", 4, 4));
    
    udgOpcodes.append(Opcode("Movie", 5, 3));
    udgOpcodes.append(Opcode("FlashAnim", 6, 4));
    udgOpcodes.append(Opcode("Voiceline", 7, 5));
    udgOpcodes.append(Opcode("Music", 8, 3));
    udgOpcodes.append(Opcode("SoundEffect", 9, 3));
    
    udgOpcodes.append(Opcode("op_0x0A", 0x0A, 2));
    udgOpcodes.append(Opcode("op_0x0B", 0x0B, 3));
    
    udgOpcodes.append(Opcode("WaitForInput", 0x0C, 0));
    udgOpcodes.append(Opcode("Continue_0x0D", 0x0D, 4));
    udgOpcodes.append(Opcode("LoadNextScript", 0x0E, 6));
    
    udgOpcodes.append(Opcode("op_0x0F", 0x0F, 0));
    
    udgOpcodes.append(Opcode("op_0x10", 0x10, 6));
    udgOpcodes.append(Opcode("op_0x11", 0x11, 0));
    
    udgOpcodes.append(Opcode("Sprite", 0x12, 5));
    udgOpcodes.append(Opcode("ScreenFlash", 0x13, 7));
    
    udgOpcodes.append(Opcode("op_0x14", 0x14, 5));
    
    udgOpcodes.append(Opcode("SetNametag", 0x15, 1));
    udgOpcodes.append(Opcode("ScreenFade", 0x16, 3));
    
    udgOpcodes.append(Opcode("SetFlag", 0x17, 3));
    
    udgOpcodes.append(Opcode("DefineLabel", 0x18, 2));
    udgOpcodes.append(Opcode("DisplayTextbox", 0x19, 1));
    udgOpcodes.append(Opcode("ValueOperation", 0x1A, 4));
    udgOpcodes.append(Opcode("GoToLabel", 0x1B, 2));
    
    udgOpcodes.append(Opcode("op_0x1C", 0x1C, 4));
    udgOpcodes.append(Opcode("op_0x1D", 0x1D, 4));
    udgOpcodes.append(Opcode("op_0x1E", 0x1E, 8));
    udgOpcodes.append(Opcode("op_0x1F", 0x1F, 4));
    
    udgOpcodes.append(Opcode("op_0x20", 0x20, 3));
    udgOpcodes.append(Opcode("op_0x21", 0x21, 3));
    udgOpcodes.append(Opcode("op_0x22", 0x22, 2));
    udgOpcodes.append(Opcode("op_0x23", 0x23, 2));
    
    udgOpcodes.append(Opcode("SkipShort_0x24", 0x24, 2));
    
    udgOpcodes.append(Opcode("End", 0x25, 0));
    
    udgOpcodes.append(Opcode("op_0x26", 0x26, 6));
    udgOpcodes.append(Opcode("op_0x27", 0x27, 3));
    udgOpcodes.append(Opcode("op_0x28", 0x28, 3));
    udgOpcodes.append(Opcode("op_0x29", 0x29, 3));
    udgOpcodes.append(Opcode("op_0x2A", 0x2A, 2));
    udgOpcodes.append(Opcode("op_0x2B", 0x2B, 4));
    udgOpcodes.append(Opcode("op_0x2C", 0x2C, 6));
    udgOpcodes.append(Opcode("op_0x2D", 0x2D, 6));
    udgOpcodes.append(Opcode("op_0x2E", 0x2E, 6));
    udgOpcodes.append(Opcode("op_0x2F", 0x2F, 1));
    
    udgOpcodes.append(Opcode("SpfCommand", 0x30, 8));
    
    udgOpcodes.append(Opcode("op_0x31", 0x31, 6));
    
    udgOpcodes.append(Opcode("FlagCheck", 0x32, 4));
    
    udgOpcodes.append(Opcode("op_0x33", 0x33, 5));
    udgOpcodes.append(Opcode("op_0x34", 0x34, 5));
    udgOpcodes.append(Opcode("op_0x35", 0x35, 5));
    udgOpcodes.append(Opcode("op_0x36", 0x36, 2));
    
    udgOpcodes.append(Opcode("SkipShort_0x37", 0x37, 2));
    
    udgOpcodes.append(Opcode("NoOperation_0x38", 0x38, 1));
    udgOpcodes.append(Opcode("DialogWindowTextIndex", 0x39, 4));
    
    udgOpcodes.append(Opcode("op_0x3A", 0x3A, 8));
    udgOpcodes.append(Opcode("op_0x3B", 0x3B, 8));
    udgOpcodes.append(Opcode("op_0x3C", 0x3C, 6));
    udgOpcodes.append(Opcode("op_0x3D", 0x3D, 10));
    udgOpcodes.append(Opcode("op_0x3E", 0x3E, 8));
    udgOpcodes.append(Opcode("op_0x3F", 0x3F, 4));
    
    udgOpcodes.append(Opcode("op_0x40", 0x40, 6));
    udgOpcodes.append(Opcode("op_0x41", 0x41, 8));
    udgOpcodes.append(Opcode("op_0x42", 0x42, 5));
    udgOpcodes.append(Opcode("op_0x43", 0x43, 3));
    udgOpcodes.append(Opcode("op_0x44", 0x44, 12));
    udgOpcodes.append(Opcode("op_0x45", 0x45, 6));
    udgOpcodes.append(Opcode("op_0x46", 0x46, 6));
    udgOpcodes.append(Opcode("op_0x47", 0x47, 6));
    udgOpcodes.append(Opcode("op_0x48", 0x48, 6));
    udgOpcodes.append(Opcode("op_0x49", 0x49, 6));
    udgOpcodes.append(Opcode("op_0x4A", 0x4A, 6));
    udgOpcodes.append(Opcode("op_0x4B", 0x4B, 6));
    udgOpcodes.append(Opcode("op_0x4C", 0x4C, 0));
    udgOpcodes.append(Opcode("op_0x4D", 0x4D, 5));
    udgOpcodes.append(Opcode("op_0x4E", 0x4E, 7));
    
    udgOpcodes.append(Opcode("NoOp", 0x4F, 0));

def initNametagList():
    nametags.append("komaru");
    nametags.append("toko");
    nametags.append("genocider");
    nametags.append("masaru");
    nametags.append("kemuri");
    nametags.append("kotoko");
    nametags.append("nagisa");
    nametags.append("monaca");
    nametags.append("nagito");
    nametags.append("kurokuma");
    nametags.append("haiji");
    nametags.append("tokuichi");
    nametags.append("shirokuma");
    nametags.append("yuta");
    nametags.append("hiroko");
    nametags.append("unknown");
    nametags.append("makoto");
    nametags.append("byakuya");
    nametags.append("mk_kid1");
    nametags.append("mk_kid2");
    nametags.append("ff");
    nametags.append("ff_a");
    nametags.append("ff_b");
    nametags.append("ff_c");
    nametags.append("ff_d");
    nametags.append("ff_e");
    nametags.append("ff_f");
    nametags.append("adult");
    nametags.append("adult_a");
    nametags.append("adult_b");
    nametags.append("adult_c");
    nametags.append("adult_d");
    nametags.append("adult_e");
    nametags.append("adult_f");
    nametags.append("adult_g");
    nametags.append("adult_h");
    nametags.append("adult_i");
    nametags.append("adult_j");
    nametags.append("adult_k");
    nametags.append("adult_l");
    nametags.append("adult_m");
    nametags.append("adult_n");
    nametags.append("adult_o");
    nametags.append("adult_p");
    nametags.append("adult_q");
    nametags.append("adult_r");
    nametags.append("adult_s");
    nametags.append("adult_t");
    nametags.append("adult_u");
    nametags.append("adult_v");
    nametags.append("adult_w");
    nametags.append("adult_x");
    nametags.append("adult_y");
    nametags.append("adult_z");
    nametags.append("adults");
    nametags.append("adult1");
    nametags.append("adult2");
    nametags.append("dummy1");
    nametags.append("dummy2");
    nametags.append("dummy3");
    nametags.append("dummy4");
    nametags.append("dummy5");
    nametags.append("dummy6");
    nametags.append("dummy7");
    nametags.append("dummy8");
    nametags.append("dummy9");
    nametags.append("dummy10");
    nametags.append("dummy11");
    nametags.append("tutorial");
    nametags.append("junko");
    nametags.append("warriors_of_hope");
    nametags.append("shop_manager");
    nametags.append("blank");
    nametags.append("unknown2");
    nametags.append("unknown3");

def GetUTF16StringReadSize(file):
    basePos = file.tell();
    count = 0;
    
    while(True):
        c = int.from_bytes(file.read(2), byteorder="little");
        if (c == 0):
            break;
        
        count += 2;
    
    file.seek(basePos, os.SEEK_SET);
    return count;

def GetOpcodeDescFromString(string):
    for i in range(0, len(udgOpcodes)):
        opcodeDesc = udgOpcodes[i];
        nameLength = len(opcodeDesc.name);
        
        if (opcodeDesc.name == string[0:nameLength]):
            return opcodeDesc;
            
    return None;
    
def GetOpcodeArguments(opcodeDesc, string):
    opNameLength = len(opcodeDesc.name);
    argsStart = opNameLength + 1; # Each line must contain a "(" after the opcode name
    argsEnd = len(string) - 3; # Each line must end with a ");"
    
    argsString = string[argsStart:argsEnd];
    if opcodeDesc.opcodeIndex == 0x0001:
        return [argsString];
    
    args_split = argsString.split(",");
    
    for i in range(0, len(args_split)):
        args_split[i] = args_split[i].strip();
    
    return args_split;
    
def GetNametagIndex(nametag):
    for i in range(0, len(nametags)):
        if nametag == nametags[i]:
            return i;
            
    return 0xFF;

def ConvertEscapeSequences(string):
    strBytes = "";
    
    i = 0;
    while(i < len(string)):
        c = string[i];
        
        match(c):
            case '\\':
                nextC = string[i + 1];
                if (nextC == 'n'):
                    strBytes += '\n';
                elif (nextC == 'r'):
                    strBytes += '\r';
                elif (nextC == '\\'):
                    strBytes += '\\';
                i += 1;
            case _:
                strBytes += c;
                
        i += 1;
    
    return strBytes;

def main():
    if (len(sys.argv) < 3):
        print("Usage: WriteScript.py <input.txt> <output.lin>");
        return;
    
    initOpcodeList();
    initNametagList();
    
    # -------------------
    
    scriptTextFile = open(sys.argv[1], "r");
    
    scriptTextFile.seek(0, os.SEEK_END);
    scriptTextFileSize = scriptTextFile.tell();
    scriptTextFile.seek(0, os.SEEK_SET);
    
    lineNum = 0;
    
    while(True):
        line = scriptTextFile.readline().lstrip();
        lineNum += 1;
        
        if (len(line) == 0):
            if (scriptTextFile.tell() == scriptTextFileSize):
                break;
            continue;
            
        opcodeDesc = GetOpcodeDescFromString(line);
        if (opcodeDesc == None):
            print(f"Unknown operation \"{line}\" at line {lineNum}");
            return;
            
        args = GetOpcodeArguments(opcodeDesc, line);
        argBytes = bytes();
        
        if opcodeDesc.argByteCount > 0:    
            match(opcodeDesc.opcodeIndex):
                case 0x01: # Text
                    argBytes = struct.pack(">H", len(strArray));
                    strArray.append(ConvertEscapeSequences(args[0]));
                case 0x15: # SetNametag
                    nametagIndex = GetNametagIndex(args[0]);
                    argBytes = struct.pack(">B", nametagIndex);
                case 0x18 | 0x1B: # DefineLabel | GoToLabel
                    argBytes = struct.pack(">H", int(args[0]));
                case 0x32: # FlagCheck
                    argBytes = struct.pack(">HBB", int(args[0]), int(args[1]), int(args[2]));
                case 0x30: # SpfCommand
                    argBytes = struct.pack(">HHHH", int(args[0]), int(args[1]), int(args[2]), int(args[3]));
                case 0x39: # DialogWindowTextIndex
                    argBytes = struct.pack(">HH", int(args[0]), int(args[1]));
                case _:
                    for i in range(0, len(args)):
                        try:
                            argBytes += struct.pack("B", int(args[i]));
                        except:
                            print(f"Failed to encode arguments for operation \"{line}\" at line {lineNum}");
                            return;
           
        scriptData.append(ScriptOp(opcodeDesc, argBytes));
    
    scriptTextFile.close();
    
    # -------------------
    
    scriptBinFile = open(sys.argv[2], "wb");
    scriptBinFile.write(struct.pack("<i", 2));
    scriptBinFile.write(struct.pack("<i", 16)); # Script code start, seems to always be set to 16
    
    scriptBinFile.write(struct.pack("<i", 0)); # String array start, written after script code
    scriptBinFile.write(struct.pack("<i", 0)); # File size, written before closing the file
    
    # String array size opcode prefix
    scriptBinFile.write(struct.pack(">H", 0x7000));
    scriptBinFile.write(struct.pack("<H", len(strArray))); # oh my god bruh, spike chunsoft wtf are you doing
    
    # Script code
    for i in range(0, len(scriptData)):
        scriptOp = scriptData[i];
        opDesc = scriptOp.opcodeDesc;
        
        opcode_encoded = opDesc.opcodeIndex + 0x7000;
        scriptBinFile.write(struct.pack(">H", opcode_encoded));
        
        if len(scriptOp.argBytes) > 0:
            for j in range(0, opDesc.argByteCount):
                scriptBinFile.write(struct.pack("B", scriptOp.argBytes[j]));
        else:
            for j in range(0, opDesc.argByteCount):
                scriptBinFile.write(struct.pack("B", 0xFF));
    
    # String array
    strArrayStart = scriptBinFile.tell();
    strArrayLength = len(strArray);
    scriptBinFile.write(struct.pack("<i", strArrayLength));
    
    # String offsets
    strWriteOffset = 0;
    for i in range(0, strArrayLength):
        string = strArray[i];
        strArrayDataStart = strArrayLength * 4 + 4;
        
        scriptBinFile.write(struct.pack("<i", strArrayDataStart + strWriteOffset));
        strWriteOffset += len(string) * 2 + 2;
        
    # String data
    for i in range(0, strArrayLength):
        string = strArray[i];
        string_u16 = string.encode("utf_16_le");
        
        for j in range(0, len(string_u16)):
            scriptBinFile.write(struct.pack("B", string_u16[j]));
            
        scriptBinFile.write(struct.pack("<H", 0x0000));
    
    fileSize = scriptBinFile.tell();
    
    scriptBinFile.seek(8, os.SEEK_SET);
    scriptBinFile.write(struct.pack("<i", strArrayStart));
    scriptBinFile.write(struct.pack("<i", fileSize));
    
    scriptBinFile.close();
    
main();
