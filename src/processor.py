
class Processor:
    def __init__(self, compiler, arranger, layout, displayer) -> None:
        self.compiler = compiler
        self.arranger = arranger
        self.layout = layout
        self.displayer = displayer

    def process(self, source, scene):
        rooms, exc = self.compiler.compile(source)
        if exc:
            return exc
        self.arranger.arrange(rooms)
        self.displayer.display(room)
    