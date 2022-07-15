"""
For operations = ["TYPE Code", "TYPE Signal", "MOVE_CURSOR -3", "SELECT 5 8", "TYPE ou", "UNDO", "TYPE nio"], the output should be solution(operations) = "CodeSignaniol".

Initially the text is empty,
After the "TYPE Code" operation, the text is "Code|" (where the | symbol represents the cursor position),
After the "TYPE Signal" operation, the text is "CodeSignal|",
After the "MOVE_CURSOR -3", the cursor moves three symbols back, so the text is "CodeSig|nal",
After the "SELECT 5 8" operation, the selected text is "igna", the cursor is moved to the end of selected area "CodeSigna|l",
After the "TYPE ou" operation, since the previous operation was "SELECT", the selected text is deleted and replaced with the text "ou", the cursor stays after the typed text, so the text is "CodeSou|l",
After the "UNDO" operation, the last operation "TYPE" is undone and text and cursor is back as it was before the "TYPE" operation, so the text is "CodeSigna|l",
After the "TYPE nio" operation, the text is "CodeSignanio|l",
So the final string is "CodeSignaniol".
For operations = ["TYPE MyCat", "SELECT 2 3", "MOVE_CURSOR -1", "TYPE he", "SELECT 0 1", "TYPE His"], the output should be solution(operations) = "HisCheat".

"""
class TextEditor:
    def __init__(self):
        self.s = ""
        self.cursor = 0
        self.selected = None
        self.prevtype = None
        self.prevmovecursor = None
        self.deletedtext = None
        self.deletedcursorpos = None
    
    def type(self, text):
        if self.selected:
            start, end = self.selected
            print(start, end)
            print(self.s)
            print(self.s[5:9])
            self.deletedtext = self.s[int(start): (int(end) + 1)]
            self.deletedcursorpos = self.cursor
            words = list(self.s)
            for i in range(int(start), int(end)+1):
                words[i] = ""
            self.s = "".join(words)
            self.cursor -= (int(end)+1-int(start))
            self.s = self.s[:self.cursor] + text + self.s[self.cursor:]
            self.cursor += len(text)
            self.selected = None
        else:
            self.s = self.s[:self.cursor] + text + self.s[self.cursor:]
            self.cursor += len(text)
        self.prevtype = text
        self.prevmovecursor = None

    def movecursor(self, spaces):
        self.selected = None
        self.cursor += int(spaces)
        self.prevmovecursor = int(spaces)
        self.prevtype = None
    
    def select(self, start, end):
        self.cursor = int(end) + 1
        self.prevmovecursor = None 
        self.prevtype = None
        self.selected = (start, end)
        print("self.selected", self.selected)
    
    def undo(self):
        if self.prevtype:
            print("self.s", self.s)
            print("self.prevtype", self.prevtype)
            print("self.cursor", self.cursor)
            print(self.cursor - len(self.prevtype))
            print(self.s[:self.cursor - len(self.prevtype)])
            self.s = self.s[:self.cursor - len(self.prevtype)] + self.deletedtext + self.s[self.cursor:]
            self.deletedtext = None
            self.cursor = self.deletedcursorpos
            self.deletedcursorpos = None
        if self.prevmovecursor:
            self.movecursor(self, -(self.prevmovecursor))    
        self.prevtype = None
        self.prevmovecursor = None


if __name__ == "__main__":
    operations = ["TYPE Code", "TYPE Signal", "MOVE_CURSOR -3", "SELECT 5 8", "TYPE ou", "UNDO", "TYPE nio"]
    expected = "CodeSignaniol"
    obj = TextEditor()
    for i, operation in enumerate(operations):
        codes = operation.split()
        print(operation)
        if codes[0] == "TYPE":
            print("codes[1]", codes[1])
            print("obj.type", obj.type)
            obj.type(codes[1])
            print("++++++++++++++++++")
        if codes[0] == "MOVE_CURSOR":
            obj.movecursor(codes[1])
        if codes[0] == "SELECT":
            obj.select(codes[1], codes[2])
        if codes[0] == "UNDO":
            obj.undo()
        print(obj.cursor)
        print(obj.s)
    print(obj.s)
    print(expected == obj.s)

    