package aula04;


public class Caneta {
    private String modelo;
    private float ponta;
    private String cor;
    private boolean tampada;
   
    public Caneta(String m, String c, float p){
        this.modelo = m;
        this.cor = c;
        this.ponta = p;
        
    }

    public String getModelo() {
        return modelo;
    }

    public boolean isTampada() {
        return tampada;
    }
    
    public void status(){
        System.out.println("Modelo: " + this.modelo);
        System.out.println("Uma caneta " + this.cor);
        System.out.println("Ponta: " + this.ponta);
        System.out.println("Esta tampada? " + this.tampada); 
    }
}
