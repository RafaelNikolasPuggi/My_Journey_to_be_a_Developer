package aula.pkg09;

public class Aula09 {

    public static void main(String[] args) {
        //Classes
        Pessoa[] p = new Pessoa[5];
        Livro[] l = new Livro[3];
               
        /*
        Construtor Pessoa
        (String nome, String sexo, int idade)
        */
        p[0] = new Pessoa("Rafael", "M", 25);
        p[1] = new Pessoa("Marina", "F", 24);
        p[2] = new Pessoa("Cristofer", "M", 38);
        p[3] = new Pessoa("Tolkien", "M", 100);
        p[4] = new Pessoa("Marilu", "F", 70);
        
        /*
        Constutor Livro
        (String titulo, int totPaginas, Pessoa autor, Pessoa leitor)
        */
        l[0] = new Livro("Eragon", 400, p[2], p[0]);
        l[1] = new Livro("LOTR", 600, p[3], p[4]);
        l[2] = new Livro("Terror numseionde", 200, p[4], p[1]);
        
        //Metodos
        l[2].abrir();
        l[2].folhear(45);
        l[2].avancarPag();
        System.out.println(l[2].detalhes());
        
        l[1].fechar();
        System.out.println(l[1].detalhes());
    }
    
}
