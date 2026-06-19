class TextFileHandler:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            return 'File not found'
        else:
            return content
    
    def write_file(self, content):
        try:
            with open(self.file_path, 'a', encoding='utf-8') as f:
                f.write(content + '\n')
        except FileNotFoundError:
            return 'File not found'
        
handler = TextFileHandler('example.txt')
print(handler.read_file())
