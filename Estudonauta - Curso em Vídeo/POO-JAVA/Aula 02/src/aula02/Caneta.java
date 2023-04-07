package aula02;

public class Caneta {
    public String modelo;
    public String cor;
    protected float conta;
    protected int carga;
    private boolean tampada;
    private float ponta;
    public void status(){
        System.out.println("Modelo: " + this.modelo);
        System.out.println("Uma caneta " + this.cor);
        System.out.println("Ponta: " + this.ponta);
        System.out.println("Carga: " + this.carga);
        System.out.println("Esta tampada? " + this.tampada);
        
    }
    protected void rabiscar() {
        if (this.tampada == true){
            System.out.println("ERRO! Não posso rabiscar.");
        } else{
            System.out.println("Estou rabiscando");
        }
    }
    
    public void tampar() {
        this.tampada = true;
    }
    
    public void destampar(){
        this.tampada = false;
    }
}

