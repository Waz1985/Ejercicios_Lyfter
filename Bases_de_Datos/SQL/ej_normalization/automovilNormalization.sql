PRAGMA foreign_keys = ON;

CREATE TABLE
    IF NOT EXISTS Make (
        idMake INTEGER PRIMARY KEY AUTOINCREMENT,
        MakeName TEXT NOT NULL UNIQUE
    );

CREATE TABLE
    IF NOT EXISTS Model (
        idModel INTEGER PRIMARY KEY AUTOINCREMENT,
        idMake INTEGER NOT NULL,
        ModelName TEXT NOT NULL,
        UNIQUE (idMake, ModelName),
        FOREIGN KEY (idMake) REFERENCES Make (idMake) ON DELETE NO ACTION ON UPDATE NO ACTION
    );

CREATE INDEX IF NOT EXISTS idx_model_make ON Model (idMake);

CREATE TABLE
    IF NOT EXISTS Automovil (
        idCar INTEGER PRIMARY KEY AUTOINCREMENT,
        VIN TEXT NOT NULL UNIQUE,
        idModel INTEGER NOT NULL,
        Color TEXT NOT NULL,
        Year INTEGER NOT NULL,
        FOREIGN KEY (idModel) REFERENCES Modelo (idModel) ON DELETE NO ACTION ON UPDATE NO ACTION
    );

CREATE INDEX IF NOT EXISTS idx_automovil_model ON Automovil (idModel);

    IF NOT EXISTS Owner (
        idOwner INTEGER PRIMARY KEY AUTOINCREMENT,
        OwnerName TEXT NOT NULL,
        OwnerPhone TEXT NOT NULL
    );

CREATE TABLE
    IF NOT EXISTS InsuranceCompany (
        idInsurance INTEGER PRIMARY KEY AUTOINCREMENT,
        CompanyName TEXT NOT NULL
    );

CREATE TABLE
    IF NOT EXISTS Policy (
        idPolicy INTEGER PRIMARY KEY AUTOINCREMENT,
        InsurancePolicy TEXT NOT NULL,
        InsuranceCompany_idInsurance INTEGER NOT NULL,
        FOREIGN KEY (InsuranceCompany_idInsurance) REFERENCES InsuranceCompany (idInsurance) ON DELETE NO ACTION ON UPDATE NO ACTION
    );

CREATE INDEX IF NOT EXISTS idx_policy_insurancecompany ON Policy (InsuranceCompany_idInsurance);

CREATE TABLE
    IF NOT EXISTS Automovil_has_Owner (
        Automovil_idCar INTEGER NOT NULL,
        Owner_idOwner INTEGER NOT NULL,
        Policy_idPolicy INTEGER NOT NULL,
        PRIMARY KEY (Automovil_idCar, Owner_idOwner),
        FOREIGN KEY (Automovil_idCar) REFERENCES Automovil (idCar) ON DELETE NO ACTION ON UPDATE NO ACTION,
        FOREIGN KEY (Owner_idOwner) REFERENCES Owner (idOwner) ON DELETE NO ACTION ON UPDATE NO ACTION,
        FOREIGN KEY (Policy_idPolicy) REFERENCES Policy (idPolicy) ON DELETE NO ACTION ON UPDATE NO ACTION
    );

CREATE INDEX IF NOT EXISTS idx_aho_owner ON Automovil_has_Owner (Owner_idOwner);

CREATE INDEX IF NOT EXISTS idx_aho_automovil ON Automovil_has_Owner (Automovil_idCar);

CREATE INDEX IF NOT EXISTS idx_aho_policy ON Automovil_has_Owner (Policy_idPolicy);