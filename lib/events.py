
class Header:
    def __init__(self, head):
        self.date = head[0]
        self.time = head[1]
        self.second = head[2]
        self.lat_one = head[3]
        self.lat_two = head[4]
        self.lon = head[5]
        self.depth = head[6]
        self.mag = head[7]
        self.n_phas = 0 #head[8]
        self.gap = head[9]
        self.dmin = head[10]
        self.rms = head[11]
        self.erh = head[12]
        self.erz = head[13]
        self.qm = head[14]
        self.n_stns = head[15]
        self.wave_form = head[16]
        self.volcano_id = head[17]
        self.user_id = head[18]
        self.richter_mag = head[19]

class Event:
    def __init__(self, head, phases):
        self.head = Header(head)
        self.stns = phases
        self.phases = 0
    

