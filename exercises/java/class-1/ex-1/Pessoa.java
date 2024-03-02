
// Faça um programa que realize a calculo IMC

public class Pessoa {
	String nome;
	double peso;
	double altura;

	Pessoa(String s, double p, double a) {
		nome = s;
		peso = p;
		altura = a;
	}

	public double calculaIMC() {
		return peso / (altura * altura);
	}

	public void mostraDados() {
		System.out.println("Nome..." + nome);
		System.out.println("altura..." + altura);
		System.out.println("Peso..." + peso);
		System.out.println("IMC..." + calculaIMC());

	}
}
