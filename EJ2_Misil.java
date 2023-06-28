import javax.swing.JOptionPane;

public class EJ2_Misil {
    public static void main (String[] args) {
        // Zona de recursos
        float Vo, d,Dist, Dif,Angulo1;
        double Angulo;
        // Procesos
        Vo = Float.parseFloat(JOptionPane.showInputDialog("Digite la velocidad inicial: "));
        Angulo = Double.parseDouble(JOptionPane.showInputDialog("Digite el angulo: "));
        d = Float.parseFloat(JOptionPane.showInputDialog("Digite la distancia del tiro al blanco: "));
        // Calculo
        Angulo1 = (float)(Math.sin(Math.toRadians(Angulo*2)));
        Dist = (float)(Math.floor((Math.pow(Vo,2)*Angulo1)/9.81));
        Dif = Dist - d ;

        // Salidas
        if(Dist == d){
            System.out.println("Dió en el blanco");
        }
        else if(Dist > d){
           System.out.println("No dió en el blanco, cayo adelante por "+Dif+" metros. Una distancia de " +Dist+ " metros y un angulo de "+Angulo);
        }
        else if(Dist < d){
            System.out.println("No dió en el blanco, cayo atrás por " +(-Dif)+ " metros. Una distancia de " +Dist+ "metros y angulo de " +Angulo);
        }
    }
}