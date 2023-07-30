# db_jose

1.Filtrador		
	Input	.sdf de lotus
	Output	.Txt de los compuestos
	1.1	Extrae ID Lotus
	1.2	Extrae Smile
	1.3	Guarda en un TXT


2. webot		
	Input	.Txt de los compuestos
	Output	.csv de swissweb
	2.1	Entresaca SOLO smiles del txt "Resultados_Bot"
	2.2	query en la web SwissTargetPrediction.ch
	2.3	Descarga los resultados en formato .CSV
		
3.Nombrador		
	Input	.csv de swissweb
	Output	.csv con el nombre cambiado
	3.1	Cambie nombre al lotus Id correspondiente
