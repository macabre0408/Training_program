public class Livre{
    private int id = 0;
    private String titre, auteur;
    private double prix;

   public Livre(String titre, String auteur, double prix) {
    this.id += 1;
    this.titre = titre;
    this.auteur =auteur;
    this.prix = prix;
   }
   public int getId() {
    return id;
   }
   public String getTitre() {
    return titre;
   }
   public String getAuteur() {
    return this.auteur;
   }
   public double getPrix() {
    return prix;
   }
   public void setTitre(String titre) {
    this.titre = titre;
   }
   public void setAuteur(String auteur) {
    this.auteur = auteur;
   }
   public void setPrix(double prix){
    this.prix = prix;
   }
   @Override
   public String toString(){
        return "Le livre " + getTitre() + " ecrit par l'auteur " + getAuteur() + " coute " + getPrix();
   }
}