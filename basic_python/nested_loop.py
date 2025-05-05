salahs = ['fazr', 'zuhr', 'asr', 'magrib', 'isha', 'witr']
rakahs = [4, 12, 4, 5, 6, 3]

prayer_comb = []

for salah in salahs:
    print('Salah: ', salah)
    for rakah in rakahs:
        print(salah, rakah)
        prayer_comb.append([salah, rakah])
    
    