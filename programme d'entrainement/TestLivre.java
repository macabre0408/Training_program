import java.util.List;
import java.util.Scanner;
public class TestLivre{
    public static void main(String[] args){
        List<Livre> list = new ArrayList<Livre>();
        Scanner scan = new Scanner(System.in);
        String choix= "O";

        while(choix.equals("O")){
            System.out.println("Veuilez entrer le titre du livre n° " + getId()+1+":");
            String t = scan.nextLine();
            System.out.println("Veuilez entrer l'auteur du livre n° " + getId()+1+":");
            String a = scan.nextLine();
            System.out.println("Veuillez entrer le prix du livre n° " + getId()+1+":");
            double p = scan.nextDouble();
            System.out.println("Voulez-vous continuer ? O/N");
            choix = scan.nextLine();
            Livre l = new Livre(t, a, p);
            list.add(l);
        }
        for(int i=0; i<list.size(); i++){
            System.out.println(list.get(i).toString());
        }
    }
}