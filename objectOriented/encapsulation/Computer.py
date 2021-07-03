class Computer:

    def __init__(self, cpu, ram, memory):
        self.cpu = cpu
        self.ram = ram
        self.memory = memory

    def config(self):
        print("config is : ", self.cpu, self.ram, self.memory)


com1 = Computer("i5", "16G", "1TB")
com2 = Computer("i7", "32G", "2TB")

com1.config()
com2.config()
