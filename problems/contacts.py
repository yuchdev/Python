class Contact:
    def __init__(self, name, default_fn=lambda _: None):
        self.name = name
        self.vals = dict()
        self.default_fn = default_fn

    def __getattr__(self, item):
        if item == "name": 
            return self.name
        return self.vals[item] if item in self.vals else self.default_fn()
        
    def __setattr__(self, item, value):
        if item == "name":
            self.name = value
        else:
            self.vals[item] = value

    def __repr__(self):
        lines = [f"Name: {self.name}"]
        if self.vals:
            lines.append("attributes:")
            lines.extend(f"{k}: {v}" for k, v in self.vals.items())
        return "\n".join(lines)

john = Contact("John Smith")
john.age = 31
print(john)
