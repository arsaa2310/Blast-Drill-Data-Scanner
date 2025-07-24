import time
options = ["DRILLING", "TRAVEL", "P2H", "ISI FUEL", "EVAKUASI", "SAFETY TALK", "GANTI BIT", "GANTI ROD", 
           "WAITING AREA", "HUJAN", "WASHING", "TUNGGU PATTERN", "REST TIME", "REDRILL","BD","SERVICE"]

# cel = [[71,196], [106,196], [106,208], [71,208]]
cels = [71, 196, 108, 208]
cel = cels.copy()

x = [88, 128, 170, 212, 252, 292, 334, 376, 416, 456, 498, 538, 580, 622, 664, 704, 744]
y = [248, 260]

def tambah_waktu(t, menit_tambahan):
    jam = int(t)
    menit = int(round((t - jam) * 100))

    # Ubah semuanya ke menit
    total_menit = jam * 60 + menit + menit_tambahan

    # Kembali ke format jam.menit
    jam_baru = total_menit // 60
    menit_baru = total_menit % 60

    return float(f"{jam_baru}.{menit_baru:02d}")

t = 7.10

with open("cor.txt", "w") as sya:
    for i in range(12):                   # ← loop luar
        for k in range(6):                # ← loop dalam
            sya.write(f"{t}: "+ "{")
            for j in range(len(options)):
                sya.write(f'"{options[j]}": {x[j], y[0], x[j+1], y[1]}, ')
            
            y[0] += 10
            y[1] += 10
            # if k == 5:
            #     y[0] += 1
            #     y[1] += 1


            t = tambah_waktu(t, 10)
            sya.write("},"+"\n")
        y[0] -= 1
        y[1] -= 1


