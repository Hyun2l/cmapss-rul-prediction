CMAPSS RUL Prediction project

NASA CMAPSS 데이터를 활용해 항공 엔진의 잔여수명(RUL)을 예측하는 머신러닝 프로젝트입니다.

## Setup
```bash
conda activate cmapss-rul-prediction
pip install -r requirements.txt
```

## dataset overview from the paper
```bash
sensor_1	T2	Fan inlet temperature (팬 입구 온도)
sensor_2	T24	LPC outlet temperature (저압압축기 출구 온도)	
sensor_3	T30	HPC outlet temperature (고압압축기 출구 온도)	
sensor_4	T50	LPT outlet temperature (저압터빈 출구 온도)	
sensor_5	P2	Fan inlet pressure (팬 입구 압력)	
sensor_6	P15	Bypass-duct pressure (바이패스 덕트 압력)	
sensor_7	P30	HPC outlet pressure (고압압축기 출구 압력)	
sensor_8	Nf	Physical fan speed (팬 물리적 회전속도)	
sensor_9	Nc	Physical core speed (코어 물리적 회전속도)	
sensor_10	epr	Engine pressure ratio (엔진 압력비)	
sensor_11	Ps30	HPC outlet static pressure (고압압축기 출구 정압)	
sensor_12	phi	Fuel flow / Ps30 (연료유량 대 정압비)	
sensor_13	NRf	Corrected fan speed (보정 팬속도)	
sensor_14	NRc	Corrected core speed (보정 코어속도)	
sensor_15	BPR	Bypass ratio (바이패스비)	
sensor_16	farB	Burner fuel-air ratio (연소기 연료-공기비)	
sensor_17	htBleed	Bleed enthalpy (블리드 엔탈피)	
sensor_18	Nf_dmd	Demanded fan speed (요구/설정 팬속도)	
sensor_19	PCNfR_dmd	Demanded corrected fan speed (요구/설정 보정 팬속도)	
sensor_20	W31	HPT coolant bleed (고압터빈 냉각공기 블리드)	
sensor_21	W32	LPT coolant bleed (저압터빈 냉각공기 블리드)
```