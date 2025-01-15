import json

class Value:
    def __init__(self) -> None:
        try:
            with open("value.json", "r") as file:
                self.data = json.load(file)
        except:
            self.data = {}
            self.save()

    def save(self) -> None:
        with open("value.json", "w") as file:
            json.dump(self.data, file, indent=2)

def fibo(nmb: int, memory: Value) -> int:
    if nmb in [0, 1]:
        return nmb

    str_nmb = str(nmb)
    if str_nmb in memory.data:
        return memory.data[str_nmb]

    result = fibo(nmb-1, memory) + fibo(nmb-2, memory)
    memory.data[str_nmb] = result
    return result