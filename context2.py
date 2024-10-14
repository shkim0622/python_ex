class func:
    def __init__(self, name, age):
        self.name = name
        self.mode = age
    
    def __enter__(self):
        self.file = open(self.name, self.age)
        return self.file
    
    def __exit__(self, type, value,traceback):
        self.file.close()

# with 문을 사용하여 파일을 열고 닫음
with func('example.txt', 'r') as f:
    contents = f.read()
    print(contents)
