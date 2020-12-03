

As = [('archivo1', 10), ('archivo2', 5), ('archivo3', 3),
              ('archivo4', 8), ('archivo5', 9), ('archivo6', 1)]

D = 10
M = []
suma = 0


def maximizar(As, D):
    resolver(As,D,suma, M)
    
    




def resolver(As,D,suma, M):
	for j in As:
		if suma >= D:
			return M
		if j[1] <= D:
			M += j
			suma += j[1]

			
   
maximizar(As,D)
		

	
    		
