"""DDR2 timing parameters.

Micron MT47H64M16 (1Gb, x16, 8 banks), speed grade -25E: DDR2-800, CL = 5,
tCK = 2.5 ns. Source: Micron "1Gb: x4, x8, x16 DDR2 SDRAM" datasheet,
1GbDDR2.pdf Rev. Y 02/14, Table 12 (pp. 35-41) and p. 86 (RL = AL + CL,
WL = RL - 1). Values are in clock cycles: ns / tCK, rounded up.
"""

DDR2 = {
    "tCCD": 2,  # 2 tCK
    "tPD": 3,  # tCKE MIN = 3 tCK
    "tRAS": 16,  # 40 ns
    "tRC": 22,  # 55 ns
    "tRCD": 5,  # 12.5 ns
    "tRFC": 51,  # 127.5 ns (1Gb)
    "tRL": 5,  # AL + CL
    "tRP": 5,  # 12.5 ns
    "tRRD": 4,  # 10 ns (x16; x4/x8 is 7.5 ns = 3)
    "tRTP": 3,  # 7.5 ns
    "tFAW": 18,  # 45 ns (x16; x4/x8 is 35 ns = 14)
    "tWL": 4,  # RL - 1
    "tRTRS": 1,
    "tWR": 6,  # 15 ns
    "tAL": 0,
    "tWTR": 3,  # 7.5 ns
    "tXP": 2,  # 2 tCK
    "tCK": 1,
    "tXSNR": 55,  # tRFC + 10 ns = 137.5 ns
    "tXSRD": 200,  # 200 tCK
    "tXARD": 2,  # 2 tCK (fast exit, MR12 = 0)
}
