
package aula.pkg09;

public class Livro implements Publicação{
    //Atributos
    private String titulo;
    private int totPaginas, pagAtual;
    private boolean aberto;
    private Pessoa autor, leitor;
    
    //Construtor

    public Livro(String titulo, int totPaginas, Pessoa autor, Pessoa leitor) {
        this.titulo = titulo;
        this.totPaginas = totPaginas;
        this.autor = autor;
        this.leitor = leitor;
        this.aberto = false;
        this.pagAtual = 0;
    }

    //Getters e Setters
    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public int getTotPaginas() {
        return totPaginas;
    }

    public void setTotPaginas(int totPaginas) {
        this.totPaginas = totPaginas;
    }

    public int getPagAtual() {
        return pagAtual;
    }

    public void setPagAtual(int pagAtual) {
        this.pagAtual = pagAtual;
    }

    public boolean isAberto() {
        return aberto;
    }

    public void setAberto(boolean aberto) {
        this.aberto = aberto;
    }

    public Pessoa getAutor() {
        return autor;
    }

    public void setAutor(Pessoa autor) {
        this.autor = autor;
    }

    public Pessoa getLeitor() {
        return leitor;
    }

    public void setLeitor(Pessoa leitor) {
        this.leitor = leitor;
    }
    
    //Metodos especiais
    public String detalhes() {
        return "Livro"
                + "\n titulo = " + titulo 
                + "\n totPaginas = " + totPaginas 
                + "\n pagAtual = " + pagAtual 
                + "\n aberto = " + aberto 
                + "\n autor = " + autor.getNome()
                + "\n leitor = " + leitor.getNome()
                ;
    }
    //Metodos abstratos
    @Override
    public void abrir() {
        this.aberto = true;
    }

    @Override
    public void fechar() {
        this.aberto = false;
    }

    @Override
    public void folhear(int p) {
        if (p > this.totPaginas) {
            this.pagAtual = 0;
        }else{
        this.pagAtual = p;
        }
    }

    @Override
    public void avancarPag() {
        this.pagAtual ++;
    }

    @Override
    public void voltarPag() {
        this.pagAtual --;
    }
    
}
