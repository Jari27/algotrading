def all_tickers():
    return list(set([_ for lists in tickers.values() for _ in lists]))


""""
List of symbols, ordered by class. Use all_tickers() to get them all
"""
tickers = {}
tickers['AEX'] = [
    r"^AEX",
    "IAEX.AS",
    "URW.AS",
    "KPN.AS",
    "AGN.AS",
    "ASML.AS",
    "PHIA.AS",
    "RAND.AS",
    "TKWY.AS",
    "AD.AS",
    "HEIA.AS",
    "MT.AS",
    "DSM.AS",
    "INGA.AS",
    "ADYEN.AS",
    "ASRNL.AS",
    "WKL.AS",
    "RDSA.AS",
    "UNA.AS",
    "ABN.AS",
    "AKZA.AS",
    "NN.AS",
    "IMCD.AS",
    "ASM.AS",
    "PRX.AS",
    "REN.AS",
    "GLPG.AS",
]

tickers['SPY'] = [
    "SPY",
    "ABT",
    "ABBV",
    "ABMD",
    "ACN",
    "ATVI",
    "ADBE",
    "AMD",
    "AAP",
    "AES",
    "AFL",
    "A",
    "APD",
    "AKAM",
    "ALK",
    "ALB",
    "ARE",
    "ALXN",
    "ALGN",
    "ALLE",
    "ALL",
    "AMZN",
    "AMCR",
    "AEE",
    "AAL",
    "AEP",
    "AXP",
    "AIG",
    "AMT",
    "AWK",
    "AMP",
    "ABC",
    "AME",
    "AMGN",
    "APH",
    "ADI",
    "ANSS",
    "ANTM",
    "AON",
    "AOS",
    "APA",
    "AIV",
    "AAPL",
    "AMAT",
    "APTV",
    "ADM",
    "ANET",
    "AJG",
    "AIZ",
    "ATO",
    "ADSK",
    "ADP",
    "AZO",
    "AVB",
    "AVY",
    "AVGO",
    "BKR",
    "BLL",
    "BAC",
    "BK",
    "BAX",
    "BDX",
    "BRKB",
    "BBY",
    "BIO",
    "BIIB",
    "BLK",
    "BA",
    "BKNG",
    "BWA",
    "BXP",
    "BSX",
    "BMY",
    "BR",
    "BFB",
    "BEN",
    "CHRW",
    "COG",
    "CDNS",
    "CPB",
    "COF",
    "CAH",
    "CCL",
    "CARR",
    "CAT",
    "CBOE",
    "CBRE",
    "CDW",
    "CE",
    "CNC",
    "CNP",
    "CTL",
    "CERN",
    "CF",
    "CHTR",
    "CVX",
    "CMG",
    "CB",
    "CHD",
    "CI",
    "CINF",
    "CTAS",
    "CSCO",
    "C",
    "CFG",
    "CTXS",
    "CLX",
    "CME",
    "CMS",
    "CTSH",
    "CL",
    "CMCSA",
    "CMA",
    "CAG",
    "CXO",
    "COP",
    "COO",
    "CPRT",
    "CTVA",
    "COST",
    "COTY",
    "CCI",
    "CSX",
    "CMI",
    "CVS",
    "CRM",
    "DHI",
    "DHR",
    "DRI",
    "DVA",
    "DE",
    "DAL",
    "DVN",
    "DXCM",
    "DLR",
    "DFS",
    "DISCA",
    "DISCK",
    "DISH",
    "DG",
    "DLTR",
    "D",
    "DPZ",
    "DOV",
    "DOW",
    "DTE",
    "DUK",
    "DRE",
    "DD",
    "DXC",
    "DGX",
    "DIS",
    "ED",
    "ETFC",
    "EMN",
    "ETN",
    "EBAY",
    "ECL",
    "EIX",
    "EW",
    "EA",
    "EMR",
    "ETR",
    "EOG",
    "EFX",
    "EQIX",
    "EQR",
    "ESS",
    "EL",
    "EVRG",
    "ES",
    "EXC",
    "EXPE",
    "EXPD",
    "EXR",
    "FANG",
    "FFIV",
    "FB",
    "FAST",
    "FRT",
    "FDX",
    "FIS",
    "FITB",
    "FE",
    "FRC",
    "FISV",
    "FLT",
    "FLIR",
    "FLS",
    "FMC",
    "F",
    "FTNT",
    "FTV",
    "FBHS",
    "FOXA",
    "FOX",
    "FCX",
    "FTI",
    "GOOGL",
    "GOOG",
    "GLW",
    "GPS",
    "GRMN",
    "GD",
    "GE",
    "GIS",
    "GM",
    "GPC",
    "GILD",
    "GL",
    "GPN",
    "GS",
    "GWW",
    "HRB",
    "HAL",
    "HBI",
    "HIG",
    "HAS",
    "HCA",
    "HSIC",
    "HSY",
    "HES",
    "HPE",
    "HLT",
    "HFC",
    "HOLX",
    "HD",
    "HON",
    "HRL",
    "HST",
    "HWM",
    "HPQ",
    "HUM",
    "HBAN",
    "HII",
    "IT",
    "IEX",
    "IDXX",
    "INFO",
    "ITW",
    "ILMN",
    "INCY",
    "IR",
    "INTC",
    "ICE",
    "IBM",
    "IP",
    "IPG",
    "IFF",
    "INTU",
    "ISRG",
    "IVZ",
    "IPGP",
    "IQV",
    "IRM",
    "JKHY",
    "J",
    "JBHT",
    "JNJ",
    "JCI",
    "JPM",
    "JNPR",
    "KMX",
    "KO",
    "KSU",
    "K",
    "KEY",
    "KEYS",
    "KMB",
    "KIM",
    "KMI",
    "KLAC",
    "KSS",
    "KHC",
    "KR",
    "LNT",
    "LB",
    "LHX",
    "LH",
    "LRCX",
    "LW",
    "LVS",
    "LEG",
    "LDOS",
    "LEN",
    "LLY",
    "LNC",
    "LIN",
    "LYV",
    "LKQ",
    "LMT",
    "L",
    "LOW",
    "LYB",
    "LUV",
    "MMM",
    "MO",
    "MTB",
    "MRO",
    "MPC",
    "MKTX",
    "MAR",
    "MMC",
    "MLM",
    "MAS",
    "MA",
    "MKC",
    "MXIM",
    "MCD",
    "MCK",
    "MDT",
    "MRK",
    "MET",
    "MTD",
    "MGM",
    "MCHP",
    "MU",
    "MSFT",
    "MAA",
    "MHK",
    "MDLZ",
    "MNST",
    "MCO",
    "MS",
    "MOS",
    "MSI",
    "MSCI",
    "MYL",
    "NDAQ",
    "NOV",
    "NTAP",
    "NFLX",
    "NWL",
    "NEM",
    "NWSA",
    "NWS",
    "NEE",
    "NLSN",
    "NKE",
    "NI",
    "NBL",
    "NSC",
    "NTRS",
    "NOC",
    "NLOK",
    "NCLH",
    "NRG",
    "NUE",
    "NVDA",
    "NVR",
    "NOW",
    "ORLY",
    "OXY",
    "ODFL",
    "OMC",
    "OKE",
    "ORCL",
    "OTIS",
    "O",
    "PEAK",
    "PCAR",
    "PKG",
    "PH",
    "PAYX",
    "PAYC",
    "PYPL",
    "PNR",
    "PBCT",
    "PEP",
    "PKI",
    "PRGO",
    "PFE",
    "PM",
    "PSX",
    "PNW",
    "PXD",
    "PNC",
    "PPG",
    "PPL",
    "PFG",
    "PG",
    "PGR",
    "PLD",
    "PRU",
    "PEG",
    "PSA",
    "PHM",
    "PVH",
    "PWR",
    "QRVO",
    "QCOM",
    "RE",
    "RL",
    "RJF",
    "RTX",
    "REG",
    "REGN",
    "RF",
    "RSG",
    "RMD",
    "RHI",
    "ROK",
    "ROL",
    "ROP",
    "ROST",
    "RCL",
    "SCHW",
    "STZ",
    "SJM",
    "SPGI",
    "SBAC",
    "SLB",
    "STX",
    "SEE",
    "SRE",
    "SHW",
    "SPG",
    "SWKS",
    "SLG",
    "SNA",
    "SO",
    "SWK",
    "SBUX",
    "STT",
    "STE",
    "SYK",
    "SIVB",
    "SYF",
    "SNPS",
    "SYY",
    "T",
    "TAP",
    "TMUS",
    "TROW",
    "TTWO",
    "TPR",
    "TGT",
    "TEL",
    "TDY",
    "TFX",
    "TXN",
    "TXT",
    "TMO",
    "TIF",
    "TJX",
    "TSCO",
    "TT",
    "TDG",
    "TRV",
    "TFC",
    "TWTR",
    "TYL",
    "TSN",
    "UDR",
    "ULTA",
    "USB",
    "UAA",
    "UA",
    "UNP",
    "UAL",
    "UNH",
    "UPS",
    "URI",
    "UHS",
    "UNM",
    "VFC",
    "VLO",
    "VAR",
    "VTR",
    "VRSN",
    "VRSK",
    "VZ",
    "VRTX",
    "VIAC",
    "V",
    "VNO",
    "VMC",
    "WRB",
    "WAB",
    "WMT",
    "WBA",
    "WM",
    "WAT",
    "WEC",
    "WFC",
    "WELL",
    "WST",
    "WDC",
    "WU",
    "WRK",
    "WY",
    "WHR",
    "WMB",
    "WLTW",
    "WYNN",
    "XRAY",
    "XOM",
    "XEL",
    "XRX",
    "XLNX",
    "XYL",
    "YUM",
    "ZBRA",
    "ZBH",
    "ZION",
    "ZTS", ]

tickers['EURONEXT'] = [
    "AALB.AS",
    "ABN.AS",
    "ACCEL.AS",
    "AXS.AS",
    "ADUX",
    "ADYEN.AS",
    "AED",
    "AGN.AS",
    "AD.AS",
    "AF.AS",
    "AJAX.AS",
    "AKZA.AS",
    "ALFEN.AS",
    "ATCB.AS",
    "ATC.AS",
    "ALX.AS",
    "AMG.AS",
    "ACOMO.AS",
    "AND.AS",
    "AAA.AS",
    "APAM.AS",
    "ARCAD.AS",
    "MT.AS",
    "ASM.AS",
    "ASML.AS",
    "ASRNL.AS",
    "ATRS.AS",
    "AVTX.AS",
    "BSGR.AS",
    "BAMNB.AS",
    "BFIT.AS",
    "BESI.AS",
    "BBED.AS",
    "BEVER.AS",
    "BOKA.AS",
    "BGHL.AS",
    "BRILL.AS",
    "BRNL.AS",
    "CMCOM.AS",
    "CCEP.AS",
    "CRBN.AS",
    "CLB.AS",
    "CTAC.AS",
    "DGB.AS",
    "DPA.AS",
    "DSM.AS",
    "EAS2P.AS",
    "ENVI.AS",
    "ESP.AS",
    "ECT",
    "ECMPA.AS",
    "ENX",
    "FAST.AS",
    "FLOW.AS",
    "FNG.AS",
    "FFARM.AS",
    "FUR.AS",
    "GLPG.AS",
    "GVNV.AS",
    "HEIJM.AS",
    "HEIA.AS",
    "HEIO.AS",
    "HOLCO.AS",
    "HDG.AS",
    "HUNDP.AS",
    "HYDRA.AS",
    "ICT.AS",
    "IEX.AS",
    "IMCD.AS",
    "INGA.AS",
    "INTER.AS",
    "JDEP.AS",
    "TKWY.AS",
    "KENDR.AS",
    "KDS.AS",
    "KPN.AS",
    "LVIDE.AS",
    "BOLS.AS",
    "NEDSE.AS",
    "MORE.AS",
    "NEDAP.AS",
    "NSE.AS",
    "NEWAY.AS",
    "NIBC.AS",
    "NN.AS",
    "NOVI.AS",
    "NSI.AS",
    "OCI.AS",
    "ORANW.AS",
    "ORDI.AS",
    "PSH",
    "PHARM.AS",
    "INPHI.AS",
    "PHIA.AS",
    "PORF.AS",
    "PNL.AS",
    "PRX.AS",
    "RAND.AS",
    "REINA.AS",
    "REN.AS",
    "RWI.AS",
    "RET",
    "ROOD.AS",
    "RDSA.AS",
    "RDSB.AS",
    "SGO",
    "SBMO.AS",
    "SIFG.AS",
    "LIGHT.AS",
    "SLIGR.AS",
    "SNOW.AS",
    "STRN.AS",
    "TFG.AS",
    "TIE.AS",
    "TWEKA.AS",
    "TOM2.AS",
    "URW.AS",
    "UNA.AS",
    "VLK.AS",
    "VALUE.AS",
    "PREVA.AS",
    "VASTN.AS",
    "VVY.AS",
    "VTA.AS",
    "VPK.AS",
    "WDP",
    "WHA.AS",
    "WKL.AS",
    "YATRA.AS",
]