taxon_keys = [1334757, 1340042, 1, 1342048, 1340278, 1340556]       #["Apis", "Melipona", "Trigona", "Xylocopa", "Bombus", "Euglossa"]

params = [("taxonKey", str(key)) for key in taxon_keys]
print(params)