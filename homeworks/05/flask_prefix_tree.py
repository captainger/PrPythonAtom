from flask import Flask, request, jsonify, render_template
from heap.Heap import MinHeap

app = Flask(__name__)

class PrefixTree:
    class Sudgest:
        def __init__(self, string, freq, data_json):
            self.string = string
            self.frequency = freq
            self.json = data_json
        
        def __lt__(self, other):
            if self.frequency < other.frequency:
                return True
            return False
        
        def __gt__(self, other):
            if self.frequency > other.frequency:
                return True
            return False 

    def __init__(self):
        self.root = [{}]
    
    def add(self, string, data_json, freq):
        if self.check(string):
            return
        wrk_dict = self.root
        for char in string:
            if char not in wrk_dict[0]:
                wrk_dict[0][char] = [{}, MinHeap([])]
            wrk_dict = wrk_dict[0][char]
            new_sudg = self.Sudgest(string, freq, data_json)
            if len(wrk_dict[1]) < 10:
                wrk_dict[1].add(new_sudg)
            else:
                min_sudg = wrk_dict[1].extract_minimum()
                wrk_dict[1].add(max(min_sudg, new_sudg))
        wrk_dict.append(data_json)

        
    def check(self, string):
        wrk_dict = self.root
        for i in string:
            if i in wrk_dict[0]:
                wrk_dict = wrk_dict[0][i]
            else:
                return False
        if len(wrk_dict) != 2:
            return True
        return False
    
    def check_part(self, string):
        wrk_dict = self.root
        for i in string:
            if i in wrk_dict[0]:
                wrk_dict = wrk_dict[0][i]
            else:
                return False
        return True

    def return_top(self, string):
        if not self.check_part(string):
            return []
        wrk_dict = self.root
        for char in string:
            wrk_dict = wrk_dict[0][char]
        sudg_list = wrk_dict[1].array.copy()
        sudg_list.sort(reverse=True)
        top = []
        for s in sudg_list:
            sudgest = {'sudgest': s.string, 'json': s.json}
            top.append(sudgest)
        return top
        
        
prfx_tree = PrefixTree()
def init_prefix_tree(filename):
    with open(filename, 'r') as fn:
        for line in fn:
            string = line.split('\t')
            prfx_tree.add(string[0], string[1], string[2])

@app.route("/get_sudgest/<string>", methods=['GET', 'POST'])
def return_sudgest(string):
    sudgest_top = prfx_tree.return_top(string)
    return jsonify(sudgest_top)

@app.route("/")
def hello():
    return render_template('help.html')

if __name__ == "__main__":
    app.run()
