
//  Crie uma classe de nome "Carro" (sem o método "main") com os seguintes atributos: 
// placa (público – texto)  ano (público – inteiro) modelo (público – texto) 

public class Carro {
	String placa;
	int ano;
	String modelo;

	Carro(String s, int p, String a) {
		placa = s;
		ano = p;
		modelo = a;
	}

		public void mostraDados() {
			System.out.println("placa..." + placa);
			System.out.println("ano..." + ano);
			System.out.println("modelo..." + modelo);
		}
}