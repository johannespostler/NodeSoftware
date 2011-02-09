# -*- coding: utf-8 -*-

from vamdctap.caselessdict import CaselessDict

RETURNABLES = CaselessDict({\
'SourceID':'Source.id',
'SourceAuthorName':'Source.author',
'SourceCategory':'Source.category',
'SourcePageBegin':'Source.pages',
'SourcePageEnd':'Source.pages',
'SourceName':'Source.journal',
'SourceTitle':'Source.title',
'SourceURI':'Source.url',
'SourceVolume':'Source.volume',
'SourceYear':'Source.year',
'MethodID':'"MOBS"',
'MethodCategory':'"observed"',
'MethodDescription':'',
'AtomStateID':'AtomState.id',
'AtomSymbol':'Atom.name',
'AtomNuclearCharge':'Atom.atomic',
'AtomIonCharge':'Atom.ion',
'AtomMassNumber':'Atom.massno',
'AtomIonizationEnergy':'Atom.ionen',
'AtomConfigurationLabel':'AtomState.charid',
'AtomCompositionComponentTerm':'AtomState.term',
'AtomStateLandeFactor':'AtomState.lande',
'AtomStateLandeFactorRef':'\' \'.join(AtomState.lande_ref.references.values_list(\'id\',flat=True))',
'AtomStateEnergy':'AtomState.energy',
'AtomStateEnergyRef':'\' \'.join(AtomState.energy_ref.references.values_list(\'id\',flat=True))',
'AtomStateEnergyUnits':'1/cm',
'AtomStateDescription':'',
'RadTransComments':'Wavelength is for vacuum.',
'RadTransWavelengthExperimentalValue':'RadTran.vacwave',
'RadTransWavelengthExperimentalUnits':u'\xc5',
'RadTransProbabilityLog10WeightedOscillatorStrengthAccuracy':'RadTran.accur',
'RadTransWavelengthExperimentalSourceRef':'\' \'.join(RadTran.wave_ref.references.values_list(\'id\',flat=True))',
'RadTransFinalStateRef':'RadTran.lostate_id',
'RadTransInitialStateRef':'RadTran.upstate_id',
'RadTransLogGF':'RadTran.loggf',
'RadTransMethodRef':'OBS',
'RadTransProbabilityLog10WeightedOscillatorStrengthSourceRef':'\' \'.join(RadTran.loggf_ref.references.values_list(\'id\',flat=True))',
'RadTransProbabilityLog10WeightedOscillatorStrengthValue':'RadTran.loggf',
'RadTransBroadRadGammaLog':'RadTran.gammarad',
'RadTransBroadRadRef':'\' \'.join(RadTran.gammarad_ref.references.values_list(\'id\',flat=True))',
'RadTransBroadStarkGammaLog':'RadTran.gammastark',
'RadTransBroadStarkRef':'\' \'.join(RadTran.gammastark_ref.references.values_list(\'id\',flat=True))',
'RadTransBroadWaalsGammaLog':'RadTran.gammawaals',
'RadTransBroadWaalsAlpha':'RadTran.alphawaals',
'RadTransBroadWaalsSigma':'RadTran.sigmawaals',
'RadTransBroadWaalsRef':'\' \'.join(RadTran.waals_ref.references.values_list(\'id\',flat=True))',
'RadTransEffLande':'RadTran.landeff',
'RadTransEffLandeRef':'\' \'.join(RadTran.lande_ref.references.values_list(\'id\',flat=True))',
})

RESTRICTABLES = CaselessDict({\
'AtomSymbol':'species__name',
'AtomNuclearCharge':'species__atomic',
'AtomStateEnergy':'upstate__energy',
'RadTransWavelengthExperimentalValue':'vacwave',
'RadTransLogGF':'loggf',
'AtomIonCharge':'species__ion',
})
