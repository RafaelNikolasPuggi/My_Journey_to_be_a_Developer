
package aula.pkg07;

public class Lutador {
    
    //Atributos
    private String Nome, Nacionalidade, Categoria;
    private int Idade, Vitorias, Derrotas, Empates;
    private float Altura, Peso;
    
    //Metodo construtor
    public Lutador(
            String nom, 
            String nac,
            int ida,
            float alt,
            float pes,
            int vit,
            int der,
            int emp)
            {
    this.Nome = nom;
    this.Nacionalidade = nac;
    this.Idade = ida;
    this.Altura = alt;
    this.setPeso(pes);
    this.Vitorias = vit;
    this.Derrotas = der;
    this.Empates = emp;}
   
    
    //Metodos Set e Get

    public String getNome() {
        return Nome;
    }

    public void setNome(String no) {
        this.Nome = no;
    }

    public String getNacionalidade() {
        return Nacionalidade;
    }

    public void setNacionalidade(String Nacionalidade) {
        this.Nacionalidade = Nacionalidade;
    }

    public String getCategoria() {
        return Categoria;
    }

    public void setCategoria() {
        if (Peso < 52.2){
            this.Categoria = "Invalido, muito abaixo do peso";
        }
        else if (Peso <= 70.3){
            this.Categoria = "Leve";
        }
        else if (Peso <= 83.9){
            this.Categoria = "Médio";
        }
        else if (Peso <= 120.5){
            this.Categoria = "Pesado";
        }
        else{
            this.Categoria = "Invalido, muito acima do peso";
        }
    }

    private int getIdade() {
        return Idade;
    }

    private void setIdade(int Idade) {
        this.Idade = Idade;
    }

    private int getVitorias() {
        return Vitorias;
    }

    private void setVitorias(int Vitorias) {
        this.Vitorias = Vitorias;
    }

    private int getDerrotas() {
        return Derrotas;
    }

    private void setDerrotas(int Derrotas) {
        this.Derrotas = Derrotas;
    }

    private int getEmpates() {
        return Empates;
    }

    private void setEmpates(int Empates) {
        this.Empates = Empates;
    }

    private float getAltura() {
        return Altura;
    }

    private void setAltura(float Altura) {
        this.Altura = Altura;
    }

    private float getPeso() {
        return Peso;
    }

    public void setPeso(float pes) {
        this.Peso = pes;
        this.setCategoria();
    }
    //Metodos publicos
    public void ganharLuta(){
        this.setVitorias(this.getVitorias() + 1);
    }
    
    public void perderLuta(){
        this.setDerrotas(this.getDerrotas() + 1);
    }
    
    public void empatarLuta(){
        this.setEmpates(this.getEmpates() + 1);
    }
    
    public void aprensentar(){
        System.out.println("Lutador: " + this.Nome);
        System.out.println("Origem: " + this.Nacionalidade);
        System.out.println("Idade: " + this.Idade);
        System.out.println("ALtura " + this.Altura);
        System.out.println("Pesando: " + this.Peso);
        System.out.println("Ganhou: " + this.Vitorias);
        System.out.println("Empates: " + this.Empates);
        System.out.println("Derrotas: " + this.Derrotas);
    }
    
    public void status(){
        System.out.println("Lutador: " + this.Nome);
        System.out.println("Categoria: " + this.Categoria);
        System.out.println("Ganhou: " + this.getVitorias());
        System.out.println("Empates: " + this.Empates);
        System.out.println("Derrotas: " + this.Derrotas);
    }
    
   
 
}
