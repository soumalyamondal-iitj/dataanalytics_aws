CREATE TABLE dev.employee_info (
    employeeid integer NOT NULL ENCODE az64,
    age integer ENCODE az64,
    gender character varying(256) ENCODE lzo,
    department character varying(256) ENCODE lzo,
    yearsofexperience integer ENCODE az64,
    educationlevel integer ENCODE az64,
    salary integer ENCODE az64,
    performancerating integer ENCODE az64,
    skills character varying(256) ENCODE lzo,
    certification character varying(256) ENCODE lzo,
    PRIMARY KEY (employeeid)
) DISTSTYLE AUTO;