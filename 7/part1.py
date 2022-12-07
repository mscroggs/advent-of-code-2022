from abc import ABC, abstractmethod


class Filesystem:
    def __init__(self):
        self.dirs = []


class Base(ABC):
    def __init__(self, name, fs):
        self.name = name
        self.fs = fs
        self.parent = None

    @abstractmethod
    def size(self):
        pass

class Dir(Base):
    def __init__(self, name, fs):
        super().__init__(name, fs)
        self.contents = []

    def size(self):
        return sum(i.size() for i in self.contents)

    def cd(self, fname):
        if fname == "..":
            return self.parent
        for i in self.contents:
            if i.name == fname:
                return i
        raise ValueError("No folder")

    def mkdir(self, fname):
        d = Dir(fname, self.fs)
        d.parent = self
        self.contents.append(d)
        self.fs.dirs.append(d)

    def mkfile(self, fname, size):
        f = File(size, fname, self.fs)
        self.contents.append(f)


class File(Base):
    def __init__(self, size, name, fs):
        super().__init__(name, fs)
        self._size = size

    def size(self):
        return self._size


fs = Filesystem()
dirs = []
current_dir = None
with open("input") as f:
    for commands in f.read().split("$ ")[1:]:
        commands = commands.strip()
        if commands.startswith("cd "):
            fname = commands[3:]
            if current_dir is None:
                assert fname == "/"
                current_dir = Dir("/", fs)
            else:
                current_dir = current_dir.cd(fname)
        else:
            assert commands.startswith("ls")
            for line in commands.split("\n")[1:]:
                size, name = line.split()
                if size == "dir":
                    current_dir.mkdir(name)
                else:
                    current_dir.mkfile(name, int(size))

print(sum(d.size() for d in fs.dirs if d.size() <= 100000))
