from re import split as re_spl
from datetime import datetime
from lib.events import *

class OutRange(Exception):
    def __init__(self, msg):
        super().__init__(f'{msg}')
        

class Convert_ipn:
    def __init__(self, input, output, stations, format):
        self.count = 0
        self.format = format
        self.name_input = input
        self.name_output = output
        self.name_stations = stations
        self.stations = []
        self.ref_lev = 0 #Nivel de referencia
        self.volcano = []
        self.points_lon = []
        self.points_lat = [] 
        self.points_dep = []

        self.now = datetime.now()

        self.read_config()


    def read_files(self):
        #Archivo ipn
        f_ipn = open(self.name_input, 'r')

        # Archivo de salida
        f_out = open(self.name_output, 'wt') # abrir archivo para escribir

        with open(self.name_stations, 'r') as file:
            self.stations = file.readlines()

        stns = []

        for line in f_ipn:
            line = line.strip()
            #re.split
            C = re_spl(r'[\s]+', line)
            if line == '':
                continue
            if len(C) > 10:
                stns.clear()
                head = [line[:6],line[7:11], line[12:17], line[19], line[21:26], line[27:36],line[38:43],line[46:50], line[51:53], line[54:57], line[58:62], line[63:67], line[69:72],line[74:77], line[78:80], line[81:83], line[84:96], line[97], line[99:102], line[104:107]]
            elif len(C) > 1:
                tmp_line = line[9:]
                tmp_line = tmp_line.strip()
                stn = re_spl(r'[\s]+', tmp_line)
                #stn = [line[:8],line[9:24], line[31:36], line[37], line[39], line[73:77]]
                stn.insert(0, line[:8])
                stns.append(stn)
            else:
                event = Event(head, stns)
                self.calculate(event, f_out)

        f_ipn.close()
        f_out.close()



    def calculate(self, event, f_out):
        lines = []
        date = event.head.date + event.head.time + event.head.second

        lat = float(event.head.lat_one) + float(event.head.lat_two)/60 #Latitud en grados

        tmp_lon = event.head.lon
        lon = float(tmp_lon[0:3]) + float(tmp_lon[3:])/60 #Longitud en grados

        depth = float(event.head.depth) - self.ref_lev

        for value in event.stns:
            try:
                stn = value[0][:4]
                idx_stn = self.search_stn(stn, date)

                
                timeP, timeS = self.calculate_time(value, event.head)

                # 0 Lotos; 1 HipoDD; 2 Velest
                if self.format == 0:
                    stn_line = self.stn_lotos(idx_stn, value, timeP, timeS)
                    lines.append(stn_line)
                elif self.format == 1:
                    stn_line = self.stn_hypoDD(value, timeP, timeS)
                    lines.append(stn_line)
                else:
                    stn_line = self.stn_velest(value, timeP, timeS)
                    for element in stn_line:
                        lines.append(element)

                
                event.phases += 1 if int(value[0][-1]) in range(0,4) else 0
                event.phases += 1 if int(value[0][-1]) in range(0,4) and int(value[4]) in range(0,4) else 0

            except OutRange as m:
                lines = None
                break
            except Exception as e:
                pass
        
        if lines is not None and len(lines) > 0:
            self.points_lon.append(lon)
            self.points_lat.append(lat)
            self.points_dep.append(-depth)

            self.count += 1
            event.head.n_phas = event.phases
            head_line = self.main_line(event.head, lat, lon, depth)
            self.write_file(f_out, head_line, lines)
            lines.clear()


    def write_file(self, file_output, head, lines):
        file_output.write(head)
        if self.format == 2:
            for idx in range(len(lines)):
                if idx % 6 == 0 and idx > 0:
                    file_output.write('\n')
                file_output.write(lines[idx])
            file_output.write('\n\n')
            lines.clear()

        else:
            for idx in range(len(lines)):
                file_output.write(lines[idx])  
            lines.clear()

    def calculate_time(self, value, head):
        start_date = head.date + head.time + head.second
        dateP = value[1]    # yymmddhhmmss.ss onda P
        timeS = value[2]    # HHMM onda S

        # Tiempo de origen del sismo, to
        dto = self.date_to_secs(start_date, '%y%m%d%H%M%S.%f')
        to = datetime.fromtimestamp(dto).strftime('%d-%b-%Y %H:%M:%S.%f')

        # Tiempo de llegada de la onda P, tp_arrv
        dtp = self.date_to_secs(dateP, '%y%m%d%H%M%S.%f')
        tp_arrv = datetime.fromtimestamp(dtp).strftime('%d-%b-%Y %H:%M:%S.%f')

        # Tiempo de viaje de la onda P, tp
        tp =  round(dtp - dto, 4)

        # Tiempo de viaje de la onda S, ts
        ts = round(float(timeS)-float(dateP[10:15])+tp, 4)

        if tp < 0 or tp > 60:
            raise OutRange(f'{start_date[:6]} {start_date[6:10]} {start_date[10:]} tiempo fuera de rango')

        return tp, ts

    # Encabezado evento 
    def main_line(self, head, lat, lon, depth):
        line = ""
        date = head.date+head.time+head.second
        year = head.date[:2]
        tmp_y = '20'+ year if (int(year) in range (0, int(self.now.strftime("%y"))+1)) else '19'+year
        tmp_mag = self.parseFloat(head.mag, "{:4.2f}", 1)
        tmp_eh = self.parseFloat(head.erh, "{:5.2f}", 0)
        tmp_ev = self.parseFloat(head.erz, "{:5.2f}", 0)
        tmp_rms = self.parseFloat(head.rms, "{:5.2f}", 0)

        # 0 Lotos; 1 HipoDD; 2 Velest
        if self.format == 0:
            line = '{:11.5f} {:14.6f} {:14.5f} {:15.0f} {:18.2f}\n'.format(lon, lat, depth, head.n_phas, float(date))
        
        elif self.format == 1:
            line = '# {:4d} {:2d} {:2d} {:2d} {:2d} {:5.2f} {:8.4f} {:9.4f} {:7.2f} {:s} {:s} {:s} {:s} {:10d}\n'.format(
                    int(tmp_y), int(date[2:4]), int(date[4:6]), int(date[6:8]), int(date[8:10]), float(date[10:]), lat, lon, depth, tmp_mag, tmp_eh, tmp_ev, tmp_rms, self.count)
        
        else:
            cns = 'N' if lat > 0 else 'S'
            cew = 'E' if lon > 0 else 'W'
            tmp_lat = abs(lat)
            tmp_lon = abs(lon)
            line = '{:s} {:s} {:5.2f} {:7.4f}{:s} {:8.4f}{:s} {:7.2f}   {:>4s}    {:>3s}     {:>5s}\n'.format(
                    head.date, head.time, float(head.second), tmp_lat, cns, tmp_lon, cew, depth, tmp_mag, head.gap, tmp_rms)
        
        return line


    # Formato phases lotos
    def stn_lotos(self, idx_stn, value, tp, ts):
        line = ""
        waveP=1 #Onda P
        waveS=2 #Onda S
        wgtP = value[0][-1] # Peso onda P
        wgtS = value[4]     # Peso onda S

        if int(wgtP) in range(0,4):
            if int(wgtS) in range(0,4):
                line = '{:12d}{:12}{:11.6f}    \n{:12d}{:12}{:11.6f}    \n'.format(waveP, idx_stn, tp, waveS, idx_stn, ts)
            else:
                line = '{:12d}{:12}{:11.6f}    \n'.format(waveP, idx_stn, tp)

        return line


    # Formato phases hypodd
    def stn_hypoDD(self, value, tp, ts):
        line = ""
        weight = {'0':1.0, '1':0.5, '2':0.2, '3':0.1, '4':0}
        stn = value[0][:4]
        waveP='P' #Onda P
        waveS='S' #Onda S
        wgtP = value[0][-1] # Peso onda P
        wgtS = value[4]     # Peso onda S

        if int(wgtP) in range(0,4):
            if int(wgtS) in range(0,4):
                line = '  {:s}{:11.3f}{:8.3f}{:>4s}\n  {:s}{:11.3f}{:8.3f}{:>4s}\n'.format(stn, tp, weight[wgtP], waveP, stn, ts, weight[wgtS], waveS)
            else:
                line = '  {:s}{:11.3f}{:8.3f}{:>4s}\n'.format(stn, tp, weight[wgtP], waveP)

        return line


    # Formato phases Velest
    def stn_velest(self, value, tp, ts):
        line = ""
        stn = value[0][:4]
        waveP='P' #Onda P
        waveS='S' #Onda S
        wgtP = value[0][-1] # Peso onda P
        wgtS = value[4]     # Peso onda S

        if int(wgtP) in range(0,4):
            if int(wgtS) in range(0,4):
                return ['{:s} {:5.2f}'.format(stn+waveP+wgtP, tp), '{:s} {:5.2f}'.format(stn+waveS+wgtS, ts)]
            else:
                return ['{:s} {:5.2f}'.format(stn+waveP+wgtP, tp)]

        return line

    # Convertir str a float
    def parseFloat(self, string, flt_frm, mag):
        try:
            tmp_f = float(string)
            if mag == 1: tmp_f = abs(tmp_f)
            value = flt_frm.format(tmp_f)
        except:
            value = flt_frm.format(float('0'))
        return value

    # Buscar estacion
    def search_stn(self, stn, msg):
        for idx, value in enumerate(self.stations):
            if stn in value:
                return idx + 1
        raise ValueError(f"{msg} -- {stn} estacion no existe")


    def date_to_secs(self, date, format):
        # convierte un string en una fecha con un fomato especifico y retorna los segundos
        try:
            seconds = datetime.strptime(date, format).timestamp() # datenum
        except:
            # Solución en caso de que las horas, minutos o segundos esten fuera de rango
            current_date = date.split('.')
            tmp_date = [current_date[0][i:i+2] for i in range(0, len(current_date[0]), 2)]
            if int(tmp_date [0]) in range (0, int(self.now.strftime('%y'))+1):
                tmp_date [0] = '20'+tmp_date[0]
            else:
                tmp_date [0] = '19'+tmp_date[0]
            sec_date = datetime(int(tmp_date[0]), int(tmp_date[1]), int(tmp_date[2])).timestamp()
            sec_time = int(tmp_date[3])*3600+int(tmp_date[4])*60+float(f'{tmp_date[5]}.{current_date[1]}')

            seconds = sec_date + sec_time
        return seconds
    

    
    def read_config(self):

        tmp_file = open("./config.dat", "r")
        try:
            for idx, value in enumerate(tmp_file):
                line = value.strip()
                line = re_spl(r'[\s]+', line)
                if idx == 0 and "NR" in line[0]:
                    self.ref_lev = float(line[1])
                else:
                    self.volcano.append([line[0], float(line[1]), float(line[2]), float(line[3])])
        except Exception as e:
            pass
        tmp_file.close()
