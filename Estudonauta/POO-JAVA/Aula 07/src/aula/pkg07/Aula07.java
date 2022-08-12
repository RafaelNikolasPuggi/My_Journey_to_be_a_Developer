package aula.pkg07;

public class Aula07 {

    public static void main(String[] args) {
        
        Lutador l[] = new Lutador[6];
               
        l[0] = new Lutador("Pretty Boy","França", 31, 11.75f, 68.9f, 11, 1, 2);
        l[1] = new Lutador("Putscript", "Brasil", 29, 1.68f, 57.8f, 14, 3, 2);
        l[2] = new Lutador("Snapdragon", "EUA", 35, 1.65f, 80.9f, 12, 1, 2);
        l[3] = new Lutador("Dead Code", "Autralia", 28, 1.93f, 81.5f, 13, 2, 0);
        l[4] = new Lutador("UFO Cobol", "Brasil", 37, 1.70f, 119.2f, 5, 3, 4);
        l[5] = new Lutador("Nerfdaart", "EUA", 30, 1.81f, 105.7f, 12, 4, 2);
        
        Luta A1 = new Luta();
        A1.marcarLuta(l[1], l[1]);
        A1.lutar();
        
        
    }
    
}
