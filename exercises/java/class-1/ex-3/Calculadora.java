
public class Calculadora {
    public int numero1;
    public int numero2;

    Calculadora(int s, int p) {
		numero1 = s;
		numero2 = p;
		}
    
    public int retornaSomaAtributos() {
        return numero1 + numero2;
    }
    
    public int retornaMultiplicacaoAtributos() {
        return numero1 * numero2;
    }
    
    public void insereValoresAtributos(int num1, int num2) {
        numero1 = num1;
        numero2 = num2;
    }

    public void mostraDados() {
        System.out.println("Soma dos atributos:" + retornaSomaAtributos());
        System.out.println("Multiplicação dos atributos: " + retornaMultiplicacaoAtributos());
        System.out.println("Valor de numero1: " + numero1);
        System.out.println("Valor de numero2: " + numero2);

	}
}
