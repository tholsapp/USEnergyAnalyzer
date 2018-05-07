import pandas as pd


""" Read from CSV with PANDAS
    Column names below 
"""
geo_cols = [
  'StateCodes','State','Region','Division','Coast','Great Lakes',
]
energy_cols = [
  'TotalC2010','TotalC2011','TotalC2012','TotalC2013','TotalC2014',
  'TotalP2010','TotalP2011','TotalP2012','TotalP2013','TotalP2014',
  'TotalE2010','TotalE2011','TotalE2012','TotalE2013','TotalE2014',
  'TotalPrice2010','TotalPrice2011','TotalPrice2012','TotalPrice2013','TotalPrice2014',
  'TotalC10-11','TotalC11-12','TotalC12-13','TotalC13-14',
  'TotalP10-11','TotalP12-12','TotalP12-13','TotalP13-14',
  'TotalE10-11','TotalE11-12','TotalE12-13','TotalE13-14',
  'TotalPrice10-11','TotalPrice11-12','TotalPrice12-13','TotalPrice13-14',
  'BiomassC2010','BiomassC2011','BiomassC2012','BiomassC2013','BiomassC2014',
  'CoalC2010','CoalC2011','CoalC2012','CoalC2013','CoalC2014',
  'CoalP2010','CoalP2011','CoalP2012','CoalP2013','CoalP2014',
  'CoalE2010','CoalE2011','CoalE2012','CoalE2013','CoalE2014',
  'CoalPrice2010','CoalPrice2011', 'CoalPrice2012','CoalPrice2013','CoalPrice2014',
  'ElecC2010','ElecC2011','ElecC2012','ElecC2013','ElecC2014',
  'ElecE2010','ElecE2011','ElecE2012','ElecE2013','ElecE2014',
  'ElecPrice2010','ElecPrice2011', 'ElecPrice2012','ElecPrice2013','ElecPrice2014',
  'FossFuelC2010','FossFuelC2011', 'FossFuelC2012','FossFuelC2013','FossFuelC2014',
  'GeoC2010','GeoC2011','GeoC2012','GeoC2013','GeoC2014',
  'GeoP2010','GeoP2011','GeoP2012','GeoP2013','GeoP2014',
  'HydroC2010','HydroC2011','HydroC2012','HydroC2013','HydroC2014',
  'HydroP2010','HydroP2011','HydroP2012','HydroP2013','HydroP2014',
  'NatGasC2010','NatGasC2011','NatGasC2012','NatGasC2013','NatGasC2014',
  'NatGasE2010','NatGasE2011','NatGasE2012','NatGasE2013','NatGasE2014',
  'NatGasPrice2010','NatGasPrice2011','NatGasPrice2012','NatGasPrice2013','NatGasPrice2014',
  'LPGC2010','LPGC2011','LPGC2012','LPGC2013','LPGC2014',
  'LPGE2010','LPGE2011','LPGE2012','LPGE2013', 'LPGE2014',
  'LPGPRICE2010', 'LPGPRICE2011','LPGPRICE2012','LPGPRICE2013','LPGPRICE2014'
]
economic_cols = [
  'GDP2010Q1','GDP2010Q2','GDP2010Q3','GDP2010Q4','GDP2010',
  'GDP2011Q1','GDP2011Q2','GDP2011Q3','GDP2011Q4','GDP2011',
  'GDP2012Q1','GDP2012Q2','GDP2012Q3','GDP2012Q4','GDP2012',
  'GDP2013Q1','GDP2013Q2','GDP2013Q3','GDP2013Q4','GDP2013',
  'GDP2014Q1','GDP2014Q2','GDP2014Q3','GDP2014Q4','GDP2014',
]
census_cols = [
  'CENSUS2010POP',
  'POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIAMTE2013','POPESTIMATE2014',
  'RBIRTH2010','RBIRTH2011','RBIRTH2012','RBIRTH2013','RBIRTH2014',
  'RDEATH2010','RDEATH2011','RDEATH2012','RDEATH2013','RDEATH2014',
  'RNATURALINC2010','RNATURALINC2011','RNATURALINC2012','RNATURALINC2013','RNATURALINC2014',
  'RDOMESTICMIG2010','RDOMESTICMIG2011','RDOMESTICMIG2012','RDOMESTICMIG2013','RDOMESTICMIG2014',
  'RNETMIG2010','RNETMIG2011','RNETMIG2012','RNETMIG2013','RNETMIG2014'
]
colnames = geo_cols + energy_cols + economic_cols + census_cols
EData = pd.read_csv('fserver/static/energy_and_economic_data2010-2014.csv', names=colnames)

def get_state_codes():
  return EData.StateCodes.tolist()[1:-2]

def get_states():
  return EData.State.tolist()[1:-2]

def get_total_coal(year):
  if year == 2010:
    return EData.CoalC2010.tolist()[1:-2]
  elif year == 2011:
    return EData.CoalC2011.tolist()[1:-2]
  elif year == 2012:
    return EData.CoalC2012.tolist()[1:-2]
  elif year == 2013:
    return EData.CoalC2013.tolist()[1:-2]
  elif year == 2014:
    return EData.CoalC2014.tolist()[1:-2]

def get_total_coal_cost(year):
  if year == 2010:
    return EData.CoalPrice2010.tolist()[1:-2]
  elif year == 2011:
    return EData.CoalPrice2011.tolist()[1:-2]
  elif year == 2012:
    return EData.CoalPrice2012.tolist()[1:-2]
  elif year == 2013:
    return EData.CoalPrice2013.tolist()[1:-2]
  elif year == 2014:
    return EData.CoalPrice2014.tolist()[1:-2]

def get_total_electricity(year):
  if year == 2010:
    return EData.ElecC2010.tolist()[1:-2]
  elif year == 2011:
    return EData.ElecC2011.tolist()[1:-2]
  elif year == 2012:
    return EData.ElecC2012.tolist()[1:-2]
  elif year == 2013:
    return EData.ElecC2013.tolist()[1:-2]
  elif year == 2014:
    return EData.ElecC2014.tolist()[1:-2]

def get_total_electric_cost(year):
  if year == 2010:
    print EData.ElecPrice2010.tolist()[1:-2]
    return EData.ElecPrice2010.tolist()[1:-2]
  elif year == 2011:
    return EData.ElecPrice2011.tolist()[1:-2]
  elif year == 2012:
    return EData.ElecPrice2012.tolist()[1:-2]
  elif year == 2013:
    return EData.ElecPrice2013.tolist()[1:-2]
  elif year == 2014:
    return EData.ElecPrice2014.tolist()[1:-2]

def get_total_fossil_fuel(year):
  if year == 2010:
    return EData.FossFuelC2010.tolist()[1:-2]
  elif year == 2011:
    return EData.FossFuelC2011.tolist()[1:-2]
  elif year == 2012:
    return EData.FossFuelC2012.tolist()[1:-2]
  elif year == 2013:
    return EData.FossFuelC2013.tolist()[1:-2]
  elif year == 2014:
    return EData.FossFuelC2014.tolist()[1:-2]


def get_total_geothermal(year):
  if year == 2010:
    return EData.GeoC2010.tolist()[1:-2]
  elif year == 2011:
    return EData.GeoC2011.tolist()[1:-2]
  elif year == 2012:
    return EData.GeoC2012.tolist()[1:-2]
  elif year == 2013:
    return EData.GeoC2013.tolist()[1:-2]
  elif year == 2014:
    return EData.GeoC2014.tolist()[1:-2]

def get_total_hydropower(year):
  if year == 2010:
    return EData.HydroC2010.tolist()[1:-2]
  elif year == 2011:
    return EData.HydroC2011.tolist()[1:-2]
  elif year == 2012:
    return EData.HydroC2012.tolist()[1:-2]
  elif year == 2013:
    return EData.HydroC2013.tolist()[1:-2]
  elif year == 2014:
    return EData.HydroC2014.tolist()[1:-2]

def get_total_natural_gas(year):
  if year == 2010:
    return EData.NatGasC2010.tolist()[1:-2]
  elif year == 2011:
    return EData.NatGasC2011.tolist()[1:-2]
  elif year == 2012:
    return EData.NatGasC2012.tolist()[1:-2]
  elif year == 2013:
    return EData.NatGasC2013.tolist()[1:-2]
  elif year == 2014:
    return EData.NatGasC2014.tolist()[1:-2]

def get_total_lpg(year):
  if year == 2010:
    return EData.LPGC2010.tolist()[1:-2]
  elif year == 2011:
    return EData.LPGC2011.tolist()[1:-2]
  elif year == 2012:
    return EData.LPGC2012.tolist()[1:-2]
  elif year == 2013:
    return EData.LPGC2013.tolist()[1:-2]
  elif year == 2014:
    return EData.LPGC2014.tolist()[1:-2]

def get_census():
  return EData.CENSUS2010POP.tolist()[1:-2]


def get_total_consumtion(year):
  if year == 2010:
    return EData.TotalC2010.tolist()[1:-2]
  elif year == 2011:
    return EData.TotalC2011.tolist()[1:-2]
  elif year == 2012:
    return EData.TotalC2012.tolist()[1:-2]
  elif year == 2013:
    return EData.TotalC2013.tolist()[1:-2]
  elif year == 2014:
    return EData.TotalC2014.tolist()[1:-2]

def get_total_production(year):
  if year == 2010:
    return EData.TotalP2010.tolist()[1:-2]
  elif year == 2011:
    return EData.TotalP2011.tolist()[1:-2]
  elif year == 2012:
    return EData.TotalP2012.tolist()[1:-2]
  elif year == 2013:
    return EData.TotalP2013.tolist()[1:-2]
  elif year == 2014:
    return EData.TotalP2014.tolist()[1:-2]

def get_total_coal_census(year):
  coal = get_total_coal(year)
  cens = get_census()
  total = []
  census = []
  total_census = []
  # convert to number
  for d in coal:
    total.append(int(float(d)))
  # convert to number
  for d in cens:
    census.append(int(d))
  # calculate energy per person per state
  for x in range(0,len(coal)):
    total_census.append(((total[x] * 1000000000) / census[x]))
  return total_census

def get_total_electricity_census(year):
  coal = get_total_electricity(year)
  cens = get_census()
  total = []
  census = []
  total_census = []
  # convert to number
  for d in coal:
    total.append(int(float(d)))
  # convert to number
  for d in cens:
    census.append(int(d))
  # calculate energy per person per state
  for x in range(0,len(coal)):
    total_census.append(((total[x] * 1000000000) / census[x]))
  return total_census

def get_total_fossil_fuel_census(year):
  fuel = get_total_fossil_fuel(year)
  cens = get_census()
  total = []
  census = []
  total_census = []
  # convert to number
  for d in fuel:
    total.append(int(float(d)))
  # convert to number
  for d in cens:
    census.append(int(d))
  # calculate energy per person per state
  for x in range(0,len(fuel)):
    total_census.append(((total[x] * 1000000000) / census[x]))
  return total_census

def get_total_geothermal_census(year):
  coal = get_total_geothermal(year)
  cens = get_census()
  total = []
  census = []
  total_census = []
  # convert to number
  for d in coal:
    total.append(int(float(d)))
  # convert to number
  for d in cens:
    census.append(int(d))
  # calculate energy per person per state
  for x in range(0,len(coal)):
    total_census.append(((total[x] * 1000000000) / census[x]))
  return total_census

def get_total_hydropower_census(year):
  coal = get_total_hydropower(year)
  cens = get_census()
  total = []
  census = []
  total_census = []
  # convert to number
  for d in coal:
    total.append(int(float(d)))
  # convert to number
  for d in cens:
    census.append(int(d))
  # calculate energy per person per state
  for x in range(0,len(coal)):
    total_census.append(((total[x] * 1000000000) / census[x]))
  return total_census

def get_total_natural_gas_census(year):
  natgas = get_total_natural_gas(year)
  cens = get_census()
  total = []
  census = []
  total_census = []
  print natgas
  # convert to number
  for d in natgas:
    total.append(int(float(d)))
  # convert to number
  for d in cens:
    census.append(int(d))
  # calculate energy per person per state
  for x in range(0,len(natgas)):
    total_census.append(((total[x] * 1000000000) / census[x]))
  return total_census

def get_total_lpg_census(year):
  coal = get_total_lpg(year)
  cens = get_census()
  total = []
  census = []
  total_census = []
  # convert to number
  for d in coal:
    total.append(int(float(d)))
  # convert to number
  for d in cens:
    census.append(int(d))
  # calculate energy per person per state
  for x in range(0,len(coal)):
    total_census.append(((total[x] * 1000000000) / census[x]))
  return total_census

def get_total_census(year):
  coal = get_total(year)
  cens = get_census()
  total = []
  census = []
  total_census = []
  # convert to number
  for d in coal:
    total.append(int(d))
  # convert to number
  for d in cens:
    census.append(int(d))
  # calculate energy per person per state
  for x in range(0,len(coal)):
    total_census.append(((total[x] * 1000000000) / census[x]))
  return total_census
# test methods
if __name__ == '__main__':
  print get_states()
  print get_state_codes()
  print get_total(2010)


