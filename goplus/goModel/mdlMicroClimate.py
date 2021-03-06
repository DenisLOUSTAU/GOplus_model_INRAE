from goBases import * #Windows
#from ..goBases import * #LINUX

class MicroClimate(ELT):
    '''Group of a microclimat physical properties
        - many of the properties are only grouped in this type of object and define outer.
        - only some air property linked to the temperature, pressure and vapour content are computed
    '''
    z_ref =  var('height above soil of micro climate (m)',0.)

    #radiative flux 
    SWDif =  var('down diffuse solar radiation (W/m2)', 0)
    SWDir =  var('down direct solar radiation (W/m2)', 0)
    SWUp =  var('up solar radiation (W/m2)', 0)
    LWDw =  var('down long wave radiation (W/m2)', 0)
    LWUp =  var('up long wave radiation (W/m2)', 0)
    
    #input air properties
    TaC  = var('air temperature in degre celsius (degC)', 20)
    e = var('vapour pressure (Pa)', 2000)
    P = var( 'atmospheric pressure ( Pa)',  101600)    
    
    #other climatic properties
    Rain  =var('rainfall (Kg_H2O /m2_soil /hour)')
    u = var('wind speed (m /s)', 0)
    CO2  = var('air CO2 concentration (ppm)', 385)
    
    #vars
    TaK  = var('air temperature in degre Kelvin (degK)')
    es  = var('vapour pressure at saturation (Pa)')
    s = var('des/dT at T (Pa/degC)')
    d =var('vapour pressure deficit (Pa)')
    dq = var('vapour mass deficit (g_H2O /Kg_air)')
    Rho_Cp = var('heat capacity of air (J /m3_air /K)')
    Lambda = var('vapourisation heat (J /Kg_H2O)')
    Gamma = var('psychrometric constant Gamma (Pa /K)')
    

    
    def update(self):
    
        #temperature
        self.TaK = self.TaC + 273.15

        #Pression de vapeur saturante (Pa) - Buck 1981
        self.es = (1.0007 + 0.0000000346 * self.P) * 611.21 * exp(17.502 * self.TaC / (240.97 + self.TaC))
        self.s =  self.es * (17.502 * 240.97) / (240.97 + self.TaC) ** 2
        
        #air  vapour properties        
        self.d = max(0, self.es - self.e)
        self.dq = self.d * 0.622 / self.P * 1000
        self.Lambda = 1000000 * (2.501 - 0.00238 * self.TaC) 
        
        #thermodynamics properties of air
        _Cp = 1006         
        self.Rho_Cp = (1.292 - 0.0047132 * self.TaC + 0.000015058 * self.TaC ** 2) * _Cp
        self.Gamma = self.P * _Cp / (0.622 * self.Lambda)




