def hdr(rho, g, h):
    """Menghitung Tekanan hidrostatis (massa jenis zat cair,kedalaman) 
    Argument:
        rho (float/int) = nilai masa jenis cairannya
        g (float/int) = nilai gravitasi suatu planet atau bumi
        h (float/int) = posisi tinggi tangki bocornya
    Return:
        hdr = hasil dari perhitungan hidrostatis
    """
    rho = float(rho)
    g = float(g)
    h = float(h)
    hdr = rho*g*h
    return hdr
