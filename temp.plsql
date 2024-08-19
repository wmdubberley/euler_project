CREATE TABLE MasterEquipmentData (
    ID NUMBER(19,0) NOT NULL,
    AssetID NUMBER(19,0) NOT NULL,
    AssetNum NVARCHAR2(500),
    AssetCode NVARCHAR2(500),
    intCategoryID NUMBER(19,0),
    AssetGroup VARCHAR2(10),
    EquipmentCategory NVARCHAR2(500),
    Parent NVARCHAR2(500),
    Site NVARCHAR2(500),
    HomeDistrict CLOB,
    Location NVARCHAR2(500),
    Make NVARCHAR2(500),
    Model NVARCHAR2(500),
    SerialNumber CLOB,
    Status VARCHAR2(7) NOT NULL,
    StatusReason NVARCHAR2(500),
    dtmOfflineFrom DATE,
    Description CLOB,
    TireSize CLOB,
    Year CLOB,
    LicensePlate CLOB,
    LicensePlateState CLOB,
    RegistrationExpiration CLOB,
    Series CLOB,
    TotalWeight CLOB,
    AxleType CLOB,
    AFEX CLOB,
    DualFuel CLOB,
    Quiet CLOB,
    EmissionsTier CLOB,
    RadiatorType CLOB,
    WebastoOrESPAR CLOB,
    FESize CLOB,
    MAXPSI CLOB,
    CPump CLOB,
    PumpPurpose CLOB,
    EngineMake NVARCHAR2(500),
    EngineModel NVARCHAR2(500),
    AxleTag CLOB,
    Blower CLOB,
    Winch CLOB,
    Painted CLOB,
    WetKit CLOB,
    HDWetKit CLOB,
    SteerWeight CLOB,
    DriveWeight CLOB,
    TruckDepartment CLOB,
    ComboUnit CLOB,
    MissileSkid CLOB,
    MPumpStations CLOB,
    SafetyIronType CLOB,
    InServiceDateWireLine CLOB,
    WorkingPressurePCE CLOB,
    H2SServicePCE CLOB,
    NominalIDPCE CLOB,
    UpperConnectionPCE CLOB,
    LowerConnectionPCE CLOB,
    EngineHours NUMBER,
    EngineHoursDate DATE,
    PumpHours NUMBER,
    PumpHoursDate DATE,
    BreakerHours NUMBER,
    BreakerHoursDate DATE,
    KiloMeter NUMBER,
    KMDate DATE,
    Miles NUMBER,
    MileageDate DATE,
    WirelineCableLength NUMBER,
    CableLengthDate DATE,
    "1YearOrLevel3ExpiryDate" DATE,
    "5YearOrLevel4ExpiryDate" DATE,
    RunsInHole NUMBER,
    LastRunDate DATE,
    CONSTRAINT PK_MasterEquipmentData PRIMARY KEY (ID)
);

CREATE TABLE PumpingEvents_TEMP (
    Id NUMBER(19,0) NOT NULL,
    GUID RAW(16), -- Oracle uses RAW(16) for uniqueidentifier equivalent
    StartDateUtc TIMESTAMP(0) NOT NULL,
    EndDateUtc TIMESTAMP(0) NOT NULL,
    AssetNumber NVARCHAR2(20) NOT NULL,
    CrewName NVARCHAR2(50) NOT NULL,
    IsOpen NUMBER(1) NOT NULL, -- Oracle doesn't have BIT, using NUMBER(1)
    LostCommunication NUMBER(1) NOT NULL, -- Using NUMBER(1) for boolean fields
    IsDirty NUMBER(1),
    StrokeCount NUMBER(10) NOT NULL,
    HorsepowerHour NUMBER NOT NULL,
    DischargePressure NUMBER NOT NULL,
    PumpRate NUMBER NOT NULL,
    PowerEndInputTotal NUMBER(10) NOT NULL,
    VerCol RAW(8) NOT NULL, -- Using RAW(8) for timestamp equivalent
    CONSTRAINT PK_PumpingEvents_TEMP PRIMARY KEY (Id)
);

CREATE TABLE EngineEvents (
    Id RAW(16) NOT NULL, -- Oracle uses RAW(16) for uniqueidentifier
    StartDateUtc TIMESTAMP(7) NOT NULL,
    EndDateUtc TIMESTAMP(7) NOT NULL,
    LibertyEdge NVARCHAR2(10) NOT NULL,
    AssetNumber NVARCHAR2(20) NOT NULL,
    CrewName NVARCHAR2(50) NOT NULL,
    IsOpen NUMBER(1) NOT NULL, -- Using NUMBER(1) for boolean fields
    IsIdle NUMBER(1) NOT NULL, -- Using NUMBER(1) for boolean fields
    EngineHours NUMBER(10) NOT NULL,
    FuelConsumed NUMBER NOT NULL,
    EngineThrottle NUMBER(10) NOT NULL,
    EnginePercentLoad NUMBER NOT NULL,
    EngineGasSubstitutionPercent NUMBER NOT NULL,
    HhpHr NUMBER NOT NULL,
    CoolantTemp NUMBER NOT NULL,
    LostCommunication NUMBER(1) NOT NULL, -- Using NUMBER(1) for boolean fields
    EngineRevolutionTotal NUMBER(10) NOT NULL,
    CONSTRAINT PK_EngineEvents PRIMARY KEY (Id)
);

CREATE TABLE EngineEvents_Digi (
    Id NUMBER(19,0) NOT NULL,
    AssetNumber NVARCHAR2(20) NOT NULL,
    CrewName NVARCHAR2(50) NOT NULL,
    StartDateUtc TIMESTAMP(0) NOT NULL,
    EndDateUtc TIMESTAMP(0) NOT NULL,
    IsOpen NUMBER(1) NOT NULL, -- Using NUMBER(1) for boolean fields
    LostCommunication NUMBER(1) NOT NULL, -- Using NUMBER(1) for boolean fields
    IsIdle NUMBER(1) NOT NULL, -- Using NUMBER(1) for boolean fields
    EngineHours NUMBER(10) NOT NULL,
    DieselConsumed NUMBER NOT NULL, -- Replaced NUMBER with NUMBER for flexible precision
    NGConsumed NUMBER NOT NULL, -- Replaced NUMBER with NUMBER for flexible precision
    EstimatedDGE NUMBER NOT NULL, -- Replaced NUMBER with NUMBER for flexible precision
    GasSubstitution NUMBER NOT NULL, -- Replaced NUMBER with NUMBER for flexible precision
    HHP_H NUMBER NOT NULL, -- Replaced NUMBER with NUMBER for flexible precision
    KW_H NUMBER NOT NULL, -- Replaced NUMBER with NUMBER for flexible precision
    EngineThrottle NUMBER(10) NOT NULL,
    EngineRevolutionTotal NUMBER(19,0) NOT NULL,
    VerCol RAW(8) NOT NULL, -- Using RAW(8) for timestamp equivalent
    CONSTRAINT PK_EngineEvents_Digi PRIMARY KEY (Id)
);

CREATE TABLE DecompEvents (
    Id NUMBER(19,0) NOT NULL,
    StartDateUtc TIMESTAMP(0) NOT NULL,
    EndDateUtc TIMESTAMP(0) NOT NULL,
    AssetNumber NVARCHAR2(50) NOT NULL,
    AssetMake NVARCHAR2(50) NOT NULL,
    AssetModel NVARCHAR2(50) NOT NULL,
    VerCol RAW(8) NOT NULL, -- Using RAW(8) for timestamp equivalent
    CONSTRAINT PK_DecompEvents PRIMARY KEY (Id)
);

-- Create the DecompEvents_Statistics table in Oracle
CREATE TABLE DecompEvents_Statistics (
    Id NUMBER(19,0) NOT NULL,
    DecompEventsId NUMBER(19,0) NOT NULL,
    Field NVARCHAR2(50) NOT NULL,
    Sensor NVARCHAR2(50) NOT NULL,
    Statistic NVARCHAR2(50) NOT NULL,
    Value NUMBER NOT NULL, -- Replaced REAL with NUMBER for flexible precision
    EventTime TIMESTAMP(0) NULL,
    VerCol RAW(8) NOT NULL, -- Using RAW(8) for timestamp equivalent
    CONSTRAINT PK_DecompEvents_Statistics PRIMARY KEY (Id)
);