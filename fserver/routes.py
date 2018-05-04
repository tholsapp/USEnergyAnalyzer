
from flask import Flask,  render_template, redirect, url_for, current_app, flash, request, abort

from fserver import app
from energy_analyzer import get_states, get_state_codes, \
get_total_consumtion, get_total_production, \
get_total_coal_census, get_total_electricity_census, get_total_fossil_fuel_census, \
get_total_geothermal_census, get_total_hydropower_census, \
get_total_natural_gas_census, get_total_lpg_census


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return "about"

@app.route('/test')
def test():
	legend = 'Total Coal'
	states = get_state_codes()
	# get total coal, parse to int and calculate the total base on population
	total_coal_2010 = get_total_coal_census(2010)
	total_coal_2011 = get_total_coal_census(2011)
	total_coal_2012 = get_total_coal_census(2012)
	total_coal_2013 = get_total_coal_census(2013)
	total_coal_2014 = get_total_coal_census(2014)

	return render_template('test.html', legend=legend, states=states,
		total_coal_2010=total_coal_2010,
		total_coal_2011=total_coal_2011,
		total_coal_2012=total_coal_2012,
		total_coal_2013=total_coal_2013,
		total_coal_2014=total_coal_2014
		)

@app.route('/total-analysis')
def total_analysis():
	states = get_state_codes()
	# get total coal, parse to int and calculate the total base on population
	c_total_2010 = get_total_consumtion(2010)
	c_total_2011 = get_total_consumtion(2011)
	c_total_2012 = get_total_consumtion(2012)
	c_total_2013 = get_total_consumtion(2013)
	c_total_2014 = get_total_consumtion(2014)

	p_total_2010 = get_total_production(2010)
	p_total_2011 = get_total_production(2011)
	p_total_2012 = get_total_production(2012)
	p_total_2013 = get_total_production(2013)
	p_total_2014 = get_total_production(2014)

	return render_template('totals.html', states=states,
		c_total_2010=c_total_2010,
		c_total_2011=c_total_2011,
		c_total_2012=c_total_2012,
		c_total_2013=c_total_2013,
		c_total_2014=c_total_2014,
		p_total_2010=p_total_2010,
		p_total_2011=p_total_2011,
		p_total_2012=p_total_2012,
		p_total_2013=p_total_2013,
		p_total_2014=p_total_2014
		)

@app.route('/coal-analysis')
def coal_analysis():
	states = get_state_codes()
	# get total coal, parse to int and calculate the total base on population
	total_coal_2010 = get_total_coal_census(2010)
	total_coal_2011 = get_total_coal_census(2011)
	total_coal_2012 = get_total_coal_census(2012)
	total_coal_2013 = get_total_coal_census(2013)
	total_coal_2014 = get_total_coal_census(2014)

	return render_template('test.html',states=states,
		total_coal_2010=total_coal_2010,
		total_coal_2011=total_coal_2011,
		total_coal_2012=total_coal_2012,
		total_coal_2013=total_coal_2013,
		total_coal_2014=total_coal_2014
		)

@app.route('/electricity-analysis')
def electricity_analysis():
	states = get_state_codes()
	# get total coal, parse to int and calculate the total base on population
	total_electricity_2010 = get_total_electricity_census(2010)
	total_electricity_2011 = get_total_electricity_census(2011)
	total_electricity_2012 = get_total_electricity_census(2012)
	total_electricity_2013 = get_total_electricity_census(2013)
	total_electricity_2014 = get_total_electricity_census(2014)
	print total_electricity_2010
	return render_template('electricity.html',states=states,
		total_electricity_2010=total_electricity_2010,
		total_electricity_2011=total_electricity_2011,
		total_electricity_2012=total_electricity_2012,
		total_electricity_2013=total_electricity_2013,
		total_electricity_2014=total_electricity_2014
		)

@app.route('/geothermal-analysis')
def geothermal_analysis():
	states = get_state_codes()
	# get total coal, parse to int and calculate the total base on population
	total_geothermal_2010 = get_total_geothermal_census(2010)
	total_geothermal_2011 = get_total_geothermal_census(2011)
	total_geothermal_2012 = get_total_geothermal_census(2012)
	total_geothermal_2013 = get_total_geothermal_census(2013)
	total_geothermal_2014 = get_total_geothermal_census(2014)
	return render_template('geothermal_energy.html',states=states,
		total_geothermal_2010=total_geothermal_2010,
		total_geothermal_2011=total_geothermal_2011,
		total_geothermal_2012=total_geothermal_2012,
		total_geothermal_2013=total_geothermal_2013,
		total_geothermal_2014=total_geothermal_2014
		)

@app.route('/fossil-analysis')
def fossil_analysis():
	states = get_state_codes()
	# get total coal, parse to int and calculate the total base on population
	total_fossil_fuel_2010 = get_total_fossil_fuel_census(2010)
	total_fossil_fuel_2011 = get_total_fossil_fuel_census(2011)
	total_fossil_fuel_2012 = get_total_fossil_fuel_census(2012)
	total_fossil_fuel_2013 = get_total_fossil_fuel_census(2013)
	total_fossil_fuel_2014 = get_total_fossil_fuel_census(2014)
	return render_template('fossil_fuel.html',states=states,
		total_fossil_fuel_2010=total_fossil_fuel_2010,
		total_fossil_fuel_2011=total_fossil_fuel_2011,
		total_fossil_fuel_2012=total_fossil_fuel_2012,
		total_fossil_fuel_2013=total_fossil_fuel_2013,
		total_fossil_fuel_2014=total_fossil_fuel_2014
		)

@app.route('/hydro-power-analysis')
def hydro_analysis():
	states = get_state_codes()
	# get total coal, parse to int and calculate the total base on population
	total_hydropower_2010 = get_total_hydropower_census(2010)
	total_hydropower_2011 = get_total_hydropower_census(2011)
	total_hydropower_2012 = get_total_hydropower_census(2012)
	total_hydropower_2013 = get_total_hydropower_census(2013)
	total_hydropower_2014 = get_total_hydropower_census(2014)
	return render_template('hydro_energy.html',states=states,
		total_hydropower_2010=total_hydropower_2010,
		total_hydropower_2011=total_hydropower_2011,
		total_hydropower_2012=total_hydropower_2012,
		total_hydropower_2013=total_hydropower_2013,
		total_hydropower_2014=total_hydropower_2014
		)

@app.route('/natural-gas-analysis')
def natural_gas_analysis():
	states = get_state_codes()
	# get total coal, parse to int and calculate the total base on population
	total_natural_gas_2010 = get_total_natural_gas_census(2010)
	total_natural_gas_2011 = get_total_natural_gas_census(2011)
	total_natural_gas_2012 = get_total_natural_gas_census(2012)
	total_natural_gas_2013 = get_total_natural_gas_census(2013)
	total_natural_gas_2014 = get_total_natural_gas_census(2014)
	return render_template('natural_gas.html',states=states,
		total_natural_gas_2010=total_natural_gas_2010,
		total_natural_gas_2011=total_natural_gas_2011,
		total_natural_gas_2012=total_natural_gas_2012,
		total_natural_gas_2013=total_natural_gas_2013,
		total_natural_gas_2014=total_natural_gas_2014
		)

@app.route('/lpg-analysis')
def lpg_analysis():
	states = get_state_codes()
	# get total coal, parse to int and calculate the total base on population
	total_lpg_2010 = get_total_lpg_census(2010)
	total_lpg_2011 = get_total_lpg_census(2011)
	total_lpg_2012 = get_total_lpg_census(2012)
	total_lpg_2013 = get_total_lpg_census(2013)
	total_lpg_2014 = get_total_lpg_census(2014)
	return render_template('liquified_pertroleum_gas.html',states=states,
		total_lpg_2010=total_lpg_2010,
		total_lpg_2011=total_lpg_2011,
		total_lpg_2012=total_lpg_2012,
		total_lpg_2013=total_lpg_2013,
		total_lpg_2014=total_lpg_2014
		)

