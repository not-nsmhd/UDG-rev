import os
import sys

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
    udgOpcodes.append(Opcode("LoadEV8", 0x22, 2));
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

def WriteTextboxOpcodeAsText(op, outFile):
    strIndex = int.from_bytes(op.argBytes, byteorder="big");
    string = strArray[strIndex].replace("\n", "\\n");
    
    print(f"Text({string});", file=outFile);
    
def WriteSetNametagAsText(op, outFile):
    nametagIndex = op.argBytes[0];
    
    if (nametagIndex < len(nametags)):
        nametagStr = nametags[nametagIndex];
        print(f"SetNametag({nametagStr});", file=outFile);
    else:
        print(f"SetNametag({nametagIndex});", file=outFile);
    
def WriteMusicCommandAsText(op, outFile):
    index = op.argBytes[0];
    volume = op.argBytes[1];
    arg3 = op.argBytes[2];
    
    if (index == 255):
        index = -1;
    
    print(f"Music({index}, {volume}, {arg3});", file=outFile);
    
def WriteMovieCommandAsText(op, outFile):
    index = int.from_bytes(op.argBytes[0:2], byteorder="big");
    arg2 = op.argBytes[2];
    
    print(f"Movie({index}, {arg2});", file=outFile);
    
def WriteSpfCommandAsText(op, outFile):
    command = int.from_bytes(op.argBytes[0:2], byteorder="big");
    arg1 = int.from_bytes(op.argBytes[2:4], byteorder="big");
    arg2 = int.from_bytes(op.argBytes[4:6], byteorder="big");
    arg3 = int.from_bytes(op.argBytes[6:8], byteorder="big");
    
    print(f"SpfCommand({command}, {arg1}, {arg2}, {arg3});", file=outFile);
    
def WriteValueOperationCommandAsText(op, outFile):
    index = op.argBytes[0];
    opType = op.argBytes[1];
    opValue = int.from_bytes(op.argBytes[2:4], byteorder="big");
    
    opTypeStr = "";
    match(opType):
        case 0:
            opTypeStr = "=";
        case 1:
            opTypeStr = "+";
        case 2:
            opTypeStr = "-";
        case 3:
            opTypeStr = "*";
        case 4:
            opTypeStr = "/";
    
    print(f"ValueOperation({index}, {opTypeStr}, {opValue});", file=outFile);
    
def WriteFlagCheckCommandAsText(op, outFile):
    index = int.from_bytes(op.argBytes[0:2], byteorder="big");
    shouldNotBeEqual = op.argBytes[2];
    testValue = op.argBytes[3];
    
    print(f"FlagCheck({index}, {shouldNotBeEqual}, {testValue});", file=outFile);
    
def WriteBranchStartCommandAsText(op, outFile):
    branchIndex = int.from_bytes(op.argBytes[0:2], byteorder="big");
    print(f"GoToLabel({branchIndex});", file=outFile);
    
def WriteBranchEndCommandAsText(op, outFile):
    branchIndex = int.from_bytes(op.argBytes[0:2], byteorder="big");
    print(f"DefineLabel({branchIndex});", file=outFile);
    
def WriteDialogWindowTextIndexCommandAsText(op, outFile):
    index = int.from_bytes(op.argBytes[0:2], byteorder="big");
    flagToSet = int.from_bytes(op.argBytes[2:4], byteorder="big");
    
    print(f"DialogWindowTextIndex({index}, {flagToSet});", file=outFile);
    
def WriteSetFlagCommandAsText(op, outFile):
    flagToSet = int.from_bytes(op.argBytes[0:2], byteorder="big");
    value = op.argBytes[2];
    
    print(f"SetFlag({flagToSet}, {value});", file=outFile);
    
def WriteLoadNextScriptCommandAsText(op, outFile):
    category = int.from_bytes(op.argBytes[0:2], byteorder="big");
    main = int.from_bytes(op.argBytes[2:4], byteorder="big");
    sub = int.from_bytes(op.argBytes[4:6], byteorder="big");
    
    print(f"LoadNextScript({category}, {main}, {sub});", file=outFile);
    
def WritePrecedingTabs(nestingLevel, outFile):
    for i in range(0, nestingLevel):
        print("\t", end="", file=outFile)

def main():
    if (len(sys.argv) < 2):
        print("No script file has been specified");
        return;
    
    initOpcodeList();
    initNametagList();
    
    scriptFile = open(sys.argv[1], "rb");
    scrType = int.from_bytes(scriptFile.read(4), byteorder="little");
    codeOffset = int.from_bytes(scriptFile.read(4), byteorder="little");
    codeEnd = 0;
    strArrayOffset = 0;
    
    if (scrType == 2):
        strArrayOffset = int.from_bytes(scriptFile.read(4), byteorder="little");
    
    fileSize = int.from_bytes(scriptFile.read(4), byteorder="little");
    
    if (scrType == 2):
        codeEnd = strArrayOffset;
    else:
        codeEnd = fileSize;
    
    while (scriptFile.tell() < codeEnd):
        pos = scriptFile.tell();
        opcode = int.from_bytes(scriptFile.read(2), byteorder="big") - 0x7000;
        
        if (opcode > 0x4F):
            print("Opcode 0x{0:02X} is out of range (pos: {1})".format(opcode, scriptFile.tell()));
            return;
        
        opcodeDesc = udgOpcodes[opcode];
        
        argBytes = scriptFile.read(opcodeDesc.argByteCount);
        scriptData.append(ScriptOp(opcodeDesc, argBytes));
        
        if (opcode == 0x25):
            break;
    
    if (strArrayOffset > 0):
        scriptFile.seek(strArrayOffset, os.SEEK_SET);
        strArraySize = int.from_bytes(scriptFile.read(4), byteorder="little");
    
        for i in range(0, strArraySize):
            strOffset = int.from_bytes(scriptFile.read(4), byteorder="little");
            basePos = scriptFile.tell();
        
            scriptFile.seek(strArrayOffset + strOffset, os.SEEK_SET);
            strSize = GetUTF16StringReadSize(scriptFile);
            string = scriptFile.read(strSize).decode(encoding="utf_16_le");
        
            strArray.append(string);        
            scriptFile.seek(basePos, os.SEEK_SET);
    
    scriptFile.close();
    
    # --------------
    
    scriptTextFilePath = sys.argv[1].replace(".lin", ".txt");
    scriptTextFile = open(scriptTextFilePath, "w");
    
    nestingLevel = 0;
    
    for i in range(0, len(scriptData)):
        op = scriptData[i];
        
        WritePrecedingTabs(nestingLevel, scriptTextFile);
        
        match(op.opcodeDesc.opcodeIndex):
            case 0x00:
                # Fun fact: UDG completely ignores the argument passed into this opcode
                continue;
            case 0x01:
                WriteTextboxOpcodeAsText(op, scriptTextFile);
                continue;
            case 0x08:
                WriteMusicCommandAsText(op, scriptTextFile);
                continue;
            case 0x05:
                WriteMovieCommandAsText(op, scriptTextFile);
                continue;
            case 0x0E:
                WriteLoadNextScriptCommandAsText(op, scriptTextFile);
                continue;
            case 0x15:
                WriteSetNametagAsText(op, scriptTextFile);
                continue;
            case 0x30:
                WriteSpfCommandAsText(op, scriptTextFile);
                continue;
            case 0x17:
                WriteSetFlagCommandAsText(op, scriptTextFile);
                continue;
            case 0x1A:
                WriteValueOperationCommandAsText(op, scriptTextFile);
                continue;
            case 0x32:
                WriteFlagCheckCommandAsText(op, scriptTextFile);
                continue;
            case 0x39:
                WriteDialogWindowTextIndexCommandAsText(op, scriptTextFile);
                continue;
            case 0x1B:
                WriteBranchStartCommandAsText(op, scriptTextFile);
                nestingLevel += 1;
                continue;
            case 0x18:
                WriteBranchEndCommandAsText(op, scriptTextFile);
                nestingLevel -= 1;
                continue;
        
        print(f"{op.opcodeDesc.name}(", end="", file=scriptTextFile);
        for j in range(0, op.opcodeDesc.argByteCount):
            argByte = op.argBytes[j];
            print(f"{argByte}", end="", file=scriptTextFile);
            
            if (j != op.opcodeDesc.argByteCount - 1):
                print(", ", end="", file=scriptTextFile);
            
        print(");", end="\n", file=scriptTextFile);
        
    scriptTextFile.close();
    
main();
